<template>
  <div class="site-section" data-aos="fade">
    <div class="container">
      <div class="row mb-5">
        <div class="col-12">
          <h2 class="site-section-heading text-center">Minhas especialidades</h2>
        </div>
      </div>

      <div class="row">
        <div :class="className" :key="index" v-for="(pair, index) in specialtiesPairs">
          <div class="site-block-half d-lg-flex">
            <div class="image specialty" :style="`background-image: url(${pair[0].image});`"></div>
            <div class="text">
              <h3>{{pair[0].title}}</h3>
              <p>{{pair[0].subtitle}}</p>
            </div>
          </div>
          <div class="site-block-half d-lg-flex specialty" v-if="pair[1]">
            <div class="image" :style="`background-image: url(${pair[1].image});`"></div>
            <div class="text">
              <h3>{{pair[1].title}}</h3>
              <p>{{pair[1].subtitle}}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {chunk} from 'lodash'

export default {
  props: {
    specialties: {
      type: Array,
      required: true,
    },
    pairs: {
      type: Boolean,
      required: false,
      default: false,
    },
  },
  computed: {
    className() {
      return this.pairs ? 'col-md-6' : 'col-md-12'
    },
    specialtiesPairs() {
      return chunk(this.specialties, 2)
    },
  },
}
</script>

<style scoped>
.specialty {
  min-height: 250px;
}
</style>