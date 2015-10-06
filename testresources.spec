#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : testresources
Version  : 0.2.7
Release  : 13
URL      : https://pypi.python.org/packages/source/t/testresources/testresources-0.2.7.tar.gz
Source0  : https://pypi.python.org/packages/source/t/testresources/testresources-0.2.7.tar.gz
Summary  : Testresources, a pyunit extension for managing expensive test resources
Group    : Development/Tools
License  : Apache-2.0
Requires: testresources-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fixtures-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : testtools
BuildRequires : testtools-python

%description
testresources: extensions to python unittest to allow declarative use
of resources by test cases.

%package python
Summary: python components for the testresources package.
Group: Default

%description python
python components for the testresources package.


%prep
%setup -q -n testresources-0.2.7

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pushd py2; py.test-2.7 ; popd
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
