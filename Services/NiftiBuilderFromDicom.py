import dicom2nifti
import glob
import os
import nibabel as nib
import numpy as np
import shutil


def create_nifti_images_from_dicom_series(in_path_images='D:/GraduateWorkData/dicom_groups/images/*',
                                          out_path_images='D:/GraduateWorkData/nifti files/images'):
    list_images = glob.glob(in_path_images)
    for patient in list_images:
        patient_name = os.path.basename(os.path.normpath(patient))
        dicom2nifti.dicom_series_to_nifti(patient, os.path.join(out_path_images, patient_name + '.nii.gz'))


def create_nifti_labels_from_dicom_series(in_path_labels='D:/GraduateWorkData/dicom_groups/labels/*',
                                          out_path_labels='D:/GraduateWorkData/nifti files/labels'):
    list_labels = glob.glob(in_path_labels)
    for patient in list_labels:
        patient_name = os.path.basename(os.path.normpath(patient))
        dicom2nifti.dicom_series_to_nifti(patient, os.path.join(out_path_labels, patient_name + '.nii.gz'))


def delete_empty_labels(input_nifti_file_path, input_images_file_path, removed_images_path, removed_labels_path):
#'D:/GraduateWorkData/nifti files/labels/*

    for patient in glob.glob(input_nifti_file_path):
        nifti_file = nib.load(patient)

        fdata = nifti_file.get_fdata()

        np_unique = np.unique(fdata)

        if len(np_unique) == 1:
            patient_name = os.path.basename(os.path.normpath(patient))
            image_path = os.path.join(input_images_file_path, patient_name)
            #print(patient, '\n', image_path, '\n\n')
            shutil.move(patient, removed_labels_path)
            shutil.move(image_path, removed_images_path)
