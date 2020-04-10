<template>
  <div class="card">
    <header class="card-header">
      <p class="card-header-title">
        {{ product.name }}
      </p>
    </header>
    <figure class="image is-4by3">
      <img :src="`/media/${product.photo}`" alt="" />
    </figure>
    <div class="card-content">
      <div class="content">
        <p>{{ product.stock }} disponibles</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    product: {
      type: Object,
      default: () => null
    }
  }
}
</script>

<style lang="stylus" scoped></style>
