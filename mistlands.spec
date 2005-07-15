# TODO:
# - make some optimizations depending on processor...
Summary:	Mistlands - online role-playing game
Summary(pl):	MIstlands - gra online typu RPG
Name:		mistlands
Version:	0.4.0
Release:	0.1
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/zerofps/%{name}-%{version}-linux.tar.bz2
# Source-md5:	fa30bf78655bcffc5ae36c9d70e48252
URL:		http://www.zeropointgameplay.com/mistlands/intro.html
# Really needed??
#BuildRequires:	gcc >= 3.4
BuildRequires:	lua50-devel
BuildRequires:	sed
BuildRequires:	tolua++
BuildRequires:	SDL-devel >= 1.2.7
BuildRequires:	SDL_net-devel >= 1.2.5
BuildRequires:	OpenAL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mistlands is a online role-playing game created by Zero Point
Gameplay. Some quick facts. Mistlands...

- is Not a Massively Multiplayer Online Role-Playing Game (MMORPG).
- Free to download and play. All servers are run by the players.
- Game in development and as such may be unstable from time to time.

%description -l pl
Mistlands to gra online typu RPG tworzona przez Zero Point Gameplay.
Troche szybkich faktów o grze...

- To nie jest gra przeznaczona do rozgrywki dla wielu graczy (MMORPG)
- Darmowa do pobrania i grania. Wszystkie serwery tworzone przez
  graczy.
- Gra jest w trakcie tworzenie, wiêc od czasu do czasu mo¿e byæ
  niestabilna.

%prep
%setup -q -n zerofpsv2
tar -jxvf src.tar.bz2

%build
cd src
%{__make} \
	CXX=%{__cxx} \
	CC=%{__cc} \
	CXXFLAGS="%{rpmcxxflags} -I%{_includedir}/lua50 -I%{_includedir} -I%{_includedir}/AL" \
	C_ARGS="%{rpmcflags} -I%{_includedir}/lua50 -I%{_includedir} -I%{_includedir}/AL"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post
#%post	-p /sbin/ldconfig

%preun

%postun
#%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
#%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*

#%attr(755,root,root) %{_bindir}/*

#%{_datadir}/%{name}

# initscript and its config
#%attr(754,root,root) /etc/rc.d/init.d/%{name}
#%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
