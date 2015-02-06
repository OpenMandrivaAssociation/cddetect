Summary:	A tool for detecting the type of a CD/DVD without mounting it
Name:		cddetect
Version:	2.1
Release:	3
License:	GPLv2+
Group:		Archiving/Cd burning
Url:		http://www.bellut.net/projects.html
Source0:	http://www.bellut.net/files/%{name}-%{version}.tar.bz2

%description
This program tries to detect the type of a CD/DVD without mounting it.
It detects audio, ISO, VCD, SVCD and Video-DVD.

%files
%doc COPYING
%{_bindir}/%{name}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}

%build
sed -i -e '1i#include <limits.h>' %{name}.c || die
%make CFLAGS="%{optflags}"

%install
mkdir -p %{buildroot}%{_bindir}
install -D %{name} %{buildroot}%{_bindir}


