import glob
import os
import shutil

#in_path = 'D:/GraduateWorkData/dicom_file/images'
#out_path = 'D:/GraduateWorkData/dicom_groups/images'


def create_groups(in_path, out_path):
    for patient in glob.glob(in_path+'/*/'):
        patient_name = os.path.basename(os.path.normpath(patient))
        number_folders = int(len(glob.glob(patient+'/*'))/30)

        for i in range(number_folders):
            output_path_name = os.path.join(out_path, patient_name+'_'+str(i))
            os.mkdir(output_path_name)
            for j, file in enumerate(glob.glob(patient+'/*')):
                if j == 30:
                    break
                #shutil.move(file, output_path_name)
                shutil.copy(file, output_path_name)
