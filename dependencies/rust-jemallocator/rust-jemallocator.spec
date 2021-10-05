# Generated by rust2rpm 16
%bcond_without check
%global debug_package %{nil}

%global crate jemallocator

Name:           rust-%{crate}
Version:        0.3.2
Release:        1%{?dist}
Summary:        Rust allocator backed by jemalloc

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/jemallocator
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Rust allocator backed by jemalloc.}

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

%package     -n %{name}+alloc_trait-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc_trait-devel %{_description}

This package contains library source intended for building other packages
which use "alloc_trait" feature of "%{crate}" crate.

%files       -n %{name}+alloc_trait-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+background_threads-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+background_threads-devel %{_description}

This package contains library source intended for building other packages
which use "background_threads" feature of "%{crate}" crate.

%files       -n %{name}+background_threads-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+background_threads_runtime_support-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+background_threads_runtime_support-devel %{_description}

This package contains library source intended for building other packages
which use "background_threads_runtime_support" feature of "%{crate}" crate.

%files       -n %{name}+background_threads_runtime_support-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+debug-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+debug-devel %{_description}

This package contains library source intended for building other packages
which use "debug" feature of "%{crate}" crate.

%files       -n %{name}+debug-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+disable_initial_exec_tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+disable_initial_exec_tls-devel %{_description}

This package contains library source intended for building other packages
which use "disable_initial_exec_tls" feature of "%{crate}" crate.

%files       -n %{name}+disable_initial_exec_tls-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+profiling-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+profiling-devel %{_description}

This package contains library source intended for building other packages
which use "profiling" feature of "%{crate}" crate.

%files       -n %{name}+profiling-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+stats-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+stats-devel %{_description}

This package contains library source intended for building other packages
which use "stats" feature of "%{crate}" crate.

%files       -n %{name}+stats-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+unprefixed_malloc_on_supported_platforms-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unprefixed_malloc_on_supported_platforms-devel %{_description}

This package contains library source intended for building other packages
which use "unprefixed_malloc_on_supported_platforms" feature of "%{crate}" crate.

%files       -n %{name}+unprefixed_malloc_on_supported_platforms-devel
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
* Tue Oct 05 18:44:01 BST 2021 Alexander Manning <mail@alex-m.co.uk> - 0.3.2-1
- Initial package