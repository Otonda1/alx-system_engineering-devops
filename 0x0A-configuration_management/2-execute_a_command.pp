#using pkill to terminate a process using puppet

exec { 'puppet_using_pkill':
  command => 'pkill killmenow',
  path    => '/usr/bin',
}
