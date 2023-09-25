<template>
    <div class="icons">
        <div class="icons-box">
            <span class="tab-icons"> <i class="bi bi-hospital"></i><p>Organization</p></span>
            <span class="tab-icons"><i class="bi bi-building-fill"></i><p>Account</p></span>
            <span class="tab-icons"><i class="bi bi-person-fill"></i> <p>HCP</p></span>
            
            
           
        </div>
    </div>
</template>
<script>
export default {
    name:"myTabs"
}
</script>
<style scoped>
.tab-icons{
    display: flex;

}
.tab-icons i{
    
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 1.5vw;
    font-weight: 500;
    margin: 0 0.5vw;
}
.icons{
    width: 100%;
  
    display: flex;
    justify-content: center;
    align-items: center;
    height: 8vh;
}
.icons-box{
    display: flex;
    width: 25vw;
    justify-content: space-between;
    height: 100%;
   
    
}
.icons-box p{
    display: flex;
    height: 100%;
    justify-content: center;
    align-items: center;
    font-size: 1vw;
    font-weight: 500;
  
}
</style>