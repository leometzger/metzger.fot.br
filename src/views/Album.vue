<template>
  <div>
    <subheader :image="album.image" :title="album.title" :subtitle="album.subtitle" />
    <album :images="album.images" />
    <contact-me />
  </div>
</template>

<script>
import Album from '../components/Album'
import Subheader from '../components/Subheader'
import ContactMe from '../components/ContactMe'

import {find} from 'lodash'
import {albums} from '../data'

export default {
  components: {Album, ContactMe, Subheader},
  computed: {
    album() {
      const albumId = this.$route.params.id
      const album = find(albums, {id: albumId}) || {title: '', images: []}

      return Object.assign(album, {
        subtitle: `${album.images.length} Fotos / ${album.type}`,
      })
    },
  },
}
</script>