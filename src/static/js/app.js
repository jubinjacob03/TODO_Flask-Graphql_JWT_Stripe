console.log(user);

class App {
	todos = new Map(todos.map((todo) => [todo.id, todo]));

	inputTitle = document.getElementById("new-title");
	inputDesc = document.getElementById("new-desc");

	addTaskBtn = document.querySelector(".add-task-btn");
	logoutBtn = document.querySelector(".sign-out-btn");

	constructor() {
		this.updateTable();

		this.addTaskBtn.addEventListener("click", this.onAddTask.bind(this));
		this.logoutBtn.addEventListener("click", this.onLogout.bind(this));
	}

	getRowHtml(todo) {
		const imgUrl = localStorage.getItem(todo.id);

		return `
        <td>
            <div class="input-box">
                <input value="${
									todo.title
								}" class="input-title" type="text" placeholder="Enter title" required />
            </div>
        </td>
        <td>
            <div class="input-box">
                <input value="${
									todo.description
								}" class="input-desc" type="text" placeholder="Enter description" required />
            </div>
        </td>
        <td>${todo.time}</td>
        ${
					user.premium
						? `
            <td>
                ${
									!imgUrl
										? `<div class="input-box">
                    <input class="input-image" type="text" placeholder="Add url of image" required />
                </div>
                <button class="edit-btn"><b>Add</b></button>`
										: `
                                        <div class="todo-img-box">
                                            <img src=${imgUrl} />
                                        </div>`
								}
            </td>
            `
						: ``
				}
        <td>
            <button class="save-btn"><b>Save</b></button>
            <button class="delete-btn"><b>Delete</b></button>
        </td>`;
	}

	updateTable() {
		// clear the rows
		const tbody = document.querySelector("tbody");
		while (tbody.firstChild) {
			tbody.firstChild.remove();
		}

		// add them again
		this.todos.forEach((todo, id) => {
			const tr = document.createElement("tr");

			console.log(todo);

			tr.dataset.id = id;
			tr.innerHTML = this.getRowHtml(todo);

			tbody.appendChild(tr);

			const saveBtn = tr.querySelector(".save-btn");
			const deleteBtn = tr.querySelector(".delete-btn");

			saveBtn.addEventListener("click", () => this.onSaveTask(tr));
			deleteBtn.addEventListener("click", () => this.onDeleteTask(tr));

			if (user.premium && !localStorage.getItem(id)) {
				const imgBtn = tr.querySelector(".edit-btn");
				imgBtn.addEventListener("click", () => this.onAddImage(tr));
			}
		});
	}

	async onAddTask() {
		const title = this.inputTitle.value;
		const desc = this.inputDesc.value;

		try {
			const payload = {
				query: `mutation {
                    addTodo(input: {
                        title: "${title}",
                        description: "${desc}"
                    }) {
                        todo {
                            id
                            title
                            description
                            time
                        }
                        status
                    }
                }`,
			};

			const resp = await fetch("/todos", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify(payload),
			});
			const body = await resp.json();

			const data = body.data.addTodo;

			if (!resp.ok || !data.status) {
				throw new Error("Failed to add todo.");
			}

			console.log(data);

			this.todos.set(data.todo.id, data.todo);
			this.updateTable();

			this.inputTitle.value = "";
			this.inputDesc.value = "";
		} catch (error) {
			console.error(error);
			alert(error.message);
		}
	}

	async onSaveTask(tr) {
		const inputTitle = tr.querySelector(".input-title");
		const inputDesc = tr.querySelector(".input-desc");

		const id = Number(tr.dataset.id);

		const title = inputTitle.value;
		const desc = inputDesc.value;

		try {
			const payload = {
				query: `mutation {
                        updateTodo(
                            id: ${id},
                            input: {
                                title: "${title}",
                                description: "${desc}"
                            }
                        ) {
                            todo {
                                id
                                title
                                description
                                time
                            }
                            status
                        }
                    }`,
			};

			const resp = await fetch("/todos", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify(payload),
			});
			const body = await resp.json();

			const data = body.data.updateTodo;

			if (!resp.ok || !data.status) {
				throw new Error("Failed to save todo.");
			}

			console.log(data);

			this.todos.set(id, data.todo);
			this.updateTable();

			this.inputTitle.value = "";
			this.inputDesc.value = "";
		} catch (error) {
			console.error(error);
			alert(error.message);
		}
	}

	async onDeleteTask(tr) {
		const id = Number(tr.dataset.id);

		try {
			const payload = {
				query: `mutation {
                        deleteTodo(id: ${id}) {
                            status
                        }
                    }`,
			};

			const resp = await fetch("/todos", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify(payload),
			});
			const body = await resp.json();

			const data = body.data.deleteTodo;

			if (!resp.ok || !data.status) {
				throw new Error("Failed to delete todo.");
			}

			console.log(data);

			this.todos.delete(id);
			this.updateTable();

			this.inputTitle.value = "";
			this.inputDesc.value = "";
		} catch (error) {
			console.error(error);
			alert(error.message);
		}
	}

	onLogout() {
		window.location.pathname = "/logout";
	}

	onAddImage(tr) {
		console.log(tr);

		const id = Number(tr.dataset.id);
		const inputUrl = tr.querySelector(".input-image");

		localStorage.setItem(id, inputUrl.value);
		this.updateTable();
	}
}

const app = new App();
