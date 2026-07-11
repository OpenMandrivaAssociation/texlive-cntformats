%global tl_name cntformats
%global tl_revision 34668

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7
Release:	%{tl_revision}.1
Summary:	A different way to read counters
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cntformats
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cntformats.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cntformats.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package offers package or class authors a way to format counters
with 'patterns'. These patterns do not affect 'normal' LaTeX treatment
of counters.

