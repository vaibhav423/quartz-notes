#nvim
# Neovim Tricks

## increment/decrement numbers in visual mode
v_g_ctrl_a to increment numbers in visual mode
v_g_ctrl_x to decrement numbers in visual mode

set nrformats+=alpha to work with letters as well (normally only works with numbers)
### example
a -- below 5 lines were a 
b -- come here do inc/dec 
c
d
e
f

## temporary nvim treesitter delete line bug fix
  file : ../../termux/usr/share/nvim/runtime/lua/vim/treesitter.lua
  ┃    195 +   -- Guard against stale treesitter node positions after buffer
  ┃          mutations
  ┃    196 +   local line_count = api.nvim_buf_line_count(buf)
  ┃    197 +   if start_row >= line_count or end_row >= line_count then
  ┃    198 +     return ''
  ┃    199 +   end
