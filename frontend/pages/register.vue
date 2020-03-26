<template>
  <div class="container">
    <div class="columns is-centered">
      <div class="column is-6 is-12-mobile">
        <h1 class="title">Regístrate</h1>
        <h2 class="subtitle">Crea tu cuenta para luchar contra la COVID-19</h2>
        <form @submit.stop.prevent="register()">
          <!-- first name -->
          <label for="" class="label">Nombre</label>
          <b-field>
            <b-input
              v-model.trim.lazy="$v.form.firstName.$model"
              expanded
            ></b-input>
          </b-field>
          <!-- end first name -->

          <!-- first name -->
          <label for="" class="label">Apellidos</label>
          <b-field>
            <b-input
              v-model.trim.lazy="$v.form.lastName.$model"
              expanded
            ></b-input>
          </b-field>
          <!-- end first name -->

          <!-- first name -->
          <label for="" class="label">Correo electrónico</label>
          <b-field>
            <b-input
              v-model.trim.lazy="$v.form.email.$model"
              type="email"
              expanded
            ></b-input>
          </b-field>
          <!-- end first name -->

          <!-- first name -->
          <label for="" class="label">Contraseña</label>
          <b-field>
            <b-input
              v-model="$v.form.password.$model"
              type="password"
              expanded
            ></b-input>
          </b-field>
          <!-- end first name -->

          <b-field>
            <b-button
              type="is-primary"
              native-type="submit"
              :loading="form.loading"
              :disabled="$v.form.$invalid"
            >
              Crear cuenta
            </b-button>
          </b-field>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import gql from 'graphql-tag'
import { required, email } from 'vuelidate/lib/validators'
export default {
  data() {
    return {
      form: {
        firstName: null,
        lastName: null,
        email: null,
        password: null,
        loading: false
      }
    }
  },
  validations: {
    form: {
      firstName: {
        required
      },
      lastName: {
        required
      },
      email: {
        required,
        email
      },
      password: {
        required
      }
    }
  },
  methods: {
    register() {
      this.$v.form.$touch()
      if (!this.$v.form.$invalid) {
        this.form.loading = true
        this.$apollo
          .mutate({
            mutation: gql`
              mutation register(
                $firstName: String!
                $lastName: String!
                $email: String!
                $password: String!
              ) {
                register(
                  firstName: $firstName
                  lastName: $lastName
                  email: $email
                  password: $password
                ) {
                  status
                }
              }
            `,
            variables: {
              firstName: this.form.firstName,
              lastName: this.form.lastName,
              email: this.form.email,
              password: this.form.password
            }
          })
          .then(({ data }) => {
            if (data.register.status === 'ok') {
              this.form.loading = false
              this.$buefy.toast.open('Se creó tu cuenta')
            }
          })
      }
    }
  }
}
</script>

<style scoped></style>
