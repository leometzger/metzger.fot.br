<template>
  <div class="block-testimony">
    <img :src="image" alt="Image" class="img-fluid" />
    <p>&ldquo;{{testimonial}}&rdquo;</p>
    <p class="small">&mdash; {{person}}</p>
  </div>
</template>

<script>
export default {
  props: {
    person: {
      type: String,
      required: true,
    },
    testimonial: {
      type: String,
      required: true,
    },
    image: {
      type: String,
      required: true,
    },
  },
}
</script>