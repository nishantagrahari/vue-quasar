<template>
  <Header />
  <Tabs />
  <SummaryView />
  <!-- This is where the route components will be rendered -->
  <Footer />
</template>
<script>

import Header from './header/Header.vue'
import SummaryView from './SummaryView.vue'
import Footer from "./header/Footer.vue"
import Tabs from "./header/Tabs.vue"




export default {
  name: 'HomePage',

  components: {

    Header,
    Tabs,
    SummaryView,
    Footer
    
  }
}
</script>

<style scoped>
q-page-container {
  height: 100%;
  width: 100%;
}
</style>
