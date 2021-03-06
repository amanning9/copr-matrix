%{?python_enable_dependency_generator}

%global forgeurl https://github.com/mautrix/facebook
%global commit 203bb4bb45f78905de17dc185045ddbd67651f25
Version:    0.4.1~rc1

%forgemeta

Name:       mautrix-facebook
Release:    1%{?dist}
Summary:    Matrix to facebook messenger bridge written in python.
License:    ASL 2.0
URL:        %{forgeurl}
Source0:    %{forgesource}
Source1:    mautrix-facebook.service
BuildArch:  noarch

Patch0:     log.patch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd-rpm-macros

Requires:       systemd

#Manually include the end-to-end dependencies.
#This is because python-olm is called libolm-python3 in fedora.
Requires:       libolm-python3
Requires:       python3-unpaddedbase64
%py_provides    mautrix-facebook+e2be

Suggests:       mautrix-facebook+animated_stickers

%{?systemd_requires}

%description
Facebook to Matrix Bridge

%{?python_extras_subpkg:%python_extras_subpkg -n %{name} -i %{python3_sitelib}/*.egg-info metrics animated_stickers}

%prep
%forgesetup
%autopatch -p0

%build
%py3_build

%install
%py3_install

install -p -D -T -m 0600 %{buildroot}%{python3_sitelib}/mautrix_facebook/example-config.yaml %{buildroot}%{_sysconfdir}/mautrix/facebook/config.yaml
rm -r %{buildroot}%{_prefix}/example-config.yaml

install -p -D -T -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/mautrix-facebook.service

%post
%systemd_post mautrix-facebook.service

%preun
%systemd_preun mautrix-facebook.service

%postun
%systemd_postun_with_restart mautrix-facebook.service


%files
%license LICENSE
%doc *.md
%{python3_sitelib}/mautrix_facebook/
%{python3_sitelib}/mautrix_facebook*.egg-info/

%{python3_sitelib}/maufbapi/

%{_unitdir}/mautrix-facebook.service
%attr(755,root,root) %dir %{_sysconfdir}/mautrix/facebook
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/mautrix/facebook/*
