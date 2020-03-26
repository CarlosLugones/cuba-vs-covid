<template>
  <div>
    <Navbar />

    <section class="main-content">
      <div class="container">
        <div class="columns">
          <div class="column is-3">
            <b-menu>
              <b-menu-list>
                <b-menu-item
                  icon="factory"
                  label="Talleres"
                  @click="navigateTo('/dashboard/workshops')"
                ></b-menu-item>
                <b-menu-item icon="printer-3d" label="Productos"></b-menu-item>
              </b-menu-list>
            </b-menu>
          </div>
          <div class="column is-9">
            <nuxt />
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'
import Navbar from '~/components/Navbar'
export default {
  auth: true,
  components: { Navbar },
  mounted() {
    this.loadAuth()
  },
  methods: {
    navigateTo(path) {
      if (this.$router.path !== path) {
        this.$router.replace('/dashboard/workshops')
      }
    },
    ...mapMutations({
      loadAuth: 'auth/loadFromCookie'
    })
  }
}
</script>
