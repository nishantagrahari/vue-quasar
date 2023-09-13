<template>
    <div class='master-filter'>        
        <StateFilter @state-filter='applyStateFilter'/>
        <TerritoryFilter            
            :is-state-selected="isStateSelected"
            :state-filter='mapped1' 
            @territory-filter='applyTerrFilter'
        />
    </div>
    <div>
        <ChartMetrix @custom-filter='applyCustomFilter'/>
    </div>   
    <div class='chart-view'>      
        <ChartTable3
            :custom-filter='mapped3' 
            :state-filter='mapped1' 
            :terr-filter='mapped2' 
            :is-state-selected="isStateSelected"
        />
        <ChartTable4
            :custom-filter='mapped3' 
            :state-filter='mapped1' 
            :terr-filter='mapped2' 
            :is-state-selected="isStateSelected"
        />
    </div>


</template>

<script>
import ChartMetrix from './chart/ChartMetrix.vue'
import ChartTable3 from './chart/ChartTable3.vue'
import ChartTable4 from './chart/ChartTable4.vue'
import StateFilter from './master-filter/StateFilter.vue'
import TerritoryFilter from './master-filter/TerritoryFilter.vue'


let mapped1='';
let mapped2='';
let mapped3='Potential';
// let chartKey=""

export default{

    data(){
        // true for stateselected will disable the filter
        return {mapped1,mapped2,isStateSelected:true,mapped3}
    },

    components:{
        ChartMetrix,
        ChartTable3,ChartTable4,
        StateFilter,TerritoryFilter
    },

    methods:{
        //functions to accepts state & territory filter
        applyStateFilter(val){
            // console.log("Filter-state",val)  
            this.mapped1=val.map(x=>x)
            if(val.length!=0){     
                //if state is selected then enable the territory filter
                //and viceversa        
                this.isStateSelected=false
            }
            else{
                this.isStateSelected=true
            }
          
        },

        applyTerrFilter(v){
               console.log("Filter-territroy",v)       
              this.mapped2=v.map(x=>x) 
                  
        },

        applyCustomFilter(v){
            console.log(v)
            this.mapped3=v
        }

    },

}

</script>


<style scoped>
.master-filter{
   display: flex;
   justify-content: left;
   align-items: center;
}


.chart-view{
   display: flex;
   justify-content: center;
   align-items: center;
   width: 100%;
   height:50vh;
   padding: 2vh;
}

</style>