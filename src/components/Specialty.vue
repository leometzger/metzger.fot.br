<template>
  <div class="site-block-half d-lg-flex">
    <div class="image" :style="`background-image: url(${image});`"></div>
    <div class="text">
      <h3>{{title}}</h3>
      <p>{{description}}</p>
    </div>
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
    description: {
      type: String,
      required: true,
    },
  },
}
</script>