%define		_class		XML
%define		_subclass	sql2xml
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.3.4
Release:	9
Summary:	Returns XML from a SQL-query
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/XML_sql2xml/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
This class takes a PEAR::DB-Result Object, a sql-query-string, an
array and/or an xml-string/file and returns a xml-representation of
it.


%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/doc/*
%doc %{upstream_name}-%{version}/%{_subclass}_ext.php
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.4-6mdv2011.0
+ Revision: 667701
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.4-5mdv2011.0
+ Revision: 607169
- rebuild

* Wed Nov 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.4-4mdv2010.1
+ Revision: 464964
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.3.4-3mdv2010.0
+ Revision: 426678
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.3.4-2mdv2009.1
+ Revision: 321942
- rebuild

* Sat Aug 16 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.4-1mdv2009.0
+ Revision: 272602
- 0.3.4

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.3.2-10mdv2009.0
+ Revision: 224899
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-9mdv2008.1
+ Revision: 178572
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-8mdv2007.0
+ Revision: 82979
- Import php-pear-XML_sql2xml

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-8mdk
- new group (Development/PHP)

* Mon Jan 16 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-7mdk
- fix bad package.xml file (#20643)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-1mdk
- initial Mandriva package (PLD import)

