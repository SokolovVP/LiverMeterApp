import axios from 'axios'
import http from './http-common'

class image_service {
  upload_image(image_data) {
    if (image_data) {
      const form_data = new FormData()
      form_data.append('image_data', image_data)

      return http.post('/', form_data, { headers: { 'Content-Type': 'multipart/form-data' } })
    } else {
      alert('there is no data')
    }
  }
}

export default new image_service()
