<template>
  <div>
    <subheader />
    <specialty-images />
  </div>
</template>

<script>
import Subheader from '../components/Subheader'
import SpecialtyImages from '../components/Single'

export default {
  props: {
    Subheader,
    SpecialtyImages,
  },
}
</script>