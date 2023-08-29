<template>
  <div class="q-pa-md">
    <q-table    
      
      hide-bottom
      separator="cell"
      dense
      :rows="rows"
      :columns="columns"
      row-key="id"
      style="border-radius:0;"
      >

      <template v-slot:header="props">
        <q-tr :props="props">
          <q-th
            v-for="col in props.cols"
            :key="col.name"
            :props="props"
            class= "bg-grey-4"
            style="font-size:13px;  font-weight:Bold "              
          >
            {{ col.label }}
          </q-th>
        </q-tr>
      </template>
      
      <template v-slot:body="props">
        <q-tr :props="props">          
          <q-td
            v-for="col in props.cols"
            :key="col.name"
            :props="props"
          >
            
            <q-btn 
                   v-if="col.name ==='Tier'"
                   style="width: 100%; padding:0; margin:0; border-radius:0;color:white" class= "bg-blue-4"
            >
              <q-btn size="sm" color="black" class="header_row" ref="H1" round dense @click="props.expand=!props.expand" :icon="props.expand ? 'remove' : 'add'" />{{ col.value }}
            </q-btn>

            <q-btn 
                   v-else
                   style="width: 100%; padding:0; margin:0; border-radius:0;color:white" class= "bg-blue-4"
            >              
              {{ col.value }}
            </q-btn>


          </q-td>
        </q-tr> 
        
          
        <q-tr v-show="props.expand" :props="props" > 
           <!-- <pre>{{props}}</pre>           -->        
          <template v-if= "props.row.sub">          
              <q-td              
                 v-for = "sub_col in props.row.sub"                              
                 :key="sub_col" >
                <!-- <pre>{{props}}</pre> -->
                <q-btn  v-if="props.row.sub[0]===sub_col" class='inner_button'>
                  
                   <q-btn size="sm" color="black" @click="props.expand2=!props.expand2"  round dense  :icon="props.expand2 ? 'remove' : 'add'"  />
                    {{sub_col}}
                   </q-btn>
               
                <q-btn  v-else class='inner_button' >{{sub_col}}</q-btn>  
              </q-td>          
          </template>
         </q-tr>   


          <!-- <pre>{{props}}</pre>           -->
        
          <!-- <q-td 
            style="padding:0;margin:0;border:0;"> -->

            
            <!-- <template :body="props">
              <q-btn :body="props" size="sm" color="black" round dense @click="props.expand = !props.expand" :icon="props.expand ? 'add' : 'remove'" />{{"D10"}} 
             -->

            <!-- <q-tr v-show="props.expand" :props="props">
              <q-td>H</q-td>
              <q-td>40</q-td>
              <q-td>10</q-td>
            </q-tr>
               -->
            <!-- </template> -->
          <!-- </q-td> -->
          <!-- <q-td
            style="padding:0;margin:0;border:0;" >
            <q-btn class='inner_button' >
              <template v-if="props.row.sub">
                {{props.row.sub[1]}}
              </template>
            </q-btn> -->
          <!-- </q-td> -->
          <!-- <q-td
          style="padding:0;margin:0;border:0;">
            <q-btn class='inner_button'>
              {{ 10}}   
            </q-btn>
          </q-td>
          <q-td
          style="padding:0;margin:0;border:0;">
            <q-btn class='inner_button'>
              {{5}}   
            </q-btn>
          </q-td>
          <q-td
          style="padding:0;margin:0;border:0;">
            <q-btn class='inner_button'>
              {{ 4000}}   
            </q-btn>
          </q-td>
          <q-td
          style="padding:0;margin:0;border:0;">
            <q-btn class='inner_button'>
              {{'2%'}}   
            </q-btn>
          </q-td>
          
             -->
          
            <!-- <pre>{{props}}</pre> -->
            
          
      

            <!-- <q-tr v-show="props.expand2" :props="props">
              <q-td colspan="100%">
                  <div >nishant</div>  
                </q-td>  
            </q-tr>
            -->




      </template>
    </q-table>
  </div>
</template>

<script>
const columns = [
  {
    name: 'Tier',
    label: 'Tier',
    align: 'left',
    field:'Tier',
    format: val => `${val}`
  },
  { name: '#Orgs', align: 'center', label: '#Orgs', field: 'orgs'},
  { name: '#Accounts', label: '#Accounts', field: 'accounts'},
  { name: '#HCPs', label: '#HCPs', field: 'hcps'},
  { name: 'Product sales', label: 'Product sales', field: 'sales'},
  { name: '%Potential', label: '%Potential', field: 'potential'}  
]

const rows = [
  {  
    id:'1',
    Tier:'H',
    name: 'nishant',
    orgs: 45,
    accounts: 150,
    hcps: 340,
    sales: 15635,
    potential: '29%',
    sub:['D10',5,10,5,4000,'29%']
  },
  {  
    id:'2',
    Tier:'M',
    name: 'nishant',
    orgs: 185,
    accounts: 548,
    hcps: 870,
    sales: 6750,
    potential: '40%',
    sub:['D11',6,11,6,5000,'40%']
  }
]

function ontoggle(){
  // console.log(document.querySelector(".inner_button"))
  console.log("nishant")
}


export default {
  setup () {
    return {
      columns,
      rows,
      ontoggle      
    }
  },
  
  methods:{
    click(){
        console.log("nishant")
    },
    button_clicked(){
      console.log("Button clicked")
    }

  }
};
</script>
