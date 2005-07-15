#
#
Summary:	Mistlands - online role-playing game
Name:		mistlands
Version:	0.4.0
Release:	0.1
License:	GPL
Group:		Games
Source:		http://dl.sourceforge.net/sourceforge/zerofps/%{name}-%{version}-linux.tar.bz2
# Source-md5:	fa30bf78655bcffc5ae36c9d70e48252
URL:		http://www.zeropointgameplay.com/mistlands/intro.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mistlands is a online role-playing game created by Zero Point Gameplay.
Some quick facts. Mistlands...

 * is Not a Massively Multiplayer Online Role-Playing Game (MMORPG).
 * is Open Source and code is hosted on sourceforge.
 * is free to download and play. All servers are run by the players.
 * is a game in development and as such may be unstable from time to time´.

%prep
%setup -q -n zerofpsv2

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%%{__gettextize}
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
#cp -f /usr/share/automake/config.sub .
%configure
%{__make}

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
