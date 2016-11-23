Summary: Benchmarking authorative and recursing DNS servers
Name: dnsperf
Version: 2.1.0.0
Release: 1%{?dist}
License: MIT
Url: http://www.nominum.com/support/measurement-tools/
Source: ftp://ftp.nominum.com/pub/nominum/dnsperf/%{version}/dnsperf-src-%{version}-1.tar.gz
Group: Applications/Internet
BuildRequires: bind-devel >= 9.3.0, libcap-devel, gzip, openssl-devel
BuildRequires: krb5-devel, libxml2-devel, GeoIP-devel
Requires: gnuplot pcapy python-dns

%description
This is dnsperf, a collection of DNS server performance testing tools.
For more information, see the dnsperf(1) and resperf(1) man pages.

%prep
%setup -q -n dnsperf-src-%{version}-1

%configure

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS -I/usr/include/bind9 -I." %{?_smp_mflags}

%install
rm -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install
install contrib/queryparse/queryparse %{buildroot}/%{_bindir}
install -D -m 644 contrib/queryparse/queryparse.1 %{buildroot}/%{_mandir}/man1/queryparse.1
gzip %{buildroot}/%{_mandir}/man1/queryparse.1

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root,-)
%doc README RELEASE_NOTES
%{_bindir}/*
%{_mandir}/*/*

%changelog
* Wed Nov 23 2016 - 2.1.0.0-1
- Removed queryfile and hmacsha

* Wed Apr 20 2016 Paul Wouters <pwouters@redhat.com> - 2.1.0.0-1
- Updated to 2.1.0.0 (rhbz#1305929)
- Remove incorporated patches
- Updated example query file with upstream
- Fixup bad changelog dates
- Use gunzip not bunzip2 as upstream query file is only gzipped
