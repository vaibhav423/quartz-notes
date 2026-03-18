#nvim

# Nvim-todos
https://youtu.be/7xRbaWBzIMQ [nvim copilot chat ]
https://youtu.be/B8BoPkga-_E [nvim copilot chat ]
https://github.com/nvim-neorg/neorg/wiki [noeorg smth similar to obsidian]
https://github.com/benlubas/molten-nvim [awesome way to run code and take notes]
https://youtu.be/fFHlfbKVi30 [web development 1 hr video]
https://github.com/fang2hou/blink-copilot?tab=readme-ov-file [ copilot-lua ]
init-and-pin-dir etc to lua


set a keymap to copy imaage into clipboard
termux-clipboard-set -i /path/to/your/image.png



see how to make nvim work with large files 
## error while dd in treesitter highlighter,
fix this when doing dd (occurs sometime not sure how to reproduce)


Error in decoration provider "line" (ns=nvim.treesitter.highlighter):
Error executing lua: ...rmux/files/usr/share/nvim/runtime/lua/vim/treesitter.lua:195: Index out of bounds
stack traceback:
	[C]: in function 'nvim_buf_get_text'
	...rmux/files/usr/share/nvim/runtime/lua/vim/treesitter.lua:195: in function 'get_url'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:409: in function 'fn'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:239: in function 'for_each_highlight_state'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:358: in function 'on_line_impl'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:457: in function <...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:451>
Error in decoration provider "line" (ns=nvim.treesitter.highlighter):
Error executing lua: ...rmux/files/usr/share/nvim/runtime/lua/vim/treesitter.lua:195: Index out of bounds
stack traceback:
	[C]: in function 'nvim_buf_get_text'
	...rmux/files/usr/share/nvim/runtime/lua/vim/treesitter.lua:195: in function 'get_url'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:409: in function 'fn'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:239: in function 'for_each_highlight_state'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:358: in function 'on_line_impl'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:457: in function <...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:451>
	[C]: at 0x5e797b47a8
Error in decoration provider "line" (ns=nvim.treesitter.highlighter):
Error executing lua: ...rmux/files/usr/share/nvim/runtime/lua/vim/treesitter.lua:195: Index out of bounds
stack traceback:
	[C]: in function 'nvim_buf_get_text'
	...rmux/files/usr/share/nvim/runtime/lua/vim/treesitter.lua:195: in function 'get_url'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:409: in function 'fn'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:239: in function 'for_each_highlight_state'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:358: in function 'on_line_impl'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:457: in function <...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:451>
	[C]: at 0x5e797b47a8
Error in decoration provider "line" (ns=nvim.treesitter.highlighter):
Error executing lua: ...rmux/files/usr/share/nvim/runtime/lua/vim/treesitter.lua:195: Index out of bounds
stack traceback:
	[C]: in function 'nvim_buf_get_text'
	...rmux/files/usr/share/nvim/runtime/lua/vim/treesitter.lua:195: in function 'get_url'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:409: in function 'fn'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:239: in function 'for_each_highlight_state'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:358: in function 'on_line_impl'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:457: in function <...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:451>
Error in decoration provider "line" (ns=nvim.treesitter.highlighter):
Error executing lua: ...rmux/files/usr/share/nvim/runtime/lua/vim/treesitter.lua:195: Index out of bounds
stack traceback:
	[C]: in function 'nvim_buf_get_text'
	...rmux/files/usr/share/nvim/runtime/lua/vim/treesitter.lua:195: in function 'get_url'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:409: in function 'fn'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:239: in function 'for_each_highlight_state'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:358: in function 'on_line_impl'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:457: in function <...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:451>
	[builtin#36]: at 0x7a4e2a245c
	...s/usr/share/nvim/runtime/lua/vim/lsp/semantic_tokens.lua:307: in function 'handler'
	...rmux/files/usr/share/nvim/runtime/lua/vim/lsp/client.lua:682: in function 'fn'
	vim/_editor.lua:366: in function <vim/_editor.lua:365>
Error in decoration provider "line" (ns=nvim.treesitter.highlighter):
Error executing lua: ...rmux/files/usr/share/nvim/runtime/lua/vim/treesitter.lua:195: Index out of bounds
stack traceback:
	[C]: in function 'nvim_buf_get_text'
	...rmux/files/usr/share/nvim/runtime/lua/vim/treesitter.lua:195: in function 'get_url'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:409: in function 'fn'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:239: in function 'for_each_highlight_state'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:358: in function 'on_line_impl'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:457: in function <...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:451>
Error in decoration provider "line" (ns=nvim.treesitter.highlighter):
Error executing lua: ...rmux/files/usr/share/nvim/runtime/lua/vim/treesitter.lua:195: Index out of bounds
stack traceback:
	[C]: in function 'nvim_buf_get_text'
	...rmux/files/usr/share/nvim/runtime/lua/vim/treesitter.lua:195: in function 'get_url'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:409: in function 'fn'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:239: in function 'for_each_highlight_state'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:358: in function 'on_line_impl'
	...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:457: in function <...sr/share/nvim/runtime/lua/vim/treesitter/highlighter.lua:451>
	[builtin#36]: at 0x7a4e2a245c
	...s/usr/share/nvim/runtime/lua/vim/lsp/semantic_tokens.lua:307: in function 'handler'
	...rmux/files/usr/share/nvim/runtime/lua/vim/lsp/client.lua:682: in function 'fn'
	vim/_editor.lua:366: in function <vim/_editor.lua:365>

[[nvim_treesiter_issue]]
