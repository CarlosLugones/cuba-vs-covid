<template>
  <div class="card">
    <header class="card-header">
      <p class="card-header-title">
        {{ workshop.name }}
      </p>
    </header>
    <div class="card-content">
      <div class="content">
        <p><b>Abre:</b> {{ workshop.fromTime }}</p>
        <p><b>Cierra:</b> {{ workshop.toTime }}</p>
      </div>
    </div>
    <footer class="card-footer">
      <a href="#" class="card-footer-item">Modificar</a>
      <a href="#" class="card-footer-item">Eliminar</a>
    </footer>
  </div>
</template>

<script>
export default {
  props: {
    workshop: {
      type: Object,
      default: () => null
    },
    admin: {
      type: Boolean,
      default: false
    }
  }
}
</script>

<style scoped></style>
