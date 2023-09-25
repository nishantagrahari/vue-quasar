<template>
    <button class="reset-btn" @click="redirect">
        Reset Filters
    </button>
</template>
<script>
export default {
   name:"MyResetBtn",
   methods:{
    redirect(){
        console.log("reloading")
        window.location.reload()
    }
}
}

</script>
<style scoped>
.reset-btn{
    border: 1px solid black;
    cursor:pointer;
    transition: 0.5s ease;
    border-radius: 1vw;
    width: 10vw;
    height:7vh;
    background-color:#c8c8c8 ;
}

.reset-btn:hover{
  background-color:#e6e1e1 ;
}
</style>