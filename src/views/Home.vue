<template>
  <div>
    <subheader
      :title="subheaderTitle"
      :subtitle="subheaderSubtitle"
      image="images/covers/home.jpeg"
    />
    <profile image="images/profile.jpg" />
    <specialties :specialties="specialties" />
    <testimonials :testimonials="testimonials" :background="background" />
    <albums :albums="albums" />
  </div>
</template>

<script>
import Albums from '../components/Albums'
import Specialties from '../components/Specialties'
import Profile from '../components/Profile'
import Testimonials from '../components/Testimonials'
import Subheader from '../components/Subheader'

import {albums, specialties} from '../data'

export default {
  name: 'home',
  components: {
    Specialties,
    Albums,
    Testimonials,
    Subheader,
    Profile,
  },
  computed: {
    subheaderTitle() {
      return 'Metzger Fotografias'
    },
    subheaderSubtitle() {
      return 'Fotografia corporativa para agregar valor à marca'
    },
    albums() {
      return albums
    },
    specialties() {
      return specialties
    },
    background() {
      return 'images/covers/testimonials.jpeg'
    },
    testimonials() {
      return [
        {
          person: 'Leonardo Metzger',
          testimonial: 'Testing',
          image: 'images/covers/testimonials.jpeg',
        },
      ]
    },
  },
}
</script>
