<template>
  <div class="site-section pt-0" data-aos="fade">
    <div class="container">
      <div class="row">
        <div class="col-md-12 mb-5">
          <h2 class="text-black">{{title}}</h2>
        </div>
      </div>
      <div class="row">
        <div class="col-md-12">
          <div v-for="(skill, index) in skills" :key="index">
            <h2 class="h5">{{skill.name}}</h2>
            <div class="progress mb-4">
              <div
                class="progress-bar"
                role="progressbar"
                aria-valuemin="0"
                aria-valuemax="100"
                :aria-valuenow="skill.percentage"
                :style="`width: ${skill.percentage}%;`"
              >{{skill.percentage}}%</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: true,
    },
    skills: {
      type: Array,
      required: true,
    },
  },
}
</script>