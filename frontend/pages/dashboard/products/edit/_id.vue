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
        :photo="form.photo"
        @photo:uploaded="($url) => (form.photo = $url)"
      />

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
  mounted() {
    this.$apollo
      .query({
        query: gql`
          query product($id: String!) {
            product(id: $id) {
              name
              stock
              photo
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
              mutation updateProduct(
                $id: String!
                $name: String!
                $stock: Int!
                $photo: String
              ) {
                updateProduct(
                  id: $id
                  name: $name
                  stock: $stock
                  photo: $photo
                ) {
                  status
                }
              }
            `,
            variables: {
              id: this.$route.params.id,
              name: this.form.name,
              stock: this.form.stock,
              photo: this.form.photo
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
