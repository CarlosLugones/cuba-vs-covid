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
        <b-table-column field="id" label="Nombre">
          {{ props.row.name }}
        </b-table-column>
        <b-table-column field="id" label="Inventario">
          {{ props.row.stock }}
        </b-table-column>
        <b-table-column label="Acciones">
          <b-button>
            <b-icon icon="pencil"></b-icon>
          </b-button>
          <b-button>
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
            }
          }
        `
      })
      .then(({ data }) => {
        this.products = data.viewerProducts
      })
  }
}
</script>

<style scoped></style>
