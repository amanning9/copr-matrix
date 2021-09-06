# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/go-check/check
%global goipath         github.com/go-check/check
%global commit          10cb98267c6cb43ea9cd6793f29ff4089c306974

%gometa

%global goaltipaths     launchpad.net/gocheck gopkg.in/check.v1

%global common_description %{expand:
Rich testing for the Go language.}

%global golicenses      LICENSE
%global godocs          README.md TODO

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Rich testing for the Go language

# Upstream license specification: BSD-2-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/kr/pretty)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Mon Sep 06 2021 Alexander Manning <mail@alex-m.co.uk> - 0-0.1%{?dist}.20210906git10cb982
- Initial package

