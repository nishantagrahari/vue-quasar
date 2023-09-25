<template>
  <!-- <q-page class="flex flex-center"> -->
    <!-- <div class="q-pa-md" style="width: 50vw"> -->
     <div class="q-gutter-y-md column" style="max-width: 300px; padding:1vw">
        <q-select 
          filled 
          v-model="model"           
          :options="options"
          stack-label
          options-cover 
          label="Select Filter"
                 
        >
         
          <!-- <template v-slot:selected>
            {{ customRender(model) }}
          </template> -->
          <!-- <pre>{{console.log(model.opt)}}</pre> -->
          <!-- <template v-slot:selected-item="model">
            
          </template> -->

        </q-select>  <pre>{{ customRender(model) }}</pre>

        <!-- equivalent -->
        <!-- <q-select color="orange" filled v-model="model" :options="options" label="Label">
          <template v-if="model" v-slot:append>
            <q-icon name="cancel" @click.stop.prevent="model = null" class="cursor-pointer" />
          </template>
        </q-select> -->
    </div>
  <!-- </div> -->
  <!-- </q-page> -->
</template>


<script>
import { ref } from 'vue'

const options= ['Google', 'Facebook', 'Twitter', 'Apple', 'Oracle' ]

export default {
  setup () {
    return {
      //default label
      model: ref('Nishant'),
      options,
  }},

  methods:{
    customRender(val){
      console.log(val)
    }
  }}

 
  
</script>



