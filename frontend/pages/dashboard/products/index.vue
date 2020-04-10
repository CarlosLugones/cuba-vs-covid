<template>
  <div>
    <b-button
      type="is-primary"
      @click="$router.replace('/dashboard/products/add')"
    >
      Añadir producto
    </b-button>
    <b-table :data="products">
      <template slot-scope="props">
        <b-table-column field="id" label="Foto">
          <img :src="`/media/${props.row.photo}`" alt="" width="30pt" />
        </b-table-column>
        <b-table-column field="id" label="Nombre">
          {{ props.row.name }}
        </b-table-column>
        <b-table-column field="id" label="Inventario">
          {{ props.row.stock }}
        </b-table-column>
        <b-table-column label="Acciones">
          <b-button
            @click="$router.replace(`/dashboard/products/edit/${props.row.id}`)"
          >
            <b-icon icon="pencil"></b-icon>
          </b-button>
          <b-button @click="remove(props.row.id)">
            <b-icon icon="delete"></b-icon>
          </b-button>
        </b-table-column>
      </template>
    </b-table>
  </div>
</template>

<script>
import gql from 'graphql-tag'
export default {
  layout: 'dashboard',
  data() {
    return {
      products: []
    }
  },
  mounted() {
    this.$apollo
      .query({
        query: gql`
          query viewerProducts {
            viewerProducts {
              id
              name
              stock
              photo
            }
          }
        `
      })
      .then(({ data }) => {
        this.products = data.viewerProducts
      })
  },
  methods: {
    remove(id) {
      this.$apollo
        .mutate({
          mutation: gql`
            mutation removeProduct($id: String!) {
              removeProduct(id: $id) {
                status
              }
            }
          `,
          variables: {
            id
          }
        })
        .then(({ data }) => {
          if (data.removeProduct.status === 'ok') {
            const index = this.products.findIndex((i) => i.id === id)
            this.products.splice(index, 1)
          }
        })
    }
  }
}
</script>

<style scoped></style>
