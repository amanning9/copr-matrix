# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/multiformats/go-multihash
%global goipath         github.com/multiformats/go-multihash
Version:                0.0.16

%gometa

%global common_description %{expand:
Multihash implementation in Go.}

%global golicenses      LICENSE multihash/LICENSE
%global godocs          README.md multihash/README.md opts/README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Multihash implementation in Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/minio/blake2b-simd)
BuildRequires:  golang(github.com/minio/sha256-simd)
BuildRequires:  golang(github.com/mr-tron/base58/base58)
BuildRequires:  golang(github.com/multiformats/go-varint)
BuildRequires:  golang(golang.org/x/crypto/blake2s)
BuildRequires:  golang(golang.org/x/crypto/sha3)

%description
%{common_description}

%gopkg

%prep
%goprep
# spec test fails
rm spec_test.go

%build
for cmd in multihash; do
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
%license LICENSE multihash/LICENSE
%doc README.md multihash/README.md opts/README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Mon Sep 06 2021 Alexander Manning <mail@alex-m.co.uk> - 0.0.16-1%{?dist}
- Initial package