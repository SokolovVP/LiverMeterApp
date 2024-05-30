<template>
  <div id="imageViewerContainer">
    <div id="imageContainer">
      <img id="imageViewerImage" :src="`${filepath}/${filename}`" />
      <div id="image_description">{{ props.description }}</div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const props = defineProps(['filename', 'filepath', 'description'])

const filepath = ref('')
const filename = ref('')
const full_image_path = ref('')

onMounted(() => {
  filepath.value = props.filepath
  filename.value = props.filename

  full_image_path.value = filepath.value + '\\' + filename.value + ''
  console.log(full_image_path.value)
})
</script>

<style>
#imageViewerContainer {
  width: 450px;
  height: 450px;
}

#imageViewerImage {
  width: 450px;
  height: 450px;
}
</style>
