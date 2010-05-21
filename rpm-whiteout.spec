# TODO
# - pick items from PLD-doc/RPM-loops.txt
%define		rev	%(R="$Revision: 1.34 $"; RR="${R##: }"; echo ${RR%%?})
Summary:	PLD Linux RPM macros dealing with loop errors
Name:		rpm-whiteout
Version:	%{rev}
Release:	1
License:	GPL
Group:		Base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD Linux RPM macros dealing with loop errors in RPM packages in PLD
Linux Distribution that can't solved easily or not wanted to be
solved.

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
	php-pear-PEAR-core>php-pear-Console_Getopt \
	vim-rt>vim \
	vim-rt>vim-plugin-securemodelines \
	vim-rt>vim-syntax-spec \
	vim-rt>vim-syntax-poldek \
	java-sun-jre>java-sun-tools \
	openjdk-jre>openjdk-tools \
	glibc>nss-softokn-freebl \
	glibc>tzdata \
	ZendFramework-Zend_Controller>ZendFramework-Zend_Dojo \
	ZendFramework-Zend_Controller>ZendFramework-Zend_Json \
	ZendFramework-Zend_Controller>ZendFramework-Zend_Layout \
	ZendFramework-Zend_Controller>ZendFramework-Zend_Session \
	ZendFramework-Zend_Controller>ZendFramework-Zend_View \
	ZendFramework-Zend_Controller>ZendFramework-Zend_Uri \
	ZendFramework-Zend_Validate>ZendFramework-Zend_Uri \
	ZendFramework-Zend_Cache>ZendFramework-Zend_Json \
	ZendFramework-Zend_Cache>ZendFramework-Zend_Log \
	ZendFramework-Zend_Layout>ZendFramework-Zend_View \
	kdelibs>kdelibs-shared \
	kdebase-desktop>kde-kside-PLD \
	kdebase-desktop>kde-logoutpic-PLD \
	kdebase-desktop>kde-splash-Default \
	konqueror>kdeaddons-fsview \
	konqueror>kdeaddons-konqueror \
	konqueror>kdemultimedia-audiocd \
	koffice-kexi>koffice-kspread \
	rc-scripts>blockdev \
	esound-libs>esound-alsa \
	initramfs-tools>cryptsetup-luks-initramfs \
	initramfs-tools>dmraid-initramfs \
	initramfs-tools>lvm2-initramfs \
	initramfs-tools>mdadm-initramfs \
	initramfs-tools>multipath-tools-initramfs \
	initramfs-tools>openct-initramfs \
	initramfs-tools>opensc-initramfs \
	initramfs-tools>udev-initramfs \
	gmplayer>mplayer-skin-KDE \
	QtGui>Qt3Support \
	QtGui>QtSvg \
	upstart>dbus \
%%{nil}

# dependency whiteouts if main pkg requires it's subpkg, this should be handed
# somehow in rpm itself, but for now keep the list.
%%_dependency_whiteouts_subpkg	\
	lighttpd>lighttpd-mod_dirlisting \
	lighttpd>lighttpd-mod_indexfile \
	lighttpd>lighttpd-mod_staticfile \
	glibc-misc>glibc \
	glibc-misc>glibc64 \
	glibc-localedb-all>glibc \
	localedb-src>glibc \
	gtk+2>gtk+2-cups \
	hal>hal-info \
	amarok>amarok-xine \
	util-vserver>vserver-distro-pld \
	util-vserver-build>vserver-distro-pld \
	roundcubemail>roundcubemail-skin-default \
	php-simplexml>php-spl \
	phorum>phorum-db-mysql \
	phorum>phorum-db-mysqli \
	phorum>phorum-db-sql_pool \
%%{nil}

EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# this should be replaced on upgrade
%config %verify(not md5 mtime size) /etc/rpm/macros.whiteout
