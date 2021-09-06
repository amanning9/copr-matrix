# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/anacrolix/utp
%global goipath         github.com/anacrolix/utp
Version:                0.1.0

%gometa

%global common_description %{expand:
Use anacrolix/go-libutp instead.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Use anacrolix/go-libutp instead

# Upstream license specification: MPL-2.0
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/anacrolix/envpprof)
BuildRequires:  golang(github.com/anacrolix/missinggo)
BuildRequires:  golang(github.com/anacrolix/missinggo/inproc)
BuildRequires:  golang(github.com/anacrolix/missinggo/pproffd)
BuildRequires:  golang(github.com/anacrolix/sync)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/anacrolix/missinggo/leaktest)
BuildRequires:  golang(github.com/bradfitz/iter)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(golang.org/x/net/nettest)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Mon Sep 06 2021 Alexander Manning <mail@alex-m.co.uk> - 0.1.0-1%{?dist}
- Initial package

