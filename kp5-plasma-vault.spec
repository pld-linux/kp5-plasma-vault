#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.27.6
%define		qtver		5.15.2
%define		kpname		plasma-vault

Summary:	KDE Plasma Vault
Name:		kp5-%{kpname}
Version:	5.27.6
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	691c482776250f6ea4de3ce69f9ba9ae
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	fontconfig-devel
BuildRequires:	kf5-attica-devel
BuildRequires:	kf5-kactivities-stats-devel
BuildRequires:	kf5-kauth-devel
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kdeclarative-devel
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-kglobalaccel-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-knotifyconfig-devel
BuildRequires:	kf5-kpeople-devel
BuildRequires:	kf5-krunner-devel
BuildRequires:	kf5-kwallet-devel
BuildRequires:	kf5-plasma-framework-devel
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xorg-driver-input-evdev-devel
BuildRequires:	xorg-driver-input-synaptics-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
Plasma Vault is an open-source encryption solution for KDE with which
you can create encrypted folders to contain private files of any
format.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%{_libdir}/qt5/plugins/kf5/kded/plasmavault.so
%{_libdir}/qt5/plugins/kf5/kfileitemaction/plasmavaultfileitemaction.so
%{_libdir}/qt5/plugins/plasma/applets/plasma_applet_vault.so
%{_datadir}/metainfo/org.kde.plasma.vault.appdata.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.vault
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.vault/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.vault/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.vault/contents/ui/VaultItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.vault/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.vault/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.plasma.vault/metadata.json
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.vault.desktop
