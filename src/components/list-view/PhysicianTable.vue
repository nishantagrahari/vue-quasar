<template>
     <q-table
        separator="cell"
        dense
        hide-bottom
        hide-header        
        :rows="filtered_physician"
        :columns="columns"      
        row-key="id"
        style="border-radius:0;width:100%;height:100%"  
    > 
    
        <template v-slot:body="props">
            <q-tr 
             :props="props"            
            >                  
                <q-td 
                    v-for="col in props.cols"
                    :key="col.name"
                    :props="props"
                    dense
                    style="width:20%"  
                >                   
                      <div class="first_button" v-if="col.value ==='PHYSICIAN'">{{ col.value }}</div>
                      <div class="second_button" v-else>{{ col.value }}</div>                  
                </q-td>
            </q-tr>
        
        </template>
  </q-table>
</template>





<script>

const columns = [
  { name: 'level',label: 'LEVEL',field:'level'},
  { name: 'Id', label: 'ID',field: 'id'},
  { name: 'Name', label: 'NAME',field: 'name'},
  { name: 'Address', label: 'ADDRESS', field: 'address'}
]




const rows = [
    [
        { 
            level:'PHYSICIAN',
            id:'1',
            name:'Howard Lewis',
            address:'NY'
        },
        { 
            level:'PHYSICIAN',
            id:'2',
            name:'Neil Chandrabhan Chevli',
            address:'NY'
        }
        
    ],
    [
         {  
            level:'PHYSICIAN',
            id:'3',    
            name:'Lee Roy Wiederhold',
            address:'Boston'
        },
        {  
            level:'PHYSICIAN',
            id:'4',    
            name:'Todd Allen Swanson',
            address:'SanMateo'
        }
             
    ],
    [
        {  
            level:'PHYSICIAN',
            id:'5',    
            name:'Nishant Agrahari',
            address:'NY'
        }    
    ]
]


export default {

    props:['phyName'],

    computed: {
        filtered_physician(){
            console.log(this.phyName)

            if(this.phyName == "The University Of Texas Health Science Center At San Antonio"){               
                return rows[0];
            }else if (this.phyName == "Md Anderson Neuro Oncology"){
                return rows[1];
            }else{
                return rows[2];
            }   
    }},    

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
            height:80%
        }
        
        .q-table--no-wrap th, .q-table--no-wrap td,.q-table--no-wrap th[data-v-04ec3b9e]{
            white-space: wrap; 
        }

      
         .first_button{
            width: 100%; 
            padding:0; 
            margin:0; 
            border-radius:0;
            color:black;
            background-color:white;
            height:100%;
            font-size: 0.8rem;
            display:flex;
            align-items: center;
            justify-content: right;
            text-align: right;

            
        }

        .second_button{
            width: 100%; 
            padding:0; 
            margin:0; 
            border-radius:0;
            color:black;
            background-color:white;
            height:100%;
            font-size: 0.8rem;
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