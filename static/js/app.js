const app = new Vue({
  el: "#app",
  delimiters: ['[[', ']]'],
  data: {
    message: "Hello",
    words: []
  },
  mounted() {
    this.loadWords();
  },
  methods: {
    loadWords() {
      return fetch('/mots')
        .then(rep => rep.json())
        .then(data => console.log(data))
    }
  }
});