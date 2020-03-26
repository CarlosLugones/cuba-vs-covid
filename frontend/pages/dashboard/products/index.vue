<template>
  <div>
    <b-button
      type="is-primary"
      @click="$router.replace('/dashboard/products/add')"
    >
      Añadir producto
    </b-button>
  </div>
</template>

<script>
export default {
  layout: 'dashboard'
}
</script>

<style scoped></style>
