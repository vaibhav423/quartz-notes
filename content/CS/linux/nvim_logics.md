#nvim
# Neovim Runtimepath Execution Logic

The sourcing mechanism for any directory $D$ present in the `runtimepath` can be defined by the set of files $S$:

$$S = \{ f \in D/\text{plugin}/ \mid \text{suffix}(f) \in \{ \text{.lua}, \text{.vim} \} \}$$

### Standard Directory Hierarchy

* **`~/.config/nvim/`** (Primary RTP Entry)
    * `init.lua` (The entry point)
    * **`lua/`** (Required modules; not auto-sourced)
    * **`plugin/`** (Auto-sourced at startup)
    * **`ftplugin/`** (Sourced on specific FileType events)
    * **`after/`** (Sourced after all other RTP entries)
        * **`plugin/`** (Final overrides)

### Initialization Order

1.  **User Config:** `init.lua` or `init.vim`
2.  **Plugin Paths:** Every `{rtp}/plugin/` (excluding `after/`)
3.  **Runtime:** Global system scripts
4.  **Final Word:** Every `{rtp}/after/plugin/`

# Neovim `lua/` Directory Logic

Unlike the `plugin/` directory, the `lua/` folder is a **module library**. Files here remain dormant until explicitly loaded.

### 1. The Mapping Logic
Neovim adds the `lua/` subfolder of every entry in your `runtimepath` to the Lua search path. The mapping follows this formula:

$$\text{require}('A.B') \implies \exists \, D \in \text{rtp} \mid \text{File} = D/\text{lua}/A/B.\text{lua}$$

### 2. Sourcing Comparison

| Feature | `plugin/` | `lua/` |
| :--- | :--- | :--- |
| **Trigger** | Automatic (Startup) | Manual (`require`) |
| **Logic** | Procedural Scripting | Modular Programming |
| **Namespacing** | Global Scope | Encapsulated |
| **Caching** | None (Re-sourced) | `package.loaded` (Cached) |



### 3. File Resolution Hierarchy
When you call `require('module')`, Neovim searches in this priority:
1.  `lua/module.lua`
2.  `lua/module/init.lua` (Treats the folder as a package)

---

### 4. Structure of your AstroNvim environment
Based on your paths, your `lua/` files are organized to prevent collisions between the core framework and your user overrides:

* **Framework Logic:** Found in `.../lazy/AstroNvim/lua/astronvim/`
* **Your Custom Logic:** Found in `~/.config/nvim/lua/`

> **Note:** Because Lua caches modules, calling `require('example')` a second time will not execute the code again. You must restart Neovim or delete the entry from the global `package.loaded` table to see changes.

# Why `mkview`/`loadview` Fails with AstroNvim Folding

## AstroNvim's Fold Setup

AstroNvim configures folding as:

```lua
foldmethod = "expr"
foldexpr   = "v:lua.require'astroui.folding'.foldexpr()"
foldlevel  = 99  -- all folds open by default
```

The `foldexpr` is a lazy, on-demand function — it does not compute fold levels upfront. It is called by Neovim line-by-line as needed, delegating to treesitter which parses asynchronously.

## Why `mkview`/`loadview` Fails

`mkview` saves the current fold state as a Vimscript file. For `foldmethod=expr` it produces something like:

```vim
setlocal foldmethod=expr
setlocal foldexpr=v:lua.require'astroui.folding'.foldexpr()
setlocal foldlevel=99
sil! normal! zo
```

When `loadview` runs on re-open, it restores `foldlevel=99` (all folds open). Then AstroNvim's own `FileType` autocmd fires and resets `foldexpr`, triggering a full recompute that overwrites whatever `loadview` just did. `loadview` never had a chance.

The only way `mkview` works reliably is with `foldmethod=manual`, where fold state is absolute and nothing recomputes it. With `foldmethod=expr`, the expression always wins.

## The Custom Solution

The fix bypasses the problem by:

1. Saving only the **line numbers of closed folds** — not the foldmethod or foldlevel
2. Restoring **after** AstroNvim's `FileType` handler finishes (via `vim.schedule`)
3. Waiting with `vim.defer_fn` until treesitter has actually computed foldlevels (checking `foldlevel(lnum) > 0`)
4. Closing exactly those lines using `zc` — working **with** the expr folds rather than against them

