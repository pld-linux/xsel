Summary:	X selection manipulation program
Summary(pl.UTF-8):	Program do manipulacji schowkiem X
Name:		xsel
Version:	0.9.6
Release:	1
License:	BSD-like
Group:		Applications
Source0:	http://www.vergenet.net/~conrad/software/xsel/download/%{name}-%{version}.tar.gz
# Source0-md5:	cec2fb09a4101b7f2beab8094234e2f4
URL:		http://www.vergenet.net/~conrad/software/xsel/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XSel is a command-line program for getting and setting the contents of
the X selection. Normally this is only accessible by manually
highlighting information and pasting it with the middle mouse button.

%description -l pl.UTF-8
XSel to działający z linii poleceń program do pobierania i ustawiania
zawartości schowka X. Zwykle jest to dostępne tylko przez ręczne
podświetlanie informacji i wklejanie ich środkowym przyciskiem myszy.

%prep
%setup -q

%build
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1x*
