<template>
  <div>
    <subheader title="Entre em contato" image="images/covers/home.jpeg" />
    <contact />
  </div>
</template>

<script>
import Subheader from '../components/Subheader'
import Contact from '../components/Contact'

export default {
  components: {Contact, Subheader},
}
</script>