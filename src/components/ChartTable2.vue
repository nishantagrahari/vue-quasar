<template>
        
        <canvas ref="mychart"></canvas>
    
</template>

<script>
    import Chart from 'chart.js/auto'
    import ChartDataLabels from 'chartjs-plugin-datalabels';
    // import { ref } from 'vue'
    
    Chart.register(ChartDataLabels); //Plugins needs to be registered in the latest version
    
    const chartTittle="340B vs Non-340B by Potential"

    const data = {
                    labels: [
                                '340B',
                                'Non-340B'
                            ],
                    datasets: [{
                        label: 'Total # account ',
                        data: [
                                {Accounts:{value:3},Potential:{value:200},Percent:{value:30}}, 
                                {Accounts:{value:5},Potential:{value:500},Percent:{value:50}}                                
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
                                                                return (value.Percent.value) + '%' + "\n"+"("+(value.Potential.value) +")";
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

export default{

    props:['filterName'],

    // setup () {
    //     return {
    //         model: ref('Potential'),
    //         options,
    //         chartTittle:ref('Nishant')
    //     }
    // },
    
    data(){
        return { 
                mychartdata:data,
                myconfig:config,
                mychartTittle:chartTittle
            }
    },

   

   methods:{
    customRender(val){
        // console.log(val)
      //changing label of chart based on it
    //   this.mychartTittle=val
      
    this.myconfig.options.plugins.title.text="340B vs Non-340B by "+val
    //   console.log(val) 
    //   this.chartTittle=val
    //   console.log(this.mychartTittle)
    let path='http://127.0.0.1:5000/Chart2/'+val
     
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
    
  },

  mounted(){
        this.customRender(this.filterName)
   },

}
</script>


<style scoped>

.chart{
    width:70vw;
    height: 50vh;
    padding: 1vw
}

</style>