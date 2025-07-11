#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v27
# autospec commit: 65cf152
#
Name     : ibus-libpinyin
Version  : 1.16.4
Release  : 46
URL      : https://sourceforge.net/projects/libpinyin/files/ibus-libpinyin/ibus-libpinyin-1.16.4.tar.gz
Source0  : https://sourceforge.net/projects/libpinyin/files/ibus-libpinyin/ibus-libpinyin-1.16.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: ibus-libpinyin-data = %{version}-%{release}
Requires: ibus-libpinyin-libexec = %{version}-%{release}
Requires: ibus-libpinyin-license = %{version}-%{release}
Requires: ibus-libpinyin-locales = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : gettext
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(ibus-1.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libnotify)
BuildRequires : pkgconfig(libpinyin)
BuildRequires : pkgconfig(libsoup-3.0)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : sed
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
ibus-libpinyin
Intelligent Pinyin engine based on libpinyin for IBus
Description
It includes a Chinese Pinyin input method and a Chinese ZhuYin (Bopomofo) input method based on libpinyin for IBus.

%package data
Summary: data components for the ibus-libpinyin package.
Group: Data

%description data
data components for the ibus-libpinyin package.


%package libexec
Summary: libexec components for the ibus-libpinyin package.
Group: Default
Requires: ibus-libpinyin-license = %{version}-%{release}

%description libexec
libexec components for the ibus-libpinyin package.


%package license
Summary: license components for the ibus-libpinyin package.
Group: Default

%description license
license components for the ibus-libpinyin package.


%package locales
Summary: locales components for the ibus-libpinyin package.
Group: Default

%description locales
locales components for the ibus-libpinyin package.


%prep
%setup -q -n ibus-libpinyin-1.16.4
cd %{_builddir}/ibus-libpinyin-1.16.4
pushd ..
cp -a ibus-libpinyin-1.16.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1750773814
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --disable-lua-extension
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --disable-lua-extension
make  %{?_smp_mflags}
popd
%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1750773814
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ibus-libpinyin
cp %{_builddir}/ibus-libpinyin-%{version}/COPYING %{buildroot}/usr/share/package-licenses/ibus-libpinyin/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
%find_lang ibus-libpinyin
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/applications/ibus-setup-libbopomofo.desktop
/usr/share/applications/ibus-setup-libpinyin.desktop
/usr/share/glib-2.0/schemas/com.github.libpinyin.ibus-libpinyin.gschema.xml
/usr/share/ibus-libpinyin/db/english.db
/usr/share/ibus-libpinyin/db/table.db
/usr/share/ibus-libpinyin/default.xml
/usr/share/ibus-libpinyin/icons/chinese.svg
/usr/share/ibus-libpinyin/icons/english.svg
/usr/share/ibus-libpinyin/icons/full-punct.svg
/usr/share/ibus-libpinyin/icons/full.svg
/usr/share/ibus-libpinyin/icons/half-punct.svg
/usr/share/ibus-libpinyin/icons/half.svg
/usr/share/ibus-libpinyin/icons/ibus-bopomofo.svg
/usr/share/ibus-libpinyin/icons/ibus-pinyin.svg
/usr/share/ibus-libpinyin/icons/lua-converter.svg
/usr/share/ibus-libpinyin/icons/simp-chinese.svg
/usr/share/ibus-libpinyin/icons/trad-chinese.svg
/usr/share/ibus-libpinyin/network.txt
/usr/share/ibus-libpinyin/setup/config.py
/usr/share/ibus-libpinyin/setup/dicttreeview.py
/usr/share/ibus-libpinyin/setup/enginefile.py
/usr/share/ibus-libpinyin/setup/ibus-libpinyin-preferences.ui
/usr/share/ibus-libpinyin/setup/keyboardshortcut.py
/usr/share/ibus-libpinyin/setup/main2.py
/usr/share/ibus-libpinyin/setup/shortcuteditor.py
/usr/share/ibus/component/libpinyin.xml
/usr/share/metainfo/libpinyin.appdata.xml

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/ibus-engine-libpinyin
/usr/libexec/ibus-engine-libpinyin
/usr/libexec/ibus-setup-libpinyin

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ibus-libpinyin/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files locales -f ibus-libpinyin.lang
%defattr(-,root,root,-)

