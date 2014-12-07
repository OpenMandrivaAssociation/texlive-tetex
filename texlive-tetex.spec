# revision 34229
# category TLCore
# catalog-ctan /obsolete/systems/unix/teTeX
# catalog-date 2012-09-11 08:43:58 +0200
# catalog-license other-free
# catalog-version 3.0
Name:		texlive-tetex
Version:	3.0
Release:	25
Summary:	scripts and files originally written for or included in teTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/obsolete/systems/unix/teTeX
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tetex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tetex.doc.tar.xz
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
family, designed for ease of compilation, installation and
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
# installed by texlive-kpathsea.bin
#%%{_bindir}/kpsetool
%{_bindir}/kpsewhere
%{_bindir}/texconfig-dialog
%{_bindir}/texconfig-sys
%{_bindir}/texlinks
%{_bindir}/updmap
%{_bindir}/updmap-sys
%{_texmfdistdir}/dvips/tetex/config.builtin35
%{_texmfdistdir}/dvips/tetex/config.dfaxhigh
%{_texmfdistdir}/dvips/tetex/config.dfaxlo
%{_texmfdistdir}/dvips/tetex/config.download35
%{_texmfdistdir}/dvips/tetex/config.gsftopk
%{_texmfdistdir}/dvips/tetex/config.maxmem
%{_texmfdistdir}/dvips/tetex/config.outline
%{_texmfdistdir}/dvips/tetex/config.pdf
%{_texmfdistdir}/dvips/tetex/config.pk
%{_texmfdistdir}/dvips/tetex/config.www
%{_texmfdistdir}/fonts/enc/dvips/tetex/09fbbfac.enc
%{_texmfdistdir}/fonts/enc/dvips/tetex/0ef0afca.enc
%{_texmfdistdir}/fonts/enc/dvips/tetex/10037936.enc
%{_texmfdistdir}/fonts/enc/dvips/tetex/1b6d048e.enc
%{_texmfdistdir}/fonts/enc/dvips/tetex/71414f53.enc
%{_texmfdistdir}/fonts/enc/dvips/tetex/74afc74c.enc
%{_texmfdistdir}/fonts/enc/dvips/tetex/aae443f0.enc
%{_texmfdistdir}/fonts/enc/dvips/tetex/b6a4d7c7.enc
%{_texmfdistdir}/fonts/enc/dvips/tetex/bbad153f.enc
%{_texmfdistdir}/fonts/enc/dvips/tetex/d9b29452.enc
%{_texmfdistdir}/fonts/enc/dvips/tetex/f7b6d320.enc
%{_texmfdistdir}/fonts/enc/dvips/tetex/mtex.enc
%{_texmfdistdir}/fonts/map/dvips/tetex/Makefile
%{_texmfdistdir}/fonts/map/dvips/tetex/README
%{_texmfdistdir}/fonts/map/dvips/tetex/base14flags.ltx
%{_texmfdistdir}/fonts/map/dvips/tetex/base14flags.tex
%{_texmfdistdir}/fonts/map/dvips/tetex/dvipdfm35.map
%{_texmfdistdir}/fonts/map/dvips/tetex/dvips35.map
%{_texmfdistdir}/fonts/map/dvips/tetex/mathpple.map
%{_texmfdistdir}/fonts/map/dvips/tetex/pdftex35.map
%{_texmfdistdir}/fonts/map/dvips/tetex/ps2pk35.map
%{_texmfdistdir}/scripts/texlive/allcm.sh
%{_texmfdistdir}/scripts/texlive/allneeded.sh
%{_texmfdistdir}/scripts/texlive/dvi2fax.sh
%{_texmfdistdir}/scripts/texlive/dvired.sh
%{_texmfdistdir}/scripts/texlive/fmtutil-sys.sh
%{_texmfdistdir}/scripts/texlive/fmtutil.sh
%{_texmfdistdir}/scripts/texlive/kpsetool.sh
%{_texmfdistdir}/scripts/texlive/kpsewhere.sh
%{_texmfdistdir}/scripts/texlive/texconfig-dialog.sh
%{_texmfdistdir}/scripts/texlive/texconfig-sys.sh
%{_texmfdistdir}/scripts/texlive/texlinks.sh
%{_texmfdistdir}/scripts/texlive/updmap-sys.sh
%{_texmfdistdir}/scripts/texlive/updmap.pl
%config(noreplace) %{_texmfdistdir}/web2c/updmap.cfg
%doc %{_mandir}/man1/allcm.1*
%doc %{_texmfdistdir}/doc/man/man1/allcm.man1.pdf
%doc %{_mandir}/man1/allec.1*
%doc %{_texmfdistdir}/doc/man/man1/allec.man1.pdf
%doc %{_mandir}/man1/allneeded.1*
%doc %{_texmfdistdir}/doc/man/man1/allneeded.man1.pdf
%doc %{_mandir}/man1/dvi2fax.1*
%doc %{_texmfdistdir}/doc/man/man1/dvi2fax.man1.pdf
%doc %{_mandir}/man1/dvired.1*
%doc %{_texmfdistdir}/doc/man/man1/dvired.man1.pdf
%doc %{_mandir}/man1/fmtutil-sys.1*
%doc %{_texmfdistdir}/doc/man/man1/fmtutil-sys.man1.pdf
%doc %{_mandir}/man1/fmtutil.1*
%doc %{_texmfdistdir}/doc/man/man1/fmtutil.man1.pdf
%doc %{_mandir}/man1/kpsepath.1*
%doc %{_texmfdistdir}/doc/man/man1/kpsepath.man1.pdf
%doc %{_mandir}/man1/kpsetool.1*
%doc %{_texmfdistdir}/doc/man/man1/kpsetool.man1.pdf
%doc %{_mandir}/man1/kpsewhere.1*
%doc %{_texmfdistdir}/doc/man/man1/kpsewhere.man1.pdf
%doc %{_mandir}/man1/kpsexpand.1*
%doc %{_texmfdistdir}/doc/man/man1/kpsexpand.man1.pdf
%doc %{_mandir}/man1/texlinks.1*
%doc %{_texmfdistdir}/doc/man/man1/texlinks.man1.pdf
%doc %{_mandir}/man1/updmap-sys.1*
%doc %{_texmfdistdir}/doc/man/man1/updmap-sys.man1.pdf
%doc %{_mandir}/man1/updmap.1*
%doc %{_texmfdistdir}/doc/man/man1/updmap.man1.pdf
%doc %{_mandir}/man5/fmtutil.cnf.5*
%doc %{_texmfdistdir}/doc/man/man5/fmtutil.cnf.man5.pdf
%doc %{_mandir}/man5/updmap.cfg.5*
%doc %{_texmfdistdir}/doc/man/man5/updmap.cfg.man5.pdf
%doc %{_texmfdistdir}/doc/tetex/TETEXDOC.pdf
%doc %{_texmfdistdir}/doc/tetex/teTeX-FAQ

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

