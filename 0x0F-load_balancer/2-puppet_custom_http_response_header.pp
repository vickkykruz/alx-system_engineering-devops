# custom_http_response_header.pp

# Check if puppetlabs-stdlib module is installed
$stdlib_module_installed = find_module('stdlib') ? {
  true  => true,
  false => false,
}

# Install puppetlabs-stdlib module if not installed
if $stdlib_module_installed == false {
  exec { 'install_stdlib_module':
    command => 'sudo puppet module install puppetlabs-stdlib',
    path    => ['/usr/bin', '/bin'],
    logoutput => true,
  }
}

# Updating Packages before performing installations
package { 'nginx':
  ensure => 'latest',
}

# Creating an index.html page
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Performing a "moved permanently redirection" (301)
file_line { 'nginx_redirect_config':
  path   => '/etc/nginx/sites-enabled/default',
  line   => 'server_name _;',
  match  => '.*',
  after  => '.*',
  ensure => present,
}

file { '/etc/nginx/sites-enabled/default':
  ensure  => file,
  content => "server_name _;\n\trewrite ^/redirect_me https://github.com/vickkykruz permanent;",
}

# Creating a 404 Custom error page
file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page",
}

file_line { 'nginx_404_config':
  path   => '/etc/nginx/sites-enabled/default',
  line   => 'listen 80 default_server;',
  match  => '.*',
  after  => '.*',
  ensure => present,
}

file { '/etc/nginx/sites-enabled/default':
  ensure  => file,
  content => "listen 80 default_server;\n\terror_page 404 /404.html;\n\tlocation = /404.html {\n\t\troot /var/www/html;\n\t\tinternal;\n\t}",
}

# Creating an HTTP response header
file_line { 'nginx_header_config':
  path   => '/etc/nginx/sites-enabled/default',
  line   => 'server_name _;',
  match  => '.*',
  after  => '.*',
  ensure => present,
}

file_line { 'nginx_header_addition':
  path   => '/etc/nginx/sites-enabled/default',
  line   => 'server_name _;',
  match  => '.*',
  after  => '.*',
  content => "add_header X-Served-By $hostname;",
}

# Testing configurations for syntax errors
exec { 'nginx_test_config':
  command => 'sudo nginx -t',
}

# Restart nginx after implementing changes
service { 'nginx':
  ensure    => 'running',
  subscribe => File['/etc/nginx/sites-enabled/default'],
}
