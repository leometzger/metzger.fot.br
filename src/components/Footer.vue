<template>
  <footer class="site-footer">
    <div class="container">
      <div class="row">
        <div class="col-lg-4">
          <div class="mb-5">
            <h3 class="footer-heading mb-4">Sobre Metzger Fotografias</h3>
            <p>
              A fotografia corporativa, especialidade da Metzger Fotografias,
              reúne visão empresarial, técnica e artística para buscar a melhor imagem.
              Aquela que representa a essência do cliente. O reflexo é a valorização não apenas
              dos produtos ou serviços retratados, mas da imagem da empresa transmitida ao mercado.
            </p>
          </div>
        </div>
        <div class="col-lg-4 mb-5 mb-lg-0">
          <div class="row mb-5">
            <div class="col-md-12">
              <h3 class="footer-heading mb-4">Links</h3>
            </div>
            <div class="col-md-6 col-lg-6">
              <ul class="list-unstyled">
                <li>
                  <a href="#">Home</a>
                </li>
                <li>
                  <a href="#">Albuns</a>
                </li>
                <li>
                  <a href="#">Serviços</a>
                </li>
              </ul>
            </div>
            <div class="col-md-6 col-lg-6">
              <ul class="list-unstyled">
                <li>
                  <a href="#">Sobre</a>
                </li>
                <li>
                  <a href="#">Contato</a>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <div class="col-lg-4 mb-5 mb-lg-0">
          <h3 class="footer-heading mb-4">Me Siga</h3>
          <follow-me />
        </div>
      </div>
      <copyright />
    </div>
  </footer>
</template>

<script>
import Copyright from './Copyright'
import FollowMe from './FollowMe'

export default {
  components: {Copyright, FollowMe},
}
</script>