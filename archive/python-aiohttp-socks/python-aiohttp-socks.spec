%{?python_enable_dependency_generator}
%global pypi_name aiohttp-socks
%global srcname aiohttp_socks
%global _description \
SOCKS proxy connector for aiohttp. SOCKS4(a) and SOCKS5 are supported.

Name:           python-%{pypi_name}
Version:        0.6.0
Release:        1%{?dist}
Summary:        SOCKS proxy connector for aiohttp

License:        ASL 2.0
URL:            https://pypi.org/project/aiohttp-socks/
Source:         %{pypi_source}

BuildArch:      noarch

%description %{_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}
rm -vrf *.egg-info
sed -i -e 's/\r//' README.md

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.egg-info/

%changelog
* Sun Mar 28 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.6.0-1
- Update to 0.6.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 10 2020 Timothy Redaelli <tredaelli@redhat.com> - 0.5.3-1
- Update to 0.5.3 (the last version that doesn't need python-socks) (#1785253)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Dec 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.2-1
- Update to 0.2.2

* Sun Dec 30 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-1
- Initial package
