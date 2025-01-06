const base_url = 'http://127.0.0.1:8000/'
function button_action(css_class, view_url){
    document.querySelectorAll(css_class).forEach(button => {
        button.addEventListener('click', function () {
            const taskId = parseInt(this.getAttribute('task-id')); 
            const csrfToken = document.querySelector('meta[name="csrf-token"]').content;
            const container = button.closest('.list-item')
            var action_url = view_url + `${taskId}/`;  
            fetch(action_url, {
                method: 'POST', 
                headers: {
                    'Content-Type': 'application/json', 
                    'X-CSRFToken': csrfToken 
                },
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Error processing the request');
                }
                return response.json() 
            })
            .then(data=>{
                if (data.is_checked !== undefined) {
                    container.classList.toggle('checked', data.is_checked);
                }
            }
            )
            .catch(error => console.error('Erro:', error)); 
        });
    });
}
button_action('.list-item-action-button.one', base_url + `todolist/check/`)


