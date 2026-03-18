#nvim

# `treesitter highlighter crashes with "Index out of bounds" in nvim_buf_get_text after line deletion in large buffers

**Repository:** `neovim/neovim`

## Description

When deleting a line (e.g. with `dd`) in a large buffer with treesitter highlighting active, the decoration provider throws a repeating error:

```
Error in decoration provider "line" (ns=nvim.treesitter.highlighter):
Error executing lua: ...runtime/lua/vim/treesitter.lua:195: Index out of bounds
stack traceback:
    [C]: in function 'nvim_buf_get_text'
    ...runtime/lua/vim/treesitter.lua:195: in function 'get_url'
    ...runtime/lua/vim/treesitter/highlighter.lua:409: in function 'fn'
    ...runtime/lua/vim/treesitter/highlighter.lua:239: in function 'for_each_highlight_state'
    ...runtime/lua/vim/treesitter/highlighter.lua:358: in function 'on_line_impl'
    ...runtime/lua/vim/treesitter/highlighter.lua:457: in function <...highlighter.lua:451>
```

## Steps to reproduce

1. Open a markdown file with ~150+ lines that contains markdown image links e.g. `![alt](path/to/image.png)`
2. Enable treesitter highlighting (default in recent nvim)
3. Place cursor on any line near the end of the buffer
4. Press `dd` to delete the line

## Expected

Line is deleted silently.

## Actual

The error above fires repeatedly (once per redraw) until the screen settles.

## Root cause

In `lua/vim/treesitter/highlighter.lua`, `on_line_impl` iterates active treesitter matches and calls `get_url` for each capture. `get_url` calls `buf_range_get_text` in `lua/vim/treesitter.lua:185`, which calls `nvim_buf_get_text` with row positions derived from the parse tree. After a line deletion the parse tree still contains stale node positions that reference rows beyond the new buffer line count, causing `nvim_buf_get_text` to throw `Index out of bounds`.

The decoration provider fires synchronously during redraw, which can happen before the treesitter parser has had a chance to re-parse the updated buffer.

## Suggested fix

In `buf_range_get_text` (`lua/vim/treesitter.lua:185`), clamp node positions against the current buffer line count before calling `nvim_buf_get_text`:

```lua
local line_count = api.nvim_buf_line_count(buf)
if start_row >= line_count or end_row >= line_count then
  return ''
end
```

## Environment

- Neovim (Termux build on Android)
- Filetype: `markdown`
- Treesitter markdown parser active
- Only reproducible with larger buffers (~150+ lines)
