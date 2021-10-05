# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate phf

Name:           rust-%{crate}
Version:        0.10.0
Release:        1%{?dist}
Summary:        Runtime support for perfect hash function data structures

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/phf
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Runtime support for perfect hash function data structures.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc ../README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+macros-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+macros-devel %{_description}

This package contains library source intended for building other packages
which use "macros" feature of "%{crate}" crate.

%files       -n %{name}+macros-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+phf_macros-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+phf_macros-devel %{_description}

This package contains library source intended for building other packages
which use "phf_macros" feature of "%{crate}" crate.

%files       -n %{name}+phf_macros-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+proc-macro-hack-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+proc-macro-hack-devel %{_description}

This package contains library source intended for building other packages
which use "proc-macro-hack" feature of "%{crate}" crate.

%files       -n %{name}+proc-macro-hack-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+uncased-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+uncased-devel %{_description}

This package contains library source intended for building other packages
which use "uncased" feature of "%{crate}" crate.

%files       -n %{name}+uncased-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unicase-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unicase-devel %{_description}

This package contains library source intended for building other packages
which use "unicase" feature of "%{crate}" crate.

%files       -n %{name}+unicase-devel
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
* Tue Oct 05 19:02:20 BST 2021 Alexander Manning <mail@alex-m.co.uk> - 0.10.0-1
- Initial package