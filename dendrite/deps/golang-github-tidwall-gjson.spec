# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/tidwall/gjson
%global goipath         github.com/tidwall/gjson
Version:                1.9.0

%gometa

%global common_description %{expand:
Get JSON values quickly - JSON parser for Go.}

%global golicenses      LICENSE
%global godocs          README.md SYNTAX.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Get JSON values quickly - JSON parser for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/tidwall/match)
BuildRequires:  golang(github.com/tidwall/pretty)

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
* Mon Sep 06 2021 Alexander Manning <mail@alex-m.co.uk> - 1.9.0-1%{?dist}
- Initial package

