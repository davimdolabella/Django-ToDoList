task_tilte = document.querySelectorAll('.list-item-text')
tasks_check_button = document.querySelectorAll('.list-item-action-button-link.one')
tasks_check_button.forEach(check_button => {
    check_button.addEventListener('click', function(){
        container = check_button.parentElement.parentElement.parentElement
        container.classList.toggle('checked')
        
    })
});