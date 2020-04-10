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
            <div class="column">
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
              <b-button type="is-black" size="is-large" icon-left="filter">
                Filtrar
              </b-button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import gql from 'graphql-tag'
export default {
  data() {
    return {
      stlmodel: null,
      provinces: [],
      cities: [],
      filterForm: {
        province: null,
        city: null
      }
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
    }
  }
}
</script>

<style lang="stylus" scoped></style>
