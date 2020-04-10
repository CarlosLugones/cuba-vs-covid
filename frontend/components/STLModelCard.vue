<template>
  <div class="card" @click="$router.replace(`/stlmodel/${stlmodel.id}`)">
    <header class="card-header">
      <p class="card-header-title">
        {{ stlmodel.name }}
      </p>
    </header>
    <figure class="image is-4by3">
      <img :src="`/media/${stlmodel.photo}`" alt="" />
    </figure>
    <div class="card-content">
      <div class="content">
        <p>{{ stlmodel.stock }} disponibles</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    stlmodel: {
      type: Object,
      default: () => null
    }
  }
}
</script>

<style lang="stylus" scoped>
.card:hover
  cursor pointer
</style>
