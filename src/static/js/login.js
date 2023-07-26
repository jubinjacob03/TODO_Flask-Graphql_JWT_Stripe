const emailField = document.getElementById("email");
const passField = document.getElementById("password");

const btn = document.querySelector(".btn");

btn.addEventListener("click", async (event) => {
	event.preventDefault();
	try {
		const form = new FormData();
		form.append("email", emailField.value);
		form.append("password", passField.value);

		const resp = await fetch("/login", {
			method: "POST",
			headers: {
				"Content-Type": "application/x-www-form-urlencoded",
			},
			body: new URLSearchParams(form),
		});

		const data = await resp.json();

		if (!resp.ok) {
			throw new Error(data.message);
		}

		window.location.pathname = "/app";
	} catch (error) {
		alert(error.message);
	}
});
