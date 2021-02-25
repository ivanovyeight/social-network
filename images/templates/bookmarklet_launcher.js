(function(){
    if (window.myBookmarklet !== undefined){
        myBookmarklet()
    }
    document.body.appendChild(
        document.createElement('script')
    ).src='https://debb53c77e39.ngrok.io/static/js/bookmarklet.js?r='+
        Math.floor(Math.random()*99999999999999999999)
})();