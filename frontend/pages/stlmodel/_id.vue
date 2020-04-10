<template>
  <div>
    <div v-if="stlmodel" class="hero is-dark is-bold">
      <div class="hero-body">
        <div class="container">
          <div class="columns is-multiline is-centered">
            <div class="column is-3">
              <img
                :src="`/media/${stlmodel.photo}`"
                alt=""
                width="200pt"
                style="border-radius: 10pt"
              />
            </div>
            <div class="column is-4">
              <h2 class="subtitle">{{ stlmodel.name }}</h2>
              <p>Disponibilidad total: {{ stlmodel.stock }}</p>
              <a
                :href="`/media/${stlmodel.file}`"
                target="_blank"
                class="button is-primary is-medium margin-top-10"
              >
                <b-icon icon="download" slyle="margin-right: 10pt"></b-icon>
                <span>Descargar modelo STL</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- filter -->
    <div v-if="stlmodel" class="hero is-info">
      <div class="hero-body">
        <div class="container">
          <div class="columns is-centered">
            <div class="column">
              <b-field label="Provincia" label-position="inside">
                <b-select
                  v-model="filterForm.province"
                  placeholder="Selecciona una provincia"
                  expanded
                  size="is-medium"
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
            </div>

            <div class="column">
              <b-field label="Municipio" label-position="inside">
                <b-select
                  v-model="filterForm.city"
                  placeholder="Selecciona un municipio"
                  expanded
                  size="is-medium"
                  :disabled="!filterForm.province"
                >
                  <option
                    v-for="city in cities"
                    :key="city.id"
                    :value="city.id"
                  >
                    {{ city.name }}
                  </option>
                </b-select>
              </b-field>
            </div>

            <div class="column is-narrow">
              <b-button
                type="is-black"
                size="is-large"
                icon-left="filter"
                @click="filter()"
              >
                Filtrar
              </b-button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- end filter -->

    <!-- filter results -->
    <div class="container margin-top-10" style="padding: 20pt">
      <div v-if="results.length > 0" class="has-text-centered margin-bottom-10">
        Hemos encontrado {{ results.length }}
        {{ results.length > 1 ? 'makers' : 'maker' }} con disponibilidad de este
        producto.
      </div>
      <div class="columns is-multiline is-centered">
        <div
          v-for="result in results"
          :key="result.id"
          class="column is-3 is-12-mobile"
        >
          <ProductCard :product="result" />
        </div>
      </div>
      <div v-if="results.length === 0" class="has-text-centered">
        No hay makers con disponibilidad de este producto en la zona
        especificada.
      </div>
    </div>
    <!-- end filter results -->
  </div>
</template>

<script>
import gql from 'graphql-tag'
import ProductCard from '~/components/ProductCard'

export default {
  components: { ProductCard },
  data() {
    return {
      stlmodel: null,
      provinces: [],
      cities: [],
      filterForm: {
        province: null,
        city: null,
        loading: false
      },
      results: []
    }
  },
  async mounted() {
    // Load stlmodel
    this.$apollo
      .query({
        query: gql`
          query stlmodel($id: String!) {
            stlmodel(id: $id) {
              id
              name
              photo
              stock
              file
            }
          }
        `,
        variables: {
          id: this.$route.params.id
        }
      })
      .then(({ data }) => {
        this.stlmodel = data.stlmodel
        this.filter()
      })

    // Load provinces
    const { data } = await this.$apollo.query({
      query: gql`
        query provinces {
          provinces {
            id
            name
          }
        }
      `
    })
    this.provinces = data.provinces
  },
  methods: {
    loadCities(city) {
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
            provinceId: this.filterForm.province
          }
        })
        .then(({ data }) => {
          this.cities = data.cities
          if (city) {
            this.filterForm.city = city
          }
        })
    },
    filter() {
      this.filterForm.loading = true
      this.$apollo
        .query({
          query: gql`
            query filterProducts(
              $stlmodel: String!
              $province: String
              $city: String
            ) {
              filterProducts(
                stlmodel: $stlmodel
                province: $province
                city: $city
              ) {
                id
                stock
                owner {
                  id
                  firstName
                  lastName
                  avatar
                  phone
                  fromTime
                  toTime
                  address {
                    line1
                    line2
                  }
                }
              }
            }
          `,
          variables: {
            stlmodel: this.$route.params.id,
            province: this.filterForm.province,
            city: this.filterForm.city
          }
        })
        .then(({ data }) => {
          this.filterForm.loading = true
          this.results = data.filterProducts
        })
    }
  }
}
</script>

<style lang="stylus" scoped></style>
