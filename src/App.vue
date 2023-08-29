<template>
  <!-- <q-layout> -->
    <!-- <q-page-container> -->
      <!-- <HelloWorld /> -->
      <!-- <TableComponent /> -->
      <!-- <ExpandableTable /> -->
      <!-- <TierSummary /> -->
      <!-- <OrgTable /> -->
      <DynamicTree />
      <!-- <Accounttable /> -->
    <!-- </q-page-container>
  </q-layout> -->
</template>

<script>
import { ref } from 'vue'
// import HelloWorld from './components/HelloWorld.vue'
// import TableComponent from './components/TableComponent.vue'
// import ExpandableTable from './components/ExpandableTable.vue'
// import TierSummary from './components/TierSummary.vue'
// import OrgTable from './components/OrgTable.vue'
import DynamicTree from './components/DynamicTree.vue'


export default {
  name: 'LayoutDefault',

  components: {
    // ExpandableTable
    // HelloWorld 
    // TableComponent
    // TierSummary
    // OrgTable    
    DynamicTree
  },

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