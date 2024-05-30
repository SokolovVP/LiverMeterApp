<template>
  <div id="imageViewsContainer">
    <ImageViewer
      v-bind:filename="route.query['filename'] + '.png'"
      v-bind:filepath="route.query['segmented_dir']"
      v-bind:description="descr1"
    />
    <ImageViewer
      v-bind:filename="route.query['filename'] + '.png'"
      v-bind:filepath="route.query['orig_dir']"
      v-bind:description="descr2"
    />
  </div>
</template>

<script setup>
import ImageViewer from '../components/ImageViewer.vue'
import { useRoute } from 'vue-router'
import { onMounted, ref, reactive } from 'vue'

const route = useRoute()

const descr1 = `Кадр МРТ снимка в сагиттальной проекции с наибольшим видимым размером интересуемого органа.\nРазмер органа составляет ${route.query['organ_area']} пикселей.`
const descr2 = `Полученная маска интересуемого органа.`

onMounted(() => {})
</script>

<style>
#imageViewsContainer {
  display: flex;

  justify-content: space-around;
  align-items: center;
  height: 80vh;
}
</style>
