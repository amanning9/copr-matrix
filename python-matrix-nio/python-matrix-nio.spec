# Created by pyp2rpm-3.3.5
%global pypi_name matrix-nio

Name:           python-%{pypi_name}
Version:        0.19.0
Release:        1%{?dist}
Summary:        A Python Matrix client library, designed according to sans I/O principles

License:        None
URL:            https://github.com/poljar/matrix-nio
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
[![Build Status]( [![codecov]( [![license]( [![Documentation Status]( [![nio](

%{?python_extras_subpkg:%python_extras_subpkg -n %{name} -i %{python3_sitelib}/*.egg-info e2e}

%prep
%autosetup -n %{pypi_name}-%{version}

sed -i 's|aiofiles>=0.6.0,<0.7.0|aiofiles>=0.6.0,<0.8.0|g' setup.py

%build
%py3_build

%install
%py3_install

%files
%license LICENSE.md
%doc README.md
%{python3_sitelib}/nio
%{python3_sitelib}/matrix_nio-%{version}-py%{python3_version}.egg-info

%changelog
* Thu May 13 2021 Alex Manning <git@alex-m.co.uk> - 0.17.0-1
- Initial package.
