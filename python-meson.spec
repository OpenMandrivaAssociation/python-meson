Name:		python-meson
Version:	0.18.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/m/meson-python/meson_python-%{version}.tar.gz
Summary:	Meson Python build backend (PEP 517)
URL:		https://pypi.org/project/meson-python/
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pyproject-metadata)
BuildRequires:	meson
BuildArch:	noarch

%description
Meson Python build backend (PEP 517)

%files
%{py_sitedir}/mesonpy
%{py_sitedir}/meson_python-*.*-info
