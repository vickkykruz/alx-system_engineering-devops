# command to solve the request

exec {'start':
  provider => shell,
  command  => 'sudo sed -i "s/15/4000/" /etc/default/nginx;sudo service nginx restart'
}
