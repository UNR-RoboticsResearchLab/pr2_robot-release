Name:           ros-indigo-pr2-robot
Version:        1.6.9
Release:        0%{?dist}
Summary:        ROS pr2_robot package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_robot
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-imu-monitor
Requires:       ros-indigo-pr2-bringup
Requires:       ros-indigo-pr2-camera-synchronizer
Requires:       ros-indigo-pr2-computer-monitor
Requires:       ros-indigo-pr2-controller-configuration
Requires:       ros-indigo-pr2-ethercat
Requires:       ros-indigo-pr2-run-stop-auto-restart
BuildRequires:  ros-indigo-catkin

%description
This stack collects PR2-specific components that are used in bringing up a
robot.

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
* Tue Sep 01 2015 Austin Hendrix <ahendrix@willowgarage.com> - 1.6.9-0
- Autogenerated by Bloom

* Fri Feb 13 2015 Austin Hendrix <ahendrix@willowgarage.com> - 1.6.7-0
- Autogenerated by Bloom

