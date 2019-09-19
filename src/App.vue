<template>
  <div id="site-wrap">
    <site-mobile-menu />
    <app-header />
    <router-view />
    <footer />
  </div>
</template>

<script>
import SiteMobileMenu from './components/SiteMobileMenu'
import AppHeader from './components/Header'
import AppFooter from './components/Footer'

export default {
  components: {AppFooter, AppHeader, SiteMobileMenu},
}
</script>
