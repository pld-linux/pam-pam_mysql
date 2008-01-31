%define 	modulename pam_mysql
%define	_rc	RC1
%define	_rel	1
Summary:	PAM module for auth UNIX users using MySQL data base
Summary(pl.UTF-8):	moduł PAM uwierzytelniający użytkowników Linuksa poprzez bazę danych MySQL
Name:		pam-%{modulename}
Version:	0.7
Release:	0.%{_rc}.%{_rel}
Epoch:		0
License:	GPL
Group:		Base
Source0:	http://dl.sourceforge.net/pam-mysql/%{modulename}-%{version}%{_rc}.tar.gz
# Source0-md5:	6177183d7e98dc12f2e444c9fbd4f13c
URL:		http://sourceforge.net/projects/pam-mysql/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	mysql-devel
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Obsoletes:	pam_mysql
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir	/%{_lib}

%description
Pam_mysql aims to provide a backend neutral means of authenticating
users against an MySQL database.

%description -l pl.UTF-8
Moduł PAM pozwalający na uwierzytelnianie użytkowników Linuksa poprzez
bazę danych MySQL.

%prep
%setup -q -n %{modulename}-%{version}%{?_rc}
%{__sed} -i -e 's/sinclude(.*)//' configure.in

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} \
	CFLAGS="`mysql_config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install	\
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT/%{_lib}/security/pam_mysql.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog INSTALL NEWS README
%attr(755,root,root) /%{_lib}/security/pam_mysql.so
