<template>
    <div class="q-pa-md">
        <q-select class="customFilter"
          filled 
          v-model="model"           
          :options="options"
          stack-label         
          label="Select Filter"
        />
        {{ customRender(model)}}
    </div>
</template>

<script>
import {ref} from 'vue';

const options= ['Potential','% Diagnosis Pats','% Treated Pats','Product A Sales','Product B Sales' ]
const model= ref('Potential')

export default {
    data(){
        return{
            options,model
        }
    },
    emits:['custom-filter'],
    methods:{
       customRender(val){
          this.$emit('custom-filter',val)
       }     
    }
}
</script>
<style scoped>
.customFilter{
    width: 15vw;
    
}

</style>