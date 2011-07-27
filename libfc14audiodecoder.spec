%define name libfc14audiodecoder
%define version 1.0.2
%define release %mkrel 2

%define major 1
%define libname %mklibname fc14audiodecoder %major
%define develname %mklibname -d fc14audiodecoder
Summary: Future Composer audio decoding library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://sourceforge.net/projects/xmms-fc/files/%name/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: Sound
Url: http://xmms-fc.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Decode music files written on a Commodore Amiga using Future Composer.

This library provides a C API for an old audio decoder that has been used
in several plug-ins for versatile audio players like XMMS, BMP, Audacious
and GStreamer. It is based on unmaintained/stable code which used to be
a `Future Composer Reference Player for Linux'. Because of how the source
code has been imported into a CVS repository long since its last major
modification, the timestamps of the files in CVS and in released tarballs
do not reflect that the core of the decoder has not been changed for
years. Except for cosmetical adjustments, indentation, dropping of unused
pieces, and partial reorganization for OOP.

%package -n %libname
Group: System/Libraries
Summary: Shared library for decoding Future Composer music
%description -n %libname
Decode music files written on a Commodore Amiga using Future Composer.

This library provides a C API for an old audio decoder that has been used
in several plug-ins for versatile audio players like XMMS, BMP, Audacious
and GStreamer. It is based on unmaintained/stable code which used to be
a `Future Composer Reference Player for Linux'. Because of how the source
code has been imported into a CVS repository long since its last major
modification, the timestamps of the files in CVS and in released tarballs
do not reflect that the core of the decoder has not been changed for
years. Except for cosmetical adjustments, indentation, dropping of unused
pieces, and partial reorganization for OOP.

%package -n %develname
Group: Development/C
Summary: Development files of %name
Requires: %libname = %version-%release
Provides: %name-devel = %version-%release

%description -n %develname
Decode music files written on a Commodore Amiga using Future Composer.

This library provides a C API for an old audio decoder that has been used
in several plug-ins for versatile audio players like XMMS, BMP, Audacious
and GStreamer. It is based on unmaintained/stable code which used to be
a `Future Composer Reference Player for Linux'. Because of how the source
code has been imported into a CVS repository long since its last major
modification, the timestamps of the files in CVS and in released tarballs
do not reflect that the core of the decoder has not been changed for
years. Except for cosmetical adjustments, indentation, dropping of unused
pieces, and partial reorganization for OOP.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files -n %libname
%defattr(-,root,root)
%doc README
%_libdir/%name.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%_libdir/%name.la
%_libdir/%name.so
%_includedir/fc14audiodecoder.h
