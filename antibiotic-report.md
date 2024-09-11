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
- Patient
    - name (string)
    - dateOfBirth (date)
    - medicalRecordNumber (integer)
    - gender (enum)
    - collectionDate (date)
    - source (string)
    - orderingProvider (string)
    - diagnosis (string)
    - isReceivingTherapy (boolean)
    - testOrdered (boolean)
- Staff (user)
- Specimen
    - type (enum)
    - directGrainStrain (enum)
    - cultureReadout (struct)
        - date (date)
        - time (time)
        - criticalResults
    - colonyDescription (string)
    - biochemicalReactions (string)
    - simulatedBiochems (struct)
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

- getPatientInformation - this will retrieve information about the patient. For example, name, date of birth, gender, etc., any information about just the patient. Parameters: patientId

- getSpecimenInformation - this will retrieve information about the specimen. Things like the specimen name, specimen ID, etc. Anything that only pertains to the specimen. Don't mistake specimen information for patient specimen information, any specimen information that is not the same for every patient it interacts with is patientSpecimen information, as the data is reliant on both. Parameters: specimenId

- getPatientSpecimenInformation - this will retrieve information about the patients specimen test that is getting the antibiotic report run. For example, culture results will be a part of patient-specimen information as it is dependent on both the patient, and the specimen. Parameters: patientId, specimenId
