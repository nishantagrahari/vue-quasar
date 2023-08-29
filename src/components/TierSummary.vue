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
            style="font-size:13px; font-weight:Bold "              
          >
            <q-btn class='header_button'>{{ col.label }}</q-btn>
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
                   class="parent_button" 
            >
              <q-btn size="sm" color="black" class="header_row"  round dense @click="props.expand=!props.expand" :icon="props.expand ? 'remove' : 'add'" />{{ col.value }}
            </q-btn>

            <q-btn 
                   v-else
                   class="parent_button"
            >              
              {{ col.value }}
            </q-btn>
          </q-td>
        </q-tr> 
        


        <!-- On expanding props  -->
        <q-tr v-show="props.expand" :props="props" > 
           <!-- <pre>{{props}}</pre>           -->        
          <template v-if= "props.row.sub">          
                               
                <q-td><div class="inner_button" >{{props.row.sub[0]}}</div></q-td>
                <q-td><div class='inner_button' :style="{width: (props.row.sub[1]/props.row.orgs)*100 + '%'}" style="background-color:#99DBF5">{{props.row.sub[1]}}</div></q-td>
                <q-td><div class='inner_button' :style="{width: (props.row.sub[2]/props.row.accounts)*100  + '%'}" style="background-color:#99DBF5">{{props.row.sub[2]}}</div></q-td>
                <q-td><div class='inner_button' :style="{width: (props.row.sub[3]/props.row.hcps)*100 + '%'}" style="background-color:#99DBF5">{{props.row.sub[3]}}</div></q-td>
                <q-td><div class='inner_button' :style="{width: (props.row.sub[4]/props.row.sales)*100 + '%'}" style="background-color:#99DBF5">{{props.row.sub[4]}}</div></q-td>
                <q-td><div class='inner_button' >{{props.row.sub[5]}}</div></q-td>
                
          </template>   
        
        </q-tr>

         <q-tr v-show="props.expand" :props="props" >  
            <template v-if= "props.row.sub2">          
              
                <q-td><div class="inner_button" >{{props.row.sub2[0]}}</div></q-td>
                <q-td><div class='inner_button' :style="{width: (props.row.sub2[1]/props.row.orgs)*100 + '%'}" style="background-color:#99DBF5">{{props.row.sub2[1]}}</div></q-td>
                <q-td><div class='inner_button' :style="{width: (props.row.sub2[2]/props.row.accounts)*100  + '%'}" style="background-color:#99DBF5">{{props.row.sub2[2]}}</div></q-td>
                <q-td><div class='inner_button' :style="{width: (props.row.sub2[3]/props.row.hcps)*100 + '%'}" style="background-color:#99DBF5">{{props.row.sub2[3]}}</div></q-td>
                <q-td><div class='inner_button' :style="{width: (props.row.sub2[4]/props.row.sales)*100 + '%'}" style="background-color:#99DBF5">{{props.row.sub2[4]}}</div></q-td>
                <q-td><div class='inner_button' >{{props.row.sub2[5]}}</div></q-td>
                
          </template>   
         </q-tr> 



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
    sub:['D10',40,100,50,9000,'29%'],
    sub2:['D11',45,110,40,2000,'34%'],
    sub3:['D12',45,12,70,3000,'20%']
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
    sub:['D13',100,110,600,5000,'10%'],
    sub2:['D14',120,150,500,2000,'64%']
  }
  

]




export default {
 
  setup () {
    return {
      columns,
      rows    
    }
  },
  
  methods:{
    click(){
        console.log("nishant")
    },
    button_clicked(){
      console.log("Button clicked")
    },
    
  }
};
</script>


<style scoped>
  h1{
      font-size: 1vh;
  }

  .q-pa-md{
      width: 50vw;
  }


  .parent_button{
      width: 100%; 
      padding:0; 
      margin:0; 
      border-radius:0;
      color:white;
      background-color: #19A7CE;
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