# Created by pyp2rpm-3.3.5
%global pypi_name maubot
%global forgeurl https://github.com/maubot/maubot

#global commit 7679a0e97cf842f47f083c01baa1ba4199266f9a

Version:        0.3.1

%{?python_enable_dependency_generator}

%forgemeta

Name:           %{pypi_name}
Release:        1%{?dist}
Summary:        A plugin-based Matrix bot system

License:        None
URL:            %{forgeurl}
Source0:        %forgesource
Source1:        maubot.service

Patch0:         config.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  systemd-rpm-macros
BuildRequires:  yarnpkg
BuildRequires:  nodejs

Requires:       systemd
Requires:       python3-feedparser

#Manually include the end-to-end dependencies.
Requires:       libolm-python3
Requires:       python3-unpaddedbase64
%py_provides    maubot+e2be

%description
A plugin-based [Matrix]() bot system written in Python.

%prep
%forgesetup
#autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

#Munge the maubot version.
sed -i "s/__version__.*$/__version__ = \"%{version}\"/g" maubot/__meta__.py

# Get some newer version 'cos fedora.
sed -i "s|click>=7,<8|click>=7,<9|g" requirements.txt
sed -i "s|SQLAlchemy>=1,<1.4|SQLAlchemy>=1,<1.5|g" requirements.txt

# Maubot does not keep up with the bridges.
sed -i "s|^mautrix.*|mautrix|g" requirements.txt

%build
%py3_build

pushd maubot/management/frontend
yarn
yarn build
popd

%install
%py3_install

mkdir -p %{buildroot}%{_datadir}/%{pypi_name}

mkdir -p %{buildroot}%{_sharedstatedir}/%{pypi_name}/plugin
mkdir -p %{buildroot}%{_sharedstatedir}/%{pypi_name}/crypto

mkdir -p %{buildroot}%{_sysconfdir}/%{pypi_name}
cp %{buildroot}/usr/example-config.yaml %{buildroot}%{_datadir}/%{pypi_name}/base-config.yaml
mv %{buildroot}/usr/example-config.yaml %{buildroot}%{_sysconfdir}/%{pypi_name}/config.yaml

install -p -D -T -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/maubot.service

cp -r maubot/management/frontend/build %{buildroot}%{_datadir}/%{pypi_name}/static

%post
%systemd_post maubot.service

%preun
%systemd_preun maubot.service

%postun
%systemd_postun_with_restart maubot.service

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%{_datadir}/%{pypi_name}
%dir %{_sysconfdir}/%{pypi_name}
%config(noreplace) %{_sysconfdir}/%{pypi_name}/config.yaml

%{_sharedstatedir}/%{pypi_name}

%{_bindir}/mbc

%{_unitdir}/maubot.service


%changelog
* Sun Feb 07 2021 Alex Manning <git@alex-m.co.uk> - 0.1.0-1
- Initial package.
