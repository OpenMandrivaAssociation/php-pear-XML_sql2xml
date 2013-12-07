%define	_class	XML
%define	_subclass	sql2xml
%define	modname	%{_class}_%{_subclass}

Summary:	Returns XML from a SQL-query
Name:		php-pear-%{modname}
Version:	0.3.4
Release:	11
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/XML_sql2xml/
Source0:	http://download.pear.php.net/package/%{modname}-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
This class takes a PEAR::DB-Result Object, a sql-query-string, an
array and/or an xml-string/file and returns a xml-representation of
it.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{modname}-%{version}/doc/*
%doc %{modname}-%{version}/%{_subclass}_ext.php
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{modname}.xml

