#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	DBI-SQLite
Summary:	Extension to Class::DBI for SQLite
Summary(pl.UTF-8):	Rozszerzenie Class::DBI dla SQLite
Name:		perl-Class-DBI-SQLite
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	25e80b9d2f2d66e6fc51d487f0894802
URL:		http://search.cpan.org/dist/Class-DBI-SQLite/
%if %{with tests}
BuildRequires:	perl-Class-DBI >= 0.85
BuildRequires:	perl-DBD-SQLite >= 0.07
BuildRequires:	perl-Ima-DBI >= 0.27
BuildRequires:	perl-SQL-Statement >= 1.004
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::DBI::SQLite is an extension to Class::DBI for DBD::SQLite,
which allows you to populate auto incremented row id after insert.
set_up_table method allows you to automate the setup of columns and
primary key by using of SQLite PRAGMA statement (with SQL::Statement
module).

%description -l pl.UTF-8
Class::DBI::SQLite to rozszerzenie Class::DBI dla DBD::SQLite,
pozwalające wypełniać automatycznie zwiększany identyfikator wiersza
po instrukcji INSERT. Metoda set_up_table pozwala zautomatyzować
ustawianie kolumn i klucza głównego poprzez użycie instrukcji SQLite
PRAGMA (przy użyciu modułu SQL::Statement).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Class/DBI/SQLite.pm
%{_mandir}/man3/*
