Summary:	Georgian resources for SeaMonkey
Summary(pl):	Gruzyjskie pliki jêzykowe dla SeaMonkeya
Name:		seamonkey-lang-ka
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/contrib-localized/seamonkey-%{version}.ka-GE.langpack.xpi
# Source0-md5:	73042ed25a41518298b2b2dede912251
Source1:	gen-installed-chrome.sh
URL:		http://www.mozilla.org/projects/seamonkey/
BuildRequires:	unzip
Requires(post,postun):	seamonkey >= %{version}
Requires(post,postun):	textutils
Requires:	seamonkey >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_chromedir	%{_datadir}/seamonkey/chrome

%description
Georgian resources for SeaMonkey.

%description -l pl
Gruzyjskie pliki jêzykowe dla SeaMonkeya.

%prep
%setup -q -c
install %{SOURCE1} .
./gen-installed-chrome.sh locale chrome/{GE,ka-GE,ka-unix}.jar \
	> lang-ka-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install chrome/{GE,ka-GE,ka-unix}.jar $RPM_BUILD_ROOT%{_chromedir}
install lang-ka-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}
cp -r defaults myspell $RPM_BUILD_ROOT%{_datadir}/seamonkey

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/ka-GE.jar
%{_chromedir}/ka-unix.jar
%{_chromedir}/GE.jar
%{_chromedir}/lang-ka-installed-chrome.txt
%{_datadir}/seamonkey/defaults/messenger/GE
%{_datadir}/seamonkey/defaults/profile/GE
%{_datadir}/seamonkey/myspell/ka-GE*
