<template>
  <div>
    <b-button
      type="is-primary"
      class="margin-bottom-10"
      @click="$router.replace('/dashboard/workshops/add')"
    >
      Añadir taller
    </b-button>
    <div class="columns is-multiline">
      <div v-for="workshop in workshops" :key="workshop.id" class="column is-4">
        <WorkshopCard :workshop="workshop" />
      </div>
    </div>
  </div>
</template>

<script>
import gql from 'graphql-tag'
import WorkshopCard from '~/components/WorkshopCard'
export default {
  components: { WorkshopCard },
  layout: 'dashboard',
  data() {
    return {
      workshops: []
    }
  },
  mounted() {
    this.$apollo
      .query({
        query: gql`
          query viewerWorkshops {
            viewerWorkshops {
              id
              name
              phone
              fromTime
              toTime
            }
          }
        `
      })
      .then(({ data }) => {
        this.workshops = data.viewerWorkshops
      })
  }
}
</script>

<style scoped></style>
