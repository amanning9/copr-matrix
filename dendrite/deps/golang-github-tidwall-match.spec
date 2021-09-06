# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/tidwall/match
%global goipath         github.com/tidwall/match
Version:                1.0.3

%gometa

%global common_description %{expand:
Simple string pattern matcher for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Simple string pattern matcher for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

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
* Mon Sep 06 2021 Alexander Manning <mail@alex-m.co.uk> - 1.0.3-1%{?dist}
- Initial package
