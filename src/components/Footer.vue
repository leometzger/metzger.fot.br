<template>
  <footer class="site-footer">
    <div class="container">
      <div class="row">
        <div class="col-lg-4"></div>
        <div class="col-lg-4 mb-5 mb-lg-0">
          <div class="row mb-5">
            <div class="col-md-12">
              <h3 class="footer-heading mb-4">Navegação</h3>
            </div>
            <div class="col-md-6 col-lg-6">
              <ul class="list-unstyled">
                <li>
                  <router-link href="#">Home</router-link>
                </li>
                <li>
                  <router-link to="photography">Fotografia</router-link>
                </li>
                <li>
                  <router-link to="galery">Galeria</router-link>
                </li>
                <li>
                  <router-link to="services">Services</router-link>
                </li>
              </ul>
            </div>
            <div class="col-md-6 col-lg-6">
              <ul class="list-unstyled">
                <li>
                  <a href="#">Sobre mim</a>
                </li>
                <li>
                  <a href="#">Entre em contato</a>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div class="col-lg-4 mb-5 mb-lg-0">
          <h3 class="footer-heading mb-4">Me siga</h3>
          <follow-me />
        </div>
      </div>
      <div class="row pt-5 mt-5 text-center">
        <copyright />
      </div>
    </div>
  </footer>
</template>

<script>
import Copyright from './Copyright'

export default {
  components: {Copyright},
}
</script>