<template>
  <div class="site-section border-bottom">
    <div class="container">
      <div class="row text-center justify-content-center mb-5">
        <div class="col-md-7" data-aos="fade-up">
          <h2>Minhas fotos</h2>
        </div>
      </div>

      <div class="row">
        <album-cover
          v-for="(album, index) in albums"
          :key="index"
          :title="album.title"
          :subtitle="album.subtitle"
          :image="album.image"
          :route="album.route"
        />
      </div>
    </div>
  </div>
</template>

<script>
import AlbumCover from './AlbumCover'

export default {
  components: {AlbumCover},
  props: {
    albums: {
      type: Array,
      required: true,
    },
  },
}
</script>