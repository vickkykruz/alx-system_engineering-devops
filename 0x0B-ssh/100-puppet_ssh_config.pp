#!/usr/bin/env bash
# Let’s practice using Puppet to make changes to our configuration

exec { 'echo':
  path    => '/usr/bin:/bin',
  command => 'echo "    PasswordAuthentication no\n    IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
  returns => [0,1]
}
