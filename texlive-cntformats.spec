Name:		texlive-cntformats
Version:	34668
Release:	1
Summary:	A different way to read counters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cntformats
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cntformats.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cntformats.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers package or class authors a way to format
counters with 'patterns'. These patterns do not affect 'normal'
LaTeX treatment of counters.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/cntformats
%doc %{_texmfdistdir}/doc/latex/cntformats

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
