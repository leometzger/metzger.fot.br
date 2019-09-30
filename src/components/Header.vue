<template>
  <header class="site-navbar py-3" role="banner">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-6 col-xl-2">
          <h1 class="mb-0">
            <router-link to="/" class="text-black h2 mb-0">
              <img src="/images/logo_deitada.png" style="width: 120px;" />
            </router-link>
          </h1>
        </div>
        <div class="col-10 col-md-8 d-none d-xl-block">
          <nav
            class="site-navigation position-relative text-right text-lg-center"
            role="navigation"
          >
            <ul class="site-menu js-clone-nav mx-auto d-none d-lg-block">
              <li>
                <router-link to="/">Home</router-link>
              </li>
              <li class="has-children">
                <a>Albuns</a>
                <ul class="dropdown">
                  <li v-for="(album, index) in albums" :key="index">
                    <router-link :to="album.route">{{album.title}}</router-link>
                  </li>
                </ul>
              </li>
              <li>
                <router-link to="/services">Serviços</router-link>
              </li>
              <li>
                <router-link to="/about">Sobre</router-link>
              </li>
              <li>
                <router-link to="/contact">Contato</router-link>
              </li>
            </ul>
          </nav>
        </div>

        <div class="col-6 col-xl-2 text-right">
          <div class="d-none d-xl-inline-block">
            <ul
              class="site-menu js-clone-nav ml-auto list-unstyled d-flex text-right mb-0"
              data-class="social"
            >
              <li>
                <a
                  href="https://www.facebook.com/metzgerfotografias"
                  target="_blank"
                  class="pl-0 pr-3"
                >
                  <span class="icon-facebook"></span>
                </a>
              </li>
              <li>
                <a
                  href="https://www.instagram.com/metzgerfotografias"
                  target="_blank"
                  class="pl-3 pr-3"
                >
                  <span class="icon-instagram"></span>
                </a>
              </li>
            </ul>
          </div>
          <div
            class="d-inline-block d-xl-none ml-md-0 mr-auto py-3"
            style="position: relative; top: 3px;"
          >
            <a href="#" class="site-menu-toggle js-menu-toggle text-black">
              <span class="icon-menu h3"></span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  props: {
    albums: {
      type: Array,
      required: true,
    },
  },
}
</script>