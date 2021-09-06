# Generated by go2rpm 1.5.0
%bcond_without check

# https://github.com/pressly/goose
%global goipath         github.com/pressly/goose
Version:                3.1.0

%gometa

%global common_description %{expand:
A database migration tool. Supports SQL migrations and Go functions.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        A database migration tool. Supports SQL migrations and Go functions

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/ClickHouse/clickhouse-go)
BuildRequires:  golang(github.com/denisenkom/go-mssqldb)
BuildRequires:  golang(github.com/go-sql-driver/mysql)
BuildRequires:  golang(github.com/lib/pq)
BuildRequires:  golang(github.com/mattn/go-sqlite3)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/ziutek/mymysql/godrv)
BuildRequires:  golang(io/fs)

%if %{with check}
# Tests
BuildRequires:  golang(embed)
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
%doc examples README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Mon Sep 06 2021 Alexander Manning <mail@alex-m.co.uk> - 3.1.0-1%{?dist}
- Initial package
