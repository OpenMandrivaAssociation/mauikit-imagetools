%define major 4

#define snapshot 20220106
%define libname %mklibname MauiKit-imagetools
%define oldlibname %mklibname MauiKit-imagetools 3
%define devname %mklibname -d MauiKit-imagetools

Name:		mauikit-imagetools
Version:	4.0.2
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	MauiKit ImageTools is a set of QtQuick components providing basic image editing capabilities.
Url:		https://mauikit.org/
Source0:	https://invent.kde.org/maui/mauikit-imagetools/-/archive/%{?snapshot:master/mauikit-imagetools-master.tar.bz2#/mauikit-imagetools-%{snapshot}.tar.bz2}%{!?snapshot:v%{version}/mauikit-imagetools-v%{version}.tar.bz2}
#Patch0:		mauikit-imagetools-2.1.0-fix-warnings.patch
#Patch1:		leptonica-1.83.patch
#Patch2:		mauikit-imagetools-exiv2-0.28.patch

License:	LGPL-2.1-or-later, CC0 1.0, BSD-2-Clause
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(tesseract)
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(MauiKit4)
BuildRequires:  cmake(Leptonica)
BuildRequires:  cmake(OpenCV)
BuildRequires:  cmake(KQuickImageEditor)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6ConfigWidgets)
#BuildRequires:	cmake(KDecoration2)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Declarative)
#BuildRequires:	cmake(KF5Plasma)
#BuildRequires:	cmake(KF5PlasmaQuick)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:  cmake(KExiv2Qt6)
BuildRequires:	cmake(Git)
BuildRequires:	cmake(KF6SyntaxHighlighting)
BuildRequires:	cmake(KF6Attica)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6WebEngineCore)
BuildRequires:  cmake(VulkanHeaders)
#BuildRequires:	qt5-qtgraphicaleffects
#BuildRequires:	qt5-qtdeclarative
#BuildRequires:	qt5-qtquickcontrols2
#BuildRequires:  kquickimageeditor
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
%rename %{oldlibname}
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
%autosetup -p1 -n %{name}-%{?snapshot:master}%{!?snapshot:v%{version}}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang mauikitimagetools

%files -f mauikitimagetools.lang
%{_libdir}/qt6/qml/org/mauikit/imagetools
%dir %{_datadir}/org/mauikit/imagetools
%{_datadir}/org/mauikit/imagetools/cities.db

%files -n %{libname}
%{_libdir}/libMauiKitImageTools4.so.%{major}*

%files -n %{devname}
%{_includedir}/MauiKit4/ImageTools
# FIXME this seems odd, but should be fixed upstream
%{_includedir}/MauiKit4/FileBrowsing/imagetools_version.h
%{_libdir}/cmake/MauiKitImageTools4
%{_libdir}/libMauiKitImageTools4.so
