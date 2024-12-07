<template>
  <q-page class="q-pa-md">
    <q-card>
      <q-card-section>
        <div class="text-h6">Expense Tracker</div>
      </q-card-section>

      <!-- Expense Input Section -->
      <q-card-section>
        <q-input v-model="expense.amount" label="Amount" type="number" filled />
        <q-select 
          v-model="expense.category" 
          :options="categories" 
          label="Select Category" 
          filled
        />
        <q-btn class="q-mt-md" color="primary" label="Add Expense" @click="addExpense" />
      </q-card-section>

      <!-- Expense List Section -->
      <q-card-section>
        <div class="text-h6">Monthly Expenses: {{ totalExpense }}</div>
        <q-list bordered>
          <q-item v-for="(item, index) in expenses" :key="index">
            <q-item-section>
              {{ item.category }}: ₹{{ item.amount }}
            </q-item-section>
          </q-item>
        </q-list>
      </q-card-section>

      <!-- Logout Button -->
      <q-card-section>
        <q-btn class="q-mt-md" color="secondary" label="Logout" @click="logout" />
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script>
import axios from 'axios';
import { Notify } from 'quasar';  // For notifications

export default {
  data() {
    return {
      expense: { amount: 0, category: '' },
      expenses: [], // List of expenses
      categories: ['Groceries', 'Shopping', 'Rent', 'Utilities', 'Miscellaneous'], // Dropdown options
    };
  },
  computed: {
    totalExpense() {
      return this.expenses.reduce((sum, exp) => sum + parseFloat(exp.amount), 0);
    },
  },
  methods: {
    async addExpense() {
      if (!this.expense.amount || !this.expense.category) {
        this.$q.notify('Please fill all fields');
        return;
      }
      try {
        const response = await axios.post('/add-expense', this.expense);
        this.expenses.push(response.data); // Update local expenses
        this.expense = { amount: 0, category: '' }; // Reset form
      } catch (error) {
        this.$q.notify('Failed to add expense');
      }
    },

    logout() {
      // Clear session or authentication token (depending on your backend)
      // Example for session-based logout:
      axios.post('/logout').then(() => {
        this.$router.push('/login'); // Redirect to login page
      }).catch(() => {
        Notify.create({
          message: 'Logout failed',
          color: 'negative',
          position: 'top',
        });
      });
    },
  },
  async mounted() {
    try {
      const response = await axios.get('/expenses');
      this.expenses = response.data; // Load initial expenses
    } catch (error) {
      this.$q.notify('Failed to fetch expenses');
    }
  },
};
</script>
