# NOTE: there are also TTF fonts in tarball
Summary:	Adobe Source Blank - font with blank rendered as not blank
Summary(pl.UTF-8):	Adobe Source Blank - font z odstępem wyświetlanym jako niepusty
Name:		fonts-OTF-Adobe-Blank
Version:	1.030
Release:	1
License:	OFL v1.1
Group:		Fonts
Source0:	http://downloads.sourceforge.net/adobe-blank.adobe/AdobeBlank.otf
# Source0-md5:	5f4074d39eff916ed6586d1afaf38584
URL:		http://sourceforge.net/projects/sourcecodepro.adobe/
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         otffontsdir     %{_fontsdir}/OTF

%description
Font characteristics:
- All Unicode code points are covered
- All code points are rendered using a non-spacing and non-marking
  glyph

%description -l pl.UTF-8
Charakterystyka fontu:
- pokrywa wszystkie punkty kodowe Unicode
- wszystkie punkty kodowe są renderowane przy użyciu bezodstępowych,
bezznakowych glifów.

%prep
%setup -q -c -T

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{otffontsdir}

install -p %{SOURCE0} $RPM_BUILD_ROOT%{otffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst OTF

%postun
fontpostinst OTF

%files
%defattr(644,root,root,755)
%{otffontsdir}/AdobeBlank.otf
