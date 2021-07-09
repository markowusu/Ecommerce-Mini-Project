<template>
    <div class="signup">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h2 class="title ">
                    Sign Up 
                </h2>
                <form @submit.prevent="submitForm">

                <div class="field">
                <label for="username">Username</label>
                <div class="control ">
                <input placeholder="Macos" class="input" type="text" v-model="username">
                </div>
                </div>
                
                 <div class="field">
                <label for="password">Password</label>
                <div class="control">
                <input  type="password" class="input" v-model="password">
                </div>
                </div>


                 <div class="field">
                <label for="password">Repeat Password</label>
                <div class="control">
                <input  type="password" class="input" v-model="password2">
                </div>
                </div>

                <div class="notification is-danger " v-if="errors.length">
                <p v-for="error in errors" v-bind:key="error"> {{error}}</p>
                </div>

                  <div class="field">
                  <div class="control">
                  <button class="button is-dark">
                  sign up 
                  </button>
                  </div>
                  </div> 

                  <hr>
                  <router-link to="/log-in">log in </router-link>
                
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data(){
        return {
        username: '',
        password: '',
        password2: '',
        errors: []
        }
    },
    mounted() {
        document.title = 'Sign Up |'
      
    },
    methods:{
        submitForm(){
         this.errors = []

         if(this.username === ''){
             this.errors.push("Input a username")
         }

         if(this.password == ''){
             this.errors.push("This cannot be empty")
         }
          if(this.password == this.password2){
             this.errors.push("Both must be the same.")
         }

         if(!this.errors.length){
             const formData = {
                 username : this.username,
                 password : this.password
             }
             axios
             .post('/api/v1/users', formData)
             .then(response =>{
                 this.$router.push('/log-in')
             }
             )
             .catch( error => {
                 if(error.response){
                     for (const parameter in error.response.data){
                         this.errors.push(`${parameter}: ${error.response.data[$parameter]}`)
                     }
                        console.log(JSON.stringify(error.response.data))
                 }
                else if (error.message){
                    this.errors.push('There is an error ')

                    console.log(JSON.stringify(error))

                }
         }
             )
         
         }

        }
}
}
</script>