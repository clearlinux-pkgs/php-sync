#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
# autospec version: v3
# autospec commit: c1050fe
#
Name     : php-sync
Version  : 1.1.3
Release  : 62
URL      : https://pecl.php.net/get/sync-1.1.3.tgz
Source0  : https://pecl.php.net/get/sync-1.1.3.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: php-sync-lib = %{version}-%{release}
Requires: php-sync-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : perl(Getopt::Long)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
CubicleSoft PHP Extension:  Synchronization Objects (sync)
==========================================================

%package lib
Summary: lib components for the php-sync package.
Group: Libraries
Requires: php-sync-license = %{version}-%{release}

%description lib
lib components for the php-sync package.


%package license
Summary: license components for the php-sync package.
Group: Default

%description license
license components for the php-sync package.


%prep
%setup -q -n sync-1.1.3
cd %{_builddir}/sync-1.1.3
pushd ..
cp -a sync-1.1.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-sync
cp %{_builddir}/sync-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-sync/ecfd41d79faa61324c023968e6a2e56b968201c1 || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20230831/sync.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-sync/ecfd41d79faa61324c023968e6a2e56b968201c1
