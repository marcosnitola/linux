set number
set rnu
syntax on
"set cursorline
set showcmd
set autoindent
set ic
set mouse=a
 
"set statusline=
"set statusline+=\ %F\ %M\ %Y\ %r
"set statusline+=%=
"set statusline+=\ %l\ %c\ %p%%
set laststatus=2
"set shiftwidth=4
set tabstop=2
set expandtab

" Statusline custom 1
"set statusline=%<%f\ %h%m%r%=%-14.(%l,%c%V%)\ %P
"set statusline=\ %<%f\ %h%m%=%14.(%l,%c%V%)\ %P
set statusline=%#Visual#\ %<%f\ %*%h%m%=%14.(%l,%c%V%)\ %P


" Statusline with mode
"set statusline=%#WildMenu#\ %{StatuslineMode()}\ %*
"set statusline+=%#Visual#\ %t\ %*%y%h%m
"set statusline+=%=%F:%l:%c\ (%P)
set statusline=%#WildMenu#\ %{StatuslineMode()}\ %*
"set statusline+=%{GitBranch()}
set statusline+=%#Visual#\ %{FileT()}%<\ %t\ %*%h%m
set statusline+=%=%F%l%c\ (%P)
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

function! FileT()
  let filetypes = &filetype
  if filetypes == "vim"
    return ""
  elseif filetypes == "html"
    return ""
  elseif filetypes == "css"
    return ""
  elseif filetypes == "javascript"
    return ""
  elseif filetypes == "sh"
    return ""
  elseif filetypes == "help"
    return ""
  elseif filetypes == "txt"
    return ""
  elseif filetypes == "yaml"
    return ""
  elseif filetypes == "markdown"
    return ""
  else
    return ""
  endif
endfunction
