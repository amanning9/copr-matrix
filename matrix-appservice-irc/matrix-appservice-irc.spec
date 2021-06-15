%global forgeurl https://github.com/matrix-org/matrix-appservice-irc
Version: 0.26.1
%global tag %version

%forgemeta

Name:           matrix-appservice-irc
Release:        1%{?dist}
Summary:        Matrix Bridge for IRC.

License:        Apache 2
URL:            %forgeurl
Source0:        %forgesource
Source1:        %{name}.service

BuildRequires:  nodejs-devel
BuildRequires:  npm
BuildRequires:  systemd-rpm-macros
BuildRequires:  git
BuildRequires:  make

Requires:       nodejs

%global debug_package %{nil}

%description
Matrix bridge for IRC.

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%prep
%forgesetup

%build
npm install --no-audit --no-fund --omit=dev
chmod -R -x+X *

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{name}
cp -pr \
    package.json \
    app.js \
    bin \
    %{buildroot}%{nodejs_sitelib}/%{name}
cp -pr node_modules %{buildroot}%{nodejs_sitelib}/%{name}

install -m 644 -D config.sample.yaml %{buildroot}%{_sysconfdir}/%{name}/config.yaml
install -m 644 -D %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

%files
%license LICENSE
%doc README.md
%{nodejs_sitelib}/%{name}
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/%{name}

%changelog
* Fri Feb 26 12:10:49 GMT 2021 Alex Manning <git@alex-m.co.uk>
-