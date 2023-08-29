<template>
     <div class="q-pa-md">
     <!-- <q-table
        :rows= "rows"
        row-key="name"
        hide-bottom
        hide-header
        separator="cell"
        dense 
        style="border-radius:0;width:100%;height:100%">       
    
        <template v-slot:body="props">
            <q-tr 
             :props="props"            
            >                  
                <q-td 
                    v-for="col in props.cols"
                    :key="col.name"
                    :props="props"
                    dense                     
                >
                   <q-btn flat
                      round
                      :icon="props.expand ? 'remove' : 'add'"
                      @click="props.expand = !props.expand" 
                      v-if="col.value ==='Account'"
                      class="first_button"    
                   >
                      {{ col.value }}
                   </q-btn>
                   <div class="second_button" v-else>{{ col.value }}</div>
                </q-td>
            </q-tr>

            <q-tr
                v-show="props.expand"
                :props="props"
            >     
           
                <td :colspan="4">
                    <PhysicianTable />
                </td>
                     
            </q-tr>
        
        </template>
  </q-table> -->

  <q-table    
      
      separator="cell"
      dense
      hide-bottom
      hide-header
      
      :rows="rows"
      :columns="columns"      
      row-key="id"
      style="border-radius:0;width:100%;height:100%"         
      
      >

      <template v-slot:header="props">
            <q-tr :props="props">
            <q-th
                v-for="col in props.cols"
                :key="col.name"
                :props="props"
                class= "bg-grey-4"
                style="font-size:13px; font-weight:Bold;width:20%"              
            >
                <q-btn class='header_button'>{{ col.label }}</q-btn>
            </q-th>
            </q-tr>
       </template>
      
      <template v-slot:body="props">
        <q-tr :props="props">
            <!-- {{console.log(props.cols)}}   -->

          <q-td
            v-for="col in props.cols"
            :key="col.name"
            :props="props"
            style="width:20%"  
          >            
                <q-btn 
                      class="first_button"
                      v-if="col.value==='Account'"                      
                      flat                      
                      :icon="props.expand ? 'remove' : 'add'"
                      @click="props.expand = !props.expand"                     
                >
                  {{ col.value }} 
                  <!-- {{console.log(props.row.name)}} -->
                </q-btn>
                <div class="second_button" v-else>{{ col.value }}</div>

          </q-td>        

          
        </q-tr>

        <q-tr
            v-show="props.expand"
            :props="props"
        >      
  
          <q-td :colspan="4">
            
           <PhysicianTable />
          </q-td>
         
        </q-tr>
        

      </template>
           
                
     </q-table>    
  </div>
</template>


<script>
import PhysicianTable from './PhysicianTable.vue'


const columns = [
  { name: 'level',label: 'LEVEL',field:'level'},
  { name: 'Id', label: 'ID',field: 'id'},
  { name: 'Name', label: 'NAME',field: 'name'},
  { name: 'Address', label: 'ADDRESS', field: 'address'}
]

const rows = [
  { 
    level:'Account',
    id:'1',
    name:'University Of Texas Medical Branch At Galveston',
    address:'NY'
  },
  { 
    level:'Account',
    id:'2',
    name:'The University Of Texas Health Science Center At San Antonio',
    address:'NY'
  },
  {  
    level:'Account',
    id:'3',
    name:'The University Of Texas Health Science Center At Houston',
    address:'Boston'
  },
  {  
    level:'Account',
    id:'4',    
    name:'Md Anderson Neuro Oncology',
    address:'SanMateo'
  },
  {  
    level:'Account',
    id:'5',    
    name:'Ut Health East Texas Long Term Acute Care',
    address:'NY'
  }        
]

export default {
    props:['OrgName'],
    components:{PhysicianTable},
    setup(){
        return{
            rows,columns
        }
    }
}

</script>


<style scoped>
     .q-pa-md[data-v-1626b67a]{
         width:90%;
         height:50%
       }
       
       /* .q-table--dense .q-table td:first-child,.q-table--dense .q-table td,.q-table--dense .q-table td:last-child{
            white-space: nowrap; 
            overflow: hidden; 
            text-overflow: ellipsis; 
            }
         */
        .q-table--no-wrap th, .q-table--no-wrap td,.q-table--no-wrap th[data-v-04ec3b9e]{
              white-space: wrap; 
        }
       

        /* .q-pa-md{
            width: 50vw;
        } */


        .first_button{
            width: 100%; 
            padding:0; 
            margin:0; 
            border-radius:0;
            color:black;
            background-color:#dde5e7;
            height:100%;
            font-size: 1rem;
            /* display:flex;
            align-items: center;
            justify-content: center; */
            text-align: center;

            
        }
      
         .second_button{
            width: 100%; 
            padding:0; 
            margin:0; 
            border-radius:0;
            color:black;
            background-color:#dde5e7;
            height:100%;
            font-size: 1rem;
            display:flex;
            align-items: center;
            justify-content: center;
            text-align: center;

            
        }



        .inner_button{
            width: 100%; 
            padding:0; 
            margin:0;    
            border:1px;
            border-style: solid;
            border-color: lightgray;
            height:100%;
            background-color: white;
            font-weight: bold;
            font-size:1.6vh ;
            display:flex;
            align-items: center;
            justify-content: center;
        }

        .header_button{
            width: 100%; 
            padding:0; 
            margin:0; 
            border-radius:0;
            text-align:center;
            border:0;
            height:100%;
            font-weight: bold;
            font-size: 2vh;    
        }




        .q-table--dense .q-table td:first-child,.q-table--dense .q-table td,.q-table--dense .q-table td:last-child,.q-table--dense .q-table th,.q-table--dense .q-table th:first-child,.q-table--dense .q-table th:last-child{
            padding:0;
            margin:0;
            border:0;
        }

   
</style>