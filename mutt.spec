#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0xADEF768480316BDA (kevin@8t8.us)
#
Name     : mutt
Version  : 2.2.12
Release  : 95
URL      : https://bitbucket.org/mutt/mutt/downloads/mutt-2.2.12.tar.gz
Source0  : https://bitbucket.org/mutt/mutt/downloads/mutt-2.2.12.tar.gz
Source1  : https://bitbucket.org/mutt/mutt/downloads/mutt-2.2.12.tar.gz.asc
Summary  : Text-based mail client
Group    : Development/Tools
License  : GPL-2.0
Requires: mutt-bin = %{version}-%{release}
Requires: mutt-info = %{version}-%{release}
Requires: mutt-locales = %{version}-%{release}
Requires: mutt-man = %{version}-%{release}
BuildRequires : OpenSP
BuildRequires : bison
BuildRequires : buildreq-configure
BuildRequires : cyrus-sasl-dev
BuildRequires : docbook-utils
BuildRequires : gdbm
BuildRequires : gnupg
BuildRequires : krb5-dev
BuildRequires : libidn-dev
BuildRequires : lynx
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(com_err)
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(tokyocabinet)
BuildRequires : pkgconfig(zlib)
BuildRequires : pypi-idna
BuildRequires : texinfo
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Mutt is a small but very powerful text based program for reading and sending
electronic mail under unix operating systems, including support for color
terminals, MIME, OpenPGP, and a threaded sorting mode.

%package bin
Summary: bin components for the mutt package.
Group: Binaries

%description bin
bin components for the mutt package.


%package doc
Summary: doc components for the mutt package.
Group: Documentation
Requires: mutt-man = %{version}-%{release}
Requires: mutt-info = %{version}-%{release}

%description doc
doc components for the mutt package.


%package extras
Summary: extras components for the mutt package.
Group: Default

%description extras
extras components for the mutt package.


%package info
Summary: info components for the mutt package.
Group: Default

%description info
info components for the mutt package.


%package locales
Summary: locales components for the mutt package.
Group: Default

%description locales
locales components for the mutt package.


%package man
Summary: man components for the mutt package.
Group: Default

%description man
man components for the mutt package.


%prep
%setup -q -n mutt-2.2.12
cd %{_builddir}/mutt-2.2.12
pushd ..
cp -a mutt-2.2.12 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1694443094
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static --with-mailpath=/var/spool/mail/ \
--enable-imap \
--enable-pop \
--enable-smtp \
--with-gss \
--with-gnutls \
--with-sasl \
--enable-sidebar \
--enable-hcache \
--enable-debug
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static --with-mailpath=/var/spool/mail/ \
--enable-imap \
--enable-pop \
--enable-smtp \
--with-gss \
--with-gnutls \
--with-sasl \
--enable-sidebar \
--enable-hcache \
--enable-debug
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1694443094
rm -rf %{buildroot}
pushd ../buildavx2/
%make_install_v3
popd
%make_install
%find_lang mutt
## install_append content
ln -s mutt %{buildroot}%{_bindir}/mail
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/mutt
/V3/usr/bin/mutt_pgpring
/V3/usr/bin/pgpewrap
/usr/bin/flea
/usr/bin/mail
/usr/bin/mutt
/usr/bin/mutt_pgpring
/usr/bin/muttbug
/usr/bin/pgpewrap

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/mutt/*

%files extras
%defattr(-,root,root,-)
/usr/bin/smime_keys

%files info
%defattr(0644,root,root,0755)
/usr/share/info/mutt.info

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mutt.1
/usr/share/man/man1/mutt_pgpring.1
/usr/share/man/man1/pgpewrap.1
/usr/share/man/man1/smime_keys.1
/usr/share/man/man5/mbox.5
/usr/share/man/man5/mmdf.5
/usr/share/man/man5/muttrc.5

%files locales -f mutt.lang
%defattr(-,root,root,-)

