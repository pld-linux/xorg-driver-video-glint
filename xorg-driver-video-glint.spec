Summary:	X.org video driver for GLINT/Permedia video chips
Summary(pl):	Sterownik obrazu X.org dla uk³adów graficznych GLINT/Permedia
Name:		xorg-driver-video-glint
Version:	1.0.0.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/driver/xf86-video-glint-%{version}.tar.bz2
# Source0-md5:	395afc539197490e860306f8b73cf089
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xf86dgaproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRequires:	xorg-xserver-server-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for GLINT/Permedia video chips. It supports 3Dlabs
(GLINT MX, GLINT 500TX, GLINT 300SX, GLINT GAMMA, GLINT DELTA, GLINT
GAMMA2, Permedia, Permedia 2, Permedia 2v, Permedia 3, R3, R4) and
Texas Instruments (Permedia, Permedia 2) chips.

%description -l pl
Sterownik obrazu X.org dla uk³adów graficznych GLINT/Permedia.
Obs³uguje uk³ady 3Dlabs (GLINT MX, GLINT 500TX, GLINT 300SX, GLINT
GAMMA, GLINT DELTA, GLINT GAMMA2, Permedia, Permedia 2, Permedia 2v,
Permedia 3, R3, R4) oraz Texas Instruments (Permedia, Permedia 2).

%prep
%setup -q -n xf86-video-glint-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	drivermandir=%{_mandir}/man4

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc DRI.txt README.pm3
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/glint_drv.so
%{_mandir}/man4/glint.4x*
