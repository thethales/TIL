# Increase the Mini Player Size in Cousera using Tamper/Grease Monkey
# This script may or may not work depending on changes made by coursera in their CSS and HTML site structure
# Should be Working up to 2020/03
# #GreaseMonkey
```Javascript
// ==UserScript==
// @name         Coursera Plus
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Slight alterations in coursera layout
// @author       thethales
// @match        https://www.coursera.org/learn/*
// @grant        none
// ==/UserScript==

(function() {


    function addStyle(styleStr) {
        var style = document.createElement('style');
        style.textContent = styleStr;
        document.head.append(style);
    }

    //Adds a slight increase of 100px to the mini scrollabe player, so there's more area for view without invanding the transcription text area
    addStyle('.rc-VideoMiniPlayer.mini .rc-VideoMiniControls, .rc-VideoMiniPlayer.mini .video-main-player-container {width:400px !important}');
})();


```