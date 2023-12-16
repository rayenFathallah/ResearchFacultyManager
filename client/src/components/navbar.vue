<template>
    <header>
      <nav class="navbar navbar-expand-md red_bg">
        <div class="container">
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarCollapse">
            <ul class="navbar-nav me-auto mb-2 mb-md-0">
              <li class="nav-item"> 
                <router-link class="nav-link linkk" to="/facultes">Facultés</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link linkk" to="/publications">Publication</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link linkk" to="/labos">Laboratoires</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link linkk" to="/chercheurs">Chercheurs</router-link>
              </li>

            </ul>

          </div>
        </div>
      </nav>
    </header>

  </template>
  <style>
    .red_bg {
      background-color : #D33E46;
    }
    .nav_img {
      height : 70px;
    }
    .linkk {
      color : white;
    }
  </style>
  <script>
  import { defineComponent } from 'vue';
  
  export default defineComponent({
    name: 'NavBar',
    computed: {
      isLoggedIn: function() {
        return true
      }
    },
    methods: {
      async logout () {
        console.log("logged out");
      }
    },
  });
  </script>
  
  <style scoped>
  a {
    cursor: pointer;
  }
  </style>