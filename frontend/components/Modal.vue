<template>
  <b-modal
    :active.sync="active"
    :can-cancel="false"
    has-modal-card
    @keypress.esc="close()"
  >
    <div class="modal-card" style="width: auto">
      <section class="modal-card-body">
        <button
          v-if="cancellable"
          type="button"
          class="modal-close is-large"
          @click="close()"
        >
          <i class="icon icon-times"></i>
        </button>
        <slot></slot>
      </section>
    </div>
  </b-modal>
</template>

<script>
export default {
  props: {
    active: {
      type: Boolean,
      default: false
    },
    cancellable: {
      type: Boolean,
      default: true
    },
    closable: {
      type: Boolean,
      default: true
    }
  },
  methods: {
    close() {
      if (this.cancellable) {
        this.$emit('close')
      }
    }
  }
}
</script>

<style lang="stylus" scoped>
.modal .modal-card .modal-card-body
  padding 50pt 50pt 50pt 50pt

  .icon
    color #000000
    font-size 15pt
    padding 0 15pt 0 15pt

  .modal-close
    position absolute
    top 10pt
    right 20pt

    &::before, &::after
      display none

  .modal-close:hover
    background none
</style>
