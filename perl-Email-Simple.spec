%define modname	Email-Simple
%define modver 2.216

Summary:	Simple parsing of RFC2822 message format and headers
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Email/Email-Simple-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Email::Date::Format)
BuildRequires: perl(Capture::Tiny)
BuildRequires:	perl-devel
Obsoletes:	perl-Email-Simple-Creator <= 1.424.0
Provides:	perl-Email-Simple-Creator  = 1.424.0

%description
Email::Simple is the first deliverable of the "Perl Email Project", a reaction
against the complexity and increasing bugginess of the Mail::* modules. In
contrast, Email::* modules are meant to be simple to use and to maintain, pared
to the bone, fast, minimal in their external dependencies, and correct.

%prep
%setup -qn %{modname}-%{modver}

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
%{_mandir}/man3/*



