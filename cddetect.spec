Name:		cddetect
Summary:	A tool for detecting the type of a CD/DVD without mounting it
Version:	2.1
Release:	1
License:	GPLv2+
Source0:	http://www.bellut.net/files/%{name}-%{version}.tar.bz2
URL:		http://www.bellut.net/projects.html
Group:		Archiving/Cd burning

%description
This program tries to detect the type of a CD/DVD without mounting it.
It detects audio, ISO, VCD, SVCD and Video-DVD.

%prep
%setup -q -n %{name}

%build
sed -i -e '1i#include <limits.h>' %{name}.c || die
%make

%install
mkdir -p %{buildroot}%{_bindir}
install -D -s %{name} %{buildroot}%{_bindir}

%files
%{_bindir}/%{name}


%changelog
* Wed Jan 04 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.1-1
+ Revision: 753402
- imported package cddetect

