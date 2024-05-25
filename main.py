import cv2
import glob
import os
from Services.VideoFramesDivider import VideoFramesDivider
from Services import DicomGroupsBuilder
from Services import NiftiBuilderFromDicom



#DicomGroupsBuilder.create_groups('D:/GraduateWorkData/dicom_file2/images', 'D:/GraduateWorkData/dicom_groups2/images')
#DicomGroupsBuilder.create_groups('D:/GraduateWorkData/dicom_file2/labels', 'D:/GraduateWorkData/dicom_groups2/labels')


# NiftiBuilderFromDicom.create_nifti_images_from_dicom_series(in_path_images='D:/GraduateWorkData/dicom_groups2/images/*',
#                                                             out_path_images='D:/GraduateWorkData/nifti_files2/images')
# NiftiBuilderFromDicom.create_nifti_labels_from_dicom_series(in_path_labels='D:/GraduateWorkData/dicom_groups2/labels/*',
#                                                             out_path_labels='D:/GraduateWorkData/nifti_files2/labels')
# NiftiBuilderFromDicom.delete_empty_labels('D:/GraduateWorkData/nifti_files2/labels/*',
#                                           'D:/GraduateWorkData/nifti_files2/images',
#                                           'D:/GraduateWorkData/nifti_files2/removed_images',
#                                           'D:/GraduateWorkData/nifti_files2/removed_labels')




















