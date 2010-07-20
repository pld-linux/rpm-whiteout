# TODO
# - pick items from PLD-doc/RPM-loops.txt
%define		rev	%(R="$Revision: 1.36 $"; RR="${R##: }"; echo ${RR%%?})
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
	esound-libs>esound-alsa \
	glibc>nss-softokn-freebl \
	glibc>tzdata \
	gmplayer>mplayer-skin-KDE \
	initramfs-tools>cryptsetup-luks-initramfs \
	initramfs-tools>dmraid-initramfs \
	initramfs-tools>lvm2-initramfs \
	initramfs-tools>mdadm-initramfs \
	initramfs-tools>multipath-tools-initramfs \
	initramfs-tools>openct-initramfs \
	initramfs-tools>opensc-initramfs \
	initramfs-tools>udev-initramfs \
	kdebase-desktop>kde-kside-PLD \
	kdebase-desktop>kde-logoutpic-PLD \
	kdebase-desktop>kde-splash-Default \
	kdelibs>kdelibs-shared \
	koffice-kexi>koffice-kspread \
	konqueror>kdeaddons-fsview \
	konqueror>kdeaddons-konqueror \
	konqueror>kdemultimedia-audiocd \
	openjdk-jre>openjdk-tools \
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
	amarok>amarok-xine \
	glibc-localedb-all>glibc \
	glibc-misc>glibc \
	glibc-misc>glibc64 \
	gtk+2>gtk+2-cups \
	hal>hal-info \
	java-sun-jre>java-sun-tools \
	lighttpd>lighttpd-mod_dirlisting \
	lighttpd>lighttpd-mod_indexfile \
	lighttpd>lighttpd-mod_staticfile \
	localedb-src>glibc \
	phorum>phorum-db-mysql \
	phorum>phorum-db-mysqli \
	phorum>phorum-db-sql_pool \
	php-simplexml>php-spl \
	roundcubemail>roundcubemail-skin-default \
	util-vserver-build>vserver-distro-pld \
	util-vserver>vserver-distro-pld \
	vim-rt>vim \
%%{nil}

EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# this should be replaced on upgrade
%config %verify(not md5 mtime size) /etc/rpm/macros.whiteout
