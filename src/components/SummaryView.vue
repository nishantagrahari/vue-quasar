<template>
  <div class="q-pa-md">
    <div class="master-filter-section">
      <div class="master-filter">
        <StateFilter @state-filter="applyStateFilter" />
        <TerritoryFilter
          :is-state-selected="isStateSelected"
          :state-filter="mapped1"
          @territory-filter="applyTerrFilter"
        />
      </div>
      <ResetBtn />
    </div>
    <div class="title"><span>Tier Summary</span></div>

    <TierSummary
      :state-filter="mapped1"
      :terr-filter="mapped2"
      :is-state-selected="isStateSelected"
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
          :terr-filter="mapped2"
          :is-state-selected="isStateSelected"
        />
        <ChartTable4
          :custom-filter="mapped3"
          :state-filter="mapped1"
          :terr-filter="mapped2"
          :is-state-selected="isStateSelected"
        />
      </div>
    </div>
    <GoogleMap
      :custom-filter="mapped3"
      :state-filter="mapped1"
      :terr-filter="mapped2"
      :is-state-selected="isStateSelected"
    />
  </div>
</template>

<script>
import ChartMetrix from "./chart/ChartMetrix.vue";
import ChartTable3 from "./chart/ChartTable3.vue";
import ChartTable4 from "./chart/ChartTable4.vue";
import StateFilter from "./master-filter/StateFilter.vue";
import TerritoryFilter from "./master-filter/TerritoryFilter.vue";
import GoogleMap from "./GoogleMap.vue";
import TierSummary from "./TierSummary.vue";
import ResetBtn from "./master-filter/ResetFilter.vue";

let mapped1 = "";
let mapped2 = "";
let mapped3 = "Potential";
// let chartKey=""

export default {
  data() {
    // true for stateselected will disable the filter
    return { mapped1, mapped2, isStateSelected: true, mapped3 };
  },

  components: {
    GoogleMap,
    ChartMetrix,
    ChartTable3,
    ChartTable4,
    StateFilter,
    TerritoryFilter,
    TierSummary,
    ResetBtn,
  },

  methods: {
    //functions to accepts state & territory filter
    applyStateFilter(val) {
      // console.log("Filter-state",val)
      this.mapped1 = val.map((x) => x);
      if (val.length != 0) {
        //if state is selected then enable the territory filter
        //and viceversa
        this.isStateSelected = false;
      } else {
        this.isStateSelected = true;
      }
    },

    applyTerrFilter(v) {
      console.log("Filter-territroy", v);
      this.mapped2 = v.map((x) => x);
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
  display: flex;
  justify-content: space-around;
  background-color: #e6e6e6;
  align-items: center;
  padding: 1vw;
  margin: 0 0 1vw 0;
}
.master-filter {
  padding: 0 1vw;
  display: flex;

  align-items: center;
  flex: 1;
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
