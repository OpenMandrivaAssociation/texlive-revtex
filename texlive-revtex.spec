# revision 19652
# category Package
# catalog-ctan /macros/latex/contrib/revtex
# catalog-date 2010-08-12 13:35:15 +0200
# catalog-license lppl1.3
# catalog-version 4.1r
Name:		texlive-revtex
Version:	4.1r
Release:	6
Summary:	Styles for various Physics Journals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/revtex
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/revtex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/revtex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/revtex.source.tar.xz
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
%{_texmfdistdir}/bibtex/bst/revtex/aipauth4-1.bst
%{_texmfdistdir}/bibtex/bst/revtex/aipnum4-1.bst
%{_texmfdistdir}/bibtex/bst/revtex/apsrev4-1.bst
%{_texmfdistdir}/bibtex/bst/revtex/apsrmp4-1.bst
%{_texmfdistdir}/tex/latex/revtex/aip4-1.rtx
%{_texmfdistdir}/tex/latex/revtex/aps10pt4-1.rtx
%{_texmfdistdir}/tex/latex/revtex/aps11pt4-1.rtx
%{_texmfdistdir}/tex/latex/revtex/aps12pt4-1.rtx
%{_texmfdistdir}/tex/latex/revtex/aps4-1.rtx
%{_texmfdistdir}/tex/latex/revtex/apsrmp4-1.rtx
%{_texmfdistdir}/tex/latex/revtex/ltxdocext.sty
%{_texmfdistdir}/tex/latex/revtex/ltxfront.sty
%{_texmfdistdir}/tex/latex/revtex/ltxgrid.sty
%{_texmfdistdir}/tex/latex/revtex/ltxutil.sty
%{_texmfdistdir}/tex/latex/revtex/reftest4-1.tex
%{_texmfdistdir}/tex/latex/revtex/revsymb4-1.sty
%{_texmfdistdir}/tex/latex/revtex/revtex4-1.cls
%doc %{_texmfdistdir}/doc/latex/revtex/00readme.tex
%doc %{_texmfdistdir}/doc/latex/revtex/DOWNLOAD
%doc %{_texmfdistdir}/doc/latex/revtex/README
%doc %{_texmfdistdir}/doc/latex/revtex/aip/aipguide4-1.pdf
%doc %{_texmfdistdir}/doc/latex/revtex/aip/aipguide4-1.tex
%doc %{_texmfdistdir}/doc/latex/revtex/aip/docs.sty
%doc %{_texmfdistdir}/doc/latex/revtex/aps/apsguide4-1.pdf
%doc %{_texmfdistdir}/doc/latex/revtex/aps/apsguide4-1.tex
%doc %{_texmfdistdir}/doc/latex/revtex/auguide/auguide4-1.pdf
%doc %{_texmfdistdir}/doc/latex/revtex/auguide/auguide4-1.tex
%doc %{_texmfdistdir}/doc/latex/revtex/auguide/docs.sty
%doc %{_texmfdistdir}/doc/latex/revtex/auguide/summary4-1.pdf
%doc %{_texmfdistdir}/doc/latex/revtex/auguide/summary4-1.tex
%doc %{_texmfdistdir}/doc/latex/revtex/auguide/whatsnew4-1.pdf
%doc %{_texmfdistdir}/doc/latex/revtex/auguide/whatsnew4-1.tex
%doc %{_texmfdistdir}/doc/latex/revtex/sample/aip/aipsamp.bib
%doc %{_texmfdistdir}/doc/latex/revtex/sample/aip/aipsamp.pdf
%doc %{_texmfdistdir}/doc/latex/revtex/sample/aip/aipsamp.tex
%doc %{_texmfdistdir}/doc/latex/revtex/sample/aip/aiptemplate.tex
%doc %{_texmfdistdir}/doc/latex/revtex/sample/aip/fig_1.eps
%doc %{_texmfdistdir}/doc/latex/revtex/sample/aip/fig_2.eps
%doc %{_texmfdistdir}/doc/latex/revtex/sample/aps/apssamp.bib
%doc %{_texmfdistdir}/doc/latex/revtex/sample/aps/apssamp.pdf
%doc %{_texmfdistdir}/doc/latex/revtex/sample/aps/apssamp.tex
%doc %{_texmfdistdir}/doc/latex/revtex/sample/aps/apstemplate.tex
%doc %{_texmfdistdir}/doc/latex/revtex/sample/aps/fig_1.eps
%doc %{_texmfdistdir}/doc/latex/revtex/sample/aps/fig_2.eps
%doc %{_texmfdistdir}/doc/latex/revtex/sample/aps/vid_1a.eps
%doc %{_texmfdistdir}/doc/latex/revtex/sample/aps/vid_1b.eps
%doc %{_texmfdistdir}/doc/latex/revtex/source/aip.pdf
%doc %{_texmfdistdir}/doc/latex/revtex/source/ltxdocext.pdf
%doc %{_texmfdistdir}/doc/latex/revtex/source/ltxfront.pdf
%doc %{_texmfdistdir}/doc/latex/revtex/source/ltxgrid.pdf
%doc %{_texmfdistdir}/doc/latex/revtex/source/ltxutil.pdf
%doc %{_texmfdistdir}/doc/latex/revtex/source/revtex4-1.pdf
#- source
%doc %{_texmfdistdir}/source/latex/revtex/aip.dtx
%doc %{_texmfdistdir}/source/latex/revtex/ltxdocext.dtx
%doc %{_texmfdistdir}/source/latex/revtex/ltxfront.dtx
%doc %{_texmfdistdir}/source/latex/revtex/ltxgrid.dtx
%doc %{_texmfdistdir}/source/latex/revtex/ltxutil.dtx
%doc %{_texmfdistdir}/source/latex/revtex/revtex4-1.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.1r-2
+ Revision: 755662
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 4.1r-1
+ Revision: 719452
- texlive-revtex
- texlive-revtex
- texlive-revtex
- texlive-revtex

