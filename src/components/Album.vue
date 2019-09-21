<template>
  <div>
    <div class="site-section" data-aos="fade">
      <div class="container">
        <div class="row no-gutters" id="lightgallery">
          <div
            v-for="(image, index) in images"
            :key="index"
            class="col-sm-6 col-md-4 col-lg-3 col-xl-2 item"
            data-aos="fade"
            :data-src="image.big"
            :data-sub-html="makeHtmlTitle(image.title)"
          >
            <a href="#">
              <img :src="image.small" alt="IMage" class="img-fluid" />
            </a>
          </div>
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
  methods: {
    makeHtmlTitle(title) {
      return `<h4>${title}</h4>`
    },
  },
}
</script>