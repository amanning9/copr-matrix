# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/multiformats/go-base36
%global goipath         github.com/multiformats/go-base36
Version:                0.1.0

%gometa

%global common_description %{expand:
# FIXME}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        None

License:        # FIXME

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
* Mon Sep 06 2021 Alexander Manning <mail@alex-m.co.uk> - 0.1.0-1%{?dist}
- Initial package
