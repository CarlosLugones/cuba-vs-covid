export default {
  mode: 'universal',

  /*
   ** Headers of the page
   */
  head: {
    title: process.env.npm_package_name || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: process.env.npm_package_description || ''
      }
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }]
  },

  /*
   ** Customize the progress-bar color
   */
  loading: { color: '#fff' },

  /*
   ** Global CSS
   */
  css: ['~/assets/styles.css'],

  /*
   ** Plugins to load before mounting the App
   */
  plugins: [
    { src: '~/plugins/vuex', ssr: true },
    { src: '~/plugins/vuelidate' }
  ],

  /*
   ** Nuxt.js dev-modules
   */
  buildModules: [
    // Doc: https://github.com/nuxt-community/eslint-module
    '@nuxtjs/eslint-module'
  ],

  /*
   ** Nuxt.js modules
   */
  modules: [
    '@nuxtjs/auth',
    // Doc: https://buefy.github.io/#/documentation
    'nuxt-buefy',
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
    // Doc: https://github.com/nuxt-community/dotenv-module
    '@nuxtjs/dotenv',
    '@nuxtjs/apollo',
    '@nuxtjs/moment',
    'cookie-universal-nuxt'
  ],

  auth: {
    redirect: {
      login: '/login',
      logout: '/',
      callback: '/accounts/callback',
      home: false,
      user: '/profile'
    },
    strategies: {
      local: {
        endpoints: {
          logout: true,
          user: false
        },
        tokenRequired: true,
        tokenType: 'JWT'
      }
    },
    // User will be redirected on login/logouts.
    watchLoggedIn: true
  },

  /*
   ** Axios module configuration
   ** See https://axios.nuxtjs.org/options
   */
  axios: {},

  apollo: {
    tokenExpires: 7,
    includeNodeModules: true,
    // Note: Setting JWT would repeat the prefix defined in Apollo `tokenType` in `local` strategy
    authenticationType: '',
    defaultOptions: {
      $query: {
        loadingKey: 'loading',
        fetchPolicy: 'cache-and-network'
      }
    },
    clientConfigs: {
      default: '~/apollo/client.js'
    }
  },

  moment: {
    defaultLocale: 'es-do',
    locales: ['es-do']
  },

  /*
   ** Build configuration
   */
  build: {
    /*
     ** You can extend webpack config here
     */
    extend(config, ctx) {}
  }
}
