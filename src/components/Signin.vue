<template>
  <section class="signin-main">
    <main>
      <div class="signin-form-container">
        <h3>Welcome to IQVIA Affiliations Tool</h3>
        <!-- method to be changed after adding authentication -->
        <div class="form">
          <input
            type="text"
            placeholder="Username"
            name="username"
            v-model="username"
            required
          />
          <input
            type="password"
            placeholder="Password"
            name="password"
            v-model="password"
            required
          />
          <button @click="signin">Signin</button>
        </div>
      </div>
      <img src="../assets/sigin_page_img.png" alt="IQVIA logo" />
    </main>
  </section>
</template>
<script>
export default {
  name: "MySignin",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    signin() {
      

      if (this.username === "sample_user" && this.password === "123456") {
        
        window.location.href = "/home";
      }
    },
  },
};
</script>
<style scoped>
button:focus {
  border: none;
  outline: none;
}
.signin-main {
  width: 100vw;
  height: 100vh;
  /* min-height: 641px;
    min-width: 1422px; */
}
main {
  position: relative;
  width: 100%;
  height: 100%;
  background: linear-gradient(112.17deg, #065788 4.05%, #1ba1db 83.26%);
}

.signin-form-container {
  position: absolute;
  top: 30%;
  left: 10%;
  height: 50%;
  width: 25%;
}
.signin-form-container h3 {
  color: white;
  font-size: 2.5vw;
  width: 100%;
  margin-bottom: 2%;
}
.signin-form-container .form {
  display: flex;
  flex-direction: column;
  height: 80%;
}
.signin-form-container .form input {
  border-radius: 2vw;
  height: 14%;
  margin: 2% 0;
  padding: 0.5vw 1vw;
  font-size: 1vw;
}
.signin-form-container .form button {
  border-radius: 2vw;
  cursor: pointer;
  height: 14%;
  margin: 2% 0;
  padding: 0.5vw 1vw;
  font-size: 1vw;
  font-weight: 600;
  color: white;
  border: 0.1vw solid white;
  background-color: #0c6ca0;
}
img {
  position: absolute;
  right: 0;
  top: 50%;
  width: 27%;
  height: 33%;
  max-width: 30vw;
  max-height: 35vh;
}
</style>
