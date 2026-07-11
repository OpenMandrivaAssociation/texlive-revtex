%global tl_name revtex
%global tl_revision 67271

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.2f
Release:	%{tl_revision}.1
Summary:	Styles for various Physics Journals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/revtex
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/revtex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/revtex.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/revtex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Includes styles for American Physical Society, American Institute of
Physics, and Optical Society of America. The distribution consists of
the RevTeX class itself, and several support packages.

