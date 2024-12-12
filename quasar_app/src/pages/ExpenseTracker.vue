<template>
  <q-page class="q-pa-md">
    <q-card>
      <q-card-section>
        <div class="flex justify-between">
          <div class="text-h6">Expense Tracker</div>
          <q-btn color="secondary" label="Logout" @click="logout" />
        </div>
      </q-card-section>

      <q-card-section>
        <q-input v-model="expense.amount" label="Amount" type="number" filled />
        <q-select 
          v-model="expense.category" 
          :options="categories" 
          label="Select Category" 
          filled
        />
        <q-btn color="primary" label="Add Expense" class="q-mt-md" @click="addExpense" />
      </q-card-section>

      <q-card-section>
        <div class="text-h6">Monthly Expenses: ₹{{ totalExpense }}</div>
        <q-list bordered>
          <q-item v-for="(item, index) in expenses" :key="index">
            <q-item-section>
              {{ item.category }}: ₹{{ item.amount }}
            </q-item-section>
          </q-item>
        </q-list>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script>
import axios from 'axios';

axios.defaults.withCredentials = true; // Ensure cookies are sent with each request

export default {
  data() {
    return {
      expense: { amount: '', category: '' },
      expenses: [],
      categories: ['Groceries', 'Shopping', 'Rent', 'Utilities', 'Miscellaneous'],
    };
  },
  computed: {
    totalExpense() {
      return this.expenses.reduce((sum, expense) => sum + parseFloat(expense.amount), 0);
    },
  },
  methods: {
    async addExpense() {
      if (!this.expense.amount || !this.expense.category) {
        this.$q.notify({ message: 'Please fill in all fields', color: 'negative' });
        return;
      }
      try {
        const response = await axios.post('/add-expense', this.expense);
        this.expenses.push(response.data);
        this.expense = { amount: '', category: '' };
        this.$q.notify({ message: 'Expense added successfully', color: 'positive' });
      } catch (error) {
        this.$q.notify({ message: 'Failed to add expense', color: 'negative' });
      }
    },
    async logout() {
      try {
        await axios.post('/logout');
        this.$router.push('/login');
      } catch {
        this.$q.notify({ message: 'Logout failed', color: 'negative' });
      }
    },
  },
  async mounted() {
    try {
      const response = await axios.get('/expenses');
      this.expenses = response.data;
    } catch {
      this.$q.notify({ message: 'Failed to fetch expenses', color: 'negative' });
    }
  },
};
</script>
