import re
import os.path

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from WebServices.UploadService import UploadService
from Services.LiverSegmenter import segment_liver
from Services.SaveImageService import save_image


images_root_dir_path = 'D:/универ (D)/4 КУРС/диплом/LiverMeterApp/Images'
uploaded_images_dir_path = os.path.normpath(os.path.join(images_root_dir_path, 'Uploaded'))
saved_images_dir_path = os.path.normpath(os.path.join(images_root_dir_path, 'Processed'))
orig_images_dir_path = os.path.normpath(os.path.join(images_root_dir_path, 'Original'))


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def home():
    if request.method == 'GET':
        return jsonify({'data': 'MRI LIVER SEGMENTATION'})
    elif request.method == 'POST':

        _img = request.files['image_data']
        _filename = UploadService.upload_file(_img, os.path.normpath(
            os.path.join(images_root_dir_path, uploaded_images_dir_path)))

        _filename = re.sub(r'\.nii', '', _filename)
        _filename = re.sub(r'\.gz', '', _filename)

        _filepath = os.path.join(uploaded_images_dir_path, _filename)

        orig_image, segmented_img = segment_liver(filepath=_filepath+'.nii.gz')

        segmented_image_path = save_image(saved_images_dir_path, _filename, segmented_img)
        original_image_path = save_image(orig_images_dir_path, _filename, segmented_img)

        return jsonify({'filename': _filename})


app.run(debug=True)
