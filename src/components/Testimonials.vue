<template>
  <div
    class="py-5 site-block-testimonial"
    :style="`background-image: url(${background});`"
    data-stellar-background-ratio="0.5"
  >
    <div class="container">
      <div class="row block-13 mb-5">
        <div class="col-md-12 text-center" data-aos="fade">
          <div class="nonloop-block-13 owl-carousel"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Testimonial from './Testimonial'

export default {
  components: {Testimonial},
  props: {
    testimonials: {
      type: Array,
      required: false,
    },
    background: {
      type: String,
      required: true,
    },
  },
}
</script>