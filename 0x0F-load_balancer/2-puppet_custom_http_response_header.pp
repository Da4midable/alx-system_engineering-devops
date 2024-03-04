#!/usr/bin/bash
# File: 2-puppet_custom_http_response_header
package { 'nginx':
  ensure => installed,
}


file { '/etc/puppetlabs/facter/facts.d/hostname.rb':
  ensure  => present,
  content => "#!/usr/bin/ruby\nFacter.add('hostname') { setcode 'hostname' }",
  mode    => '0755',
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
    server {
      listen 80 default_server;
      server_name _;

      location / {
        add_header X-Served-By $::hostname;
        root /var/www/html;
        index index.html;
      }
    }
  ",
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
