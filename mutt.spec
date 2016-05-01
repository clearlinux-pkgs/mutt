#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mutt
Version  : 1.6.1
Release  : 13
URL      : http://fossies.org/linux/misc/mutt-1.6.1.tar.gz
Source0  : http://fossies.org/linux/misc/mutt-1.6.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: mutt-bin
Requires: mutt-doc
Requires: mutt-locales
BuildRequires : bison
BuildRequires : gdb
BuildRequires : gnupg
BuildRequires : idna
BuildRequires : libidn-dev
BuildRequires : ncurses-dev

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


%package locales
Summary: locales components for the mutt package.
Group: Default

%description locales
locales components for the mutt package.


%prep
%setup -q -n mutt-1.6.1

%build
%configure --disable-static --with-mailpath=/var/spool/mail/
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
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
/usr/bin/flea
/usr/bin/mail
/usr/bin/mutt
/usr/bin/muttbug
/usr/bin/pgpewrap
/usr/bin/pgpring
/usr/bin/smime_keys

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/mutt/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*

%files locales -f mutt.lang 
%defattr(-,root,root,-)

