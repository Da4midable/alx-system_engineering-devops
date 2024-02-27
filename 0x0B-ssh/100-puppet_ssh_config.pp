#!/usr/bin/env bash
# using Puppet to make changes to configuration file

file { '/etc/ssh/ssh_config':
	ensure => present, 
}

file_line { 'Turn off passwd auth':
	path => '/etc/ssh/ssh_config',
	line => 'PasswordAuthentication no',
	match => '^#PasswordAuthentication',
}

file_line { 'Declare identity file':
	path => '/etc/ssh/ssh_config',
	line => 'IdentityFile ~/.ssh/school',
	match => '^#IdentityFile',
}
