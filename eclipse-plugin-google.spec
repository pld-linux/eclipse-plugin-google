# TODO:
# - com.google.appengine.eclipse.sdkbundle_1.2.1.v200905131156/
# - com.google.gwt.eclipse.sdkbundle.linux_1.6.4.v200904062254 is x86 centric (build from source?)
%define		pluginver	1.0.1
%define		appengver	1.2.1
%define		gwtver		1.6.4
%include	/usr/lib/rpm/macros.java
Summary:	Google Plugin for Eclipse
Name:		eclipse-plugin-google
Version:	%{pluginver}
Release:	0.7
License:	Apache License, v2.0
Group:		Development/Tools
URL:		http://code.google.com/eclipse/
# http://code.google.com/eclipse/docs/install-from-zip.html
Source0:	http://dl.google.com/eclipse/plugin/3.3/zips/gpe-e33-latest.zip
# Source0-md5:	955d207982a0ec954b1c067019c33694
Source1:	http://dl.google.com/eclipse/plugin/3.3/features/com.google.appengine.eclipse.sdkbundle.e33.feature_%{appengver}.v200905131156.jar
# Source1-md5:	44dbeb0e33c1458658b1626b86efd677
Source2:	http://dl.google.com/eclipse/plugin/3.3/plugins/com.google.appengine.eclipse.sdkbundle_%{appengver}.v200905131156.jar
# Source2-md5:	ebc7c16b7291830497a24312980919c6
Source3:	http://dl.google.com/eclipse/plugin/3.3/features/com.google.gwt.eclipse.sdkbundle.e33.feature_%{gwtver}.v200904062254.jar
# Source3-md5:	8de9b4a53690e36e4af4fdd0e02f1528
Source4:	http://dl.google.com/eclipse/plugin/3.3/plugins/com.google.gwt.eclipse.sdkbundle.linux_%{gwtver}.v200904062254.jar
# Source4-md5:	9fe86bcde62ab891569b96fdb6fc0752
BuildRequires:	rpm-javaprov
BuildRequires:	unzip
Requires:	eclipse >= 3.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		eclipsedir	%{_datadir}/eclipse

# somewhy rpm-4.5 searches for ELF provides even the .so files are not executable
%define		_noautoprovfiles	%{_datadir}/eclipse

%description
The Google Plugin for Eclipse is the fastest way to start developing
Google Web Toolkit and App Engine applications, allowing you to go
from installing the plugin to deploying an Ajax "Hello World" in a
matter of minutes. Simply install the plugin and get started. If you
don't have the GWT and App Engine SDKs installed, the plugin can take
care of that for you.

The plugin currently supports Google App Engine and Google Web Toolkit
development.

%package appengine
Summary:	Google App Engine for Java SDK Bundle for Eclipse
Version:	%{appengver}
Group:		Development/Tools
Requires:	%{name} = %{pluginver}-%{release}

%description appengine
Google App Engine for Java SDK Bundle for Eclipse.

%package gwt
Summary:	Google Web Toolkit SDK Bundle for Eclipse
Version:	%{gwtver}
Group:		Development/Tools
Requires:	%{name} = %{pluginver}-%{release}

%description gwt
Google Web Toolkit SDK Bundle for Eclipse.

%prep
%setup -qc
install -d appengine gwt
%{__unzip} -d appengine -qq %{SOURCE2}
%{__unzip} -d gwt -qq %{SOURCE4}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{eclipsedir}/{features,plugins}
cp -a features/* $RPM_BUILD_ROOT%{eclipsedir}/features
cp -a plugins/* $RPM_BUILD_ROOT%{eclipsedir}/plugins

# appengine sdkbundle
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{eclipsedir}/features
cp -a appengine $RPM_BUILD_ROOT%{eclipsedir}/plugins/$(basename %{SOURCE2} .jar)
# gwt sdkbundle
cp -a %{SOURCE3} $RPM_BUILD_ROOT%{eclipsedir}/features
cp -a gwt $RPM_BUILD_ROOT%{eclipsedir}/plugins/$(basename %{SOURCE4} .jar)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{eclipsedir}/features/com.google.gdt.eclipse.suite.e33.feature_*
%{eclipsedir}/plugins/com.google.appengine.eclipse.core_*.jar
%{eclipsedir}/plugins/com.google.gdt.eclipse.core_*.jar
%{eclipsedir}/plugins/com.google.gdt.eclipse.suite_*.jar
%{eclipsedir}/plugins/com.google.gwt.eclipse.core_*.jar

%files appengine
%defattr(644,root,root,755)
%{eclipsedir}/features/com.google.appengine.eclipse.sdkbundle.e33.feature_*.jar
%{eclipsedir}/plugins/com.google.appengine.eclipse.sdkbundle_*

%files gwt
%defattr(644,root,root,755)
%{eclipsedir}/features/com.google.gwt.eclipse.sdkbundle.e33.feature_*.jar
# XXX: ix86 mozilla inside
%{eclipsedir}/plugins/com.google.gwt.eclipse.sdkbundle.linux_*
