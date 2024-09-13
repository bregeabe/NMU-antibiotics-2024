# Antibiotic report

## Overview
The clinical sciences department creates antibiotic reports based on micro-organisms to find MIC's for patient treatment. Right now, they do this process by pen and paper. While it gets the job done, it has proven to be ineffective and an inaccurate representation of the industry. 

Our software solution would function from a birdseye view is as quite simple. We would need to have a form to enter patient information, a "Specimen Requisition Form". This information would then be able to be represented as a barcode that could be printed out, and scanned to add more information, and view current information. 

## System expectations

From a software standpoint, we can approach this intuitively and provide a deliverable without too much overhead.

1. Make the "Specimen Requisition", and "Work Card" forms
2. Have an sql database holding each forms information, linking by an ID. 
3. Allow our data to be populated by scanning the barcode

We want to be able to store the data in these cards, and have the data be loaded and populated into our program upon barcode scan. 

We can achieve this by the relation in the database, upon scanning, it calls a get request to our database based upon the ID scanned. Similarly, upon editing date, it will post this data to the database, in which it can be retrieved later (GET and POST are just naming conventions, this will not be a network-based application. All local.)

## Entities
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
    - *testOrdered* (boolean) - What kind of test was ordered for the patient?
- **Staff** (user)
- **Specimen**
    - *type* (enum) - What type is the specimen - CSF, Urine, Sputum etc.
    - *directGramStain* (enum) - Test that checks to see if you have a bacterial infection.
    - *cultureReadout* (struct) - read out cultures each day until they can be finalized. 
        - date (date) - MM/DD/YYYY
        - time (time) - Military time
        - criticalResults - Document if a result was "critical" and called directly to the provider.
    - *colonyDescription* (string) - physically describe the colonies.
    - *biochemicalReactions* (string) - list all biochemical testing performed and what the results were.
    - *simulatedBiochems* (struct) - These are simulated tests to demonstrate ideas to the tests they cannot run.
        - testName (string) 
        - describeInoculation 
        - temperature (integer)
        - duration (string) 
        - atmosphericConditions
        
## Entity relation diagram
![diagram](./assets/antibiotic-report-diagram.png)

## Queries

- Patient information, patientId, retrieves information about the patient.

- Specimen information, specimenId, retrieves information about the specimen.

# Events

- add/edit patient - 

- add/edit specimen - 

- add/edit patientSpecimen - 

- getPatientInformation - this will retrieve information about the patient. For example, name, date of birth, gender, etc., any information about just the patient. Parameters: patientId

- getSpecimenInformation - this will retrieve information about the specimen. Things like the specimen name, specimen ID, etc. Anything that only pertains to the specimen. Don't mistake specimen information for patient specimen information, any specimen information that is not the same for every patient it interacts with is patientSpecimen information, as the data is reliant on both. Parameters: specimenId

- getPatientSpecimenInformation - this will retrieve information about the patients specimen test that is getting the antibiotic report run. For example, culture results will be a part of patient-specimen information as it is dependent on both the patient, and the specimen. Parameters: patientId, specimenId
