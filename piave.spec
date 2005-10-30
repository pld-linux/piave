# TODO: consider separating more plugins into subpackages
Summary:	Multimedia render and effect engine
Summary(pl):	Silnik wy¶wietlania i robienia efektów multimedialnych
Name:		piave
Version:	0.2.4
Release:	3
Epoch:		1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/modesto/%{name}-%{version}.tar.gz
# Source0-md5:	fdf6e94f9fdaae5547e641109e50e7b1
Patch0:		%{name}-configure.patch
URL:		http://sourceforge.net/projects/modesto/
BuildRequires:	SDL-devel >= 1.1.8
BuildRequires:	SDL_image-devel
BuildRequires:	alsa-lib-devel >= 0.9.0
BuildRequires:	arts-devel >= 13:0.9.5
BuildRequires:	artsc-devel >= 13:0.9.5
BuildRequires:	autoconf
BuildRequires:	automake
#BuildRequires:	ffmpeg-devel
BuildRequires:	freetype-devel >= 2.1.0
BuildRequires:	libavc1394-devel >= 0.4.1
BuildRequires:	libdv-devel >= 0.98
BuildRequires:	libraw1394-devel
BuildRequires:	libsndfile-devel >= 1.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	libxml2-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PIAVE is render and effect engine for Modesto project. Modesto is a
professional non-linear video-, audio- and midi editor for GNU/Linux
written in C++ with the TOAD GUI Library.

%description -l pl
PIAVE jest silnikiem wy¶wietlania i robienia efektów dla projeku
Modesto. Modesto jest profesjonalnym nieliniowym edytorem wideo, audio
i midi dla GNU/Linux zakodowanym w C++ przy u¿yciu biblioteki GUI
TOAD.

%package iostream-arts
Summary:	aRts input/output stream plugin for piave
Summary(pl):	Wtyczka wej¶cia/wyj¶cia strumieni aRts dla piave
Group:		X11/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description iostream-arts
aRts input/output stream plugin for piave.

%description iostream-arts -l pl
Wtyczka wej¶cia/wyj¶cia strumieni aRts dla piave.

%package devel
Summary:	Header files required to build programs using piave
Summary(pl):	Pliki nag³ówkowe wymagane przez programy u¿ywaj±ce piave
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	SDL-devel >= 1.1.8
Requires:	SDL_image-devel
Requires:	libavc1394-devel >= 0.4.1
Requires:	libraw1394-devel
Requires:	libstdc++-devel
Requires:	libxml2-devel >= 2.0.0

%description devel
Header files required to build programs using piave.

%description devel -l pl
Pliki nag³ówkowe niezbêdne do kompilacji programów korzystaj±cych z
piave.

%package static
Summary:	Static piave library
Summary(pl):	Statyczna biblioteka piave
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static piave library.

%description static -l pl
Statyczna biblioteka piave.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
#	--with-ffmpeg - requires different version of ffmpeg
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/piave/plugins/*/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/piave
%attr(755,root,root) %{_libdir}/libpiave.so.*.*.*
%dir %{_libdir}/piave
%dir %{_libdir}/piave/plugins
%dir %{_libdir}/piave/plugins/effects
%attr(755,root,root) %{_libdir}/piave/plugins/effects/libalphablend.so
%attr(755,root,root) %{_libdir}/piave/plugins/effects/libimage.so
%attr(755,root,root) %{_libdir}/piave/plugins/effects/libinvert.so
%attr(755,root,root) %{_libdir}/piave/plugins/effects/libtextmaster.so
%dir %{_libdir}/piave/plugins/iostream
# R: alsa-lib
%attr(755,root,root) %{_libdir}/piave/plugins/iostream/libalsastream.so
%attr(755,root,root) %{_libdir}/piave/plugins/iostream/libavistream.so
## R: ffmpeg
#%attr(755,root,root) %{_libdir}/piave/plugins/iostream/libffstream.so
%attr(755,root,root) %{_libdir}/piave/plugins/iostream/libossstream.so
# R: libdv
%attr(755,root,root) %{_libdir}/piave/plugins/iostream/librawdvstream.so
%attr(755,root,root) %{_libdir}/piave/plugins/iostream/libsdlstream.so
# R: libsndfile
%attr(755,root,root) %{_libdir}/piave/plugins/iostream/libsndfilestream.so
# R: libvorbis
%attr(755,root,root) %{_libdir}/piave/plugins/iostream/libvorbisfilestream.so

%files iostream-arts
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/piave/plugins/iostream/libartsstream.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpiave.so
%{_libdir}/libpiave.la
%{_includedir}/libpiave

%files static
%defattr(644,root,root,755)
%{_libdir}/libpiave.a