perl -pi -e 's|\$TEXMFROOT/tlpkg|%{_datadir}/tlpkg|;'		\
    texmf-dist/scripts/texlive/updmap.pl

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/texlive/updmap.pl updmap
    ln -sf %{_texmfdistdir}/scripts/texlive/updmap-sys.sh updmap-sys
    ln -sf %{_texmfdistdir}/scripts/texlive/allcm.sh allcm
    ln -sf allcm allec
    ln -sf %{_texmfdistdir}/scripts/texlive/allneeded.sh allneeded
    ln -sf %{_texmfdistdir}/scripts/texlive/dvi2fax.sh dvi2fax
    ln -sf %{_texmfdistdir}/scripts/texlive/dvired.sh dvired
    ln -sf %{_texmfdistdir}/scripts/texlive/fmtutil.sh fmtutil
    ln -sf %{_texmfdistdir}/scripts/texlive/fmtutil-sys.sh fmtutil-sys
    ln -sf %{_texmfdistdir}/scripts/texlive/kpsetool.sh kpsetool
    ln -sf %{_texmfdistdir}/scripts/texlive/kpsewhere.sh kpsewhere
    ln -sf %{_texmfdistdir}/scripts/texlive/texconfig-dialog.sh texconfig-dialog
    ln -sf %{_texmfdistdir}/scripts/texlive/texconfig-sys.sh texconfig-sys
    ln -sf %{_texmfdistdir}/scripts/texlive/texlinks.sh texlinks
    ln -sf %{_texmfdistdir}/scripts/texlive/updmap.pl updmap
    ln -sf %{_texmfdistdir}/scripts/texlive/updmap-sys.sh updmap-sys
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man5
mv %{buildroot}%{_texmfdistdir}/doc/man/man5/*.5 %{buildroot}%{_mandir}/man5
rm -f %{buildroot}%{_bindir}/kpsetool
