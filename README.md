Extract Patient Data from Files using Python (Jupyter and Django):

1. Read HL7 data files. ( using Jupyter ) to connect Jupyter Notebook with Django you need to use (django-extensions==3.2.3)

use this command to run this script(python manage.py shell_plus --lab --no-browser)

Parse the HL7 messages to extract patient information.

2.Store Data in Django Database(using the Jupyter):

3. Define Django models for Encounter_charges and Error_charges.

4. Store valid patient data in the Patient table. fields(patient first name, last name, date of birth, MRN (MEDICAL RECORD NUMBER),Physician name,phone )

5. Data Processing:

Check for missing fields (DOB, MRN, PATIENT NAME) in the extracted patient data.

If the above fields are missed consider that as error charges

6. Store the error charges in the Error_charges table with error as (dob not found, patient name not found,mrn not found )

7. Display Errors as Cards(UI in application): Error title and its count

Implement a Django view to fetch and display errors as cards in a frontend interface.

Time Duration for the above task: 1 day
