# create manifest that kills a process named `killmenow` using `exec` and `pkill`
exec { 'pkill -f killmenow':
  provider => 'shell'
}
