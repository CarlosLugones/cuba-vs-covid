<template>
  <div>
    <Navbar />

    <section class="main-content">
      <nuxt />
    </section>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'
import Navbar from '~/components/Navbar'
export default {
  components: { Navbar },
  mounted() {
    this.loadAuth()
  },
  methods: {
    ...mapMutations({
      loadAuth: 'auth/loadFromCookie'
    })
  }
}
</script>
