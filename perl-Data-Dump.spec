#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Data-Dump
Version  : 1.25
Release  : 24
URL      : https://cpan.metacpan.org/authors/id/G/GA/GARU/Data-Dump-1.25.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GA/GARU/Data-Dump-1.25.tar.gz
Summary  : 'Pretty printing of data structures'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Data-Dump-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Data::Dump
==========
This module provides a few functions that traverse their
argument list and return a string containing Perl code that,
when C<eval>ed, produces a deep copy of the original arguments.

%package dev
Summary: dev components for the perl-Data-Dump package.
Group: Development
Provides: perl-Data-Dump-devel = %{version}-%{release}
Requires: perl-Data-Dump = %{version}-%{release}

%description dev
dev components for the perl-Data-Dump package.


%package perl
Summary: perl components for the perl-Data-Dump package.
Group: Default
Requires: perl-Data-Dump = %{version}-%{release}

%description perl
perl components for the perl-Data-Dump package.


%prep
%setup -q -n Data-Dump-1.25
cd %{_builddir}/Data-Dump-1.25

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Data::Dump.3
/usr/share/man/man3/Data::Dump::Filtered.3
/usr/share/man/man3/Data::Dump::Trace.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Data/Dump.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Dump/FilterContext.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Dump/Filtered.pm
/usr/lib/perl5/vendor_perl/5.34.0/Data/Dump/Trace.pm
