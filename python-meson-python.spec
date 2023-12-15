Name:		python-meson-python
Version:	0.15.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/m/meson-python/meson_python-%{version}.tar.gz
Summary:	Meson Python build backend (PEP 517)
URL:		https://pypi.org/project/meson-python/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pyproject-metadata)
BuildArch:	noarch

%description
Meson Python build backend (PEP 517)

%prep
%autosetup -p1 -n meson_python-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/mesonpy
%{py_sitedir}/meson_python-*.*-info
