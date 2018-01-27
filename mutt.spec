#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xADEF768480316BDA (kevin@8t8.us)
#
Name     : mutt
Version  : 1.9.3
Release  : 34
URL      : ftp://ftp.mutt.org/pub/mutt/mutt-1.9.3.tar.gz
Source0  : ftp://ftp.mutt.org/pub/mutt/mutt-1.9.3.tar.gz
Source99 : ftp://ftp.mutt.org/pub/mutt/mutt-1.9.3.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: mutt-bin
Requires: mutt-doc
Requires: mutt-locales
BuildRequires : bison
BuildRequires : gdb
BuildRequires : gdbm
BuildRequires : gnupg
BuildRequires : idna
BuildRequires : krb5-dev
BuildRequires : libidn-dev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(com_err)
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(tokyocabinet)

%description
===================
When updating mutt from an earlier release or from Mercurial, please
make sure to read the compatibility notes in ``UPDATING''. Older changes
between mutt-1.2 and mutt-1.4 are listed in NEWS.

%package bin
Summary: bin components for the mutt package.
Group: Binaries

%description bin
bin components for the mutt package.


%package doc
Summary: doc components for the mutt package.
Group: Documentation

%description doc
doc components for the mutt package.


%package extras
Summary: extras components for the mutt package.
Group: Default

%description extras
extras components for the mutt package.


%package locales
Summary: locales components for the mutt package.
Group: Default

%description locales
locales components for the mutt package.


%prep
%setup -q -n mutt-1.9.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517088945
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static --with-mailpath=/var/spool/mail/ --enable-imap --enable-pop --enable-smtp --with-gss --with-gnutls --enable-sidebar --enable-hcache
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1517088945
rm -rf %{buildroot}
%make_install
%find_lang mutt
## make_install_append content
ln -s mutt %{buildroot}%{_bindir}/mail
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/smime_keys
/usr/bin/mail
/usr/bin/mutt
/usr/bin/pgpewrap
/usr/bin/pgpring

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/mutt/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*

%files extras
%defattr(-,root,root,-)
/usr/bin/smime_keys

%files locales -f mutt.lang
%defattr(-,root,root,-)

