#nvim
# blink.cmp Wikilink Completion

## Problem

Inside `[[]]`, markdown-oxide returns fuzzy-matched completions ranked by nucleo score. blink.cmp re-ranks these using its own fuzzy scorer, which only sees the word after the last space — so typing `[[ hypr]]` makes blink score against `hypr` but ignores the leading space that triggered block-reference mode. The result: recently modified files (sorted by mtime when query is empty) or unrelated matches beat the correct result.

## How markdown-oxide scores completions

When `cmp_text` (everything between `[[` and cursor) is empty, markdown-oxide returns all referenceables sorted by file modification time — most recently modified first. When `cmp_text` is non-empty, it runs nucleo fuzzy matching and stores the score as a plain integer string in the LSP `sortText` field, e.g. `"312"`. Higher number = better match.

## Why blink fights it

blink runs its own fuzzy pass over all LSP items after receiving them. This pass:

1. Extracts the keyword using `iskeyword` boundaries — stops at spaces, so `" hypr"` becomes just `"hypr"` as the keyword.
2. Writes its own score into `item.score`, overwriting anything set in `transform_items`.
3. Sorts by `item.score` descending.

So even if markdown-oxide ranked "hyprland" first, blink's rescore using only `"hypr"` can produce a different order and overwrites the result.

## Why transform_items cannot fix this

`transform_items` runs before blink's fuzzy pass. Setting `item.score` there is pointless because line 141 of `fuzzy/init.lua` unconditionally overwrites it:

```lua
item.score = scores[idx]
```

`item.sortText` is the only field blink never touches after receiving the LSP response.

## The fix

A custom sort function in `fuzzy.sorts`. Sort functions receive `(a, b)` items after scoring and can return `true`, `false`, or `nil` (defer to next function). They have no context parameter, so `inside_wikilink()` reads the live cursor position directly.

```lua
local function inside_wikilink()
  local cursor = vim.api.nvim_win_get_cursor(0)
  local line   = vim.api.nvim_buf_get_lines(0, cursor[1] - 1, cursor[1], false)[1] or ""
  return line:sub(1, cursor[2]):match("%[%[[^%]]*$") ~= nil
end

local function wikilink_sort(a, b)
  if not inside_wikilink() then return nil end
  local sa = tonumber(a.sortText)
  local sb = tonumber(b.sortText)
  if sa == nil and sb == nil then return nil end
  if sa == nil then return false end
  if sb == nil then return true end
  if sa ~= sb then return sa > sb end  -- higher nucleo score = better
  return nil
end

opts.fuzzy.sorts = { wikilink_sort, "score", "sort_text" }
```

`wikilink_sort` runs first. Inside `[[]]` it compares `sortText` as numbers descending. Outside `[[]]` it returns `nil`, deferring to blink's own `score` sort.

## Other settings

**`use_proximity = false`** — blink boosts items whose text appears near the cursor in the buffer. This caused words like "how are you praveen" (written nearby) to outrank "hyprland". Disabled globally.

**`should_show_items` on snippets/buffer/path** — these providers are hidden inside `[[]]` since only LSP (markdown-oxide) is relevant there. `sources.default` cannot be used for this because blink calls it with no arguments during trigger character detection — there is no context available at that point.
