# install flask using puppet

exec { 'flask_install':
  command => 'pip3 install Flask==2.1.0',
  path    => '/usr/local/bin:/usr/bin',
}
