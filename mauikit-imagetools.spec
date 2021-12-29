%define major 2

%define libname %mklibname MauiKit-imagetools %{major}
%define devname %mklibname -d MauiKit-imagetools

Name:		mauikit-imagetools
Version:	2.1.0
Release:	1
Summary:	MauiKit ImageTools is a set of QtQuick components providing basic image editing capabilities.
Url:		http://mauikit.org/
Source0:	https://invent.kde.org/maui/mauikit-imagetools/-/archive/v%{version}/mauikit-imagetools-v%{version}.tar.bz2
Patch0:		mauikit-imagetools-2.1.0-fix-warnings.patch

License:	LGPL-2.1-or-later, CC0 1.0, BSD-2-Clause
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(MauiKit)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  cmake(KQuickImageEditor)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KDecoration2)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5PlasmaQuick)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(Git)
BuildRequires:	cmake(KF5SyntaxHighlighting)
BuildRequires:	cmake(KF5Attica)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5WebEngine)
BuildRequires:	qt5-qtgraphicaleffects
BuildRequires:	qt5-qtdeclarative
BuildRequires:	qt5-qtquickcontrols2
BuildRequires:  kquickimageeditor
Requires:	%{libname} = %{EVRD}

%description
Library for developing MAUI applications

MauiKit is a set of utilities and "templated" controls based on Kirigami and
QCC2 that follow the ongoing work on the Maui HIG.

It lets you quickly create a Maui application and access utilities and
widgets shared amoing the other Maui apps.

%package -n %{libname}
Summary:	Library files for mauikit-imagetools
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libname}
Library files for mauikit-imagetools

MauiKit is a set of utilities and "templated" controls based on Kirigami and
QCC2 that follow the ongoing work on the Maui HIG.

It lets you quickly create a Maui application and access utilities and
widgets shared amoing the other Maui apps.

%package -n %{devname}
Summary:	Development files for mauikit-imagetools
Group:		Development/KDE and Qt
Requires:	%{name} = %{EVRD}

%description -n %{devname}
Development files for mauikit-imagetools

MauiKit is a set of utilities and "templated" controls based on Kirigami and
QCC2 that follow the ongoing work on the Maui HIG.

It lets you quickly create a Maui application and access utilities and
widgets shared amoing the other Maui apps.


%prep
%autosetup -p1 -n %{name}-v%{version}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_libdir}/qt5/qml/org/mauikit/imagetools
%dir %{_datadir}/org/mauikit/imagetools
%{_datadir}/org/mauikit/imagetools/cities.db

%files -n %{libname}
%{_libdir}/libMauiKitImageTools.so.1*
%{_libdir}/libMauiKitImageTools.so.%{major}*

%files -n %{devname}
%{_includedir}/MauiKit/ImageTools
# FIXME this seems odd, but should be fixed upstream
%{_includedir}/MauiKit/FileBrowsing/imagetools_version.h
%{_libdir}/cmake/MauiKitImageTools
%{_libdir}/libMauiKitImageTools.so
