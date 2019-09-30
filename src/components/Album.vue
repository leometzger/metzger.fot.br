<template>
  <div class="site-section" data-aos="fade">
    <div class="container">
      <div class="row no-gutters" id="lightgallery">
        <div
          v-for="(image, index) in images"
          :key="index"
          class="col-sm-6 col-md-4 col-lg-3 col-xl-2 item"
          data-aos="fade"
          :data-src="image"
        >
          <a href="#">
            <img :src="image" class="img-fluid small-image" />
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    images: {
      type: Array,
      required: false,
    },
  },
  mounted() {
    $('#lightgallery').lightGallery({
      zoom: false,
      download: false,
      share: false,
      pause: 2000,
    })
  },
  methods: {
    makeHtmlTitle(title) {
      return `<h4>${title}</h4>`
    },
  },
}
</script>

<style scoped>
img {
  width: 100%;
  height: 160px;
  object-fit: cover;
}
</style>