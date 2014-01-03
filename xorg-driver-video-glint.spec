Summary:	X.org video driver for GLINT/Permedia video chips
Summary(pl.UTF-8):	Sterownik obrazu X.org dla układów graficznych GLINT/Permedia
Name:		xorg-driver-video-glint
Version:	1.2.8
Release:	4
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-glint-%{version}.tar.bz2
# Source0-md5:	775579c67dc55ff4909de3638bafd19f
Patch0:		mibstore.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.8.0
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.99.1
BuildRequires:	xorg-proto-xf86dgaproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
%{?requires_xorg_xserver_videodrv}
Requires:	xorg-xserver-server >= 1.0.99.901
Provides:	xorg-driver-video
Obsoletes:	X11-driver-glint < 1:7.0.0
Obsoletes:	XFree86-3DLabs
Obsoletes:	XFree86-driver-glint < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for GLINT/Permedia video chips. It supports 3Dlabs
(GLINT MX, GLINT 500TX, GLINT 300SX, GLINT GAMMA, GLINT DELTA, GLINT
GAMMA2, Permedia, Permedia 2, Permedia 2v, Permedia 3, R3, R4) and
Texas Instruments (Permedia, Permedia 2) chips.

%description -l pl.UTF-8
Sterownik obrazu X.org dla układów graficznych GLINT/Permedia.
Obsługuje układy 3Dlabs (GLINT MX, GLINT 500TX, GLINT 300SX, GLINT
GAMMA, GLINT DELTA, GLINT GAMMA2, Permedia, Permedia 2, Permedia 2v,
Permedia 3, R3, R4) oraz Texas Instruments (Permedia, Permedia 2).

%prep
%setup -q -n xf86-video-glint-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README README.pm3
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/glint_drv.so
%{_mandir}/man4/glint.4*
