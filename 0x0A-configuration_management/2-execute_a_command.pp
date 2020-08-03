# excecute a command
exec { 'pkill':
    command => 'pkill -x killmenow',
    path    => '/usr/bin/',
}
