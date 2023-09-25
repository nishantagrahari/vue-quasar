<template> 

    {{ dataToParent(model)}}

    
      <q-select
        class=" filter1"
        
        v-model="model"
        use-input
        use-chips
        multiple        
        :options="options"
        label="Select State"        
        label-color="white"    
        option-class="custom-option-css"    
      
        @filter= "filterFn" 
          
      >
      
        <template v-slot:no-option >
          <q-item>
            <q-item-section class="text-grey">
              No results
            </q-item-section>
          </q-item>
        </template>      

      </q-select>
 
</template>

<script>
import { ref } from 'vue'
// import vue from '@vitejs/plugin-vue'

const state = []
const options = ref(state)

export default {
  // props:['labelName','filterName'],

  data () {
    // const options = ref(stringOptions)
    return {
      model: ref(null),
      state,
      options,
      // labelName

  }},

  mounted(){
    
    let path='http://127.0.0.1:5000/master-filter/state'
    // let mapped=''
     
    fetch(path)
    .then((response)=>{
        if(response.ok){
            return(response.json())
        }      
    
    })
    .then((data)=>{  
      // this.state=data.output
      console.log(data.output)
      for (let i=0;i<data.output.length;i++){
          //  console.log(data.output[i])
           this.state.push(data.output[i][0])
      }
      //  this.mapped=this.state.map(x=>x)
      //  console.log(this.state)
      //  this.state.map((item)=>{
      //    console.log(item)
      //  })

      //  this.state.filter(function(item){
      //    console.log(item)
      //  })
     
    }) 
    .catch((err)=>{
      console.log(err)
    })
  },

  
  emits:['state-filter'],

  methods:{
       filterFn (val, update) {    
        update(() => {
          const needle = val.toLowerCase()
          options.value = state.filter(v => v.toLowerCase().indexOf(needle) > -1)
        //   console.log(options)
        })
      },

      dataToParent(s){
         //returns list of arrays 
        if(s!==null){
          this.$emit('state-filter',s)


      }
    }}



}  


</script>
<style scoped>

.filter1{
  width: 20vw;
  background-color:#00a3e0;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0 3vw ;
  margin-right: 1vw ;
  border-radius: 0.5vw;
  
}


</style>