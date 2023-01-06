var modalBtns=document.querySelectorAll('.modal-open');

modalBtns.forEach(function(btn){
    btn.onclick=function(){
        var modal=btn.getAttribute('data-modal');
        document.getElementById(modal).style.display='flex';
    };

});

var closeBtns=document.querySelectorAll('.modal-close');

closeBtns.forEach(function(btn){
    btn.onclick=function(){
        var modal=(btn.closest('.my-modal').style.display='none');
    };
});

window.onclick = function(e){
    if(e.target.classList.contains('my-modal')){
        e.target.style.display = 'none';
    }
};








