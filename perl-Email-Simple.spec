%define module      Email-Simple
%define name        perl-%{module}
%define version     2.00.4
%define up_version  2.004
%define release     %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Simple parsing of RFC2822 message format and headers
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Email/%{module}-%{up_version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Email::Simple is the first deliverable of the "Perl Email Project", a reaction
against the complexity and increasing bugginess of the Mail::* modules. In
contrast, Email::* modules are meant to be simple to use and to maintain, pared
to the bone, fast, minimal in their external dependencies, and correct.

%prep
%setup -q -n %{module}-%{up_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

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


