<template>
  <div>
    <subheader
      :title="subheaderTitle"
      :subtitle="subheaderSubtitle"
      image="images/industrial/3.jpg"
    />
    <profile image="images/profile.jpg" />
    <specialties :specialties="specialties" />
    <testimonials :testimonials="testimonials" />
    <photographies :photographies="photographies" />
  </div>
</template>

<script>
import Specialties from '../components/Specialties'
import Photographies from '../components/Phothographies'
import Profile from '../components/Profile'
import Testimonials from '../components/Testimonials'
import Subheader from '../components/Subheader'

export default {
  name: 'home',
  components: {
    Specialties,
    Photographies,
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
    photographies() {
      return [
        {
          title: 'Associativismo',
          subtitle: '5 Fotos / Pessoas',
          image: 'images/associativism/0.jpg',
          route: {
            name: '#',
            params: {},
          },
        },
        {
          title: 'Celebridades',
          subtitle: '10 Fotos / Pessoas',
          image: 'images/celebrities/1.jpg',
          route: {
            name: '#',
            params: {},
          },
        },
        {
          title: 'Eventos',
          subtitle: '10 Fotos / Pessoas',
          image: 'images/events/1.jpg',
          route: {
            name: '#',
            params: {},
          },
        },
        {
          title: 'Industriais',
          subtitle: '10 Fotos / Indústria',
          image: 'images/industrial/0.jpg',
          route: {
            name: '#',
            params: {},
          },
        },
        {
          title: 'Interiores',
          subtitle: '10 Fotos / Lugares',
          image: 'images/interiors/0.jpg',
          route: {
            name: '#',
            params: {},
          },
        },
        {
          title: 'Produtos',
          subtitle: '10 Fotos / Indústria',
          image: 'images/products/0.jpg',
          route: {
            name: '#',
            params: {},
          },
        },
        {
          title: 'Profissionais',
          subtitle: '10 Fotos / Pessoas',
          image: 'images/professionals/0.jpg',
          route: {
            name: '#',
            params: {},
          },
        },
      ]
    },
    specialties() {
      return [
        {
          title: 'Associativismo',
          subtitle: '',
          image: 'images/associativism/1.jpg',
        },
        {
          title: 'Eventos',
          subtitle: '',
          image: 'images/events/1.jpg',
        },
      ]
    },
    testimonials() {
      return [
        {
          person: 'Leonardo Metzger',
          testimonial: 'Testing',
          image: 'images/events/1.jpg',
        },
      ]
    },
  },
}
</script>
