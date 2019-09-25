<template>
  <div>
    <subheader />
    <album />
  </div>
</template>

<script>
import Subheader from '../components/Subheader'
import Album from '../components/Album'

export default {
  props: {
    Subheader,
    Album
  },
}
</script>