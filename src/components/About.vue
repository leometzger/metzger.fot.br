<template>
  <div class="site-section" data-aos="fade">
    <div class="container">
      <div class="row mb-5">
        <div class="col-md-4 mb-5">
          <img :src="image" alt="Images" class="img-fluid" />
        </div>
        <div class="col-md-6 ml-auto">
          <h3 class="text-black mb-3">{{title}}</h3>
          <p v-for="(paragraph, index) in paragraphs" :key="index">{{paragraph}}</p>
          <p class="mt-5 mb-3">Me siga</p>
          <p>
            <a href="#" class="p-2">
              <span class="icon-instagram"></span>
            </a>
            <a href="#" class="p-2">
              <span class="icon-facebook"></span>
            </a>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    image: {
      type: String,
      required: true,
    },
    title: {
      type: String,
      required: true,
    },
    paragraphs: {
      type: Array,
      required: true,
    },
  },
}
</script>