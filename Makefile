all: rpm

rpm:
	yum install -y rpm-build make gcc
	rpmbuild --define "_topdir ${PWD}" -ba SPECS/tgcd.spec

.PHONY: all
