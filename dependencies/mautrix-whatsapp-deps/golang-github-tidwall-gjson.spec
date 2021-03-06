# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/tidwall/gjson
%global goipath         github.com/tidwall/gjson
Version:                1.14.1

%gometa

%global common_description %{expand:
Get JSON values quickly - JSON parser for Go.}

%global golicenses      LICENSE
%global godocs          SYNTAX.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Get JSON values quickly - JSON parser for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Mon Jun 13 2022 Alex Manning <mail@alex-m.co.uk> - 1.14.1-1
- Initial package
