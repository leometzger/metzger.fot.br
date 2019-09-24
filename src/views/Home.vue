<template>
  <div>
    <subheader
      :title="subheaderTitle"
      :subtitle="subheaderSubtitle"
      image="images/industrial/0.jpg"
    />
    <profile image="images/profile.jpg" />
    <specialties :specialties="specialties" />
    <testimonials :testimonials="testimonials" :background="background" />
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
          image: 'images/events/4.jpg',
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
          subtitle: '...',
          image: 'images/associativism/8.jpg',
        },
        {
          title: 'Celebridades',
          subtitle: 'Pessoas fotografadas ...',
          image: 'images/celebrities/9.jpg',
        },
        {
          title: 'Eventos',
          subtitle:
            'Diversos eventos são fotografados conforme a sua necessidade',
          image: 'images/events/4.jpg',
        },
        {
          title: 'Indústriais',
          subtitle: 'Fotos industriais são uma das principais ...',
          image: 'images/industrial/4.jpg',
        },
        {
          title: 'Interiores',
          subtitle: 'Fotos de interiores...',
          image: 'images/interiors/4.jpg',
        },
        {
          title: 'Produtos',
          subtitle: 'Produtos sao uma fonte...',
          image: 'images/products/4.jpg',
        },
        {
          title: 'Profissionais',
          subtitle: 'Profissionais fotografados nas industrias...',
          image: 'images/professionals/26.jpg',
        },
      ]
    },
    background() {
      return 'images/events/12.jpg'
    },
    testimonials() {
      return [
        {
          person: 'Leonardo Metzger',
          testimonial: 'Testing',
          image: 'images/events/0.jpg',
        },
      ]
    },
  },
}
</script>
