<template>
  <!-- <q-layout> -->
    <!-- <q-page-container> -->
      <!-- <MasterFilter /> -->
      <!-- <HelloWorld /> -->
      <!-- <TableComponent /> -->
      <!-- <ExpandableTable /> -->
      <!-- <TierSummary /> -->
      <!-- <OrgTable /> -->
      <!-- <DynamicTree /> -->
      <!-- <ChartTable1 /> -->
      <!-- <ChartTable2 /> -->
      <!-- <Accounttable /> -->
      <SummaryView />
    <!-- </q-page-container>
  </q-layout> -->
</template>

<script>
import { ref } from 'vue'
// import MasterFilter from './components/MasterFilter.vue'
// import HelloWorld from './components/HelloWorld.vue'
// import TableComponent from './components/TableComponent.vue'
// import ExpandableTable from './components/ExpandableTable.vue'
// import TierSummary from './components/TierSummary.vue'
// import OrgTable from './components/OrgTable.vue'
// import DynamicTree from './components/DynamicTree.vue'
// import ChartTable1 from './components/chart/ChartTable1.vue'
// import ChartTable2 from './components/ChartTable2.vue'
import SummaryView from './components/SummaryView.vue'



export default {
  name: 'LayoutDefault',

  components: {
    // MasterFilter,
    // ExpandableTable
    // HelloWorld 
    // TableComponent
    // TierSummary
    // OrgTable    
    // DynamicTree
    // ChartTable2
    // ChartTable1
    SummaryView
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