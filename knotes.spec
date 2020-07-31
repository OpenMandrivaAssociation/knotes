%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE notes application
Name:		knotes
Version:	20.07.90
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	cmake(Grantlee5)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DNSSD)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5GlobalAccel)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5ItemModels)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5AkonadiNotes)
BuildRequires:	cmake(KF5AkonadiMime)
BuildRequires:	cmake(KF5CalendarUtils)
BuildRequires:	cmake(KF5KontactInterface)
BuildRequires:	cmake(KF5Libkdepim)
BuildRequires:	cmake(KF5Mime)
BuildRequires:	cmake(KF5PimCommonAkonadi)
BuildRequires:	cmake(KF5PimTextEdit)
BuildRequires:	cmake(KF5AkonadiSearch)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5GrantleeTheme)
BuildRequires:	xsltproc
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	pkgconfig(x11)
Requires:	akonadi-notes-agent
Requires:	kdepim-runtime

%description
KNotes aims to be a useful and full featured notes application for
the KDE project. It tries to be as fast and lightweight as possible
although including some advanced features.

%files -f all.lang
%{_kde5_applicationsdir}/org.kde.knotes.desktop
%{_bindir}/knotes
%{_datadir}/config.kcfg/knotesglobalconfig.kcfg
%{_datadir}/config.kcfg/notesagentsettings.kcfg
%{_datadir}/kconf_update/knotes*
%dir %{_datadir}/knotes/
%{_datadir}/knotes/*
%{_datadir}/kontact/ksettingsdialog/knotes.setdlg
%{_docdir}/*/*/knotes
%{_iconsdir}/hicolor/*/actions/knotes_*.*
%{_iconsdir}/hicolor/*/apps/knotes.*
%{_kde5_services}/kcmknotessummary.desktop
%{_kde5_services}/knote_*.desktop
%{_kde5_services}/kontact/knotesplugin.desktop
%{_datadir}/qlogging-categories5/knotes.categories
%{_datadir}/qlogging-categories5/knotes.renamecategories
%{_datadir}/knsrcfiles/knotes_printing_theme.knsrc
%{_kde5_xmlguidir}/knotes/*.rc
%{_datadir}/metainfo/org.kde.knotes.appdata.xml
%{_datadir}/dbus-1/interfaces/org.kde.KNotes.xml
%{_datadir}/dbus-1/interfaces/org.kde.kontact.KNotes.xml
%{_qt5_plugindir}/kcm_knote.so
%{_qt5_plugindir}/kcm_knotessummary.so
%{_qt5_plugindir}/kontact5/kontact_knotesplugin.so

#-----------------------------------------------------------------------------

%package -n akonadi-notes-agent
Summary:	Akonadi notes agent
Group:		Graphical desktop/KDE
Requires:	knotes

%description -n akonadi-notes-agent
Akonadi notes agent. It adds notes received via network and handles note
alarm notifications.

%files -n akonadi-notes-agent -f akonadi_notes_agent.lang
%{_bindir}/akonadi_notes_agent
%{_datadir}/akonadi/agents/notesagent.desktop
%{_docdir}/*/*/akonadi_notes_agent
%{_datadir}/knotifications5/akonadi_notes_agent.notifyrc

#----------------------------------------------------------------------------

%define knotesprivate_major 5
%define libknotesprivate %mklibname knotesprivate %{knotesprivate_major}

%package -n %{libknotesprivate}
Summary:	KDE PIM shared library
Group:		System/Libraries

%description -n %{libknotesprivate}
KDE PIM shared library.

%files -n %{libknotesprivate}
%{_libdir}/libknotesprivate.so.%{knotesprivate_major}*

#----------------------------------------------------------------------------

%define notesharedprivate_major 5
%define libnotesharedprivate %mklibname notesharedprivate %{notesharedprivate_major}

%package -n %{libnotesharedprivate}
Summary:	KDE PIM shared library
Group:		System/Libraries

%description -n %{libnotesharedprivate}
KDE PIM shared library.

%files -n %{libnotesharedprivate}
%{_libdir}/libnotesharedprivate.so.%{notesharedprivate_major}*

#----------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name}
%find_lang libnoteshared
cat *.lang >all.lang

%find_lang akonadi_notes_agent
