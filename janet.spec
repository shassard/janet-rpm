%undefine _debugsource_packages

Summary: A dynamic language and bytecode vm
Name: janet
Version: 1.23.0
Release: 1 
License: MIT
Group: Development/Languages
Source: https://github.com/janet-lang/janet/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
URL: https://github.com/janet-lang/janet
#BuildRequires: gtkglext-devel
BuildRequires: gcc

%description
Janet is a functional and imperative programming language and bytecode
interpreter. It is a lisp-like language, but lists are replaced by other
data structures (arrays, tables (hash table), struct (immutable hash table),
tuples). The language also supports bridging to native code written in C,
meta-programming with macros, and bytecode assembly.

%prep
%setup -q
sed -i -e 's|/usr/local|/usr|' -e 's|$(PREFIX)/lib|%{_libdir}|' Makefile

%build
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files 
%doc *.md *.txt
%{_bindir}/*
%{_includedir}/%{name}
%{_libdir}/lib%{name}.*
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sat Jul 2 2022 Stephen Hassard <steve@hassard.net> - 1.23.0-1
- Bump to 1.23.0

* Sat Apr 30 2022 Stephen Hassard <steve@hassard.net> - 1.21.1-2
- Update build dependencies for CentOS Stream 9

* Sun Mar 27 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.21.1-1
- Rebuilt for Fedora
