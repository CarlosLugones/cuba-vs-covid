<template>
  <div>
    <b-navbar>
      <template slot="brand">
        <b-navbar-item tag="router-link" :to="{ path: '/' }">
          <img
            src="/img/covid.jpg"
            alt=""
            height="28"
            style="border-radius: 50%"
          />
          <span style="margin-left: 5pt">CubaVSCovid</span>
        </b-navbar-item>
      </template>
      <template slot="start">
        <b-navbar-item href="#">
          Inicio
        </b-navbar-item>
        <b-navbar-item href="#">
          Documentation
        </b-navbar-item>
        <b-navbar-dropdown label="Info">
          <b-navbar-item href="#">
            About
          </b-navbar-item>
          <b-navbar-item href="#">
            Contact
          </b-navbar-item>
        </b-navbar-dropdown>
      </template>

      <template slot="end">
        <b-navbar-item tag="div">
          <div class="buttons">
            <nuxt-link class="button is-primary" to="/register">
              <strong>Registrarme</strong>
            </nuxt-link>
            <nuxt-link class="button" to="/login">
              Entrar
            </nuxt-link>
          </div>
        </b-navbar-item>
      </template>
    </b-navbar>

    <section class="main-content">
      <nuxt />
    </section>
  </div>
</template>

<script>
export default {}
</script>
