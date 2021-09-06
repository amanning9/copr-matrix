# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/libp2p/go-libp2p
%global goipath         github.com/libp2p/go-libp2p
Version:                0.15.0~rc.1
%global tag             0.15.0-rc.1

%gometa

%global common_description %{expand:
Libp2p implementation in Go.}

%global golicenses      LICENSE
%global godocs          examples README.md p2p/net/README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Libp2p implementation in Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/gdamore/tcell/v2)
BuildRequires:  golang(github.com/gogo/protobuf/io)
BuildRequires:  golang(github.com/gogo/protobuf/proto)
BuildRequires:  golang(github.com/google/uuid)
BuildRequires:  golang(github.com/ipfs/go-datastore)
BuildRequires:  golang(github.com/ipfs/go-datastore/namespace)
BuildRequires:  golang(github.com/ipfs/go-datastore/query)
BuildRequires:  golang(github.com/ipfs/go-datastore/sync)
BuildRequires:  golang(github.com/ipfs/go-ipfs-util)
BuildRequires:  golang(github.com/ipfs/go-log/v2)
BuildRequires:  golang(github.com/jbenet/goprocess)
BuildRequires:  golang(github.com/jbenet/goprocess/context)
BuildRequires:  golang(github.com/libp2p/go-addr-util)
BuildRequires:  golang(github.com/libp2p/go-conn-security-multistream)
BuildRequires:  golang(github.com/libp2p/go-eventbus)
BuildRequires:  golang(github.com/libp2p/go-msgio/protoio)
BuildRequires:  golang(github.com/libp2p/go-netroute)
BuildRequires:  golang(github.com/libp2p/go-stream-muxer-multistream)
BuildRequires:  golang(github.com/libp2p/go-tcp-transport)
BuildRequires:  golang(github.com/libp2p/go-ws-transport)
BuildRequires:  golang(github.com/libp2p/zeroconf/v2)
BuildRequires:  golang(github.com/multiformats/go-multiaddr)
BuildRequires:  golang(github.com/multiformats/go-multiaddr-dns)
BuildRequires:  golang(github.com/multiformats/go-multiaddr/net)
BuildRequires:  golang(github.com/multiformats/go-multistream)
BuildRequires:  golang(github.com/rivo/tview)
BuildRequires:  golang(github.com/whyrusleeping/mdns)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/ipfs/go-detect-race)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

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
* Mon Sep 06 2021 Alexander Manning <mail@alex-m.co.uk> - 0.15.0-rc.1-1%{?dist}
- Initial package

