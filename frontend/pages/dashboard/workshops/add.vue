<template>
  <div>
    <nav class="breadcrumb" aria-label="breadcrumbs">
      <ul>
        <li><nuxt-link to="/dashboard/workshops">Talleres</nuxt-link></li>
        <li class="is-active"><a href="#">Crear taller</a></li>
      </ul>
    </nav>
    <form @submit.stop.prevent="add()">
      <!-- name -->
      <label for="" class="label">Nombre del taller</label>
      <b-field>
        <b-input v-model="$v.form.name.$model"></b-input>
      </b-field>
      <!-- end name -->

      <!-- phone -->
      <label for="" class="label">Teléfono</label>
      <b-field>
        <b-input v-model="$v.form.phone.$model"></b-input>
      </b-field>
      <!-- end phone -->

      <!-- address line 1 -->
      <label for="" class="label">Línea 1 de la dirección</label>
      <b-field>
        <b-input v-model="$v.form.address.line1.$model"></b-input>
      </b-field>
      <!-- end address line 1 -->

      <!-- address line 2 -->
      <label for="" class="label">Línea 2 de la dirección</label>
      <b-field>
        <b-input v-model="form.address.line2"></b-input>
      </b-field>
      <!-- end address line 2 -->

      <!-- address province -->
      <label for="" class="label">Provincia</label>
      <b-field>
        <b-select
          v-model="$v.form.address.province.$model"
          placeholder="Selecciona una provincia"
          expanded
          @input="loadCities()"
        >
          <option
            v-for="province in provinces"
            :key="province.id"
            :value="province.id"
          >
            {{ province.name }}
          </option>
        </b-select>
      </b-field>
      <!-- end address province -->

      <!-- address city -->
      <label for="" class="label">Municipio</label>
      <b-field>
        <b-select
          v-model="$v.form.address.city.$model"
          placeholder="Selecciona un municipio"
          expanded
          :disabled="!$v.form.address.province.$model"
        >
          <option v-for="city in cities" :key="city.id" :value="city.id">
            {{ city.name }}
          </option>
        </b-select>
      </b-field>
      <!-- end address city -->

      <!-- from time -->
      <label for="" class="label">Hora de apertura</label>
      <b-field>
        <b-timepicker
          v-model="$v.form.fromTime.$model"
          rounded
          placeholder="Clic para seleccionar"
          icon="clock"
        >
        </b-timepicker>
      </b-field>
      <!-- end from time -->

      <!-- to time -->
      <label for="" class="label">Hora de cierre</label>
      <b-field>
        <b-timepicker
          v-model="$v.form.toTime.$model"
          rounded
          placeholder="Clic para seleccionar"
          icon="clock"
        >
        </b-timepicker>
      </b-field>
      <!-- end to time -->

      <b-field>
        <b-button
          type="is-primary"
          native-type="submit"
          :loading="form.loading"
          :disabled="$v.form.$invalid"
        >
          Añadir taller
        </b-button>
      </b-field>
    </form>
  </div>
</template>

<script>
import gql from 'graphql-tag'
import { required } from 'vuelidate/lib/validators'
export default {
  layout: 'dashboard',
  data() {
    return {
      provinces: [],
      cities: [],
      form: {
        name: null,
        phone: null,
        fromTime: null,
        toTime: null,
        address: {
          line1: null,
          line2: null,
          province: null,
          city: null
        }
      }
    }
  },
  validations: {
    form: {
      name: {
        required
      },
      phone: {
        required
      },
      fromTime: {
        required
      },
      toTime: {
        required
      },
      address: {
        line1: {
          required
        },
        province: {
          required
        },
        city: {
          required
        }
      }
    }
  },
  mounted() {
    this.$apollo
      .query({
        query: gql`
          query provinces {
            provinces {
              id
              name
            }
          }
        `
      })
      .then(({ data }) => {
        this.provinces = data.provinces
      })
  },
  methods: {
    add() {
      this.$apollo
        .mutate({
          mutation: gql`
            mutation createWorkshop(
              $name: String!
              $phone: String!
              $fromTime: Time!
              $toTime: Time!
              $addressLine1: String!
              $addressLine2: String
              $addressProvince: String!
              $addressCity: String!
            ) {
              createWorkshop(
                name: $name
                phone: $phone
                fromTime: $fromTime
                toTime: $toTime
                addressLine1: $addressLine1
                addressLine2: $addressLine2
                addressProvince: $addressProvince
                addressCity: $addressCity
              ) {
                status
              }
            }
          `,
          variables: {
            name: this.form.name,
            phone: this.form.phone,
            fromTime: this.$moment(this.form.fromTime).format('hh:mm'),
            toTime: this.$moment(this.form.toTime).format('hh:mm'),
            addressLine1: this.form.address.line1,
            addressLine2: this.form.address.line2,
            addressProvince: this.form.address.province,
            addressCity: this.form.address.city
          }
        })
        .then(({ data }) => {
          if (data.createWorkshop.status === 'ok') {
            this.$buefy.toast.open('Se creó el taller')
            this.$router.replace('/dashboard/workshops')
          }
        })
    },
    loadCities() {
      this.$apollo
        .query({
          query: gql`
            query cities($provinceId: String!) {
              cities(provinceId: $provinceId) {
                id
                name
              }
            }
          `,
          variables: {
            provinceId: this.form.address.province
          }
        })
        .then(({ data }) => {
          this.cities = data.cities
        })
    }
  }
}
</script>

<style scoped></style>
