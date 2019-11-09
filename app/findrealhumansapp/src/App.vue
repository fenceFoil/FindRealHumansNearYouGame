<template>
<div id="overall" >
  <div id="overlay"><h1 id="overlay-text">*Girls Are Preparing . . .*</h1></div>
  <div id="app">
    <router-view/>
  </div>
  </div>
</template>

<style>
#app {
  min-width: 1900px;
  max-width: 1940px;
  margin: auto;
  font-family: Glitter, 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#overlay {
  position: fixed; /* Sit on top of the page content */
  width: 100%; /* Full width (cover the whole page) */
  height: 100%; /* Full height (cover the whole page) */
  display: none;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0,0,0,0.9); /* Black background with opacity */
  z-index: 2; /* Specify a stack order in case you're using a different order for other elements */
  cursor: pointer; /* Add a pointer on hover */
}

#overlay-text {
  position: absolute;
  top: 50%;
  left: 50%;
  font-size: 10em;
  margin-top: -1em;
  margin-left: -5em;
  color: pink;
}

button, input, textarea{
  font-family: Glitter;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
