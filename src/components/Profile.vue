<template>
  <div class="site-block-profile-pic" data-aos="fade" data-aos-delay="200">
    <router-link to="about">
      <img :src="image" alt="Image" />
    </router-link>
  </div>
</template>


<script>
export default {
  name: 'profile',
  props: {
    image: {
      type: String,
      required: true,
    },
  },
}
</script>
