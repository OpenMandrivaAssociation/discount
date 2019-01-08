%define major 2
%define libname %mklibname markdown %{major}
%define develname %mklibname markdown -d

Summary:	A C implementation of the Markdown language
Name:		discount
Version:	2.2.4
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.pell.portland.or.us/~orc/Code/discount
Source0:	https://github.com/Orc/discount/archive/v%{version}.tar.gz
Patch0:		https://src.fedoraproject.org/rpms/discount/raw/master/f/discount-dont-run-ldconfig.patch

%description
%{summary}.

%files
%{_bindir}/markdown
%{_bindir}/makepage
%{_bindir}/mkd2html
%{_bindir}/theme
%{_mandir}/man1/*.1*
%{_mandir}/man7/*.7*

#-----------------------------------------------------------------------

%package -n %{libname}
Summary:	%{summary}
Group:		System/Libraries

%description -n %{libname}
This package contains the library needed to run programs
dynamically linked with discount

%files -n %{libname}
%{_libdir}/lib*.so.*

#-----------------------------------------------------------------------

%package -n %{develname}
Summary:	%{summary} header files
Group:		Development/Other
Requires:	%{libname} = %{EVRD}

%description -n %{develname}
This package provides headers files for discount development.

%files -n %{develname}
%{_includedir}/mkdio.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.3*

#-----------------------------------------------------------------------

%prep
%autosetup -p1
CFLAGS='%{optflags}' ./configure.sh \
	--shared \
	--prefix=%{_prefix} \
	--execdir=%{_bindir} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir} \
	--enable-all-features \
	--with-fenced-code \
	--pkg-config

%build
%make_build

%install
%make install.everything DESTDIR="%{buildroot}"

%check
%make test