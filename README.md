NGS Performance test by LUMC on SurfSARA cloud
==============================================

Introduction
------------

This repo will hold all scripts and testresults generated for the Proof of 
Concept: Scale-out solutions for HPC cluster SHARK to SurfSARA cloud.


Project activities
------------------

1. Notify SASC advisory group about project
1. Acquire account for SARAHPC
1. Let ICT Department modify firewall rules
1. Let ICT Department/INFRA modify/check static routing to virdir.cloud.sara.nl
    To take advantage of the fiber/lightpath connection to SARA.
1. Setup VM at SARA
1. Setup /virdir at SARA, mimmic /data and /usr/local 
    ( clone from shark with tools needed for this experiment )
1. Transfer FastQ files for this experiment (105 GB, from ~scr project)
1. Transfer pipeline to SARA VM
1. Setup testing environment to wrap the pipeline
1. Execute testing scripts
1. Transfer results back to cluster/LUMC local
1. Analyse results
1. Write report
1. Send report to advisory board for comments
1. Send (final) report to all parties involved in project



Project members
---------------
* Wai Yi Leung (LUMC SASC)
* Leon Mei (LUMC SASC)
* Rob Cornellise (LUMC ICT)
* Jan Bot (SurfSARA)

Associated groups shown interest in project
-------------------------------------------
* LGTC
* Human Genetics
* LUMC ICT

Grant
-----

This project is supported by a grand received from SurfSARA under number: 
> e-infra130041

Contact
-------

* SurfSARA:
    - Lykle Voort
    - Ander Astudillo

* LUMC:
    - Wai Yi Leung
