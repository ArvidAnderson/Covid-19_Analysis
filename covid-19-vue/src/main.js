import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/tailwind.css'
import firebase from 'firebase'
import firebaseConfig from './firebase_credentials'

firebase.initializeApp(firebaseConfig);
const db = firebase.firestore();
db.settings({ timestampsInSnapshots: true });

export default db

createApp(App).use(router).mount('#app')
