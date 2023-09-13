
<template>
  <!-- <AccountTable2 /> -->
 
  <div class="q-pa-md">
    <!-- <div class= "scrollable-container"> -->
    <!-- <scrollable-table :rows="rows" :columns="fixedColumn" @scroll="handleScroll" />   -->
    
    <q-table    
      
      
      class="my-sticky-header-table"
      separator="cell"
      dense
      :rows="rows"
      :columns="columns"
      row-key="id"
      style="border-radius:0;width:100%;height:100%; overflow-x: auto;" 
      flat bordered
      virtual-scroll     
      v-model:pagination="pagination"
      :rows-per-page-options="[0]"      
      
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
            <!-- {{console.log(props)}} -->
        <q-tr :props="props">
            <!-- {{console.log(props.cols)}}   -->

          <q-td
            v-for="col in props.cols"
            :key="col.name"
            :props="props"
          >            
                <q-btn 
                      class="first_button"
                      v-if="col.value==='Org'"                      
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
              v-if="props.expand"
              :props="props"            
          >   
              <q-td 
                :colspan="4"
              >                
                <AccountTable               
                    :org-name="props.row.name"
                    :key="props.row.name"
                />
            </q-td>
         
          </q-tr>
    
      </template>
       
        
    </q-table>
    <!-- </div> -->
    
  </div>
 
</template>


<script>
import AccountTable from './AccountTable.vue'
// import ScrollableTable from './ScrollableTable.vue';
// import VueScrollingTable from "vue-scrolling-table"
import "/node_modules/vue-scrolling-table/dist/style.css"

import { ref } from 'vue'



const columns = [
  { name: 'level',label: 'LEVEL',field:'level',frozen:true,style:'width:40 px'},
  { name: 'Id', label: 'ID',field: 'id',frozen:true,style:'width:40 px'},
  { name: 'Name', label: 'NAME',field: 'name',style:'width:40 px'},
  { name: 'Address', label: 'ADDRESS', field: 'address',style:'width:40 px'},
  { name: 'Address', label: 'ADDRESS', field: 'address',style:'width:40 px'},
  { name: 'Address', label: 'ADDRESS', field: 'address',style:'width:40 px'},
  { name: 'Address', label: 'ADDRESS', field: 'address',style:'width:40 px'},
  { name: 'Address', label: 'ADDRESS', field: 'address',style:'width:40 px'},
  { name: 'Address', label: 'ADDRESS', field: 'address',style:'width:40 px'},
  { name: 'Address', label: 'ADDRESS', field: 'address',style:'width:40 px'},
  { name: 'Address', label: 'ADDRESS', field: 'address',style:'width:40 px'},
  { name: 'Address', label: 'ADDRESS', field: 'address',style:'width:40 px'},
  { name: 'Address', label: 'ADDRESS', field: 'address',style:'width:40 px'},
  { name: 'Address', label: 'ADDRESS', field: 'address',style:'width:40 px'},
  { name: 'Address', label: 'ADDRESS', field: 'address',style:'width:40 px'},
  { name: 'Address', label: 'ADDRESS', field: 'address',style:'width:40 px'},
  { name: 'Address', label: 'ADDRESS', field: 'address',style:'width:40 px'},
  { name: 'Address', label: 'ADDRESS', field: 'address',style:'width:40 px'},
  { name: 'Address', label: 'ADDRESS', field: 'address',style:'width:40 px'},
  { name: 'Address', label: 'ADDRESS', field: 'address',style:'width:40 px'},
  { name: 'Address', label: 'ADDRESS', field: 'address',style:'width:40 px'},
  { name: 'Address', label: 'ADDRESS', field: 'address',style:'width:40 px'},

      
]

const fixedColumn=[{ name: 'level',label: 'LEVEL',field:'level',frozen:true,style:'width:40 px'}]

const rows = [
  {  
    id:'1',
    level:'Org',
    name:'Mayoclinic',
    address:'NY',
    account:['A1','A2','A3']
  },
  {  
    id:'2',
    level:'Org',
    name:'Mass General Brigham',
    address:'NY'
  },
  {  
    id:'3',
    level:'Org',
    name:'Kaiser Permanente',
    address:'Boston'
  },
  {  
    id:'4',
    level:'Org',
    name:'Mass General',
    address:'SanMateo'
  },
  {  
    id:'5',
    level:'Org',
    name:'University Of California Health',
    address:'NY'
  }        
]




export default {
 
  setup () {
    return {
      columns,
      rows,fixedColumn,
      pagination: ref({
        rowsPerPage: 4
      })
    }
  },
  
  components:{AccountTable},

}
</script>


<style scoped>
       .q-pa-md[data-v-1626b67a]{
         width:70%;
         height:70%
       }
       
       .q-table--no-wrap th, .q-table--no-wrap td,.q-table--no-wrap th[data-v-04ec3b9e]{
          white-space: wrap; 
        }      
        

        .first_button{
            width: 100%; 
            padding:0; 
            margin:0; 
            border-radius:0;
            color:white;
            background-color: #19A7CE;
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
            color:white;
            background-color: #19A7CE;
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

         /* ----------For implementing sticky header in the top of table */
        .my-sticky-header-table {
            height: 100%;
            width:100%;
            /* background-color: red; */
          }

        /* .my-sticky-header-table .q-table__top,
        .my-sticky-header-table .q-table__bottom,
        .my-sticky-header-table thead tr:first-child th {
          background-color: #00b4ff;
        } */

        .my-sticky-header-table thead tr th {
          position: sticky;
          z-index: 2;
          top: 0;
        }

        /* .my-sticky-header-table thead tr:first-child th {
          
        } */

        /* .my-sticky-header-table.q-table--loading thead tr:last-child th {
          top: 48px;
        } */

        /* .my-sticky-header-table tbody {
          scroll-margin-top: 48px;
        }
         */
        /*------------------ for implementing column table------------------   */
        /* .my-sticky-header-table {
          max-width: 600px;
        }

        .my-sticky-header-table thead tr:first-child th:first-child {
          background-color: #00b4ff;
        }

        .my-sticky-header-table td:first-child {
          background-color: #00b4ff;
        }*/

        /* .my-sticky-header-table td:first-child, */
        .my-sticky-header-table th:first-child {
          position: sticky;
          left: 0;
          z-index: 3;
        }


        .my-sticky-header-table td:first-child {
          position: sticky;
          left: 0;
          z-index: 1;
        }  
        
        /* .my-sticky-header-table th:first-child{
          left:0
        } */
        
        

        /* .my-sticky-column-table{ */
          /* specifying max-width so the example can */
            /* highlight the sticky column on any browser window */ 
          /* max-width: 600px}  */


        /* thead tr:first-child th:first-child { */
          /* bg color is important for th; just specify one */
          /* background-color: #00b4ff} */

        /* td:first-child{ */
          /* background-color: #00b4ff} */

        /* th:first-child,
        td:first-child{
          position: sticky;
          left: 0;
          z-index: 1
        } */

</style>


