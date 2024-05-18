#!/usr/bin/env bash
# Define a class for Nginx configuration

class nginx {

  package { 'nginx':
    ensure => present,
  }

  service { 'nginx':
    ensure => running,
    enable => true,
  }

  file { '/etc/nginx/sites-available/default':
    ensure => present,
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    content => <<EOF

server {
    listen 80;
    server_name localhost;

    location / {
        root /var/www/html;
        index index.html;
    }

  location @404 {
    return 404 'Ceci n'est pas une page';
}

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}
EOF
  }

  file { '/etc/nginx/sites-enabled/default':
    ensure => link,
    target => '/etc/nginx/sites-available/default',
  }

  file { '/var/www/html':
    ensure => directory,
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0755',
  }

  file { '/var/www/html/index.html':
    ensure => present,
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0644',
    content => "<!DOCTYPE html><html><head><title>Hello World!</title></head><body><h1>Hello World!</h1></body></html>",
  }

  notify { '/etc/nginx/sites-available/default':
    subscribe => Package['nginx'],
  }
}

include nginx
