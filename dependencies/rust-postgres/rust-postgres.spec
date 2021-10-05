# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate postgres

Name:           rust-%{crate}
Version:        0.19.2
Release:        1%{?dist}
Summary:        Native, synchronous PostgreSQL client

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/postgres
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Native, synchronous PostgreSQL client.}

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

%package     -n %{name}+array-impls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+array-impls-devel %{_description}

This package contains library source intended for building other packages
which use "array-impls" feature of "%{crate}" crate.

%files       -n %{name}+array-impls-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+with-bit-vec-0_6-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+with-bit-vec-0_6-devel %{_description}

This package contains library source intended for building other packages
which use "with-bit-vec-0_6" feature of "%{crate}" crate.

%files       -n %{name}+with-bit-vec-0_6-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+with-chrono-0_4-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+with-chrono-0_4-devel %{_description}

This package contains library source intended for building other packages
which use "with-chrono-0_4" feature of "%{crate}" crate.

%files       -n %{name}+with-chrono-0_4-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+with-eui48-0_4-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+with-eui48-0_4-devel %{_description}

This package contains library source intended for building other packages
which use "with-eui48-0_4" feature of "%{crate}" crate.

%files       -n %{name}+with-eui48-0_4-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+with-eui48-1-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+with-eui48-1-devel %{_description}

This package contains library source intended for building other packages
which use "with-eui48-1" feature of "%{crate}" crate.

%files       -n %{name}+with-eui48-1-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+with-geo-types-0_6-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+with-geo-types-0_6-devel %{_description}

This package contains library source intended for building other packages
which use "with-geo-types-0_6" feature of "%{crate}" crate.

%files       -n %{name}+with-geo-types-0_6-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+with-geo-types-0_7-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+with-geo-types-0_7-devel %{_description}

This package contains library source intended for building other packages
which use "with-geo-types-0_7" feature of "%{crate}" crate.

%files       -n %{name}+with-geo-types-0_7-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+with-serde_json-1-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+with-serde_json-1-devel %{_description}

This package contains library source intended for building other packages
which use "with-serde_json-1" feature of "%{crate}" crate.

%files       -n %{name}+with-serde_json-1-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+with-time-0_2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+with-time-0_2-devel %{_description}

This package contains library source intended for building other packages
which use "with-time-0_2" feature of "%{crate}" crate.

%files       -n %{name}+with-time-0_2-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+with-time-0_3-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+with-time-0_3-devel %{_description}

This package contains library source intended for building other packages
which use "with-time-0_3" feature of "%{crate}" crate.

%files       -n %{name}+with-time-0_3-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+with-uuid-0_8-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+with-uuid-0_8-devel %{_description}

This package contains library source intended for building other packages
which use "with-uuid-0_8" feature of "%{crate}" crate.

%files       -n %{name}+with-uuid-0_8-devel
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
* Tue Oct 05 18:45:28 BST 2021 Alexander Manning <mail@alex-m.co.uk> - 0.19.2-1
- Initial package
