Name:           ros-indigo-pr2-run-stop-auto-restart
Version:        1.6.10
Release:        4%{?dist}
Summary:        ROS pr2_run_stop_auto_restart package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_run_stop_auto_restart
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-pr2-msgs
Requires:       ros-indigo-pr2-power-board
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-std-srvs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-pr2-msgs
BuildRequires:  ros-indigo-pr2-power-board
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-std-srvs

%description
This package provides a node that monitors the state of the run stops of the
pr2_robot. When the state of the run stop changes from off to on, this node will
automatically enable the power to the motors, and reset the motors. This allows
you to use the run stop as a 'pause' button. By using the run stop as a tool to
power up the robot, the run stop is also in reach of the user once the robot
starts moving.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Feb 22 2016 Devon Ash <ahendrix@willowgarage.com> - 1.6.10-4
- Autogenerated by Bloom

* Fri Jan 22 2016 Devon Ash <ahendrix@willowgarage.com> - 1.6.10-3
- Autogenerated by Bloom

* Fri Jan 08 2016 Devon Ash <ahendrix@willowgarage.com> - 1.6.10-2
- Autogenerated by Bloom

* Fri Dec 04 2015 Devon Ash <ahendrix@willowgarage.com> - 1.6.10-1
- Autogenerated by Bloom

* Wed Sep 16 2015 Devon Ash <ahendrix@willowgarage.com> - 1.6.10-0
- Autogenerated by Bloom

* Tue Sep 01 2015 Austin Hendrix <ahendrix@willowgarage.com> - 1.6.9-0
- Autogenerated by Bloom

* Fri Feb 13 2015 Austin Hendrix <ahendrix@willowgarage.com> - 1.6.7-0
- Autogenerated by Bloom

