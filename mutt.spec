#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xADEF768480316BDA (kevin@8t8.us)
#
Name     : mutt
Version  : 1.11.1
Release  : 42
URL      : ftp://ftp.mutt.org/pub/mutt/mutt-1.11.1.tar.gz
Source0  : ftp://ftp.mutt.org/pub/mutt/mutt-1.11.1.tar.gz
Source99 : ftp://ftp.mutt.org/pub/mutt/mutt-1.11.1.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: mutt-bin = %{version}-%{release}
Requires: mutt-license = %{version}-%{release}
Requires: mutt-locales = %{version}-%{release}
Requires: mutt-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : cyrus-sasl-dev
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
When updating mutt from an earlier release or from Git, please
make sure to read the compatibility notes in ``UPDATING''.

%package bin
Summary: bin components for the mutt package.
Group: Binaries
Requires: mutt-license = %{version}-%{release}
Requires: mutt-man = %{version}-%{release}

%description bin
bin components for the mutt package.


%package doc
Summary: doc components for the mutt package.
Group: Documentation
Requires: mutt-man = %{version}-%{release}

%description doc
doc components for the mutt package.


%package extras
Summary: extras components for the mutt package.
Group: Default

%description extras
extras components for the mutt package.


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
%setup -q -n mutt-1.11.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1544564646
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static --with-mailpath=/var/spool/mail/ \
--enable-imap \
--enable-pop \
--enable-smtp \
--with-gss \
--with-gnutls \
--with-sasl \
--enable-sidebar \
--enable-hcache
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1544564646
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mutt
cp COPYRIGHT %{buildroot}/usr/share/package-licenses/mutt/COPYRIGHT
%make_install
%find_lang mutt
## install_append content
ln -s mutt %{buildroot}%{_bindir}/mail
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/smime_keys
/usr/bin/flea
/usr/bin/mail
/usr/bin/mutt
/usr/bin/mutt_pgpring
/usr/bin/muttbug
/usr/bin/pgpewrap

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/mutt/*
%doc /usr/share/info/*

%files extras
%defattr(-,root,root,-)
/usr/bin/smime_keys

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mutt/COPYRIGHT

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

