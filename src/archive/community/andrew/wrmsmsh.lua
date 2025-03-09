msh = include 'msh/msh' -- get msh
wrms = include 'wrms/wrms' -- get wrms


-- init() and cleanup() are used by both scripts, so we have to redefine them to take care of both scripts
function init()
  msh.init()
  msh.g_redraw(g)
  
  params:add_separator() -- add a separator between param lists
  
  wrms.init()
  redraw()
end

function cleanup()
  msh.cleanup()
end