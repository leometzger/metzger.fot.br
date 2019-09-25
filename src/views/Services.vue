<template>
  <div>
    <subheader title="Meus serviços" image="images/covers/home.jpeg" />
    <specialties :specialties="specialties" />
    <contact-me />
  </div>
</template>

<script>
import Subheader from '../components/Subheader'
import Specialties from '../components/Specialties'
import ContactMe from '../components/ContactMe'

import {specialties} from '../data'

export default {
  components: {ContactMe, Subheader, Specialties},
  computed: {
    specialties() {
      return specialties
    },
  },
}
</script>