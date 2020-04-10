<template>
  <div>
    <img src="/img/banner.jpg" class="banner" alt="" />
    <div class="hero is-dark is-bold">
      <div class="hero-body">
        <div class="container">
          <div class="columns is-multiline is-centered">
            <div
              v-for="product in products"
              :key="product.id"
              class="column is-2 is-12-mobile"
            >
              <ProductCard :product="product" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import gql from 'graphql-tag'
import ProductCard from '~/components/ProductCard'
export default {
  components: { ProductCard },
  data() {
    return {
      products: []
    }
  },
  mounted() {
    this.$apollo
      .query({
        query: gql`
          query existingProducts {
            existingProducts {
              id
              name
              stock
              photo
              owner {
                firstName
                lastName
              }
            }
          }
        `
      })
      .then(({ data }) => {
        this.products = data.existingProducts
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
