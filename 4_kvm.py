# Practical No. 4
# Aim:
# Installation and configuration of virtualization using KVM.

# Software Tools Required
# Virtual Machine Monitor : VMware Workstation
# Operating System : Linux (Ubuntu)

# Downloads Required
# 1. VMware Workstation Pro 17.6.0
# 2. Ubuntu 24.04 LTS ISO

# Steps to Create Virtual Machine
# 1. Open VMware Workstation
# 2. Click Create New Virtual Machine
# 3. Select Typical (Recommended)
# 4. Browse Ubuntu ISO file
# 5. Enter username and password
# 6. Set VM name: KVM
# 7. Disk size: 16 GB
# 8. Enable Virtualize Intel VT-x / AMD-V
# 9. Finish and Power On

# Ubuntu Installation
# 1. Select language: English
# 2. Keyboard layout: English US
# 3. Select Install Ubuntu
# 4. Choose Default Installation
# 5. Tick Install third-party software
# 6. Select Erase disk and install Ubuntu
# 7. Set location: Mumbai (Asia/Kolkata)
# 8. Restart system

# KVM Setup Steps

# Update system
# sudo apt update && sudo apt upgrade -y

# Check virtualization
# grep -c "svm\|vmx" /proc/cpuinfo

# Install cpu checker
# sudo apt install cpu-checker

# Verify KVM
# kvm-ok

# Install KVM packages
# sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients virt-manager bridge-utils -y

# Enable libvirt
# sudo systemctl enable libvirtd
# sudo systemctl start libvirtd

# Add user to KVM group
# sudo usermod -aG kvm $USER
# sudo usermod -aG libvirt $USER

# Logout and login again

# Result:
# KVM virtualization successfully installed and configured.
