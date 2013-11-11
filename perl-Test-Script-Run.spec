%define upstream_name    Test-Script-Run
%define upstream_version 0.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Test the script with run
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/Test-Script-Run-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(IPC::Run3)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This module exports some subs to help test and run scripts in your dist's
bin/ directory, if the script path is not absolute.

Nearly all the essential code is stolen from Prophet::Test, we think subs
like those should live below 'Test::' namespace, that's why we packed them
and created this module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/Test/

%changelog
* Sat Jan 08 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 630637
- update to new version 0.05

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 552639
- update to 0.04

* Fri Apr 30 2010 Michael Scherer <misc@mandriva.org> 0.30.0-1mdv2010.1
+ Revision: 541127
- import perl-Test-Script-Run


* Fri Apr 30 2010 cpan2dist 0.03-1mdv
- initial mdv release, generated with cpan2dist

