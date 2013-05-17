# TODO
# - pick items from PLD-doc/RPM-loops.txt
Summary:	PLD Linux RPM macros dealing with loop errors
Summary(pl.UTF-8):	Makra RPM-a do rozwiązywania zapętlonych zależności w PLD Linuksie
Name:		rpm-whiteout
Version:	1.41
Release:	3
License:	GPL
Group:		Base
Requires:	rpm-base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD Linux RPM macros dealing with loop errors in RPM packages in PLD
Linux Distribution that can't solved easily or not wanted to be
solved.

%description -l pl.UTF-8
Makra RPM-a do rozwiązywania w pakietach RPM dystrybucji PLD Linux
zapętlonych zależności, których nie można inaczej rozwiązać w łatwy
sposób.

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/rpm
cat <<'EOF' > $RPM_BUILD_ROOT/etc/rpm/macros.whiteout
#	Relations between package names that cause dependency loops
#	with legacy packages that cannot be fixed. Relations are
#	specified as
#		p>q
#	where package p has a Requires: on something that package q Provides:
#	so p is installed before q normally.
#
# Note: that there cannot be any whitespace within the string "p>q",
#	and that both p and q are package names (i.e. no version/release).

# Note: these are PACKAGE names, not Provide names.

 %%_dependency_whiteout	\
	%%{_dependency_whiteouts_subpkg}	\
	fontpostinst>t1lib \
	glibc>nss-softokn-freebl \
	glibc>tzdata \
	gmplayer>mplayer-skin-KDE \
	kdebase-desktop>kde-kside-PLD \
	kdebase-desktop>kde-logoutpic-PLD \
	kdebase-desktop>kde-splash-Default \
	kdelibs>kdelibs-shared \
	koffice-kexi>koffice-kspread \
	konqueror>kdeaddons-fsview \
	konqueror>kdeaddons-konqueror \
	konqueror>kdemultimedia-audiocd \
	php-pear-PEAR-core>php-pear-Console_Getopt \
	rc-scripts>blockdev \
	upstart>dbus \
	vim-rt>vim-plugin-securemodelines \
	vim-rt>vim-syntax-poldek \
	vim-rt>vim-syntax-spec \
 %%{nil}

# dependency whiteouts if main pkg requires it's subpkg, this should be handed
# somehow in rpm itself, but for now keep the list.
 %%_dependency_whiteouts_subpkg	\
	QtGui>Qt3Support \
	QtGui>QtSvg \
	ZendFramework-Zend_Cache>ZendFramework-Zend_Json \
	ZendFramework-Zend_Cache>ZendFramework-Zend_Log \
	ZendFramework-Zend_Controller>ZendFramework-Zend_Dojo \
	ZendFramework-Zend_Controller>ZendFramework-Zend_Json \
	ZendFramework-Zend_Controller>ZendFramework-Zend_Layout \
	ZendFramework-Zend_Controller>ZendFramework-Zend_Session \
	ZendFramework-Zend_Controller>ZendFramework-Zend_Uri \
	ZendFramework-Zend_Controller>ZendFramework-Zend_View \
	ZendFramework-Zend_Layout>ZendFramework-Zend_View \
	ZendFramework-Zend_Validate>ZendFramework-Zend_Uri \
	ZendFramework>ZendFramework-Zend_Date \
	ZendFramework>ZendFramework-Zend_Exception \
	ZendFramework>ZendFramework-Zend_Http \
	ZendFramework>ZendFramework-Zend_Loader \
	ZendFramework>ZendFramework-Zend_Loader \
	ZendFramework>ZendFramework-Zend_Registry \
	amarok>amarok-xine \
	esound-libs>esound-alsa \
	glibc64>glibc-misc \
	glibc>glibc-localedb-all \
	glibc>glibc-misc \
	glibc>localedb-src \
	gtk+2>gtk+2-cups \
	hal>hal-info \
	java-sun-jre>java-sun-jre-X11 \
	java-sun-jre>java-sun-tools \
	lighttpd>lighttpd-mod_dirlisting \
	lighttpd>lighttpd-mod_indexfile \
	lighttpd>lighttpd-mod_staticfile \
	openjdk-jre>openjdk-tools \
	phorum>phorum-db-mysql \
	phorum>phorum-db-mysqli \
	phorum>phorum-db-sql_pool \
	php-common>php-pcre \
	php-common>php-session \
	php-common>php-simplexml \
	php-common>php-spl \
	php-spl>php-simplexml \
	php52-common>php52-pcre \
	php52-common>php52-session \
	php52-common>php52-simplexml \
	php52-common>php52-spl \
	php52-spl>php52-simplexml \
	php54-common>php54-pcre \
	php54-common>php54-session \
	php54-common>php54-simplexml \
	php54-common>php54-spl \
	php54-spl>php54-simplexml \
	roundcubemail>roundcubemail-skin-default \
	util-vserver-build>vserver-distro-pld \
	util-vserver>vserver-distro-pld \
	vim>vim-rt \
 %%{nil}
EOF

%{__sed} -i -e 's|^ %|%|g' $RPM_BUILD_ROOT/etc/rpm/macros.whiteout

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# this file should be replaced on upgrade
%config %verify(not md5 mtime size) /etc/rpm/macros.whiteout
