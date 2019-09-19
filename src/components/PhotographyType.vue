<template>
  <div class="col-md-6 col-lg-4" data-aos="fade-up" data-aos-delay="500">
    <router-link class="image-gradient" to="single">
      <figure>
        <img :src="image" alt class="img-fluid" />
      </figure>
      <div class="text">
        <h3>{{title}</h3>
        <span>{{subtitle}}</span>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  props: {
    image: {
      type: String,
      required: true,
    },
    title: {
      type: String,
      required: true,
    },
    subtitle: {
      type: String,
      required: true,
    },
  },
}
</script>