(function(){
    if (window.myBookmarklet !== undefined){
        myBookmarklet();
    }
    document.body.appendChild(
        document.createElement('script')
    ).src='https://4610b536ddf7.ngrok.io/static/js/bookmarklet.js?r='+
        Math.floor(Math.random()*99999999999999999999);
})();