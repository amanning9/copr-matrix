# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate eui48

Name:           rust-%{crate}
Version:        1.1.0
Release:        1%{?dist}
Summary:        Library to generate and parse IEEE EUI-48 and EUI-64, also known as MAC-48 media access control addresses

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/eui48
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Library to generate and parse IEEE EUI-48 and EUI-64, also known as MAC-48
media access control addresses. The IEEE claims trademarks on the names EUI-48
and EUI-64, in which EUI is an abbreviation for Extended Unique Identifier.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+disp_hexstring-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+disp_hexstring-devel %{_description}

This package contains library source intended for building other packages
which use "disp_hexstring" feature of "%{crate}" crate.

%files       -n %{name}+disp_hexstring-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rustc-serialize-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rustc-serialize-devel %{_description}

This package contains library source intended for building other packages
which use "rustc-serialize" feature of "%{crate}" crate.

%files       -n %{name}+rustc-serialize-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde_bytes-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_bytes-devel %{_description}

This package contains library source intended for building other packages
which use "serde_bytes" feature of "%{crate}" crate.

%files       -n %{name}+serde_bytes-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde_json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_json-devel %{_description}

This package contains library source intended for building other packages
which use "serde_json" feature of "%{crate}" crate.

%files       -n %{name}+serde_json-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Tue Oct 05 19:02:01 BST 2021 Alexander Manning <mail@alex-m.co.uk> - 1.1.0-1
- Initial package