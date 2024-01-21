# replace the of php in wp-settings.php file

exec {'searchAndReplace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
