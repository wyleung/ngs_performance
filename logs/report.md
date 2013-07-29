Network setup report
====================

Introduction
------------

This report shows the results from the LUMC-SARA Lightpath setup.

The virtual machine running at SARA requires a setup with 3 network
interfaces.

eth0 should connect to the internal-private network in the 10.0.<vm>.x 
range where additional vms should inter-connect to. This is the only 
interface where the NFS ``virdir`` can be reached (10.0.<vm>.4).

eth1 is the public interface (to internet), no additional configuration needed.

eth2 is the second internal network interface which is used for the 
lightpath connection (needs static IP configuration)

For the complete setup in /etc/network/interfaces see the file [interfaces].







