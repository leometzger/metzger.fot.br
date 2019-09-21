<template>
  <div
    class="site-blocks-cover overlay inner-page-cover"
    :style="`background-image: url(${image});`"
    data-stellar-background-ratio="0.5"
  >
    <div class="container">
      <div class="row align-items-center justify-content-center">
        <div class="col-md-7 text-center" data-aos="fade-up">
          <h1>{{title}}</h1>
          <p v-if="subtitle" class="caption subtitle">{{subtitle}}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'subheader',
  props: {
    title: {
      type: String,
      required: true,
    },
    subtitle: {
      type: String,
      required: false,
      default: '',
    },
    image: {
      type: String,
      required: false,
      default: '',
    },
  },
}
</script>

<style lang="css" scoped>
.subtitle {
  font-size: 12px !important;
}
</style>