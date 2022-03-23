# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 12:40:33 2022

@author: camillo.majerczyk
"""

import pandas as pd
from lxml import etree as et #conda install -c anaconda lxml

#%%
raw_data = pd.read_excel(r'|Directory to the Excel File|')

raw_data['birthdate'] = raw_data['birthdate'].dt.date
raw_data['administerdate'] = raw_data['administerdate'].dt.date
raw_data['startdate'] = raw_data['startdate'].dt.date
raw_data['refilluntildate'] = raw_data['refilluntildate'].dt.date

#%%

root = et.Element('joborders')
root_jobidentifier = et.SubElement(root, 'job_identifier')
root_pistype = et.SubElement(root, 'pistype')
root_createdatetime = et.SubElement(root, 'createdatetime')
root_OISRecordId = et.SubElement(root, 'OISRecordId')
root_imageDirPath = et.SubElement(root, 'imageDirPath')
root_MultiDoseInd = et.SubElement(root, 'MultiDoseInd')
root_pharmacyid = et.SubElement(root, 'pharmacyid')

root_createdatetime.text = str(raw_data['CreationDate'].iloc[0])

#%%

root_pharmacy = et.SubElement(root, 'pharmacy')

pharmacy_id = et.SubElement(root_pharmacy, 'id')
pharmacy_name = et.SubElement(root_pharmacy, 'name')
pharmacy_DEANumber = et.SubElement(root_pharmacy, 'DEANumber')
pharmacy_address1 = et.SubElement(root_pharmacy, 'address1')
pharmacy_address2 = et.SubElement(root_pharmacy, 'address2')
pharmacy_city = et.SubElement(root_pharmacy, 'city')
pharmacy_state = et.SubElement(root_pharmacy, 'state')
pharmacy_postalcode = et.SubElement(root_pharmacy, 'postalcode')
pharmacy_phonenumber1 = et.SubElement(root_pharmacy, 'phonenumber1')
pharmacy_phonenumber2 = et.SubElement(root_pharmacy, 'phonenumber2')

#%%

root_Manufacturers = et.SubElement(root, 'Manufacturers')
Manufacturers_manufacturer = et.SubElement(root_Manufacturers, 'manufacturer')
manufacturer_id = et.SubElement(Manufacturers_manufacturer, 'id')
manufacturer_name = et.SubElement(Manufacturers_manufacturer, 'name')

#%%

root_Formulary = et.SubElement(root, 'Formulary')

for drug in raw_data.drop_duplicates(subset = ["drugname"]).iterrows():

    Formulary_drug = et.SubElement(root_Formulary, 'drug')

    drug_id = et.SubElement(Formulary_drug, 'id')
    drug_ndc = et.SubElement(Formulary_drug, 'ndc')
    drug_drugname = et.SubElement(Formulary_drug, 'drugname')
    drug_alternatename = et.SubElement(Formulary_drug, 'alternatename')
    drug_shortname = et.SubElement(Formulary_drug, 'shortname')
    drug_strength = et.SubElement(Formulary_drug, 'strength')
    drug_description = et.SubElement(Formulary_drug, 'description')
    drug_manufactureid = et.SubElement(Formulary_drug, 'manufactureid')
    drug_warning = et.SubElement(Formulary_drug, 'warning')
    drug_caution = et.SubElement(Formulary_drug, 'caution')
    drug_indications = et.SubElement(Formulary_drug, 'indications')
    drug_form = et.SubElement(Formulary_drug, 'form')
    drug_shape = et.SubElement(Formulary_drug, 'shape')
    drug_colour = et.SubElement(Formulary_drug, 'colour')
    drug_diameter = et.SubElement(Formulary_drug, 'diameter')
    drug_height = et.SubElement(Formulary_drug, 'height')
    drug_weight = et.SubElement(Formulary_drug, 'weight')
    drug_markingfront = et.SubElement(Formulary_drug, 'markingfront')
    drug_markingback = et.SubElement(Formulary_drug, 'markingback')
    
    drug_id.text = str(drug[1]['id_farmaco'])
    drug_ndc.text = str(drug[1]['ndc'])
    drug_drugname.text = str(drug[1]['drugname'])
    drug_form.text = str(drug[1]['form'])

#%%

root_Facilities = et.SubElement(root, 'Facilities')

for facility in raw_data.drop_duplicates(subset = ["id_facilitys"]).iterrows():
    
    Facilities_facility = et.SubElement(root_Facilities, 'facility')
    
    facility_id = et.SubElement(Facilities_facility, 'id')
    facility_name = et.SubElement(Facilities_facility, 'name')
    facility_address1 = et.SubElement(Facilities_facility, 'address1')
    facility_address2 = et.SubElement(Facilities_facility, 'address2')
    facility_address3 = et.SubElement(Facilities_facility, 'address3')
    facility_city = et.SubElement(Facilities_facility, 'city')
    facility_state = et.SubElement(Facilities_facility, 'state')
    facility_postalcode = et.SubElement(Facilities_facility, 'postalcode')
    facility_phonenumber1 = et.SubElement(Facilities_facility, 'phonenumber1')
    facility_phonenumber2 = et.SubElement(Facilities_facility, 'phonenumber2')
    facility_facilitypackagetype = et.SubElement(Facilities_facility, 'facilitypackagetype')
    facility_facilityInitials = et.SubElement(Facilities_facility, 'facilityInitials')
    facility_nursingStationCode = et.SubElement(Facilities_facility, 'nursingStationCode')
    
    facility_id.text = str(facility[1]['id_facilitys'])
    facility_name.text = str(facility[1]['name_facility'])

#%%

root_Physicians = et.SubElement(root, 'Physicians')

Physicians_physician = et.SubElement(root_Physicians, 'physician')

physician_id = et.SubElement(Physicians_physician, 'id')
physician_deanumber = et.SubElement(Physicians_physician, 'deanumber')
physician_title = et.SubElement(Physicians_physician, 'title')
physician_firstname = et.SubElement(Physicians_physician, 'firstname')
physician_middlename = et.SubElement(Physicians_physician, 'middlename')
physician_lastname = et.SubElement(Physicians_physician, 'lastname')
physician_initials = et.SubElement(Physicians_physician, 'initials')

#%%

root_Patients = et.SubElement(root, 'Patients')

for patient in raw_data.drop_duplicates(subset = ["id_patients"]).iterrows():
    
    Patients_patient = et.SubElement(root_Patients, 'patient')
    
    patient_id = et.SubElement(Patients_patient, 'id')
    patient_firstname = et.SubElement(Patients_patient, 'firstname')
    patient_middlename = et.SubElement(Patients_patient, 'middlename')
    patient_lastname = et.SubElement(Patients_patient, 'lastname')
    patient_address1 = et.SubElement(Patients_patient, 'address1')
    patient_address2 = et.SubElement(Patients_patient, 'address2')
    patient_address3 = et.SubElement(Patients_patient, 'address3')
    patient_city = et.SubElement(Patients_patient, 'city')
    patient_state = et.SubElement(Patients_patient, 'state')
    patient_postalcode = et.SubElement(Patients_patient, 'postalcode')
    patient_station = et.SubElement(Patients_patient, 'station')
    patient_room = et.SubElement(Patients_patient, 'room')
    patient_bed = et.SubElement(Patients_patient, 'bed')
    patient_birthdate = et.SubElement(Patients_patient, 'birthdate')
    patient_facilityId = et.SubElement(Patients_patient, 'facilityId')
    patient_imageFile = et.SubElement(Patients_patient, 'imageFile')
    
    patient_id.text = str(patient[1]['id_patients'])
    patient_firstname.text = str(patient[1]['firstname'])
    patient_lastname.text = str(patient[1]['lastname'])
    patient_station.text = str(patient[1]['station'])
    patient_birthdate.text = str(patient[1]['birthdate'])
    
    #print(patient[1]['id_patients'])
    
    for prescription in raw_data[raw_data.id_patients == patient[1]['id_patients']].drop_duplicates(subset = ["prescriptionnumber"]).iterrows():
        
        patient_Prescriptions = et.SubElement(Patients_patient, 'Prescriptions')
        
        Prescriptions_prescription = et.SubElement(patient_Prescriptions, 'prescription')
        
        patient_prescriptionnumberoriginal = et.SubElement(Prescriptions_prescription, 'prescriptionnumberoriginal')
        patient_prescriptionnumber = et.SubElement(Prescriptions_prescription, 'prescriptionnumber')
        patient_startdate = et.SubElement(Prescriptions_prescription, 'startdate')
        patient_totalquantity = et.SubElement(Prescriptions_prescription, 'totalquantity')
        patient_directions = et.SubElement(Prescriptions_prescription, 'directions')
        patient_refills = et.SubElement(Prescriptions_prescription, 'refills')
        patient_refilluntildate = et.SubElement(Prescriptions_prescription, 'refilluntildate')
        patient_priority = et.SubElement(Prescriptions_prescription, 'priority')
        patient_facilityId = et.SubElement(Prescriptions_prescription, 'facilityId')
        patient_patientId = et.SubElement(Prescriptions_prescription, 'patientId')
        patient_physicianId = et.SubElement(Prescriptions_prescription, 'physicianId')
        patient_medicationtraynumber = et.SubElement(Prescriptions_prescription, 'medicationtraynumber')
        patient_drugId = et.SubElement(Prescriptions_prescription, 'drugId')
        patient_pharmacyId = et.SubElement(Prescriptions_prescription, 'pharmacyId')
        
        patient_prescriptionnumber.text = str(prescription[1]['prescriptionnumber'])
        patient_startdate.text = str(prescription[1]['startdate'])
        patient_refilluntildate.text = str(prescription[1]['refilluntildate'])
        
        for misc in raw_data[(raw_data.id_patients == patient[1]['id_patients']) & (raw_data.prescriptionnumber == prescription[1]["prescriptionnumber"])].drop_duplicates(subset = ["ndc"]).iterrows():
        
            patient_misc = et.SubElement(Prescriptions_prescription, 'misc')
        
            patient_misc_BillingInd = et.SubElement(patient_misc, 'BillingInd')
            patient_misc_NewRefill = et.SubElement(patient_misc, 'NewRefill')
            patient_misc_FreqInd = et.SubElement(patient_misc, 'FreqInd')
            patient_misc_CycleFillFlag = et.SubElement(patient_misc, 'CycleFillFlag')
            patient_misc_Cautions = et.SubElement(patient_misc, 'Cautions')
            patient_misc_facilityPatient = et.SubElement(patient_misc, 'facilityPatient')
            patient_misc_roomBed = et.SubElement(patient_misc, 'roomBed')
            patient_misc_NDC = et.SubElement(patient_misc, 'NDC')
            patient_misc_refillsremaining = et.SubElement(patient_misc, 'refillsremaining')
            patient_misc_physicianname = et.SubElement(patient_misc, 'physicianname')
            patient_misc_substitutefor = et.SubElement(patient_misc, 'substitutefor')
            
            patient_misc_NDC.text = str(misc[1]['ndc'])
        
        prescription_dosingInformation = et.SubElement(Prescriptions_prescription, 'dosingInformation')
        
        for dose in raw_data[(raw_data.id_patients == patient[1]['id_patients']) & (raw_data.prescriptionnumber == prescription[1]["prescriptionnumber"])].drop_duplicates(subset = ["administerdate", "administertime"]).iterrows():
             
             prescription_dosingInformation_dose = et.SubElement(prescription_dosingInformation, 'dose')
             
             patient_dosingInformation_dose_administerdate = et.SubElement(prescription_dosingInformation_dose, 'administerdate')
             patient_dosingInformation_dose_administertime = et.SubElement(prescription_dosingInformation_dose, 'administertime')
             patient_dosingInformation_dose_dosingquantity = et.SubElement(prescription_dosingInformation_dose, 'dosingquantity')
             
             patient_dosingInformation_dose_administerdate.text = str(dose[1]['administerdate'])
             patient_dosingInformation_dose_administertime.text = str(dose[1]['administertime'])
             patient_dosingInformation_dose_dosingquantity.text = str(dose[1]['dose'])
        
        prescription_LabelData = et.SubElement(Prescriptions_prescription, 'LabelData')
        
        LabelData_Data = et.SubElement(prescription_LabelData, 'Data')
        
        LabelData_Data_Key = et.SubElement(LabelData_Data, 'Key')
        LabelData_Data_Value = et.SubElement(LabelData_Data, 'Value')
        
#%%Build up the tree
tree = et.ElementTree(root)
et.indent(tree, space="\t", level=0)

#%%Save the file
tree.write('newfilename.xml', encoding="utf-8")
