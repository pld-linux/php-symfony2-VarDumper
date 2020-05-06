%define		package	VarDumper
%define		php_min_version 5.3.9
Summary:	Symfony2 VarDumper Component
Name:		php-symfony2-%{package}
Version:	2.8.52
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/var-dumper/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	2b4e829bf188b23b2fe89c7a65295025
URL:		https://symfony.com/doc/2.8/components/var_dumper.html
BuildRequires:	phpab
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(gd)
Requires:	php(iconv)
Requires:	php(json)
Requires:	php(mbstring)
Requires:	php(mysql)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php(xml)
Requires:	php-dirs >= 1.6
Suggests:	php(symfony_debug)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The VarDumper component creates a global dump() function that you can
use instead of e.g. var_dump. By using it, you'll gain:

- Per object and resource types specialized view to e.g. filter out
  Doctrine internals while dumping a single proxy entity, or get more
  insight on opened files with stream_get_meta_data;
- Configurable output formats: HTML or colored command line output;
- Ability to dump internal references, either soft ones (objects or
  resources) or hard ones (=& on arrays or objects properties). Repeated
  occurrences of the same object/array/resource won't appear again and
  again anymore. Moreover, you'll be able to inspect the reference
  structure of your data;
- Ability to operate in the context of an output buffering handler.

%prep
%setup -q -n var-dumper-%{version}

%build
phpab -n -e '*/Tests/*' -o autoloader.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
rm -r $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/Tests
rm -r $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/Test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_data_dir}/Symfony/Component/VarDumper
%{php_data_dir}/Symfony/Component/VarDumper/VarDumper.php
%{php_data_dir}/Symfony/Component/VarDumper/autoloader.php
%{php_data_dir}/Symfony/Component/VarDumper/Caster
%{php_data_dir}/Symfony/Component/VarDumper/Cloner
%{php_data_dir}/Symfony/Component/VarDumper/Dumper
%{php_data_dir}/Symfony/Component/VarDumper/Exception
%{php_data_dir}/Symfony/Component/VarDumper/Resources
