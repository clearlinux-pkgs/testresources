#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x597240FE94E60165 (rbtcollins@hp.com)
#
Name     : testresources
Version  : 2.0.1
Release  : 33
URL      : http://pypi.debian.net/testresources/testresources-2.0.1.tar.gz
Source0  : http://pypi.debian.net/testresources/testresources-2.0.1.tar.gz
Source99 : http://pypi.debian.net/testresources/testresources-2.0.1.tar.gz.asc
Summary  : Testresources, a pyunit extension for managing expensive test resources
Group    : Development/Tools
License  : Apache-2.0
Requires: testresources-python3
Requires: testresources-python
Requires: fixtures
Requires: pbr
BuildRequires : fixtures
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest

BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
of resources by test cases.
        
        Copyright (C) 2005-2013  Robert Collins <robertc@robertcollins.net>
        
          Licensed under either the Apache License, Version 2.0 or the BSD 3-clause
          license at the users choice. A copy of both licenses are available in the
          project source as Apache-2.0 and BSD. You may not use this file except in
          compliance with one of these two licences.
        
          Unless required by applicable law or agreed to in writing, software
          distributed under these licenses is distributed on an "AS IS" BASIS, WITHOUT
          WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
          license you chose for the specific language governing permissions and
          limitations under that license.
        
          See the COPYING file for full details on the licensing of Testresources.
        
        
        Testresources
        +++++++++++++
        
        testresources extends unittest with a clean and simple api to provide test
        optimisation where expensive common resources are needed for test cases - for
        example sample working trees for VCS systems, reference databases for
        enterprise applications, or web servers ... let imagination run wild.
        
        Dependencies to build/selftest
        ==============================
        
        * Python 2.6+ (or 3.3+)
        * docutils

%package python
Summary: python components for the testresources package.
Group: Default
Requires: testresources-python3

%description python
python components for the testresources package.


%package python3
Summary: python3 components for the testresources package.
Group: Default
Requires: python3-core

%description python3
python3 components for the testresources package.


%prep
%setup -q -n testresources-2.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517698563
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
