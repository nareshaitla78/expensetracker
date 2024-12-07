<template>
    <q-page class="q-pa-md flex flex-center">
      <q-card class="q-ma-md" style="width: 400px">
        <q-tabs v-model="activeTab" class="text-center" align="center" dense>
          <q-tab name="login" label="Login" />
          <q-tab name="signup" label="Signup" />
        </q-tabs>
  
        <q-separator />
  
        <div v-if="activeTab === 'login'">
          <q-card-section>
            <q-input v-model="loginData.username" label="Username" filled />
            <q-input
              v-model="loginData.password"
              label="Password"
              :type="loginPasswordVisible ? 'text' : 'password'"
              filled
              >
              <template v-slot:append>
                <q-icon
                  :name="loginPasswordVisible ? 'visibility' : 'visibility_off'"
                  class="cursor-pointer"
                  @click="toggleLoginPasswordVisibility"
                />
              </template>
            </q-input>
            <q-btn class="q-mt-md" color="primary" label="Login" @click="login" />
            <q-banner v-if="loginMessage" :type="loginSuccess ? 'positive' : 'negative'" dense>
              {{ loginMessage }}
            </q-banner>
          </q-card-section>
        </div>
  
        <div v-if="activeTab === 'signup'">
          <q-card-section>
            <q-input v-model="signupData.username" label="Username" filled />
            <q-input
              v-model="signupData.password"
              label="Password"
              :type="signupPasswordVisible ? 'text' : 'password'"
              filled
            >
              <template v-slot:append>
                <q-icon
                  :name="signupPasswordVisible ? 'visibility' : 'visibility_off'"
                  class="cursor-pointer"
                  @click="toggleSignupPasswordVisibility"
                />
              </template>
            </q-input>
            <q-btn class="q-mt-md" color="primary" label="Sign Up" @click="signup" />
            <q-banner v-if="signupMessage" :type="signupSuccess ? 'positive' : 'negative'" dense>
              {{ signupMessage }}
            </q-banner>
          </q-card-section>
        </div>
      </q-card>
    </q-page>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        activeTab: 'login', // Default to login
        loginData: { username: '', password: '' },
        signupData: { username: '', password: '' },
        loginPasswordVisible: false, // Toggle visibility for login password
        signupPasswordVisible: false, // Toggle visibility for signup password
        loginMessage: '',
        loginSuccess: false,
        signupMessage: '',
        signupSuccess: false,
      };
    },
    methods: {
        async login() {
            try {
                const response = await axios.post('/login', this.loginData);
                this.loginSuccess = true;
                this.loginMessage = response.data.message;
                this.$router.push('/expense-tracker'); // Redirect to Expense Tracker
            } catch (error) {
                this.loginSuccess = false;
                this.loginMessage = error.response?.data.error || 'Login failed';
            }
            },

      async signup() {
        try {
          const response = await axios.post('/signup', this.signupData);
          this.signupSuccess = true;
          this.signupMessage = response.data.message;
        } catch (error) {
          this.signupSuccess = false;
          this.signupMessage = error.response?.data.error || 'Signup failed';
        }
      },
      toggleLoginPasswordVisibility() {
        this.loginPasswordVisible = !this.loginPasswordVisible;
      },
      toggleSignupPasswordVisibility() {
        this.signupPasswordVisible = !this.signupPasswordVisible;
      },
    },
  };
  </script>
  