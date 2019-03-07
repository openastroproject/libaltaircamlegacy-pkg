%define debug_package %{nil}

Name:           libaltaircamlegacy
Version:        1.24.11330
Release:        0
Summary:        Legay Altair camera support library
License:	GPLv2+
Prefix:         %{_prefix}
Requires:       libaltaircam
Provides:       libaltaircamlegacy = %{version}-%{release}
Obsoletes:      libaltaircamlegacy < 1.24.11330
Source:         libaltaircamlegacy-%{version}.tar.gz
Patch0:         pkg-config.patch

%description
libaltaircamlegacy is a user-space driver for legacy Altair astronomy cameras.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       libaltaircamlegacy-devel = %{version}-%{release}
Obsoletes:      libaltaircamlegacy-devel < 1.24.11330

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p0

%build

sed -e "s!@LIBDIR@!%{_libdir}!g" -e "s!@VERSION@!%{version}!g" < \
    libaltaircamlegacy.pc.in > libaltaircamlegacy.pc

%install
mkdir -p %{buildroot}%{_libdir}/pkgconfig

case %{_arch} in
  x86_64)
    cp linux/x64/libaltaircam.so %{buildroot}%{_libdir}/libaltaircamlegacy.so.%{version}
    ;;
  *)
    echo "unknown target architecture %{_arch}"
    exit 1
    ;;
esac

ln -sf %{name}.so.%{version} %{buildroot}%{_libdir}/%{name}.so.1
cp *.pc %{buildroot}%{_libdir}/pkgconfig

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%{_libdir}/*.so.*

%files devel
%{_libdir}/pkgconfig/*.pc

%changelog
* Sat Jan 26 2019 James Fidell <james@openastroproject.org> - 1.24.11330
- Initial RPM release

