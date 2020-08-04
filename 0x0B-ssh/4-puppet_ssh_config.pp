# create ssh client config file
file { '~/etc/ssd/config':
    ensure  => file,
    content => 'Host holb_server
    HostName 35.243.207.104
    User ubuntu
    IdentityFile ~/.ssh/holberton
    PasswordAuthentication no',
}
