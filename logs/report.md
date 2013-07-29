Network setup report
====================

This report shows the results from the LUMC-SARA Lightpath setup.

The virtual machine running at SARA requires a setup with 3 network interfaces.

eth0 should connect to the internal-private network in the 10.0.<vm>.x range where additional vms should inter-connect to. This is the only interface where the NFS ``virdir`` can be reached (10.0.<vm>.4).

eth1 is the public interface (to internet), no additional configuration needed.

eth2 is the second internal network interface which is used for the lightpath connection (needs static IP configuration)

For the complete setup in /etc/network/interfaces see the file [interfaces](interfaces).

The resulting route setup is as follows:

see log in [route.log](route.log)

Network speed
-------------

In the new setup with the working Ligthpath, the speed is determined by the slowest factor:
The virtual machine connected to the ``virdir``. We see a 100% load on 1 ``cpu core`` on the sftp process.
The VM itself seems not to be the problem, drops in speed doesn't relate to lack of cpu power (we have 8 cores, 1 dedicated on the sftp process)
We are still measuring the statistics, the slowdown factor can be explained by the fact that the ``virdir`` is a shared facility.

see log in [transfer-via-vm.log](transfer-via-vm.log).

In an alternate setup where we transfer directly from shark to the [`virdir`](virdir.cloud.sara.nl), we see a constant/stable connection.
The dataset is 78514052 bytes large (75GB), time take for this transfer: 33:37 min (mm:ss).

The average speed in this setup was 38926 B/s (38.01 MB/s)

see log in [sara_ngs.o5213922](sara_ngs.o5213922)






