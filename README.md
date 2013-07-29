NGS Performance test by LUMC on SurfSARA cloud
==============================================

Introduction
------------

This repo will hold all scripts and testresults generated for the Proof of 
Concept: __Scale-out solutions for HPC cluster SHARK to SurfSARA cloud__.


Project activities
------------------

1. ~~Notify SASC advisory group about project~~ 18-03-2013
1. ~~Acquire account for SARAHPC~~ 02-05-2013
1. ~~Let ICT Department modify firewall rules, allow SSH+SCP to virdir.cloud.sara.nl~~
    * Bert signed "**Aanvraagformulier externe verbingen**" 06-05-2013
1. Let ICT Department/INFRA modify/check static routing to virdir.cloud.sara.nl
    * To take advantage of the fiber/lightpath connection to SARA.
    * 06-05-2013: ~~Sent e-mail to R.Hollenbeek (ICT) to add routes to:~~
        * ~~145.100.56.18 (virdir)~~
        * ~~145.100.58.x (VM range)~~
1. ~~Setup VM at SARA~~ 03-05-2013
1. ~~Setup /virdir at SARA, mimmic /data and /usr/local~~ 03-05-2013
    * ~~( clone from shark with tools needed for this experiment )~~
1. ~~Transfer FastQ files for this experiment (105 GB, from ~scr project)~~ 03-05-2013
1. ~~Meeting Rob, Sander and Maarten about LP setup, re-connect LP and re-arrange IPs 19-07-2013~~
1. ~~Working setup in logs/interfaces logs/route.log~~
1. ~~Transfer pipeline to SARA VM see logs/transfer-via-vm.log~~
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

Associated groups shown interest in this project
------------------------------------------------
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

Acknowledgements:
----------------------------------
* Jhon Masschelein (SurfSARA) for setting up the VM and tackling the wrong setup.
* Sander Boele (SURFSara)
* Maarten Schats (LUMC ICT)

