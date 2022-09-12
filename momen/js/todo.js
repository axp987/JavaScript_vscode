const todoForm = document.getElementById("todo-form");
const todoInput = document.querySelector("#todo-form input");
const todoList = document.getElementById("todo-list");

let toDos = [];
const TODO_KEY = "todos"

function deleteButton(event) {
    const li = event.target.parentElement;
    console.log(typeof li.id, li.id); //String
    li.remove();
    toDos = toDos.filter((toDo) => toDo.id !== parseInt(li.id)); //toDos의 id는 int
    saveToDos();
    console.log(toDos);
}

function paintTodo(newTodo) { // 리스트 출력
    const li = document.createElement("li");
    const span = document.createElement("span");
    span.innerText = newTodo.text;
    li.id = newTodo.id;

    const bu = document.createElement("button");
    bu.innerText = "삭제";
    bu.addEventListener("click", deleteButton);

    li.appendChild(span); //<li> 안에 <span>
    li.appendChild(bu);
    todoList.appendChild(li); //<ul> 안에 <li>
}

function handleSubmit(event) { // 리스트 내용 입력박스
    event.preventDefault();
    const newTodo = todoInput.value;
    todoInput.value = "";
    const newTodoObj = {
        text: newTodo,
        id: Date.now()
    };
    toDos.push(newTodoObj);
    paintTodo(newTodoObj);
    saveToDos();
}

function saveToDos() { //toDos DB에 저장
    localStorage.setItem(TODO_KEY, JSON.stringify(toDos));
}

const savedToDos = localStorage.getItem(TODO_KEY);
if(savedToDos !== null) { // toDos에 저장된 값을 다른식으로 출력 //if(savedToDos) {}
    const parsedToDos = JSON.parse(savedToDos);
    toDos = parsedToDos; 
    //toDos.push가 항상 0부터 값을 집어넣기에 위구문 필요
    parsedToDos.forEach(paintTodo);
}

todoForm.addEventListener("submit", handleSubmit);



