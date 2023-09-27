<template>
  <div class="q-pa-md">
    <div class="master-filter-section">
      <div class="master-filter-sub_section">
        <div class="state-filter">
          <StateFilter @state-filter="applyStateFilter" />        
        </div>
        <ResetBtn />
      </div>
      <div class="qchip">
         <QView
            :state-filter='mapped2'
            @state-chip='finalStateFilter'       
        />
      </div> 
    </div>
    
    <div class="title"><span>Tier Summary</span></div>

    <TierSummary
      :state-filter="mapped1"     
      :is-state-selected="isStateSelected"
      @row-tier="applyTierFilter"
    />

    <div>
      <div class="title">
        <span>{{ mapped3 }} by Academic vs Community Orgs</span>
        <span>{{ mapped3 }} by 340B vs Non-340B Orgs</span>
      </div>
      <div class="custom-filter-box">
          <ChartMetrix @custom-filter="applyCustomFilter" />
        </div>
      <div class="chart-view">
        
        <ChartTable3
          :custom-filter="mapped3"
          :state-filter="mapped1"  
          :tier-filter='tierFilter'
        />

        <ChartTable4
          :custom-filter="mapped3"
          :state-filter="mapped1"        
          :tier-filter='tierFilter'
        />
      </div>
    </div>
    <GoogleMap
      :custom-filter="mapped3"
      :state-filter="mapped1"      
      :is-state-selected="isStateSelected"
      :tier-filter='tierFilter'
    />
  </div>
</template>

<script>
import ChartMetrix from "./chart/ChartMetrix.vue";
import ChartTable3 from "./chart/ChartTable3.vue";
import ChartTable4 from "./chart/ChartTable4.vue";
import StateFilter from "./master-filter/StateFilter.vue";
import GoogleMap from "./GoogleMap.vue";
import TierSummary from "./TierSummary.vue";
import ResetBtn from "./master-filter/ResetFilter.vue";
import QView from './master-filter/QchipView.vue';

let mapped1 = "";
let mapped2 = "";
let mapped3 = "Potential";
let tierFilter=''

export default {
  data() {
    // true for stateselected will disable the filter
    return { mapped1,mapped2,mapped3,tierFilter};
  },

  components: {
    GoogleMap,
    ChartMetrix,
    ChartTable3,
    ChartTable4,
    StateFilter,
    TierSummary,
    ResetBtn,
    QView
  },

  methods: {
      applyTierFilter(val){
        //function to change component value based on Tier clicked
        this.tierFilter=val
        console.log(val)
      },

      //functions to accepts state & territory filter
      applyStateFilter(val) {
        this.mapped2=val      
      },

      finalStateFilter(v){     
        this.mapped1= [...v]            
        console.log(this.mapped)
      },
    
      applyCustomFilter(v) {
        console.log(v);
        this.mapped3 = v;
      },
    },
};
</script>

<style scoped>
.master-filter-section {
  
  background-color: #e6e6e6;
  align-items: center;
  padding:1vw 1vw 0.5vw 1vw ;
  margin: 0 0 1vw 0;
}

.master-filter-sub_section{
  display: flex;
  justify-content: space-around;

}

.state-filter {
  padding: 0 1vw;
  display: flex;
  align-items: center;
  flex: 1;
}
.qchip{
   padding:0.5vw 0.7vw 0vw;
}

.chart-view {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 50vh;
  padding: 2vh;
}
.title {
  width: 100%;
  height: 5vh;
  display: flex;
  align-items: center;
  justify-content: space-around;

  background-color: #e6e6e6;
  margin: 1vh 0;
}
.title span {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  font-size: 1vw;
  font-weight: 600;
}
.custom-filter-box {
  width: 100%;
  display: flex;
  justify-content: end;
}
</style>
