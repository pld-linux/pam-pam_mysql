Summary:	PAM module for auth UNIX users using MySQL data base
Summary(pl):	modu³ PAM uwierzytelniaj±cy u¿ytkowników Linuksa poprzez bazê danych MySQL
Name:		pam-pam_mysql
Version:	0.5
Release:	1
License:	GPL
Group:		Base
# Source0-md5:	8cf002392292ae2a5774545324739a94
Source0:	http://dl.sourceforge.net/pam-mysql/pam_mysql-%{version}.tar.gz
URL:		http://sourceforge.net/projects/pam-mysql/
BuildRequires:	mysql-devel
BuildRequires:	pam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pam_mysql aims to provide a backend neutral means of authenticating
users against an MySQL database.

%description -l pl
Modu³ PAM pozwalaj±cy na uwierzytelnianie u¿ytkowników Linuksa poprzez
bazê danych MySQL.

%prep
%setup -q -n pam_mysql

%build
%{__make} CC="%{__cc}" CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D pam_mysql.so $RPM_BUILD_ROOT/lib/security/pam_mysql.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Readme Changelog
%attr(755,root,root) /lib/security/pam_mysql.so
