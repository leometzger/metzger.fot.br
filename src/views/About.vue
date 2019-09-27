<template>
  <div>
    <subheader image="/images/covers/about.jpeg" title="Sobre Metzger Fotografias" />
    <about
      title="Olá, somos a Metzger Fotografias"
      image="images/logo.png"
      :paragraphs="paragraphs"
    />
    <skills title="Minhas habilidades" :skills="skills" />
    <albums :albums="albums" />
  </div>
</template>

<script>
import About from '../components/About'
import Subheader from '../components/Subheader'
import Skills from '../components/Skills'
import Testimonials from '../components/Testimonials'
import Albums from '../components/Albums'

import {albums} from '../data'

export default {
  components: {About, Albums, Subheader, Skills},
  computed: {
    paragraphs() {
      return [
        `Um olhar clínico e apaixonado pela imagem. O foco na inovação e na qualidade. Uma linguagem visual única e atraente. A Metzger Fotografias reflete uma história de muitos anos e um olhar atualizado sobre as novas tendências da profissão que é, na verdade, pura arte.
Marcelo Metzger, neto do fundador da empresa, embora tenha se formado em Comércio Exterior, encontrou na fotografia sua verdadeira profissão. São mais de 25 anos dedicados à fotografia social, publicitária, empresarial, comercial e institucional. Sua ampla experiência o credencia a realizar trabalhos corporativos de relevância para companhias de todos os tamanhos e segmentos de atuação.`,
        `A fotografia corporativa, especialidade da Metzger Fotografias, reúne visão empresarial, técnica e artística para buscar a melhor imagem. Aquela que representa a essência do cliente. O reflexo é a valorização não apenas dos produtos ou serviços retratados, mas da imagem da empresa transmitida ao mercado.A fotografia corporativa, especialidade da Metzger Fotografias, reúne visão empresarial, técnica e artística para buscar a melhor imagem. Aquela que representa a essência do cliente. O reflexo é a valorização não apenas dos produtos ou serviços retratados, mas da imagem da empresa transmitida ao mercado.`,
      ]
    },
    skills() {
      return [
        {
          name: 'Fotografia',
          percentage: '100',
        },
        {
          name: 'Iluminação',
          percentage: '100',
        },
        {
          name: 'Photoshop',
          percentage: '90',
        },
      ]
    },
    albums() {
      return albums.map(album => {
        return Object.assign(album, {
          subtitle: `${album.images.length} Fotos / ${album.type}`,
        })
      })
    },
  },
}
</script>