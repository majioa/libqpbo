%define        _unpackaged_files_terminate_build 1
%define        origname qpbo

Name:          lib%{origname}
Version:       1.4.1
Release:       alt1
Summary:       QPBO implementation by Vladimir Kolmogorov as a system library
License:       BSD-2-Clause
Group:         Sciences/Mathematics
Url:           https://github.com/fgrsnau/libqpbo
Vcs:           https://github.com/fgrsnau/libqpbo.git

Source:        %name-%version.tar
Patch:         %name-%version-%release.patch
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gcc-common

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%ifarch x86_64 %ix86
%add_optflags -msse2
%endif

%description
Ready-to-use QPBO adaptation for OpenGM (original code courtesy of V.
Kolmogorov)

Implements algorithms for minimizing functions of binary variables with unary
and pairwise terms based on roof duality described in the following papers.


%package       devel
Group:         Development/C++
Summary:       QPBO implementation by Vladimir Kolmogorov as a system library development files.

%description   devel
Ready-to-use QPBO adaptation for OpenGM (original code courtesy of V.
Kolmogorov)

Implements algorithms for minimizing functions of binary variables with unary
and pairwise terms based on roof duality described in the following papers.


%package       devel-static
Group:         Development/C++
Summary:       QPBO implementation by Vladimir Kolmogorov as a system library static files.

%description   devel-static
Ready-to-use QPBO adaptation for OpenGM (original code courtesy of V.
Kolmogorov)

Implements algorithms for minimizing functions of binary variables with unary
and pairwise terms based on roof duality described in the following papers.


%prep
%setup
%autopatch

%build
%cmake_insource
%cmake_build

%install
%cmakeinstall_std


%files
%doc CHANGES.TXT
%_libdir/%{name}*.so.*

%files         devel
%doc CHANGES.TXT
%_libdir/%{name}*.so
%_includedir/%{origname}*
%_pkgconfigdir/%name.pc

%files         devel-static
%doc CHANGES.TXT
%_libdir/%{name}*.a


%changelog
* Sun Feb 11 2024 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt1
- initial build v1.4.1 for Sisyphus
