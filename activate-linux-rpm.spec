Summary: The "Activate Windows" watermark ported to Linux
%define version git
Version: %{version}
License: The Based License v1.3.6, https://github.com/MrGlockenspiel/activate-linux/blob/main/LICENSE.md
Name: activate-linux
Release: 1
Source: activate-linux-%{version}.tar.gz
URL: https://github.com/MrGlockenspiel/activate-linux
Buildroot: /tmp/activate-linux-git
BuildRequires: clang cairo-devel libXi-devel libX11-devel
BuildRequires: xorg-x11-proto-devel libxcb libXt-devel libXinerama-devel

%description
The "Activate Windows" watermark ported to Linux with Xlib and cairo in C

"Science isn't about WHY. It's about WHY NOT. Why is so much of our science dangerous? Why not marry safe science if you love it so much. In fact, why not invent a special safety door that won't hit you on the butt on the way out, because you are fired."

Maintained by MrGlockenspiel.

%prep
%setup -q

%build
export CFLAGS="%optflags"
%make_build

%install
export PREFIX=""
export BINDIR="%{_bindir}"
%make_install

%files
%{_bindir}/activate-linux
%license LICENSE.md
%doc ARGS.md README.md
