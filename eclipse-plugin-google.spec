%include	/usr/lib/rpm/macros.java
Summary:	Google Plugin for Eclipse
Name:		eclipse-plugin-google
Version:	1.0.1
Release:	0.2
License:	Apache License, v2.0
Group:		Development/Tools
URL:		http://code.google.com/eclipse/
# http://code.google.com/eclipse/docs/install-from-zip.html
Source0:	http://dl.google.com/eclipse/plugin/3.3/zips/gpe-e33-latest.zip
# Source0-md5:	955d207982a0ec954b1c067019c33694
BuildRequires:	rpm-javaprov
Requires:	eclipse >= 3.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		eclipsedir	%{_datadir}/eclipse

%description
The Google Plugin for Eclipse is the fastest way to start developing
Google Web Toolkit and App Engine applications, allowing you to go
from installing the plugin to deploying an Ajax "Hello World" in a
matter of minutes. Simply install the plugin and get started. If you
don't have the GWT and App Engine SDKs installed, the plugin can take
care of that for you.

The plugin currently supports Google App Engine and Google Web Toolkit
development.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{eclipsedir}/{features,plugins}
cp -a features/* $RPM_BUILD_ROOT%{eclipsedir}/features
cp -a plugins/* $RPM_BUILD_ROOT%{eclipsedir}/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{eclipsedir}/features/com.google.gdt.eclipse.suite.e33.feature_*
%{eclipsedir}/plugins/com.google.appengine.eclipse.core_*.jar
%{eclipsedir}/plugins/com.google.gdt.eclipse.core_*.jar
%{eclipsedir}/plugins/com.google.gdt.eclipse.suite_*.jar
%{eclipsedir}/plugins/com.google.gwt.eclipse.core_*.jar
