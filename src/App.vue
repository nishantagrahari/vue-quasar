<template>
 
      <router-view /> <!-- This is where the route components will be rendered -->
     
</template>

<script>
import { ref } from 'vue'



export default {
  name: 'LayoutDefault',

 

  setup () {
    return {
      leftDrawerOpen: ref(false)
    }
  }
}
</script>


<style scoped>
q-page-container{
  height:100%;
  width:100%
}



</style>