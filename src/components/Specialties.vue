<template>
  <div class="site-section" data-aos="fade">
    <div class="container">
      <div class="row mb-5">
        <div class="col-12">
          <h2 class="site-section-heading text-center">Minhas especialidades</h2>
        </div>
      </div>
      <div class="row">
        <div class="col-md-6" :key="index" v-for="(pair, index) in specialtiesPairs">
          <specialty :title="pair[0].title" :subtitle="pair[0].subtitle" :image="pair[0].image" />
          <specialty
            v-if="pair[1]"
            :title="pair[1].title"
            :description="pair[1].subtitle"
            :image="pair[1].image"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Specialty from './Specialty'
import {chunk} from 'lodash'

export default {
  components: {
    Specialty,
  },
  props: {
    specialties: {
      type: Array,
      required: true,
    },
  },
  computed: {
    specialtiesPairs() {
      return chunk(this.specialties, 2)
    },
  },
}
</script>