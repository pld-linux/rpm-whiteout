%define		rev	%(R="$Revision: 1.15 $"; RR="${R##: }"; echo ${RR%%?})
Summary:	PLD Linux RPM macros dealing with loop errors
Name:		rpm-whiteout
Version:	%{rev}
Release:	1
License:	GPL
Group:		Base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD Linux RPM macros dealing with loop errors in RPM packages in PLD Linux
Distribution that can't solved easily or not wanted to be solved.

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
#	so q is installed before p normally.
#
# XXX	Note: that there cannot be any whitespace within the string "p>q",
#	and that both p and q are package names (i.e. no version/release).

%%_dependency_whiteout	\
	php-pear-PEAR-core>php-pear-Console_Getopt \
	vim-rt>vim \
	vim-rt>vim-plugin-securemodelines \
	vim-rt>vim-syntax-spec \
	vim-rt>vim-syntax-poldek \
	lighttpd>lighttpd-mod_dirlisting \
	lighttpd>lighttpd-mod_indexfile \
	lighttpd>lighttpd-mod_staticfile \
	java-sun-jre>java-sun-tools \
	glibc>glibc-misc \
	glibc64>glibc-misc \
	ZendFramework>ZendFramework-Zend_Date \
	ZendFramework>ZendFramework-Zend_Exception \
	ZendFramework>ZendFramework-Zend_Http \
	ZendFramework>ZendFramework-Zend_Loader \
	ZendFramework>ZendFramework-Zend_Registry \
	ZendFramework-Zend_Controller>ZendFramework-Zend_Dojo \
	ZendFramework-Zend_Controller>ZendFramework-Zend_Json \
	ZendFramework-Zend_Controller>ZendFramework-Zend_Layout \
	ZendFramework-Zend_Controller>ZendFramework-Zend_Session \
	ZendFramework-Zend_Controller>ZendFramework-Zend_View \
	ZendFramework-Zend_Json>ZendFramework-Zend_Cache \
	ZendFramework-Zend_Layout>ZendFramework-Zend_View \
	gtk+2>gtk+2-cups \
	kdelibs>kdelibs-shared \
	perl-dirs>perl-base \
	hal>hal-info \
	amarok>amarok-xine \
%%{nil}
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# these should be replaced with an upgrade
%config %verify(not md5 mtime size) /etc/rpm/macros.whiteout
