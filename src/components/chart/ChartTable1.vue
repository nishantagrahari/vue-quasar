<template>
    <div style="max-width: 300px; padding:1vw">
        <q-select 
          filled 
          v-model="model"           
          :options="options"
          stack-label         
          label="Select Filter"
        />
        {{ customRender(model)}}
    </div>
    
    <p v-if="error">{{error}}</p>
    <div v-else class='main-container'>
        <div class='chart'>
            <canvas ref="mychart"></canvas>
        </div>

        <div class='chart'>  
            <ChartTable2 
                :filter-name='model' 
                :state-filter='computedstate'  
                :terr-filter='terrFilter'
                :is-state-selected='isStateSelected' 
                :key='chartKey'
            />
        </div>
    </div>        
</template>

<script>
    import Chart from 'chart.js/auto'
    import ChartTable2 from './ChartTable2'
    import ChartDataLabels from 'chartjs-plugin-datalabels';
    import { ref } from 'vue'
    const options= ['Potential','% Diagnosis Pats','% Treated Pats','Product A Sales','Product B Sales' ]

    Chart.register(ChartDataLabels); //Plugins needs to be registered in the latest version
    
    const chartTittle="Potential by academic vs community"

    const data = {
                    labels: [
                                'Academic',
                                'Community'
                            ],
                    datasets: [{
                        label: 'Total # account ',
                        data: [
                                {Accounts:{value:3},Potential:{value:600},Percent:{value:30}}, 
                                {Accounts:{value:5},Potential:{value:100},Percent:{value:50}}
                                
                              ],
                            
                        backgroundColor: [
                            'rgb(255, 99, 132)',
                            'rgb(54, 162, 235)',                            
                        ],
                        hoverOffset: 4  //When hover the segment will be popped out
                    }]
                };
    

    const config = {
                            type: 'doughnut',
                            data: data,
                            options: {
                                responsive: true, //chart will resize automatically according to the block size
                                parsing: { key: 'Accounts.value'}  ,  
                                plugins: {
                                            legend: {
                                                position: 'bottom',
                                            },
                                            title: {
                                                display: true,
                                                text: chartTittle
                                            },
                                            datalabels: {
                                                            display: true,
                                                            align: 'center',
                                                            // backgroundColor: '#ccc',
                                                            // borderRadius: 2,
                                                            color:'white',
                                                            font: {
                                                                size: 10,
                                                            },
                                                            formatter:(value) => {
                                                                // console.log(value.Percent.value)
                                                                return (value.Percent.value) + '%' +"\n"+ "("+(value.Potential.value) +")";
                                                            },
                                            }
                                            // tooltip:{
                                            //     callbacks:{
                                            //                 label: function(context) {
                                            //                     console.log(context)
                                            //                     console.log(context)

                                            //                     let label = context.dataset.label || '';

                                            //                     if (label) {
                                            //                         label += ': ';
                                            //                     }
                                            //                     if (context.parsed.y !== null) {
                                            //                         label += new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(context.parsed.y);
                                            //                     }
                                            //                     return label;

                                            //     }
                                            // }
                                                                                    
                                        }
                            },
                        };

const model=ref('Potential')
// const chartKey=''

export default{

    props:['stateFilter','terrFilter','isStateSelected'],

    components:{
      ChartTable2
    },    
    
    data(){

        // computed(model, () => {
        // Update the key to force reactivity when model changes
        //     this.key = model.value;
        // })    

        return {                 
                mychartdata:data,
                myconfig:config,
                mychartTittle:chartTittle,
                model,
                options,
                error:null
                // stateFilter,
                // terrFilter
                // chartKey
        }

    },

    computed:{
        // It will change chartKey dataproperty if the model value gets changed.
        //so as to reload chart based on it
       chartKey(){
        //  console.log(model.value)    
        //  return (model.value)
        return '${this.model}-${this.stateFilter}-${this.terrFilter}'
         
       },

       computedstate(){
          return this.stateFilter
       }
    },



   methods:{
    customRender(val){
      //changing label of chart based on metrix selected(potential,diag.....)  
      this.model=val
      this.myconfig.options.plugins.title.text="Academic vs Community by "+val
   
    // converting filter data to JSON to pass in the server
    //  console.log('State-jSON',JSON.stringify(this.stateFilter))
    //  console.log('territory-jSON',JSON.stringify(this.terrFilter))
     

     let path='http://127.0.0.1:5000/Chart/'+val
    //  console.log(path)
      
      //sending post request to the server with the state and territory filter
      //getting chart data
      
      this.error=null  //initializing the error with the null value again
      fetch(path,{
          method:'POST',
          headers:{'Content-Type':'application/json'},
          body:JSON.stringify({state:this.stateFilter,terr:this.terrFilter,isstateselected:this.isStateSelected})
      })    
      .then((response)=>{
          //Handling errors if the server is not generating the output properly
          if(response.ok){
              return(response.json())
          }else{
              throw new Error("Something went wrong")
          }    
      })
      .then((data)=>{  
        //   console.log(data)      
        for (let i=0;i<2;i++){    
            //Updating chart with the fetched data  
            this.mychartdata.datasets[0].data[i].Accounts.value= data.output[i][1]
            this.mychartdata.datasets[0].data[i].Percent.value=data.output[i][3]            
            }
        this.updateChart();
      }) 
      .catch((err)=>{        
        this.error=true
        console.log(err,"Failed to fetch data")
      })
    },

      updateChart() {       
        if (this.chart) {
             // Destroy the old chart if it exists
            this.chart.destroy();
        }
        // Create a new chart with updated data
        this.chart = new Chart(this.$refs.mychart, this.myconfig);
    }
    
  }

}
</script>


<style scoped>
.chart{
    width:70vw;
    height: 50vh;
    padding: 1vw
}

.main-container{
    display:flex;
    text-align: center;
    justify-content: center;

}

p{
    font-display: bold;
    size: 2vh;
}
</style>