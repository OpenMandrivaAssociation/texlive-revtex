Name:		texlive-revtex
Version:	56591
Release:	2
Summary:	Styles for various Physics Journals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/revtex
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/revtex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/revtex.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/revtex.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Includes styles for American Physical Society, American
Institute of Physics, and Optical Society of America. The
distribution consists of the RevTeX class itself, and several
support packages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/revtex
%{_texmfdistdir}/tex/latex/revtex
%doc %{_texmfdistdir}/doc/latex/revtex
#- source
%doc %{_texmfdistdir}/source/latex/revtex

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
