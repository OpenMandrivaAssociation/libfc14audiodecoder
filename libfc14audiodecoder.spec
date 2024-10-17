%define major 1
%define libname %mklibname fc14audiodecoder %major
%define develname %mklibname -d fc14audiodecoder
Summary: Future Composer audio decoding library
Name: libfc14audiodecoder
Version:	1.0.3
Release:	1
Source0: http://sourceforge.net/projects/xmms-fc/files/%name/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: Sound
Url: https://xmms-fc.sourceforge.net/

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
Provides: %name-devel = %{EVRD}

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
%makeinstall_std

%files -n %libname
%doc README
%_libdir/%name.so.%{major}*

%files -n %develname
%_libdir/%name.so
%_includedir/fc14audiodecoder.h


%changelog
* Wed Jul 27 2011 Götz Waschk <waschk@mandriva.org> 1.0.2-2mdv2012.0
+ Revision: 691854
- rebuild

* Mon Jul 26 2010 Götz Waschk <waschk@mandriva.org> 1.0.2-1mdv2011.0
+ Revision: 560847
- import libfc14audiodecoder


