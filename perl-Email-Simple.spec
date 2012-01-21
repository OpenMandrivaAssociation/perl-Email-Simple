%define upstream_name     Email-Simple
%define upstream_version  2.100

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:    Simple parsing of RFC2822 message format and headers
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Email/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Email::Date::Format)

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

Obsoletes: perl-Email-Simple-Creator <= 1.424.0
Provides:  perl-Email-Simple-Creator  = 1.424.0

%description
Email::Simple is the first deliverable of the "Perl Email Project", a reaction
against the complexity and increasing bugginess of the Mail::* modules. In
contrast, Email::* modules are meant to be simple to use and to maintain, pared
to the bone, fast, minimal in their external dependencies, and correct.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Email
%{_mandir}/*/*
