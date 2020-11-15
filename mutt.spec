#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xADEF768480316BDA (kevin@8t8.us)
#
Name     : mutt
Version  : 2.0.1
Release  : 68
URL      : ftp://ftp.mutt.org/pub/mutt/mutt-2.0.1.tar.gz
Source0  : ftp://ftp.mutt.org/pub/mutt/mutt-2.0.1.tar.gz
Source1  : ftp://ftp.mutt.org/pub/mutt/mutt-2.0.1.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: mutt-bin = %{version}-%{release}
Requires: mutt-info = %{version}-%{release}
Requires: mutt-license = %{version}-%{release}
Requires: mutt-locales = %{version}-%{release}
Requires: mutt-man = %{version}-%{release}
BuildRequires : OpenSP
BuildRequires : bison
BuildRequires : cyrus-sasl-dev
BuildRequires : docbook-utils
BuildRequires : gdbm
BuildRequires : gnupg
BuildRequires : idna
BuildRequires : krb5-dev
BuildRequires : libidn-dev
BuildRequires : lynx
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(com_err)
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(tokyocabinet)
BuildRequires : pkgconfig(zlib)
BuildRequires : texinfo

%description
When updating mutt from an earlier release or from Git, please
make sure to read the compatibility notes in ``UPDATING''.

%package bin
Summary: bin components for the mutt package.
Group: Binaries
Requires: mutt-license = %{version}-%{release}

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


%package license
Summary: license components for the mutt package.
Group: Default

%description license
license components for the mutt package.


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
%setup -q -n mutt-2.0.1
cd %{_builddir}/mutt-2.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605409283
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
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

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1605409283
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mutt
cp %{_builddir}/mutt-2.0.1/COPYRIGHT %{buildroot}/usr/share/package-licenses/mutt/9a05e4157c80d693ee0e8b9427a3b5c3176ed697
%make_install
%find_lang mutt
## install_append content
ln -s mutt %{buildroot}%{_bindir}/mail
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/flea
/usr/bin/mail
/usr/bin/mutt
/usr/bin/mutt_pgpring
/usr/bin/muttbug
/usr/bin/pgpewrap

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/mutt/*

%files extras
%defattr(-,root,root,-)
/usr/bin/smime_keys

%files info
%defattr(0644,root,root,0755)
/usr/share/info/mutt.info

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mutt/9a05e4157c80d693ee0e8b9427a3b5c3176ed697

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

