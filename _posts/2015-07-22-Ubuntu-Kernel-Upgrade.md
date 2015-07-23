---
layout: post
comments: true
title: How to safely upgrade your linux kernel
date: 2015-07 22:39:00
permalink: Upgrading Linux Kernel
---
It's a bit difficult safely upgrading your linux kernel from an older kernel without glitches losing your unity desktop or lightdm environement or being able to correctly log into your newly installed kernel after all has been said and done. So I decided to write this blog post after previous efforts at unsuccessfully upgrading my kernel from a Linux 3.16 version. For simplicity, we'll assume you are running a debian distro such as ubuntu or cent-os. If you have a different distro, you could download the kernel straight from [Linux Kernel](https://www.kernel.org/), untar the downloaded file and follow the instructions in the README in order to compile with cmake. After compiling your kernel, go to [setting up your new kernel](#Setting up your new kernel) to be able to log on to your new kernel when next you reboot.

The maintainers over at Ubuntu have compiled the kernel on their [ppa's](http://kernel.ubuntu.com/~kernel-ppa/mainline/) and you could pick which ever kernel you wish to upgrade to. For me, I was upgrading from 3.16 to 4.04; so for the purpose of this tutorial, our instructions will be based on upgrading to kernel 4.0.4.

First of all, make sure you have all your files properly backed up in a safe place before attempting an upgrade of your kernel.

##Files Download

For 32-bit systems, let's pull the following files from the ubuntu kernel repositories.

```
$ wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.0.4-wily/linux-headers-4.0.4-040004_4.0.4-040004.201505171336_all.deb

$ wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.0.4-wily/linux-headers-4.0.4-040004-generic_4.0.4-040004.201505171336_i386.deb

$ wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.0.4-wily/linux-image-4.0.4-040004-generic_4.0.4-040004.201505171336_i386.deb
```

If, however, your system is a 64-Bit System, yu would want to pull the following files instead:

```
$ wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.0.4-wily/linux-headers-4.0.4-040004_4.0.4-040004.201505171336_all.deb

$ wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.0.4-wily/linux-headers-4.0.4-040004-generic_4.0.4-040004.201505171336_amd64.deb

$ wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.0.4-wily/linux-image-4.0.4-040004-generic_4.0.4-040004.201505171336_amd64.deb
```

Next, install each of the files from your terminal window

	<pre><code>$ sudo dpkg -i linux-headers-4.0.4*.deb linux-image-4.0.4*.deb</pre></code>

Hang in there. Le's set up **GRUB** to point to the new kernel installation. This is necessary so that when you restart your system, your bootloader gives you the option to choose which kernel to load (Grub 2.02 does this, I have not tried it on other grub versions)

If at anytime, you want to uninstall, just go ahead and do the following:

	<pre><code>sudo apt-get remove 'linux-headers-4.0.4*' 'linux-image-4.0.4*'</pre></code>

##Setting up your new kernel

We'll assume your boot-loader is **GRUB**. The steps we carried out above will upgrade the linux installation which could also have been performed with the following (rather _unsafe_) commands:

```
sudo aptitude update
sudo aptitude safe-upgrade
```

I call those unsafe because you do not have control of wat happens during the upgrade process and it is well documented that such methods have been known to tamper with graphic drivers and what-a-view after upgrades. I generally prefer going the old-fashioned way as I describe in this post.

Depending on your system configuration settings, after the steps above, you may find that your kernel and GRUB bootloader configuration have already been updated. Matter-of-factly, GRUB may automatically select the right boot menu option when you next restart your system. But before you go ahead and restart, you want to ensure everything is correctly set or you might find (as I did) that Mr. Lightdm/Gdm/Unity Desktop doesn’t show up after your reboot. 

Therefore, we will configure GRUB to  automatically check out our new kernel, and should it fail, we would like to be able to revert to the previous kernel. Since GRUB is configured by the file `/boot/grub/grub.cfg`, it makes sense to edit this brobdinagian file. But rather than work with the bugging lines of code in `/boot/grub/grub.cfg`, we will edit relevant lines in `/etc/default/grub`, then update grub to to have `/boot/grub/grub.cfg` see our latest grub edit.

Fire up /etc/default/grub in your favorite editor and set the following configurations:

-GRUB_DEFAULT=saved
-GRUB_TIMEOUT=5
-GRUB_CMDLINE_LINUX_DEFAULT=”panic=10″

Basically, we are telling GRUB to use the last-saved selection, do an auto boot-up after 5 seconds if user does nothing, and inform all kernels to reboot after 10 seconds if they die completely. Note, the TIMEOUT option is disabled in GRUB 2.02; so if your grub version is greater than version 2.0, you can discount line 2 above. 

Next, we will set the kernel that is initially _saved_. We will set this to the known working configuration such as 

     	<pre><code>$sudo grub-set-default "Ubuntu, with Linux 3.16.0-3-generic"</pre></code>

You could check the kernel you’re currently running with `uname -a` and determine the label used to select it in `/boot/grub/grub.cfg`.  Next, we will make GRUB try the new kernel on the next reboot, such as:

		<pre><code>$sudo grub-reboot ”Ubuntu, with Linux 4.0.4-04-new”</pre></code>

We will save our configurations to the boot folder using:

		<pre><code>$sudo update-grub</pre></code>

Try rebooting. 


	<pre><code>$sudo reboot </pre></code>

You should be fine.

If everything is honky-dory, set the new kernel as the saved default for future boot-up's:

		<pre><code>$sudo grub-set-default "Ubuntu, with Linux 4.0.4-04-new”<pre><code>

Congratulations!