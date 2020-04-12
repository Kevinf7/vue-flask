<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>The date time response is from Flask:</p>
    <p>Current date time is: {{ datetime }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      datetime: null
    }
  },
  mounted() {
    axios
      .get('http://localhost:5000/api/time')
      .then(response => (this.datetime = response.data.datetime))
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
