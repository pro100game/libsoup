
%define _snap 20030425

Summary:	SOAP (Simple Object Access Protocol) implementation in C
Summary(pl):	Implementacja w C SOAP (Simple Object Access Protocol)
Name:		libsoup
Version:	1.99.18
Release:	0.%{_snap}.1
License:	LGPL
Group:		X11/Libraries
Source0:	%{name}-%{version}-%{_snap}.tar.bz2
Patch0:		%{name}-build_doc.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It provides an queued asynchronous callback-based mechanism for
sending and servicing SOAP requests, and a WSDL (Web Service
Definition Language) to C compiler which generates client stubs and
server skeletons for easily calling and implementing SOAP methods.

%description -l pl
Pakiet dostarcza interfejs kolejkowalnego, asynchronicznego mechanizmu
do wysy�ania i serwowania ��da� SOAP oraz WSDL (Web Service Definition
Language) dla kompilatora C, kt�ry generuje klienckie stub i szkielety
serwer�w dla �atwego wywo�ywania i implementowania metod SOAP.

%package devel
Summary:	Include files etc to develop SOAP applications
Summary(pl):	Pliki nag��wkowe, dokumentacja dla SOAP
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files, etc you can use to develop SOAP applications.

%description devel -l pl
Pliki nag��wkowe itp. Jednym s�owem wszystko czego potrzebujesz aby
samemu tworzy� sobie aplikacje korzystaj�ce z SOAP.

%package static
Summary:	SOAP static libraries
Summary(pl):	Biblioteki statyczne SOAP
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
SOAP static libraries.

%description static -l pl
Biblioteki statyczne SOAP.

%prep
%setup  -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}

%configure \
	--enable-ssl \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	pkgconfigdir=%{_pkgconfigdir} \
	m4datadir=%{_aclocaldir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/libsoup-ssl-proxy

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_gtkdocdir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a