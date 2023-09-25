<template>
  <div class='container'>
    <h3><center>Profile view</center></h3>
    
    <div class='inner-container'>
        <blocks-tree 
            :props="{label: 'label', expand: 'expand', children: 'children',  key:'some_id'}" 
            :data="treeData" :horizontal="treeOrientation=='0'" 
            :collapsable="true">

             <template #node="{data,context}">
                <div class='updated_node' :style="{background:changeBackground(data.id_name,context.isExpanded()), color:changeFontColor(context.isExpanded())}">
                    
                    <span>{{data.label}}</span>
                    <span v-if="data.children && data.children.length">
                        <i class="bi bi-box-arrow-up-right acc-tab-icon" id="arrow" :style="{color:changeColor(context.isExpanded())}"></i>
                    </span>
                </div>
                
            </template>
            
        </blocks-tree>
    </div>
    
  </div>    
</template>

<script>
import {reactive,ref } from 'vue';

export default {

    setup() {
        // let inputLeafId = ref();
        let iconColor="Red"
        // let selected = ref([]);
        let treeOrientation = ref("0");
        let treeData = reactive({
            label: 'Mayoclinic health system',
            expand: false,
            some_id: 1,
            id_name:"Org",
            children: [
                { label: 'Mayoclinic college of medicine and science', some_id: 2,id_name:"Account"},
                { label: 'Mayoclinic radiation Oncology', some_id: 3,id_name:"Account"},
                { label: 'Mayoclinic internal Medicine', some_id: 4,id_name:"Account"},
                { label: 'Mayoclinic health system in Mankato', some_id: 5,id_name:"Account"},
                { label: 'Mayoclinic Hospital', some_id: 6,id_name:"Account"},
                { label: 'Charter House', some_id: 7,id_name:"Account"},
                { 
                    label: 'Mayoclinic college of Continous Professional development', 
                    some_id: 8, 
                    expand: false,
                    id_name:"Account" ,
                    children: [
                        // { label: 'subchild 1', some_id: 5 },
                        {  
                            label: 'Anita Maharjan', 
                            some_id: 9,
                            id_name:"Physician"
                        
                        },
                         {  
                            label: 'Wei Ding', 
                            some_id: 10,
                            id_name:"Physician"
                           
                        },
                         {  
                            label: 'Charles Ding', 
                            some_id: 11,
                            id_name:"Physician"
                            
                        },
                        {  
                            label: 'Hope', 
                            some_id: 12,
                            id_name:"Physician"
                            
                        }
                    ]
                },
                // { label: 'child 7', some_id: 8, },
                { 
                    label: 'Mayoclinic', 
                    some_id: 13, 
                    expand: false,
                    id_name:"Account", 
                    children: [
                        // { label: 'subchild 1', some_id: 5 },
                        {  
                            label: 'Daniel Walden', 
                            some_id: 14,
                            id_name:"Physician"                            
                            
                        }
                    ]
                }, 

            ]
        });

       

        return {
            treeData,
            treeOrientation,
            iconColor
            
        }
    },
    methods: {
        changeColor(i){
            if (i==true){
                return "white"
            }else{
                return "#146c94"
            }
        },

        changeBackground(node,isExpanded){
            if(node == "Org" && isExpanded==true){
               return "#004a7c"
            }
            else if(node =="Account" && isExpanded==true){
               return "#146c94"
            }
            else{
               return "white"
            }
        },

        changeFontColor(isExpanded){
            if(isExpanded==true)  return "white"          
        }
    },
    
}

</script>



<style>
    .acc-tab-icon{
        margin-left: 0.5vw;
        font-weight: 600;
        color:#004a7c;
 
    }

    h3{
        padding:0.5vw  !important ; 
        margin:0.5vw   !important;
        font-size: 2rem !important;
        color: blue;
        font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    }


    .inner-container{
        width: 0.5vw;
    } 
    
    .org-tree-container{
        height:70vh;        
        overflow: auto;
        width: 60vw;
    }

    .org-tree-node-label{
        width: 15vw !important;       
    }

    .org-tree-node-label .org-tree-node-label-inner{
        padding:0vw !important;
    }

    .org-tree-node-label-inner{
       /* padding:0.5vw !important; */
       border:2px solid #004a7c;
       border-radius: 3px;
       color: #004a7c;
       /* background: brown; */
    }

    .updated_node{
        /* background:#004a7c; */
        width:100%;
        height:100%;
        /* color:white; */
        padding:0.1vw

    }

    .org-tree-node-children .org-tree-node-label{       
        width: 15vw !important;        
    }

    .org-tree-node-children .org-tree-node-label-inner{
        /* padding:0.5px; */
        border:2px solid #146c94;
        border-radius: 3px;
        color: #146c94;
    }

    .org-tree-node-children .org-tree-node-label .org-tree-node-children{       
        width: 15vw !important;        
    }

    .org-tree-node-children .org-tree-node-children .org-tree-node-label-inner{
        /* padding:0.5px; */
        border:2px solid #19a7ce;
        border-radius: 3px;
        color:#19a7ce
    }




</style>