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
              <q-btn size="sm" color="black" class="header_row"  round dense @click="props.expand=!props.expand;loadInnerRow(props.row,props)" :icon="props.expand ? 'remove' : 'add'" />{{ col.value }}
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
        <q-tr v-show="props.expand" v-if= "props.row.sub" :props="props" > 
           <!-- <pre>{{props}}</pre>           -->        
          <!-- <template v-if= "props.row.sub">           -->
                               
                <q-td><div class="inner_button" >{{props.row.sub[0]}}</div></q-td>
                <q-td><div class='inner_button' :style="{width: (props.row.sub[1]/props.row.orgs)*100 + '%'}" style="background-color:#99DBF5">{{props.row.sub[1]}}</div></q-td>
                <q-td><div class='inner_button' :style="{width: (props.row.sub[2]/props.row.accounts)*100  + '%'}" style="background-color:#99DBF5">{{props.row.sub[2]}}</div></q-td>
                <q-td><div class='inner_button' :style="{width: (props.row.sub[3]/props.row.hcps)*100 + '%'}" style="background-color:#99DBF5">{{props.row.sub[3]}}</div></q-td>
                <q-td><div class='inner_button' :style="{width: (props.row.sub[4]/props.row.sales)*100 + '%'}" style="background-color:#99DBF5">{{props.row.sub[4]}}</div></q-td>
                <q-td><div class='inner_button' >{{props.row.sub[5]}}</div></q-td>
                
          <!-- </template>    -->
        
        </q-tr>

         <q-tr v-show="props.expand" v-if= "props.row.sub2" :props="props" >  
            <!-- <template v-if= "props.row.sub2">          -->
              
                <q-td><div class="inner_button" >{{props.row.sub2[0]}}</div></q-td>
                <q-td><div class='inner_button' :style="{width: (props.row.sub2[1]/props.row.orgs)*100 + '%'}" style="background-color:#99DBF5">{{props.row.sub2[1]}}</div></q-td>
                <q-td><div class='inner_button' :style="{width: (props.row.sub2[2]/props.row.accounts)*100  + '%'}" style="background-color:#99DBF5">{{props.row.sub2[2]}}</div></q-td>
                <q-td><div class='inner_button' :style="{width: (props.row.sub2[3]/props.row.hcps)*100 + '%'}" style="background-color:#99DBF5">{{props.row.sub2[3]}}</div></q-td>
                <q-td><div class='inner_button' :style="{width: (props.row.sub2[4]/props.row.sales)*100 + '%'}" style="background-color:#99DBF5">{{props.row.sub2[4]}}</div></q-td>
                <q-td><div class='inner_button' >{{props.row.sub2[5]}}</div></q-td>
                
          <!-- </template>    -->
         </q-tr> 


         <q-tr v-show="props.expand" v-if= "props.row.sub3" :props="props" >  
            <!-- <template v-if= "props.row.sub3">          -->
              
                <q-td><div class="inner_button" >{{props.row.sub3[0]}}</div></q-td>
                <q-td><div class='inner_button' :style="{width: (props.row.sub3[1]/props.row.orgs)*100 + '%'}" style="background-color:#99DBF5">{{props.row.sub3[1]}}</div></q-td>
                <q-td><div class='inner_button' :style="{width: (props.row.sub3[2]/props.row.accounts)*100  + '%'}" style="background-color:#99DBF5">{{props.row.sub3[2]}}</div></q-td>
                <q-td><div class='inner_button' :style="{width: (props.row.sub3[3]/props.row.hcps)*100 + '%'}" style="background-color:#99DBF5">{{props.row.sub3[3]}}</div></q-td>
                <q-td><div class='inner_button' :style="{width: (props.row.sub3[4]/props.row.sales)*100 + '%'}" style="background-color:#99DBF5">{{props.row.sub3[4]}}</div></q-td>
                <q-td><div class='inner_button' >{{props.row.sub3[5]}}</div></q-td>
                
          <!-- </template>    -->
         </q-tr> 

         <q-tr v-show="props.expand" v-if= "props.row.sub4" :props="props" >  
            <!-- <template v-if= "props.row.sub4">          -->
              
                <q-td><div class="inner_button" >{{props.row.sub4[0]}}</div></q-td>
                <q-td><div class='inner_button' :style="{width: (props.row.sub4[1]/props.row.orgs)*100 + '%'}" style="background-color:#99DBF5">{{props.row.sub4[1]}}</div></q-td>
                <q-td><div class='inner_button' :style="{width: (props.row.sub4[2]/props.row.accounts)*100  + '%'}" style="background-color:#99DBF5">{{props.row.sub4[2]}}</div></q-td>
                <q-td><div class='inner_button' :style="{width: (props.row.sub4[3]/props.row.hcps)*100 + '%'}" style="background-color:#99DBF5">{{props.row.sub4[3]}}</div></q-td>
                <q-td><div class='inner_button' :style="{width: (props.row.sub4[4]/props.row.sales)*100 + '%'}" style="background-color:#99DBF5">{{props.row.sub4[4]}}</div></q-td>
                <q-td><div class='inner_button' >{{props.row.sub4[5]}}</div></q-td>
                
          <!-- </template>    -->
         </q-tr> 


      </template>
    </q-table>
  </div>
