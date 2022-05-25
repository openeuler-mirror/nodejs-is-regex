%{?nodejs_find_provides_and_requires}
Name:                nodejs-is-regex
Version:             1.0.4
Release:             2
Summary:             Is this value a JS regex?
License:             MIT
URL:                 https://github.com/ljharb/is-regex
Source0:             https://registry.npmjs.org/is-regex/-/is-regex-%{version}.tgz
BuildArch:           noarch
ExclusiveArch:       %{nodejs_arches} noarch
BuildRequires:       nodejs-packaging npm(tape)
%description
Is this value a JS regex? This module works cross-realm/iframe, and
despite ES6 @@toStringTag.

%prep
%setup -q -n package
rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/is-regex
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/is-regex
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%if "%{_build_arch}" == "riscv64"
%{__nodejs} --harmony test.js
%else
%{__nodejs} --harmony --es-staging test.js
%endif

%files
%{!?_licensedir:%global license %doc}
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/is-regex

%changelog
* Tue May 24 2022 YukariChiba <i@0x7f.cc> - 1.0.4-2
- Remove `--es-staging` flag which is not exist.

* Thu Aug 20 2020 wangxiao <wangxiao65@huawei.com> - 1.0.4-1
- Package init
