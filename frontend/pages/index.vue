<template>
  <div>
    <img src="/img/banner.jpg" class="banner" alt="" />
    <div class="hero is-dark is-bold">
      <div class="hero-body">
        <div class="container">
          <div class="columns is-multiline is-centered">
            <div
              v-for="stlmodel in stlmodels"
              :key="stlmodel.id"
              class="column is-2 is-12-mobile"
            >
              <STLModelCard :stlmodel="stlmodel" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import gql from 'graphql-tag'
import STLModelCard from '~/components/STLModelCard'
export default {
  components: { STLModelCard },
  data() {
    return {
      stlmodels: []
    }
  },
  mounted() {
    this.$apollo
      .query({
        query: gql`
          query existingStlmodels {
            existingStlmodels {
              id
              name
              photo
              stock
            }
          }
        `
      })
      .then(({ data }) => {
        this.stlmodels = data.existingStlmodels
      })
  }
}
</script>

<style lang="stylus" scoped>
.banner {
  width 100%
  height auto
}
</style>
