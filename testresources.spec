#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : testresources
Version  : 2.0.1
Release  : 22
URL      : http://pypi.debian.net/testresources/testresources-2.0.1.tar.gz
Source0  : http://pypi.debian.net/testresources/testresources-2.0.1.tar.gz
Summary  : Testresources, a pyunit extension for managing expensive test resources
Group    : Development/Tools
License  : Apache-2.0
Requires: testresources-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
testresources: extensions to python unittest to allow declarative use
of resources by test cases.

%package python
Summary: python components for the testresources package.
Group: Default

%description python
python components for the testresources package.


%prep
%setup -q -n testresources-2.0.1

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
