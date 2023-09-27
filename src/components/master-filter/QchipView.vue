<template>
    <template v-for="(selection,i) in stateToChip" :key="selection" >      
        <q-chip            
            removable
            outline                         
            color="primary" 
            text-color="white"
            @remove="removechip(selection,i)"
        >{{selection}}</q-chip>
    </template>   
</template>

<script>
const stateToChip=[]

export default {
    props:['stateFilter'],

    data(){
        return {stateToChip}
    },
    emits:['state-chip'],
    methods:{
        updateChip(type,item){
            if(item!== null && !this.stateToChip.includes(item)){                    
                this.stateToChip.push(item)
                this.$emit('state-chip',this.stateToChip)                    
            }
        },
    
        removechip(item,index){
            this.stateToChip.splice(index,1)
            this.$emit('state-chip',this.stateToChip)            
        }},
    

    watch:{
        stateFilter(newValue,oldValue){
        //recives different value of state      
          if( JSON.stringify(newValue)!== JSON.stringify(oldValue)){  
            //Reloading parent and inner_row          
            this.updateChip('state',newValue);        
          }
        },    
    },
}
</script>