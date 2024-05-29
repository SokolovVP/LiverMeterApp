<template>
  <div id="header_container">
    <div class="header_item" id="header_logo">МРТ СЕГМЕНТАЦИЯ ПЕЧЕНИ</div>
    <input
      type="file"
      v-on:change="upload_image_changed"
      class="header_item, header_button"
      id="upload_image_btn"
    />
    <label id="upload_label" for="upload_image_btn" class="header_item"
      ><img id="upload_img" src="./icons/upload_icon.png" />ЗАГРУЗИТЬ NIFTI ФАЙЛ</label
    >
  </div>
</template>

<script setup>
import { onMounted, reactive, ref } from 'vue'
import image_service from '@/services/image_service'

const file = ref(null)

function upload_image_changed(event) {
  isPageLoaded.value = true
  file.value = event.target.files[0]
  console.log(file.value)
  image_service
    .upload_image(file.value)
    .then((response) => {
      console.log(`${response.data.filename}`)
      return response
    })
    .catch((error) => {
      console.log(error)
      return error
    })
}

const isPageLoaded = ref(false)

onMounted(() => {
  isPageLoaded.value = false
})
</script>

<style scoped>
#header_container {
  height: 60px;
  margin: 0;
  padding: 0;
  border-bottom: 2px solid;
  padding-left: 95px;
  display: flex;
  align-items: center;
}

.header_item {
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}

.header_button {
  margin-top: 15px;
}

#header_logo {
  margin-top: 10px;
  height: 30px;
  width: 250px;
  padding-bottom: 0;
  margin-bottom: 0;
  text-align: center;
  font-size: 19px;
}
#header_logo:hover {
  cursor: pointer;
}

#upload_image_btn {
  margin-left: 100px;
  display: none;
}

#upload_img {
  width: 11px;
  height: 11px;
  padding-right: 5px;
}

#upload_label {
  margin-left: 100px;
  margin-top: 2px;
}

#upload_label:hover {
  transform: scale(1.1);
}

#upload_image_btn:hover {
  cursor: pointer;
}
</style>
