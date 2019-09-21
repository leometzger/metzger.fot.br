<template>
  <div class="site-section border-bottom">
    <div class="container">
      <div class="row text-center justify-content-center mb-5">
        <div class="col-md-7" data-aos="fade-up">
          <h2>Minhas fotos</h2>
        </div>
      </div>

      <div class="row">
        <phothography-type
          :key="index"
          v-for="(type, index) in photographies"
          :title="type.title"
          :subtitle="type.subtitle"
          :image="type.image"
          :route="type.route"
        />
      </div>
    </div>
  </div>
</template>

<script>
import PhothographyType from './PhotographyType'

export default {
  components: {PhothographyType},
  props: {
    photographies: {
      type: Array,
      required: true,
    },
  },
}
</script>