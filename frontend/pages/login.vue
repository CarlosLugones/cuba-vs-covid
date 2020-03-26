<template>
  <div class="container">
    <div class="columns is-centered">
      <div class="column is-6 is-12-mobile">
        <h1 class="title">Entrar</h1>
        <h2 class="subtitle">
          Si ya tienes una cuenta creada, introduce tus datos
        </h2>
        <form @submit.stop.prevent="login()">
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
              Entrar
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
        email: null,
        password: null,
        loading: false
      }
    }
  },
  validations: {
    form: {
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
    login() {
      this.$v.form.$touch()
      if (!this.$v.form.$invalid) {
        this.form.loading = true
        this.$apollo
          .mutate({
            mutation: gql`
              mutation login($email: String!, $password: String!) {
                login(email: $email, password: $password) {
                  status
                  token
                  user {
                    firstName
                    lastName
                    email
                  }
                }
              }
            `,
            variables: {
              email: this.form.email,
              password: this.form.password
            }
          })
          .then(({ data }) => {
            const { status, token, user } = data.login
            const jwtToken = 'JWT ' + token
            switch (status) {
              case 'ok': {
                // Save user to cookie using Vuex
                this.$auth.setStrategy('local').then(() => {
                  this.$store.commit('auth/setUser', {
                    strategy: this.$auth.strategy.name,
                    user
                  })
                  this.$auth.setToken('local', jwtToken)
                  this.$auth.setUser(user)

                  // Save auth data in cookies
                  this.$cookies.set('auth.user', user)
                  this.$cookies.set('auth._token.local', jwtToken)

                  this.$router.replace('/')
                  this.$emit('login')
                })
                break
              }
              case 'error': {
                // this.loginForm.error = true
                break
              }
            }
            this.form.loading = false
          })
      }
    }
  }
}
</script>

<style scoped></style>