</template>

<script>
// import axios from 'axios'
import {ref} from 'vue';

const columns = [
  {
    name: 'Tier',
    label: 'Tier',
    align: 'left',
    field:'Tier',
    // format: val => `${val}`
  },
  { name: '#Orgs', align: 'center', label: '#Orgs', field: 'orgs'},
  { name: '#Accounts', label: '#Accounts', field: 'accounts'},
  { name: '#HCPs', label: '#HCPs', field: 'hcps'},
  { name: 'Product sales', label: 'Product sales', field: 'sales'},
  { name: '%Potential', label: '%Potential', field: 'potential'}  
]

const rows = ref([
    {  
      id:'1',
      Tier:'H',
      name: 'nishant',
      orgs: 45,
      accounts: 150,
      hcps: 340,
      sales: 15635,
      potential: '29%'
      // sub:['D10',40,100,100,9000,'29%'],
      // sub2:['D9',45,110,150,2000,'34%'],
      // sub3:['D8',45,12,200,3000,'20%']
    },
    {  
      id:'2',
      Tier:'M',
      name: 'nishant',
      orgs: 185,
      accounts: 548,
      hcps: 870,
      sales: 6750,
      potential: '40%'
      // sub:['D7',100,110,600,5000,'10%'],
      // sub2:['D6',120,150,500,2000,'64%'],
      // sub3:['D5',120,150,500,2000,'64%']
    },
    {  
      id:'3',
      Tier:'L',
      name: 'nishant',
      orgs: 185,
      accounts: 548,
      hcps: 870,
      sales: 6750,
      potential: '40%'
      // sub:['D4',100,110,600,5000,'10%'],
      // sub2:['D3',120,150,500,2000,'64%'],
      // sub3:['D2',120,150,500,2000,'64%'],
      // sub4:['D1',120,150,500,2000,'64%']
    }    
  ])




export default {
 
  setup () { 
    
    return {
      columns:columns,
      rows:rows
      // rows:rows    
    }
  },
  
  methods:{    
    loadInnerRow(rows,prop){    
      // console.log(rows)
      
          let path="http://127.0.0.1:5000/Medium/"+rows.Tier
          // console.log(path)
          fetch(path)
          .then((response)=>{
              if(response.ok){
                  return(response.json())
              }     
          })
          .then((data)=>{       
            // console.log(data)
            // Insertion and deletion of rows
            if(rows.Tier == "H"){                 
                  if(prop.expand){
                    this.rows[0].sub = data.output[0]
                    this.rows[0].sub2 =data.output[1]
                    this.rows[0].sub3 =data.output[2]
                  }else{                    
                    delete this.rows[0].sub
                    delete this.rows[0].sub2
                    delete this.rows[0].sub3
                  }
                  
            }else if (rows.Tier == "M"){
                  if(prop.expand){
                    this.rows[1].sub = data.output[0]
                    this.rows[1].sub2 =data.output[1]
                    this.rows[1].sub3 =data.output[2]
                  }else{
                    delete this.rows[1].sub
                    delete this.rows[1].sub2
                    delete this.rows[1].sub3
                  }
                  
            }else if(rows.Tier == "L"){
                  if(prop.expand){
                    this.rows[2].sub = data.output[0]
                    this.rows[2].sub2 =data.output[1]
                    this.rows[2].sub3 =data.output[2]
                    this.rows[2].sub4 =data.output[3]
                  }else{
                    delete this.rows[2].sub
                    delete this.rows[2].sub2
                    delete this.rows[2].sub3
                    delete this.rows[2].sub4
                  }
                  
            }
           
          }) 
          .catch((err)=>{
            console.log(err)
          })
      
      }
     

  },

  mounted(){
      let path='http://127.0.0.1:5000/'
     
      fetch(path)
      .then((response)=>{
          if(response.ok){
              return(response.json())
          }      
     
      })
      .then((data)=>{        
        for (let i=0;i<3;i++){          
            this.rows[i].orgs= data.output[i][1]
            this.rows[i].accounts=data.output[i][2]
            this.rows[i].hcps=data.output[i][3]
            this.rows[i].sales= data.output[i][4]
            }
      }) 
      .catch((err)=>{
        console.log(err)
      })

  },

};

</script>


<style scoped>
  h1{
      font-size: 1vh;
  }

  .q-pa-md{
      width: 70vw;
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