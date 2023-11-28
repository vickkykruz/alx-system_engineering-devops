# File to config nginx setup

exec { 'update':
  command => 'app-get -y update',
  path => '/usr/bin/',
}

package { 'nginx':
  ensure => installed,
   name => 'nginx',
  provider => 'apt',
}

# Define Nginx services
service { 'nginx':
  ensure => running,
  enable => true,
  require => Package['nginx'],
}

# Configure Nginx site
file { '/etc/nginx/sites-available/default':
  ensure => present,
  content => "
   server {
     listen 80;
     location / {
       return 200 'Hello World';
     }
     location /redirect_me {
       return 301 http://\$host/;
     }
   }
  ",
  notify => Service['nginx'],
}

# Reload Nginx after changes
exec { 'nginx_reload':
  command => '/usr/sbin/service nginx reload',
  refreshonly => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
