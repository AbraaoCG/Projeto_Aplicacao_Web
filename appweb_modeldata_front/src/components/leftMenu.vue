<template>
    <div class="left-menu">
      <div class="website-title">
        <div class="acg">ACG</div>
      </div>
  
      <div class="navigation">
        <div class="neuralnetworkicon">
            <!-- <img alt='Neural Network Icon' src="./../assets/network.png" height="100%" width="100%" />-->
            <a>Rede Neural</a>
        </div>
        <div class="separator"></div>
        <div class="classifiericon">
             <!-- <img alt='Classifier Icon' src="./../assets/classifier.png" height="100%" width="100%" />-->
             <a>Classificador</a>
        </div>
            
        <div class="separator"></div>
  
        <div class="regressionicon">
            <!--<img alt='Classifier Icon' src="./../assets/regressor.png" height="100%" width="100%" /> --> 
            <a>Regressor</a>
        </div>
        <div class="separator"></div>
        <div class="settingsicon"></div>
      </div>
  
      <div class="footer"></div>
    </div>
  </template>
  <script>
  /* Code generated with AutoHTML Plugin for Figma */
  import './../assets/network.png'
  import './../assets/classifier.png'
  import './../assets/regressor.png'
  export default {
    name: "Left_Menu",
    components: {},
    props: {},
    data() {
      // quickfix to have components available to pass as props
      return {};
    },
  };
  </script>
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Lobster');
  .left-menu,
  .left-menu * {
    box-sizing: border-box;
  }
  .left-menu {
    background: rgba(197, 226, 255,0.6);
    padding: 17px 0px 17px 0px;
    display: flex;
    flex-direction: column;
    gap: 166px;
    align-items: center;
    justify-content: flex-start;
    width: 168px;
    height: 1080px;
    position: relative;
  }
  .website-title {
    background: #2a3036;
    border-radius: 50px;
    display: flex;
    flex-direction: column;
    gap: 0px;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    width: 111px;
    height: 79px;
    position: relative;
  }
  .a{
    text-align: center;
    position: relative;
    width: 100%;
    height: 100%;
    
  }
  .acg {
    color: #ffffff;
    text-align: center;
    font: 300 32px "Lobster";
    position: relative;
    width: 83px;
    height: 34px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .navigation {
    padding: 0px 0px 0px 0px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: center;
    justify-content: flex-start;
    flex-shrink: 0;
    width: 100%;
    position: relative;
    overflow: hidden;
    font: 300 28px "Lobster";
  }
  .neuralnetworkicon {
    padding: 10px 10px 10px 10px;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items:center;
    justify-content: flex-start;
    align-self: stretch;
    flex-shrink: 0;
    position: relative;
    overflow: hidden;
  }
  .separator {
    background: #58626d;
    flex-shrink: 0;
    width: 26.67px;
    height: 1.05px;
    position: relative;
  }
  .classifiericon {
    padding: 10px 10px 10px 10px;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items:center;
    justify-content: flex-start;
    align-self: stretch;
    flex-shrink: 0;
    height: 102px;
    position: relative;
    overflow: hidden;
  }
  .regressionicon {
    padding: 10px 10px 10px 10px;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items:center;
    justify-content: flex-start;
    align-self: stretch;
    flex-shrink: 0;
    height: 102px;
    position: relative;
    overflow: hidden;
  }
  .settingsicon {
    padding: 10px 10px 10px 10px;
    display: flex;
    flex-direction: row;
    gap: 10px;
    align-items: flex-start;
    justify-content: flex-start;
    align-self: stretch;
    flex-shrink: 0;
    height: 102px;
    position: relative;
    overflow: hidden;
  }
  .footer {
    padding: 10px 10px 10px 10px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
    justify-content: flex-start;
    flex-shrink: 0;
    width: 128px;
    height: 155px;
    position: relative;
    overflow: hidden;
  }
  </style>
  