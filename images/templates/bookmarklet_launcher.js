(function(){
    if (window.myBookmarklet !== undefined){
        myBookmarklet()
    }
    document.body.appendChild(
        document.createElement('script')
    ).src='http://localhost:8000/static/js/bookmarklet.js?r='+
        Math.floor(Math.random()*99999999999999999999)
})