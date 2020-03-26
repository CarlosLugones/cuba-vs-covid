<template>
  <div>
    <b-button
      type="is-primary"
      @click="$router.replace('/dashboard/workshops/add')"
    >
      Añadir taller
    </b-button>
  </div>
</template>

<script>
import gql from 'graphql-tag'
export default {
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
        // eslint-disable-next-line no-console
        console.log(data)
      })
  }
}
</script>

<style scoped></style>
