<template class = '.web_body'>
    <div class="side_menu">
      <Left_Menu></Left_Menu>
      <div class="fill_Left_Menu"></div>
    </div>
    <center_Body/>
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
/*   @import "./assets/Background_animate.scss"; */

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  margin-top: 0px;
  background-color: rgba(197,226,255,1);
  background-size:auto;
  flex-direction: column;
  resize: both;
  box-sizing: border-box;
  position: relative;
  background: rgb(197,226,255);
  background: linear-gradient(5deg,  rgb(160, 197, 236)0%, rgb(137, 174, 189)10%,  rgb(118, 127, 136) 20%,  rgb(93, 100, 104) 30%,rgb(57, 62, 65) 50%, rgb(93, 100, 104) 70%, rgb(118, 127, 136) 80%, rgb(160, 197, 236) 100%);
 

}

.side_menu{
  display: flex;
  height: 100%; /* Full-height: remove this if you want "auto" height */
  width: 180px; /* Set the width of the sidebar */
  background-color: rgba(114, 130, 146,0.6); /* #72829278; */
  position:fixed; /* Fixed Sidebar (stay in place on scroll) */
  flex-direction: column;
  z-index: 1; /* Stay on top */
  top: 0; /* Stay at the top */
  left: 0;
  overflow-x: hidden; /* Disable horizontal scroll */
  overflow: hidden;
}
.fill_Left_Menu{
  background: rgba(197, 226, 255,0.6);
  padding: 17px 0px 17px 0px;
  display: flex;
  flex-direction: column;
  gap: 166px;
  align-items: center;
  justify-content: flex-start;
  width: 168px;
  height: 100%;
  position: relative;
}
.center_body{

  /* background-color:rgba(197,226,255,1); /* rgba(28,31,34,1);  */
  display:flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center; 
  gap: 39px;
  
  height: 100%;
  left: 180px;
  float:center;
  position:relative;
  overflow-x: scroll; /* Disable horizontal scroll */
  overflow: hidden;

}

html {
    display:block;
    margin: 0;
    background-color: rgba(197,226,255,1);
} 
body {
  padding: 0; margin: 0; 
  height: 0;
  overflow-x:scroll; 
  overflow: scroll;
}


</style>
