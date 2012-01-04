# revision 24603
# category TLCore
# catalog-ctan /obsolete/systems/unix/teTeX
# catalog-date 2009-11-10 12:26:23 +0100
# catalog-license other-free
# catalog-version 3.0
Name:		texlive-tetex
Version:	3.0
Release:	6
Summary:	scripts and files originally written for or included in teTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/obsolete/systems/unix/teTeX
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tetex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tetex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tetex.x86_64-linux.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
# updmap requires texconfig/tcfmgr
Requires(post):	texlive-texconfig
# pdftex requires updmap
Requires(post):	texlive-pdftex.bin
Provides:	texlive-tetex.bin = %{EVRD}

%description
teTeX was a comprehensive distribution of TeX, LaTeX and
family, designed to for ease of compilation, installation and
customisation. In 2006, Thomas Esser announced he would no
longer be able to support, or to produce new versions of,
teTeX. With the appearance of TeX live 2007 (whose Unix-system
TeX support originally derived from teTeX), no-one should be
using teTeX at all, in new applications. One of the "schemes"
available when installing TeX live provides a configuration
very close to that of the old teTeX, but using modern versions
of programs and packages.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/allcm
%{_bindir}/allec
%{_bindir}/allneeded
%{_bindir}/dvi2fax
%{_bindir}/dvired
%{_bindir}/fmtutil
%{_bindir}/fmtutil-sys
%{_bindir}/kpsewhere
%{_bindir}/texconfig-dialog
%{_bindir}/texconfig-sys
%{_bindir}/texlinks
%{_bindir}/updmap
%{_bindir}/updmap-sys
%{_texmfdir}/dvips/tetex/config.builtin35
%{_texmfdir}/dvips/tetex/config.dfaxhigh
%{_texmfdir}/dvips/tetex/config.dfaxlo
%{_texmfdir}/dvips/tetex/config.download35
%{_texmfdir}/dvips/tetex/config.gsftopk
%{_texmfdir}/dvips/tetex/config.outline
%{_texmfdir}/dvips/tetex/config.pdf
%{_texmfdir}/dvips/tetex/config.pk
%{_texmfdir}/dvips/tetex/config.www
%{_texmfdir}/fonts/enc/dvips/tetex/09fbbfac.enc
%{_texmfdir}/fonts/enc/dvips/tetex/0ef0afca.enc
%{_texmfdir}/fonts/enc/dvips/tetex/10037936.enc
%{_texmfdir}/fonts/enc/dvips/tetex/1b6d048e.enc
%{_texmfdir}/fonts/enc/dvips/tetex/71414f53.enc
%{_texmfdir}/fonts/enc/dvips/tetex/74afc74c.enc
%{_texmfdir}/fonts/enc/dvips/tetex/aae443f0.enc
%{_texmfdir}/fonts/enc/dvips/tetex/b6a4d7c7.enc
%{_texmfdir}/fonts/enc/dvips/tetex/bbad153f.enc
%{_texmfdir}/fonts/enc/dvips/tetex/d9b29452.enc
%{_texmfdir}/fonts/enc/dvips/tetex/f7b6d320.enc
%{_texmfdir}/fonts/enc/dvips/tetex/mtex.enc
%{_texmfdir}/fonts/map/dvips/tetex/README
%{_texmfdir}/fonts/map/dvips/tetex/dvipdfm35.map
%{_texmfdir}/fonts/map/dvips/tetex/dvips35.map
%{_texmfdir}/fonts/map/dvips/tetex/mathpple.map
%{_texmfdir}/fonts/map/dvips/tetex/pdftex35.map
%{_texmfdir}/fonts/map/dvips/tetex/ps2pk35.map
%{_texmfdir}/scripts/tetex/updmap-sys.sh
%{_texmfdir}/scripts/tetex/updmap.pl
%config(noreplace) %{_texmfdir}/web2c/updmap.cfg
%doc %{_mandir}/man1/allcm.1*
%doc %{_texmfdir}/doc/man/man1/allcm.man1.pdf
%doc %{_mandir}/man1/allec.1*
%doc %{_texmfdir}/doc/man/man1/allec.man1.pdf
%doc %{_mandir}/man1/allneeded.1*
%doc %{_texmfdir}/doc/man/man1/allneeded.man1.pdf
%doc %{_mandir}/man1/dvi2fax.1*
%doc %{_texmfdir}/doc/man/man1/dvi2fax.man1.pdf
%doc %{_mandir}/man1/dvired.1*
%doc %{_texmfdir}/doc/man/man1/dvired.man1.pdf
%doc %{_mandir}/man1/fmtutil-sys.1*
%doc %{_texmfdir}/doc/man/man1/fmtutil-sys.man1.pdf
%doc %{_mandir}/man1/fmtutil.1*
%doc %{_texmfdir}/doc/man/man1/fmtutil.man1.pdf
%doc %{_mandir}/man1/texlinks.1*
%doc %{_texmfdir}/doc/man/man1/texlinks.man1.pdf
%doc %{_mandir}/man1/updmap-sys.1*
%doc %{_texmfdir}/doc/man/man1/updmap-sys.man1.pdf
%doc %{_mandir}/man1/updmap.1*
%doc %{_texmfdir}/doc/man/man1/updmap.man1.pdf
%doc %{_mandir}/man5/fmtutil.cnf.5*
%doc %{_texmfdir}/doc/man/man5/fmtutil.cnf.man5.pdf
%doc %{_mandir}/man5/updmap.cfg.5*
%doc %{_texmfdir}/doc/man/man5/updmap.cfg.man5.pdf
%doc %{_texmfdir}/doc/tetex/TETEXDOC.pdf
%doc %{_texmfdir}/doc/tetex/teTeX-FAQ

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

perl -pi -e 's|\$TEXMFROOT/tlpkg|%{_datadir}/tlpkg|;'		\
    texmf/scripts/tetex/updmap.pl

%build

%install
# only scripts
mkdir -p %{buildroot}%{_bindir}
cp -fpa bin/x86_64-linux/* %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdir}/scripts/tetex/updmap.pl updmap
    ln -sf %{_texmfdir}/scripts/tetex/updmap-sys.sh updmap-sys
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man5
mv %{buildroot}%{_texmfdir}/doc/man/man5/*.5 %{buildroot}%{_mandir}/man5
