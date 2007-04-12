%define version 20061126
%define release %mkrel 1

%define scim_version 1.4.5

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

Name:		scim-ruby
Summary:	SCIM IMEngine module for ruby
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	GPL
URL:		http://scim-ruby.sourceforge.jp/cgi-bin/hiki.cgi
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:	ruby
Requires:	scim >= %{scim_version}
BuildRequires:  automake1.8
BuildRequires:  ruby-devel >= %{ruby_version}
BuildRequires:  scim-devel >= %{scim_version}

%description
Scim-ruby is an SCIM IMEngine module for ruby.


%prep
%setup -q

%build
[ ! -x configure ] && ./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std mkinstalldirs='mkdir -p'

# remove unnecessary files
rm -f %{buildroot}%{_libdir}/scim-1.0/*/*/*.{a,la}

%find_lang %{name}

%clean
rm -rf %{buildroot}


%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_datadir}/scim/icons/*
%{_datadir}/scim/scim-ruby/*.rb
%{_libdir}/scim-1.0/*/IMEngine/*.so
%{_libdir}/scim-1.0/*/SetupUI/*.so


