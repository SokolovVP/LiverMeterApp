<template>
  <div id="header_container">
    <div class="header_item" id="header_logo">МРТ СЕГМЕНТАЦИЯ ПЕЧЕНИ</div>
    <button
      v-on:click="upload_image_btn_click"
      class="header_item, header_button"
      id="upload_image_btn"
    >
      + Загрузить файл
    </button>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const msg = ref('HEADER HELLO WORLD')

function upload_image_btn_click() {
  alert('clicked')
}
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
}

#upload_image_btn:hover {
  cursor: pointer;
}
</style>
