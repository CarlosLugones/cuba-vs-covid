/**
 * Store to handle auth data
 */

export const state = () => ({
  user: null,
  strategy: null
})

export const mutations = {
  loadFromCookie(state) {
    const cookie = this.$cookies.get('auth.user')
    if (cookie) {
      state.user = cookie

      // Inject into nuxt $auth
      this.$auth.setStrategy('local')
      this.$auth.setUser(state.user)
      const token = this.$cookies.get('auth._token.local')
      this.$auth.setToken('local', token)
    }
  },
  initUser(state) {
    state.user = {
      username: null,
      firstName: null,
      lastName: null,
      email: null
    }
  },
  setUser(state, payload) {
    this.commit('auth/initUser')
    // state.strategy = payload.strategy
    switch (payload.strategy) {
      case 'local': {
        state.user = payload.user
        break
      }
    }
  },
  cleanAuth(state) {
    state.user = null

    // Clean user
    this.$auth.setUser(null)
    this.$cookies.set('auth.user', null)

    // Clean token
    this.$auth.setToken('local', null)
    this.$cookies.set('auth._token.local', null)
  }
}

export const getters = {
  getUser: (state) => state.user
}
