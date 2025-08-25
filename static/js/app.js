class TypeMot {
  constructor(type_mot = {}) {
    this.id = type_mot.id || -1;
    this.type_mot = type_mot.type_mot || "";
  }
}

class Mot {
  constructor(mot = {}) {
    this.id = mot.id || -1;
    this.mot = mot.mot || "";
    this.type_mot = mot.type_mot || new TypeMot({});
    this.definition = mot.definition || "";
  }
}

const app = new Vue({
  el: "#app",
  delimiters: ['[[', ']]'],
  data: {
    mode: 'listWords',
    message: "Hello",
    words: [],
    wordsTypes: [],
    currMot: new Mot()
  },
  mounted() {
    this.loadTypesMots();
    this.loadWords();
  },
  methods: {
    loadWords() {
      return fetch('/mots')
        .then(rep => rep.json())
        .then(data => this.words = data);
    },
    loadTypesMots() {
      return fetch('types-mots')
        .then(rep => rep.json())
        .then(data => {
          this.wordsTypes = data.map(tm => new TypeMot(tm));
        })
    },
    saveWord() {
      return fetch("/mots",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(this.currMot)
        })
        .then(response => response.json())
        .then(data => {
          console.log("Mot créé :", data);
        });
    },
    addNewWord() {
      this.mode = 'addWord';
      this.currMot = new Mot();
    },
    cancel() {
      this.mode = 'listWords';
    }
  }
});