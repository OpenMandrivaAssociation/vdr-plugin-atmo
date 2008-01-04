
%define plugin	atmo
%define Plugin	atmolight
%define name	vdr-plugin-%plugin
%define version	0.0.1
%define rel	14

Summary:	VDR plugin: Atmolight-Plugin
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.edener.de/
Source:		http://www.edener.de/%Plugin.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
BuildRequires:	dos2unix
Requires:	vdr-abi = %vdr_abi

%description
Atmolight-plugin for VDR.

See http://www.vdr-wiki.de/wiki/index.php/Atmolight-plugin for
details.

%prep
%setup -q -n %Plugin-%version
dos2unix HISTORY firmware/Makefile firmware/main.hex

%vdr_plugin_params_begin %plugin
# send atmolight-data over network (e.g. 192.168.0.1:1234)
var=NETWORK_TARGET
param=--net=NETWORK_TARGET
# send atmolight-data to serial device (e.g. /dev/ttyS1)
var=SERIAL_DEVICE
param=--serial=SERIAL_DEVICE
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY firmware eagle


