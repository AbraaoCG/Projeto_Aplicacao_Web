<template class = '.web_body'>
    <span class="side_menu">
      <Left_Menu></Left_Menu>
    </span>
    <span class="center_body">  
      <center_Body/>
    </span>
</template>

<script>
import center_Body from './components/body.vue'
import Left_Menu from './components/leftMenu.vue'

export default {
  name: 'App',
  components: {
    center_Body,
    Left_Menu
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Merienda&display=swap');
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  margin-top: 0px;
  background-color: #1f2327;
  background-size:auto;
  resize: both;
  box-sizing: border-box;
  position: relative;

}
.side_menu{
  display: flex;
  height: 100%; /* Full-height: remove this if you want "auto" height */
  width: 180px; /* Set the width of the sidebar */
  background-color: #c5e2ff77;
  position:fixed; /* Fixed Sidebar (stay in place on scroll) */
  flex-direction: column;
  z-index: 1; /* Stay on top */
  top: 0; /* Stay at the top */
  left: 0;
  overflow-x: hidden; /* Disable horizontal scroll */
  overflow: hidden;
}
.center_body{
  height: 100%;
  background-color: rgba(28,31,34,1); /* */
  
  display: flex;
  flex-direction: column;
  gap: 39px;
  align-items: center;
  justify-content: flex-start;
  left: 5%;
  position:relative;
  overflow-x: hidden; /* Disable horizontal scroll */
  overflow: hidden;

}

html {
    display:block;
    margin: 0;
    background-color: #1f2327;
}
body {
  padding: 0; margin: 0; 
  overflow-x:scroll; /* Disable horizontal scroll */
  overflow: scroll;
}


</style>
