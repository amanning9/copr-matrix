# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/ipfs/go-cid
%global goipath         github.com/ipfs/go-cid
Version:                0.1.0

%gometa

%global common_description %{expand:
Content ID v1 implemented in go.}

%global golicenses      LICENSE
%global godocs          README.md _rsrch/cidiface/README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Content ID v1 implemented in go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/multiformats/go-multibase)
BuildRequires:  golang(github.com/multiformats/go-multihash)
BuildRequires:  golang(github.com/multiformats/go-varint)

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
