# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/albertorestifo/dijkstra
%global goipath         github.com/albertorestifo/dijkstra
%global commit          aba76f725f72b3086bd6957f94692feb8a5f9bb9

%gometa

%global common_description %{expand:
Dijkstra shortest path problem solved in Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Dijkstra shortest path problem solved in Go

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
* Mon Sep 06 2021 Alexander Manning <mail@alex-m.co.uk> - 0-0.1%{?dist}.20210906gitaba76f7
- Initial package
