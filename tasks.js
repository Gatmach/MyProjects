document.addEventListener('DOMContentLoaded', function () {
    let submit = document.querySelector('input[type="submit"]');
    let newTask = document.querySelector('#task');
    let tasksList = document.querySelector('#tasks');
  
    submit.disabled = true;
  
    newTask.addEventListener('input', function () {
      submit.disabled = newTask.value.length === 0;
    });
  
    document.querySelector('form').addEventListener('submit', function (event) {
      event.preventDefault();
  
      let newTaskText = newTask.value.trim();
  
      if (newTaskText.length > 0) {
        let newTaskItem = document.createElement('li');
        newTaskItem.innerText = newTaskText;
        tasksList.appendChild(newTaskItem);
        newTask.value = '';
        submit.disabled = true;
      }
    });
  });