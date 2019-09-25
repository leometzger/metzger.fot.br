<template>
  <div id="site-wrap">
    <site-mobile-menu />
    <app-header :albums="albums" />
    <router-view />
    <app-footer />
  </div>
</template>

<script>
import SiteMobileMenu from './components/SiteMobileMenu'
import AppHeader from './components/Header'
import AppFooter from './components/Footer'

import {albums} from './data'

export default {
  components: {AppFooter, AppHeader, SiteMobileMenu},
  computed: {
    albums() {
      return albums
    },
  },
}
</script>
