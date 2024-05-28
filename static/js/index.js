"use strict";

const sidebar = document.querySelector('.sidebar');
const closeBtn = document.querySelector('#btn');

closeBtn.addEventListener('click', ()=> {
    sidebar.classList.toggle('open');
    menuChangeBtn();
});

function menuChangeBtn()
{
    if(sidebar.classList.contains('open')){
        closeBtn.classList.replace('bx-menu', 'bx-menu-alt-right');
    } else
    {
        closeBtn.classList.replace('bx-menu-alt-right', 'bx-menu');
    }
}