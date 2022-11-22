" Load plugins through vim-plug
call plug#begin('~/.local/share/nvim/plugged')
Plug 'morhetz/gruvbox'
call plug#end()

" Basic settings
set nocompatible
set title
set number
set relativenumber
set cursorline
set mouse=a
set wrap
set hidden


set showcmd
set showmode
set ruler

" Color schemes
syntax enable
set background=dark
if (has("termguicolors"))
  set termguicolors
endif
" Plugin theme
colorscheme gruvbox
" other themes: desert, evening, elford, industry,  koehler, pablo, 
"hi User1 ctermbg=yellow ctermfg=black guibg=yellow guifg=black
"hi User2 ctermbg=darkcyan ctermfg=lightgray guibg=lightblue guifg=black

set showmatch
set smartcase
set ignorecase
set incsearch

"set statusline=\ %F\ %M\ %Y\ %r%=\ %l\ %c\ %p%%
set laststatus=2
set shiftwidth=2
set tabstop=2
set softtabstop=2
set shiftround
set expandtab
set autoindent

" Statusline custom 1
"set statusline=%<%f\ %h%m%r%=%-14.(%l,%c%V%)\ %P
"set statusline=\ %<%f\ %h%m%=%14.(%l,%c%V%)\ %P
set statusline=%#Visual#\ %<%f\ %*%h%m%=%14.(%l,%c%V%)\ %P


" Statusline with mode
"set statusline=%#WildMenu#\ %{StatuslineMode()}\ %*
"set statusline+=%#Visual#\ %t\ %*%y%h%m
"set statusline+=%=%F:%l:%c\ (%P)
set statusline=%#LineNr#\ %{StatuslineMode()}\ %*
"set statusline+=%{GitBranch()}
set statusline+=%#NonText#\ %{FileT()}\ %t\ %*%h%m
set statusline+=%=%<%F\ %#NonText#\ %l%c\ (%P)\ %*

" returns the current mode as uppercase 
function! StatuslineMode()
  let l:mode=mode()
  if l:mode==#"n"
    return "NORMAL"
  elseif l:mode==?"v"
    return "VISUAL"
  elseif l:mode==#"i"
    return "INSERT"
  elseif l:mode==#"R"
    return "REPLACE"
  elseif l:mode==?"s"
    return "SELECT"
  elseif l:mode==#"t"
    return "TERMINAL"
  elseif l:mode==#"c"
    return "COMMAND"
  elseif l:mode==#"!"
    return "SHELL"
  endif
endfunction

" Git branch function
function! GitBranch()
  let gitBranch = system("__git_ps1 '%s'")
  if strlen(gitBranch) > 0
    return ''.gitBranch
endfunction

" Returns the icon for the filetype
function! FileT()
  let filetypes = &filetype
  if filetypes == "vim"
    return ""
  elseif filetypes == "html"
    return ""
  elseif filetypes == "css"
    return ""
  elseif filetypes == "javascript"
    return ""
  elseif filetypes == "sh"
    return ""
  elseif filetypes == "help"
    return "ﲉ"
  elseif filetypes == "txt"
    return ""
  elseif filetypes == "yaml"
    return ""
  elseif filetypes == "markdown"
    return ""
  else
    return ""
  endif
endfunction


" Keymaps
" Setting the mapleader
let g:mapleader = 'ñ' " Mapleader is ñ
" Keymap for stop highlight
"map <esc> :noh <CR>
nnoremap <leader>/ :noh <CR>
"
