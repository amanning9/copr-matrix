# Generated by go2rpm 1.6.0
%bcond_without check

# https://github.com/mdp/qrterminal
%global goipath         github.com/mdp/qrterminal/v3
Version:                3.0.0

%gometa

%global common_description %{expand:
QR Codes in your terminal.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        QR Codes in your terminal

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

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
%doc CHANGELOG.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Mon Jun 13 2022 Alex Manning <mail@alex-m.co.uk> - 3.0.0-1
- Initial package
