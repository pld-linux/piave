# TODO:
#   - Spread libraries among devel and main package (or even -static)
#   - Consider dividing into plugins packages.

Summary:	Multimedia render and effect engine
Summary(pl):	Silnik wy¶wietlania i robienia efektów multimedialnych
Name:		piave
Version:	0.2.4
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/modesto/%{name}-%{version}.tar.gz
# Source0-md5:	fdf6e94f9fdaae5547e641109e50e7b1
URL:		http://sourceforge.net/projects/modesto/
BuildRequires:	SDL-devel
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

%package devel
Summary:	Header file required to build programs using piave
Summary(pl):	Pliki nag³ówkowe wymagane przez programy u¿ywaj±ce piave
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files required to build programs using piave.

%description devel -l pl
Pliki nag³ówkowe niezbêdne do kompilacji programów korzystaj±cych z
piave.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
    DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/effects
%dir %{_libdir}/%{name}/plugins/iostream
%{_libdir}/lib%{name}.*
%{_libdir}/%{name}/*/*/lib*

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/lib%{name}
%{_includedir}/lib%{name}/*.hh
