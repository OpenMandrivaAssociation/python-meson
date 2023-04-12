Summary:	Meson Python build backend
Name:		python-meson-python
Version:	0.12.1
Release:	1
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/meson-python/
#Source0:	https://github.com/mesonbuild/meson-python/archive/%{version}/%{name}-%{version}.tar.gz
Source0:	https://pypi.io/packages/source/m/meson_python/meson_python-%{version}.tar.gz
BuildRequires:	python%{pyver}dist(meson)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pyproject-metadata)
BuildRequires:	python%{pyver}dist(typing-extensions)
BuildRequires:	python%{pyver}dist(tomli)

BuildArch:	noarch

%description
meson-python is a Python build backend built on top of the Meson build-system.
It enables you to use Meson for your Python packages.

%files
%{py_sitedir}/mesonpy
%{py_sitedir}/meson_python-*.*-info

#---------------------------------------------------------------------------
%prep
%autosetup -p1 -n meson_python-%{version}

%build
%py_build

%install
%py_install

