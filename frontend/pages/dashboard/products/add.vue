<template>
  <div>
    <nav class="breadcrumb" aria-label="breadcrumbs">
      <ul>
        <li><nuxt-link to="/dashboard/products">Productos</nuxt-link></li>
        <li class="is-active">
          <a href="#" aria-current="page">Añadir producto</a>
        </li>
      </ul>
    </nav>
    <form @submit.stop.prevent="add()">
      <!-- name -->
      <label for="" class="label">Nombre del producto</label>
      <b-field>
        <b-input v-model="$v.form.name.$model"></b-input>
      </b-field>
      <!-- end name -->

      <!-- phone -->
      <label for="" class="label">Cantidad en inventario</label>
      <b-field>
        <b-input v-model="$v.form.stock.$model"></b-input>
      </b-field>
      <!-- end phone -->

      <PhotoUploader
        size="120pt"
        class="margin-bottom-10"
        @photo:uploaded="($url) => (form.photo = $url)"
      />

      <b-field>
        <b-button
          type="is-primary"
          native-type="submit"
          :loading="form.loading"
          :disabled="$v.form.$invalid"
        >
          Añadir producto
        </b-button>
      </b-field>
    </form>
  </div>
</template>

<script>
import gql from 'graphql-tag'
import { required, integer } from 'vuelidate/lib/validators'
import PhotoUploader from '~/components/PhotoUploader'
export default {
  layout: 'dashboard',
  components: { PhotoUploader },
  data() {
    return {
      form: {
        name: null,
        stock: null,
        photo: null
      }
    }
  },
  validations: {
    form: {
      name: {
        required
      },
      stock: {
        required,
        integer
      }
    }
  },
  methods: {
    add() {
      this.$v.form.$touch()
      if (!this.$v.form.$invalid) {
        this.$apollo
          .mutate({
            mutation: gql`
              mutation createProduct(
                $name: String!
                $stock: Int!
                $photo: String
              ) {
                createProduct(name: $name, stock: $stock, photo: $photo) {
                  status
                }
              }
            `,
            variables: {
              name: this.form.name,
              stock: this.form.stock,
              photo: this.form.photo
            }
          })
          .then(({ data }) => {
            if (data.createProduct.status === 'ok') {
              this.$buefy.toast.open('Se añadió el producto')
              this.$router.replace('/dashboard/products')
            }
          })
      }
    }
  }
}
</script>

<style scoped></style>
