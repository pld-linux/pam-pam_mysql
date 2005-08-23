%define 	modulename pam_mysql
Summary:	PAM module for auth UNIX users using MySQL data base
Summary(pl):	modu³ PAM uwierzytelniaj±cy u¿ytkowników Linuksa poprzez bazê danych MySQL
Name:		pam-%{modulename}
Version:	0.6.0
Release:	1
Epoch:		0
License:	GPL
Group:		Base
Source0:	http://dl.sourceforge.net/pam-mysql/%{modulename}-%{version}.tar.gz
# Source0-md5:	b7f59c5450d89126b7f25fa2645b1b71
URL:		http://sourceforge.net/projects/pam-mysql/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	mysql-devel
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
Obsoletes:	pam_mysql
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pam_mysql aims to provide a backend neutral means of authenticating
users against an MySQL database.

%description -l pl
Modu³ PAM pozwalaj±cy na uwierzytelnianie u¿ytkowników Linuksa poprzez
bazê danych MySQL.

%prep
%setup -q -n %{modulename}-%{version}
sed -i 's/sinclude(.*)//' configure.in

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install	\
	DESTDIR=$RPM_BUILD_ROOT

# install -D pam_mysql.so $RPM_BUILD_ROOT/%{_lib}/security/pam_mysql.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog INSTALL NEWS README
%attr(755,root,root) /%{_lib}/security/pam_mysql.so
