Summary: TCP Gender Changer Daemon
Name: tgcd
Version: 1.1.1
Release: 1%{?dist}
License: GPLv2
Source0: http://sourceforge.net/projects/tgcd/files/tgcd/1.1.1/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.conf
Group: Applications/Internet

Requires(post):     systemd
Requires(preun):    systemd
Requires(preun):    systemd

%description
tgcd is a simple Unix network utility to extend the accessibility of TCP/IP based network services beyond firewalls. This can also be used by network analysts and security experts for penetration testing and analyze the security of their network.
More info at http://tgcd.sourceforge.net/

%prep
%setup -q

%build
%configure

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
%{__install} -p -D -m 0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/systemd/system/%{name}.service
%{__install} -p -D -m 0640 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}.conf

%files
%doc README NEWS
%{_bindir}/tgcd
%doc %{_mandir}/man1/tgcd.1*
%{_prefix}/lib/systemd/system/%{name}.service
%{_sysconfdir}/%{name}.conf

%changelog
* Sun Apr 07 2020 Michel Belleau <michel.belleau@malaiwah.com> - 1.1.1-1
- Initial import
