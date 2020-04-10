<template>
  <div class="card">
    <header class="card-header">
      <p class="card-header-title">
        {{ product.owner.firstName }}
        {{ product.owner.lastName }}
      </p>
    </header>
    <figure class="image">
      <img
        v-if="product.owner.avatar"
        :src="`/media/${product.owner.avatar}`"
        alt=""
      />
      <img v-else src="/img/avatar.jpg" alt="" />
    </figure>
    <div class="card-content">
      <div class="content">
        <small>
          <p>{{ product.stock }} disponibles</p>
          <p v-if="product.owner.phone">
            <b>Teléfono:</b>
            <br />
            {{ product.owner.phone }}
          </p>
          <p v-if="product.owner.address">
            <b>Dirección:</b>
            <br />
            {{ product.owner.address.line1 }},
            {{ product.owner.address.line2 }}
          </p>
          <p v-if="product.owner.fromTime && product.owner.toTime">
            <b>Horario:</b>
            <br />
            {{ product.owner.fromTime }} a {{ product.owner.toTime }}
          </p>
        </small>
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
