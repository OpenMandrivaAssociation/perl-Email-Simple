%define upstream_name     Email-Simple
%define upstream_version  2.100

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Simple parsing of RFC2822 message format and headers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Email/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Email::Date::Format)
BuildRequires:	perl-devel

BuildArch:	noarch

Obsoletes:	perl-Email-Simple-Creator <= 1.424.0
Provides:	perl-Email-Simple-Creator  = 1.424.0

%description
Email::Simple is the first deliverable of the "Perl Email Project", a reaction
against the complexity and increasing bugginess of the Mail::* modules. In
contrast, Email::* modules are meant to be simple to use and to maintain, pared
to the bone, fast, minimal in their external dependencies, and correct.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Email
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.100.0-5mdv2012.0
+ Revision: 765196
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.100.0-4
+ Revision: 763712
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.100.0-3
+ Revision: 667127
- mass rebuild

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 2.100.0-2mdv2011.0
+ Revision: 560954
- email::simple::creator now merged within email::simple

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 2.100.0-1mdv2010.1
+ Revision: 461360
- adding missing buildrequires:
- update to 2.100

* Sun Mar 22 2009 Funda Wang <fwang@mandriva.org> 2.5.0-1mdv2009.1
+ Revision: 360218
- fix version

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - new release
    - standardized version

* Mon Aug 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.00.4-1mdv2009.0
+ Revision: 270908
- new version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.00.3-3mdv2009.0
+ Revision: 223677
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 2.00.3-2mdv2008.1
+ Revision: 180394
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.00.3-1mdv2008.0
+ Revision: 55631
- update to new version 2.00.3


* Fri Mar 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.99.8-1mdv2007.1
+ Revision: 138839
- new version

* Tue Nov 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.99.6-1mdv2007.1
+ Revision: 87873
- new version

* Fri Nov 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.99.5-1mdv2007.1
+ Revision: 85089
- new version
- Import perl-Email-Simple

* Sat Sep 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.99.0-1mdv2007.0
- New version (upstream version 1.990)

* Sat Aug 26 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.98.0-1mdv2007.0
- New version (upstream version: 1.980)

* Mon Mar 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.92-2mdk
- fix summary

* Mon Mar 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.92-1mdk
- first mdk release

