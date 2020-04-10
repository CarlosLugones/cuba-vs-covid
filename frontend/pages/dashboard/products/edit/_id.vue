<template>
  <div>
    <nav class="breadcrumb" aria-label="breadcrumbs">
      <ul>
        <li><nuxt-link to="/dashboard/products">Productos</nuxt-link></li>
        <li class="is-active">
          <a href="#" aria-current="page">Editar producto</a>
        </li>
      </ul>
    </nav>
    <form @submit.stop.prevent="update()">
      <!-- stlmodel -->
      <label for="" class="label">Modelo</label>
      <b-field>
        <b-select
          v-model="$v.form.stlmodel.$model"
          placeholder="Selecciona un modelo"
          expanded
        >
          <option
            v-for="stlmodel in stlmodels"
            :key="stlmodel.id"
            :value="stlmodel.id"
          >
            {{ stlmodel.name }}
          </option>
        </b-select>
      </b-field>
      <!-- end stlmodel -->

      <!-- stock -->
      <label for="" class="label">Cantidad en inventario</label>
      <b-field>
        <b-input v-model="$v.form.stock.$model"></b-input>
      </b-field>
      <!-- end stock -->

      <b-field>
        <b-button
          type="is-primary"
          native-type="submit"
          :loading="form.loading"
          :disabled="$v.form.$invalid"
        >
          Guardar cambios
        </b-button>
      </b-field>
    </form>
  </div>
</template>

<script>
import gql from 'graphql-tag'
import { required, integer } from 'vuelidate/lib/validators'
export default {
  layout: 'dashboard',
  data() {
    return {
      stlmodels: [],
      form: {
        stlmodel: null,
        stock: null
      }
    }
  },
  validations: {
    form: {
      stlmodel: {
        required
      },
      stock: {
        required,
        integer
      }
    }
  },
  async mounted() {
    // Load stlmodels
    const { data } = await this.$apollo.query({
      query: gql`
        query stlmodels {
          stlmodels {
            id
            name
          }
        }
      `
    })

    this.stlmodels = data.stlmodels

    this.$apollo
      .query({
        query: gql`
          query product($id: String!) {
            product(id: $id) {
              id
              stock
            }
          }
        `,
        variables: {
          id: this.$route.params.id
        }
      })
      .then(({ data }) => {
        this.form = data.product
      })
  },
  methods: {
    update() {
      this.$v.form.$touch()
      if (!this.$v.form.$invalid) {
        this.$apollo
          .mutate({
            mutation: gql`
              mutation updateProduct($id: String!, $stock: Int!) {
                updateProduct(id: $id, stock: $stock) {
                  status
                }
              }
            `,
            variables: {
              id: this.$route.params.id,
              stock: this.form.stock
            }
          })
          .then(({ data }) => {
            if (data.updateProduct.status === 'ok') {
              this.$buefy.toast.open('Se guardaron los cambios')
              this.$router.replace('/dashboard/products')
            }
          })
      }
    }
  }
}
</script>

<style scoped></style>
