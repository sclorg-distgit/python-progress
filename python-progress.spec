%{?scl:%scl_package python-%{pypi_name}}
%{!?scl:%global pkg_name %{name}}

# Created by pyp2rpm-0.5.2
%global pypi_name progress

Name:           %{?scl_prefix}python-%{pypi_name}
Version:        1.2
Release:        4%{?dist}
Summary:        Easy to use progress bars

License:        ISC
URL:            http://github.com/verigak/progress/
Source0:        https://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-devel
BuildRequires:  python-setuptools
%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}

%description
Collection of easy to use progress bars and spinners.

%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{?scl:scl enable %{scl} - << \EOF}
%{__python} setup.py build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - << \EOF}
%{__python} setup.py install --skip-build --root %{buildroot} \
    --install-purelib %{python_sitelib}
%{?scl:EOF}

%files
%doc README.rst LICENSE
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Wed May 21 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2-4
- Rebuilt for devassist09

* Tue May 13 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Feb 18 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2-2
- Add missing BR: python{,3}-setuptools

* Tue Feb 18 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2-1
- Initial package.
