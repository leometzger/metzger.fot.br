<template>
  <div id="site-wrap">
    <site-mobile-menu />
    <app-header :specialties="specialties" />
    <router-view />
    <app-footer />
  </div>
</template>

<script>
import SiteMobileMenu from './components/SiteMobileMenu'
import AppHeader from './components/Header'
import AppFooter from './components/Footer'

export default {
  components: {AppFooter, AppHeader, SiteMobileMenu},
  computed: {
    specialties() {
      return [
        {
          id: 'events',
          description: 'Eventos',
          route: {
            name: 'album',
            params: {
              id: 'events',
            },
          },
        },
      ]
    },
  },
}
</script>