The retry loop runs up to 20 times every 50ms (~1s total), handling both slow treesitter parsing and buffers that are not yet visible when multiple files are opened together.

# Completed Features

## 1. ESC Auto-Save (`after/plugin/escape_save.lua`)
Pressing `<Esc>` in insert mode automatically saves the buffer. Skips special/unnamed buffers (terminals, oil.nvim, etc.).

## 2. Date Reminder Command — `:Jeerem` (`lua/polish.lua`)
Inserts a countdown string on line 1 of the current buffer showing the number of days remaining until April 2, 2026.

## 3. Markdown LaTeX Converter Toggle — `<leader>mt` (`lua/plugins/mdrender_1.lua`)
Toggles the render-markdown.nvim LaTeX rendering command between `latex2text` and `utftex`. Useful for switching math display styles in markdown.

## 4. Smart Fold Toggle — `z1`–`z4` (`after/plugin/fold_toggle.lua`)
Keymaps for heading-level fold management:
- `zN` opens all headings at level N, opening parent levels only if they have children
- Pressing `zN` again closes only level-N folds (drops back to N-1 state)
- `<leader>z1`–`<leader>z4` applies the same logic across all windows

## 5. Marksman LSP (`lua/plugins/astrolsp.lua`)
Marksman (markdown LSP) enabled with the Termux binary path hardcoded, since Mason-installed binaries do not work on Termux.

## 6. Fold Persistence (`lua/fold_persist.lua` + `lua/plugins/astrocore.lua`)
Saves and restores fold state across sessions, working around AstroNvim's treesitter foldexpr:
- On `BufWinLeave`: saves closed fold line numbers to `~/.local/state/nvim/folds/<sha256_of_filepath>`
- On `BufWinEnter`: waits for treesitter to finish computing fold levels (retry loop up to 20×50ms), then closes the saved lines with `zc`
- A per-buffer flag (`vim.b[buf].folds_restored`) prevents double-restore

## 7. LaTeX / Math Snippets (`lua/plugins/latex.lua`)
- **vimtex** installed with all features disabled except syntax — required by `luasnip-latex-snippets.nvim` for `vimtex#syntax#in_mathzone()` math-zone detection
- **luasnip-latex-snippets.nvim** provides snippets (`\frac`, `\sum`, environments, etc.)
- LuaSnip `filetype_extend` loads tex/latex snippets inside markdown buffers
- `$`…`$` autopairs configured for markdown, tex, and latex filetypes

## utftex installation
use npm install libtexprint or clone https://github.com/bartp5/libtexprintf

git clone https://github.com/bartp5/libtexprintf
cd libtexprintf
./autogen.sh
./configure --prefix={path_to_install}
make
make install

for termux
./autogen.sh
./configure --prefix=/data/data/com.termux/files/usr/
make
make install


cd tree-sitter-latex
tree-sitter  init
\> parser name : latex
tree-sitter generate
#chroot gcc -O3 -shared -fPIC -Isrc src/parser.c src/scanner.c -o latex.so
~
 ❯ clang -o latex.so -I./src src/parser.c src/scanner.c -shared -fPIC -Os 
~
 ❯ mkdir -p ~/.local/share/nvim/lazy/nvim-treesitter/parser/
cp latex.so ~/.local/share/nvim/lazy/nvim-treesitter/parser/latex.so
## blink completion
-- Put this in your init.lua / plugin config where you call require('blink.cmp').setup()
require('blink.cmp').setup({
  cmdline = {
    enabled = true,
    keymap = {
      -- keep the cmdline preset if you like:
      preset = 'cmdline',

      -- Option A: pressing Enter inserts the top match into the cmdline (does NOT run it)
      ['<CR>'] = { 'select_and_accept', 'fallback' },

      -- Option B (alternate): pressing Enter inserts the top match AND executes the command
      -- ['<CR>'] = { 'accept_and_enter', 'fallback' },
    },

    -- Make sure list selection/pre-insert behavior is enabled
    completion = {
      list = { selection = { preselect = true, auto_insert = true } },
      -- optionally show the menu automatically while testing
      menu = { auto_show = true },
    },
  },
})
