<template>
  <div>
    <subheader />
    <my-specialties />
    <testimonial />
    <my-photography />
  </div>
</template>

<script>
import MySpecialties from '../components/MySpecialties'
import MyPhotography from '../components/MyPhotography'
import Testimonial from '../components/Testimonial'
import Subheader from '../components/Subheader'

export default {
  name: 'home',
  components: {
    MySpecialties,
    MyPhotography,
    Testimonial,
    Subheader,
  },
}
</script>
