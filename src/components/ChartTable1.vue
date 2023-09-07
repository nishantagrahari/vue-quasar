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
    
    <div class='main-container'>
        <div class='chart'>
            <canvas ref="mychart"></canvas>
        </div>

        <div class='chart'>  
            <ChartTable2 :filter-name='model' :key='chartKey'/>
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

    components:{
      ChartTable2
    },

    // computed:{
    //       chartKey = model.value    
    // },    
    
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
                // chartKey
        }

    },

    computed:{
        // It will change chartKey dataproperty if the model value gets changed.
        //so as to reload chart based on it
       chartKey(){
         console.log(model.value)
         return model.value
       }
    },

//    mounted() {
    // console.log("nishant")   
    //   new Chart(this.$refs.mychart,this.myconfig);
      //    Chart.register(ChartDataLabels);

    //   let path='http://127.0.0.1:5000/Chart/Potential'
     
    //   fetch(path)
    //   .then((response)=>{
    //       if(response.ok){
    //           return(response.json())
    //       }      
     
    //   })
    //   .then((data)=>{  
    //       console.log(data)      
    //     for (let i=0;i<2;i++){    
    //         console.log(data.output[i][1],data.output[i][3] ) 
    //         console.log(this.mychartdata.datasets[0].data[0].Accounts.value)     
    //         this.mychartdata.datasets[0].data[i].Accounts.value= data.output[i][1]
    //         this.mychartdata.datasets[0].data[i].Percent.value=data.output[i][3]            
    //         }
    //   }) 
    //   .catch((err)=>{
    //     console.log(err)
    //   })

     


//    },

   methods:{
    customRender(val){
      //changing label of chart based on it
    //   this.mychartTittle=val
      this.model=val
      this.myconfig.options.plugins.title.text="Academic vs Community by "+val
    //   console.log(val) 
    //   this.chartTittle=val
    //   console.log(this.mychartTittle)
     let path='http://127.0.0.1:5000/Chart/'+val
     
      fetch(path)
      .then((response)=>{
          if(response.ok){
              return(response.json())
          }      
     
      })
      .then((data)=>{  
        //   console.log(data)      
        for (let i=0;i<2;i++){    
            // console.log(data.output[i][1],data.output[i][3] ) 
            // console.log(this.mychartdata.datasets[0].data[0].Accounts.value)     
            this.mychartdata.datasets[0].data[i].Accounts.value= data.output[i][1]
            this.mychartdata.datasets[0].data[i].Percent.value=data.output[i][3]            
            }
        this.updateChart();
      }) 
      .catch((err)=>{
        console.log(err)
      })
    },

      updateChart() {
        // Destroy the old chart if it exists
        if (this.chart) {
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

</style>