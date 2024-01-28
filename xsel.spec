Summary:	X selection manipulation program
Summary(pl.UTF-8):	Program do manipulacji schowkiem X
Name:		xsel
Version:	1.2.1
Release:	1
License:	BSD-like
Group:		X11/Applications
#Source0Download: https://github.com/kfish/xsel/releases
Source0:	https://github.com/kfish/xsel/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a11b94ec0d664eca48d38cf6f4dea356
URL:		http://www.kfish.org/software/xsel/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.14
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
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
%doc AUTHORS COPYING ChangeLog README rant.txt release_notes
%attr(755,root,root) %{_bindir}/xsel
%{_mandir}/man1/xsel.1x*
