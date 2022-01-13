# Opentrons_LoCost_Covid19
Protocol for sequencing Covid19 genomes in large scale using the OT-2 (Opentrons)

Repository for python scripts to use with the Opentrons OT-2 for whoe genome sequencing of Covid-19 using the LoCost protocol developed for Oxford Nanopore Sequencing Chemistry

Automation of standard lab workflows allows for greater ease in upscaling processes while reducing the chances of errors and contamination. Using a liquid handling robot coupled with a python api, it has been possible to adapt a previously established protocol for Covid-19 sequencing (Quick, 2019 Amplicon sequencing protocol for SARS-CoV-2 v3 LoCost) in order to automate the majority of steps post-amplicon sequencing. This is performed using an Opentrons OT-2 robot and its API written using python to design scripts for each step. The automated process involves four stages of dilution, end preparation, barcode ligation, and library pooling. Following on from pooling it is easy perform the remaining steps of the protocol manually. Samples can be prepared in batches of 48 or 96 (including positive and negative controls) and there are variations of the script to facilitate different initial conditions and total samples. Additionally, the OT-2 has been designed with an open-source approach meaning that a variety of different types of labware and reagent reservoirs can be utilised. In this protocol specific pre-designated types of labware already recognised by the API have been used as these allow for a wide variety of labware to be used depending on what is available in the lab. This is possible as calibration is performed to the base of each type of labware being used. The labware defined in the protocol is similar to a deep well plate that requires a high clearance which allows for a range of different 96 well plates to be used without a risk of collision. The adaptability of this protocol provides a possible easy upscaling method for a wide variety of labs performing genome sequencing not just with Covid-19 but also for other high throughput processes.

This protocol has four automated steps which are listed below:

1. PCR Dilution        
option 1:  1_dilution_run_per_plate.py   option 2:1_dilution_pool_per_plate.py
 
2. End Preparation                
2_endrepair.py
 
3. Native Barcoding               
3_barcoding.py
 
4. Library Pooling     
option 1:  4_pooling_48_samples.py      option 1: 4_pooling_96_samples.py

For this automated sequencing method, download the pdf file "semi-automated-ncov-2019-locost-protocol-using-the-ot2_opentrons.pdf" along with the 4 parts of the protocol in the repository. 

Perform the steps as required for cDNA and PCR preparation. Following this, load parts 1 to 4 into the OT-2 and follow the instructions for each stage of the process. 

A pdf version of the protocols.io method is also within this directory to follow instructions for the LoCost protocol
Once the DOI is generated for this protocol, it will be added to the repository.
