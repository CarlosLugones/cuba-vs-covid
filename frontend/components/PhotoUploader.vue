<template>
  <div>
    <!-- modal -->
    <Modal :active.sync="active" @close="active = false">
      <Cropper
        ref="cropper"
        :src="photoTemp"
        :stencil-props="{
          aspectRatio: aspectRatio
        }"
        class="cropper is-rounded"
        @change="($event) => change($event)"
      />
      <div class="has-text-centered">
        <b-button
          :loading="loading"
          type="is-primary"
          class="is-rounded margin-top-10"
          @click="upload()"
        >
          Subir imagen
        </b-button>
        <p class="margin-top-10">La imagen debe pesar menos de 5 mb.</p>
      </div>
    </Modal>
    <!-- end modal -->

    <!-- photo widget -->
    <div
      v-show="photo"
      :class="editable ? 'photo is-rounded' : 'photo is-rounded'"
      :style="
        `background: url('${photo}'); width: ${size || width}; height: ${size ||
          height};`
      "
      @click="showModal()"
    >
      <div v-if="editable" class="overlay is-rounded">
        <div class="bottom flex-wrap-center">
          <b-icon icon="camera"></b-icon>
        </div>
      </div>
    </div>
    <div
      v-show="!photo"
      :class="editable ? 'empty is-rounded' : 'empty is-rounded'"
      :style="`width: ${size || width}; height: ${size || height};`"
      @click="showModal()"
    >
      <div class="overlay is-rounded flex-wrap-center">
        <b-icon icon="camera"></b-icon>
      </div>
    </div>
    <!-- end widget -->

    <input
      ref="file"
      type="file"
      accept="image/*"
      hidden
      @change="setPhotoTemp($event)"
    />
  </div>
</template>

<script>
import { Cropper } from 'vue-advanced-cropper'
// Components
import Modal from '~/components/Modal'
export default {
  components: { Cropper, Modal },
  props: {
    photo: {
      type: String,
      default: null
    },
    size: {
      type: String,
      default: null
    },
    width: {
      type: String,
      default: null
    },
    height: {
      type: String,
      default: null
    },
    aspectRatio: {
      type: Number,
      default: 1
    },
    editable: {
      type: Boolean,
      default: true
    }
  },
  data() {
    return {
      active: false,
      photoTemp: null,
      loading: false
    }
  },
  methods: {
    showModal() {
      if (this.editable) {
        this.$refs.file.click()
      }
    },
    setPhotoTemp(event) {
      const input = event.target
      if (input.files && input.files[0]) {
        const reader = new FileReader()
        reader.onload = (e) => {
          this.photoTemp = e.target.result
          this.active = true
        }
        reader.readAsDataURL(input.files[0])
      }
    },
    change(event) {
      //
    },
    async upload() {
      const { canvas } = this.$refs.cropper.getResult()
      const cropped = await new Promise((resolve, reject) => {
        canvas.toBlob(
          (blob) => {
            blob.filename = 'photo.jpeg'
            blob.name = 'photo.jpeg'
            resolve(blob)
          },
          'image/jpeg',
          1
        )
      })

      if (cropped.size / 1024 / 1024 > 5) {
        this.$buefy.dialog.alert({
          message: 'La imagen pesa más de 5 mb, intenta con una más pequeña.',
          type: 'is-black'
        })
        this.active = false
        this.photoTemp = null
      } else {
        const formData = new FormData()
        formData.append('file', cropped)
        formData.append('format', 'jpeg')

        this.loading = true
        const config = {
          headers: {
            'content-type': 'multipart/form-data'
          }
        }
        this.$axios
          .post(
            process.env.BACKEND_BASE_URL + 'uploads/upload/',
            formData,
            config
          )
          .then((response) => {
            this.loading = false
            this.active = false
            if (response.status === 200) {
              const url = response.data.url
              this.photo = url
              this.$emit('photo:uploaded', url)
            }
          })
      }
    }
  }
}
</script>

<style lang="stylus" scoped>
.cropper
  width 300pt
  height 300pt

.photo
  background-size cover !important

  .icon
    color #ffffff

.photo:hover
  cursor pointer

.empty
  background #e4e0dd

  .icon
    color #000000
    transition color 200ms

.empty:hover
  cursor pointer

.overlay
  width 100%
  height 100%
  background rgba(118, 118, 118, 0.07)

.bottom
  background #000000
  width 100%
  height 40pt
  padding 5pt
  border-top-left-radius 10pt
  border-top-right-radius 10pt
  opacity 0.7

.icon
  width 100% !important
  height 100% !important
  font-size 20pt
</style>
