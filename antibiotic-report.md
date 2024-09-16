# Antibiotic report

## Overview
The clinical sciences department creates antibiotic reports based on micro-organisms to find MIC's for patient treatment. Right now, they do this process by pen and paper. While it gets the job done, it has proven to be ineffective and an inaccurate representation of the industry. 

There are two main issues at hand.
1. In a hospital, you would fill out the forms digitaly rather than on pen and paper.
2. Finding the history of these forms is inefficent and, once again, an inaccurate representation of industry.

## System expectations

A birdseye solution is as follows:

1. Have the Specimen Requisition and Work Card forms digitalized and placed on the computer.
2. The information present in the forms would be represented as a barcode that can be printed out. 
3. The barcode can be scanned to add more information or view current information on the computer.

This results in a professional way for students to document patient and specimen info. Additionally, the students gain real world application as if they were working in the hospital itself.

## Entities
- **Staff** (user) - Student or faculty. 
 - **Patient**
    - *name* (string) - Last name, First name
    - *dateOfBirth* (date) - Date of birth in MM/DD/YYYY format.
    - *medicalRecordNumber/ PatientID* (integer) - 6 digit patient medical record number 
    - *gender* (boolean) - M of F 
    - *collectionDate* (date) - Date collected in MM/DD/YYYY
    - *collectionTime* - Collection time in military time
    - *source* (string) - Source of where the specimen was recieved. 
        - Examples include: Oral abcess swab, Urine midstream clean catch.
    - *orderingProvider* (string) - Who the ordering provider is.
        - Examples include: Dr. Renaldi, Dr. Mann, Dr. Thunell.
    - *diagnosis* (string) - The identification of a disease or condition. 
        - Examples inculude: Sore in mouth, Annual check up.
    - *isReceivingTherapy* (boolean) - is the patient recieving antimicrobial therapy?
    - *testOrdered* (string) - What kind of test was ordered for the patient?
- **Specimen**
    - *type* (enum) - What type is the specimen (CSF, Urine, Sputum etc.)
    - *directGramStain* (enum) - Test that checks to see if you have a bacterial infection / help identify it. (WBCs, EPIs, GPC, ...)  
    - *cultureReadout* (struct) - read out cultures each day until they can be finalized. 
        - date (date) - MM/DD/YYYY
        - time (time) - Military time
        - criticalResults - Document if a result was "critical" and called directly to the provider.
    - *colonyDescription* (string) - physically describe the colonies.
    - *biochemicalReactions* (string) - list all biochemical testing performed and what the results were.
    - *simulatedBiochems* (struct) - These are simulated tests to demonstrate ideas about tests they cannot run.
        - testName (string) 
        - describeInoculation 
        - temperature (integer)
        - duration (string) 
        - atmosphericConditions
        
## Entity relation diagram
![diagram](./assets/antibiotic-report-diagram.png)

## Queries

- **Q1** View Patient Information, Parameters: patientId OR name and dateOfBirth - this will retrieve information about the patient. For example, name, date of birth, gender, etc., any information about just the patient. 

- **Q2** View Specimen Information (can be barcode scan), Parameters: specimenId - this will retrieve information about the specimen. Things like the specimen name, specimen ID, etc. 

- **Q3** View all Patients - Show all patients in the system.

- **Q4** View all Specimen tied to Patient - Show all specimen tied to the patient.

## Events

- Add/Edit Patient Information - Shows the forum to either add or edit patient information.

- Add/Edit Specimen Information - Shows the forum to either add or edit specimen information.

## Platform

**R1** - The software will be installed on the computer inside of the clincal science lab room. 

**R2** - The software will be compatable with: Windows 7, Windows 8, Windows 10, Windows 11.

## User permissions

**R3** - The only users permitted are staff and students in the lab. An initial log in screen will appear and prompt for email and password. The email will be the users NMU email and password is users choice, please use fake passwords. 
- Note: This is not real authentication and the user is not tied to an account.

**R4** - To clear all patients and specimen, the professor or staff can enter a code to clear all entries. This would be useful at the start of new semesters.

## Security

**R5** - Minimal security measures will be taken with patients information as that information will be made up.

**R6** - Passwords for logging in will not be saved and only present to simulate logging into a hospitals system.

## Future Changes

- Every action may have a staff assigned to it. For example, if a new patient was added, it would show who created the form for the patient. 