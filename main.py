import re
import os.path

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS, cross_origin
from WebServices.UploadService import UploadService
from Services.LiverSegmenter import segment_liver
from Services.SaveImageService import save_image


images_root_dir_path = 'D:/универ (D)/4 КУРС/диплом/LiverMeterApp/Images'

uploaded_path = 'Uploaded'
saved_path = 'Processed'
orig_path = 'Original'

uploaded_images_dir_path = os.path.normpath(os.path.join(images_root_dir_path, uploaded_path))
saved_images_dir_path = os.path.normpath(os.path.join(images_root_dir_path, saved_path))
orig_images_dir_path = os.path.normpath(os.path.join(images_root_dir_path, orig_path))


app = Flask(__name__, static_url_path='', static_folder='Images')
CORS(app)


@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def home():
    if request.method == 'GET':
        return jsonify({'data': f'MRI LIVER SEGMENTATION: {request.host_url}'})
    elif request.method == 'POST':

        _img = request.files['image_data']
        _filename = UploadService.upload_file(_img, os.path.normpath(
            os.path.join(images_root_dir_path, uploaded_images_dir_path)))

        _filename = re.sub(r'\.nii', '', _filename)
        _filename = re.sub(r'\.gz', '', _filename)

        _filepath = os.path.join(uploaded_images_dir_path, _filename)

        orig_image, segmented_img, area = segment_liver(filepath=_filepath+'.nii.gz')

        segmented_image_path = save_image(saved_images_dir_path, _filename, segmented_img)
        original_image_path = save_image(orig_images_dir_path, _filename, orig_image)

        print('LIVER AREA = ', area)

        return jsonify({'filename': _filename}, {'segmented_dir': request.host_url + '/' + saved_path},
                       {'orig_dir': request.host_url + '/' + orig_path}, {'area': str(area)})


@app.route('/<path:path>')
def send_image(path):
    return send_from_directory(app.static_folder, path)


app.run(debug=True)
