<template>
  <div class="all-header">
    <section class="header">
      <div class="logo">
        <img
          src="https://www.iqvia.com/-/media/iqvia/iqvia-logo-color.svg?mw=300&hash=CECD41EE60F67B3B27A5D7E6E7BABDFA"
          alt=""
        />
      </div>
      <div class="tabs">
        <div class="tab">
          <i class="bi bi-geo-fill"></i>
          <p>Summary View</p>
        </div>
        <div class="tab">
          <i class="bi bi-diagram-3-fill"> </i>
          <p>Profile View</p>
        </div>
        <div class="tab">
          <i class="bi bi-table"></i>
          <p>List View</p>
        </div>
      </div>
      <div class="logoutBtn">
        <form action="/" method="get">
        <button>Logout</button>
        </form>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "MyHeader",
};
</script>
<style scoped>
.header {
  display: flex;
  width: 100%;
  height: 12vh;
  align-items: center;
  justify-content: space-between;
  padding: 0 1vw;
  background-color: #e6e6e6;
}
.logo img {
  width: 40%;
  height: 10vh;

}
.tabs {
  display: flex;
  width: 35vw;
  justify-content:space-between ;
  height: 100%;
  align-items: center;
}
.tabs .tab{
    display: flex;
    width: 10vw;
    justify-content: space-around;
   
   }

.logoutBtn button{
  border-radius: 0.5vw;
  cursor: pointer;
  background-color: #00a3e0;
  color: white;
  padding: 0.5vw;
  font-size: 1vw;
  width: 5vw;
  border: none;
  font-weight: bold;
}

.logoutBtn button:hover{
  background-color: #54b3d6;
}

</style>