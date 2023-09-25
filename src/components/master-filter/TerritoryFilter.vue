<template> 
    <!-- @filter= "filterFn"   -->
    {{ dataToParent(model)}}

    <div >
      <q-select
      class="filter2"
        :disable="isStateSelected"
        filled
        v-model="model"
        use-chips
        multiple        
        :options="computedoption"
        label="Select Territory"        
        label-color="white"        
        
        
      >
      
        <template v-slot:no-option>
          <q-item>
            <q-item-section class="text-grey">
              No results
            </q-item-section>
          </q-item>
        </template>      

      </q-select>
    </div>
</template>

<script>
import { ref} from 'vue'
// import vue from '@vitejs/plugin-vue'

const territory= []
// const temp=ref(territory)
// const options = ref(l)
// const state=ref(l)

export default {
  props:['isStateSelected','stateFilter'],

  data () {
    // const options = ref(stringOptions)
    return {
      model: ref(null),
      territory,
      // state:l
      // terr,
      // options,
      
      // labelName

  }},

  methods:{    
    terr(){
        this.territory=[]  
        // console.log("state selected",this.stateFilter)      
        let path='http://127.0.0.1:5000/master-filter/Territory'
                
        fetch(path,{
          method:'POST',
          headers:{'Content-Type':'application/json'},
          body:JSON.stringify({state:this.stateFilter})
        })
        .then((response)=>{
            if(response.ok){
                return(response.json())
            }
            else{
              throw new Error("Something went wrong the server")
            } 
        })
        .then((data)=>{
            // console.log("territory",data)  
            for (let i=0;i<data.output.length;i++){
              //  console.log(data.output[i])
              this.territory.push(data.output[i][0])
          }
          //update computed property to trigger reactivity
          // console.log("final l value",this.territory)
          this.territory=[...this.territory]   
        }) 
        .catch((err)=>{
          console.log(err)
          console.log(err.message)
        })
    },
        
    

    // filterFn (val, update) {    
    //     update(() => {
    //       const needle = val.toLowerCase()
    //       options.value = terr.filter(v => v.toLowerCase().indexOf(needle) > -1)
    //       this.territory= temp.value.filter(v => v.toLowerCase().indexOf(needle) > -1)
    //       console.log(options)
    //     })
    //   },

      dataToParent(s){
         //returns list of arrays 
        //  console.log(s)
        if(s!==null){
          this.$emit('territory-filter',s)

      }}
    
  },
  
  computed:{
    computedoption(){
      // console.log("computed",this.territory)
      return this.territory
    },

  },

  watch:{
      stateFilter(newValue,oldValue){    
        //component should be enabled and new value should be selected from state filter    
          if (!this.isStateSelected && newValue!=oldValue) {
            this.terr()
        }
      }
  },
  
  emits:['territory-filter'],

 
}  


</script>
<style scoped>
.filter2{
   width: 20vw;
  background-color:#00a3e0;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0 3vw ;
  margin-left: 1vw;
  border-radius: 0.5vw ;
}
.text-grey{
  width: 5000px;
}
</style>