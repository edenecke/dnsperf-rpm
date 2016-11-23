dnsperf - DNS server performance testing tools

Spec File from: http://pkgs.fedoraproject.org/cgit/rpms/dnsperf.git

Version: 2.1.0.0
Source: ftp://ftp.nominum.com/pub/nominum/dnsperf

Build Requires: bind-devel libcap-devel
Deployment:     gnuplot pcapy python-dns OR (--nodeps)

Notes:

Removed bind9-hmacsha.h as isc/hmacsha.h was available for our distribution
Removed example queryfile as data file was not necessary
