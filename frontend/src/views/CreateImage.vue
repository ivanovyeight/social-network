<template>
  <v-container class="grey lighten-5">
      <h1 id="Title">Bookmark an image</h1>
    <v-row no-gutters>
      <v-col
        md="6"
        offset-md="3"
      >
        <v-card
          class="pa-2"
          outlined
          tile
        >
            <ImageForm/> 
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>


<script>
    import ImageForm from '../components/ImageForm'
export default {
    components:{
        ImageForm,

    }

}
</script>

<style>
#Title {
  text-align: center;
}



</style>