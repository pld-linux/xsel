Summary:	X selection manipulation program
Summary(pl):	Program do manipulacji schowkiem X
Name:		xsel
Version:	0.9.6
Release:	1
License:	BSD-like
Group:		Applications
Source0:	http://www.vergenet.net/~conrad/software/xsel/download/%{name}-%{version}.tar.gz
# Source0-md5:	cec2fb09a4101b7f2beab8094234e2f4
URL:		http://www.vergenet.net/~conrad/software/xsel/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XSel is a command-line program for getting and setting the contents of
the X selection. Normally this is only accessible by manually
highlighting information and pasting it with the middle mouse button.

%description -l pl
XSel to dzia³aj±cy z linii poleceñ program do pobierania i ustawiania
zawarto¶ci schowka X. Zwykle jest to dostêpne tylko przez rêczne
pod¶wietlanie informacji i wklejanie ich ¶rodkowym przyciskiem myszy.

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
