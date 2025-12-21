%define	major 2
%define	libname %mklibname fc14audiodecoder %{major}
%define	develname %mklibname -d fc14audiodecoder

Summary:	Future Composer and Hippel TFMX audio decoding library
Name:	libfc14audiodecoder
Version:	2.0.0
Release:	1
License:	GPLv2+
Group:	Sound
Url:	https://github.com/mschwendt/libfc14audiodecoder
Source0:	https://github.com/mschwendt/libfc14audiodecoder/releases/download/%{version}/%{name}-%{version}.tar.bz2

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
%description
Decode music files written on a Commodore Amiga using Future Composer and.
Hippel TFMX audio format.
This library provides a C API for an old audio decoder that has been used
in several plug-ins for versatile audio players like XMMS, BMP, Audacious
and GStreamer. It is based on unmaintained/stable code which used to be
a `Future Composer Reference Player for Linux'. Because of how the source
code has been imported into a CVS repository long since its last major
modification, the timestamps of the files in CVS and in released tarballs
do not reflect that the core of the decoder has not been changed for
years. Except for cosmetical adjustments, indentation, dropping of unused
pieces, and partial reorganization for OOP.

#-----------------------------------------------------------------------------

%package -n %{libname}
Summary: Shared library for decoding Future Composer music
Group: System/Libraries

%description -n %{libname}
Decode music files written on a Commodore Amiga using Future Composer and.
Hippel TFMX audio format.
This library provides a C API for an old audio decoder that has been used
in several plug-ins for versatile audio players like XMMS, BMP, Audacious
and GStreamer.

%files -n %{libname}
%doc README.md
%{_libdir}/%{name}.so.%{major}*

#-----------------------------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group:	Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{develname}
Decode music files written on a Commodore Amiga using Future Composer and.
Hippel TFMX audio format.
This package contains the development files for %{name}.

%files -n %{develname}
%{_includedir}/fc14audiodecoder.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
# Using clang causes the build to fail
export CC=gcc
export CXX=g++
%configure
%make_build


%install
%make_install

