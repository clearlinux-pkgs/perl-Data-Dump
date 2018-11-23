#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Data-Dump
Version  : 1.23
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/G/GA/GAAS/Data-Dump-1.23.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GA/GAAS/Data-Dump-1.23.tar.gz
Summary  : 'Pretty printing of data structures'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
NAME
Data::Dump - Pretty printing of data structures
SYNOPSIS
use Data::Dump qw(dump ddx);

%package dev
Summary: dev components for the perl-Data-Dump package.
Group: Development
Provides: perl-Data-Dump-devel = %{version}-%{release}

%description dev
dev components for the perl-Data-Dump package.


%prep
%setup -q -n Data-Dump-1.23

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/Data/Dump.pm
/usr/lib/perl5/vendor_perl/5.28.0/Data/Dump/FilterContext.pm
/usr/lib/perl5/vendor_perl/5.28.0/Data/Dump/Filtered.pm
/usr/lib/perl5/vendor_perl/5.28.0/Data/Dump/Trace.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Data::Dump.3
/usr/share/man/man3/Data::Dump::Filtered.3
/usr/share/man/man3/Data::Dump::Trace.3
