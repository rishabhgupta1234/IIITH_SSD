function ValidateEmail(inputText) {
	var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
	if (inputText.value.match(mailformat)) {
		alert("Valid email address!");
		document.form1.text1.focus();
		return true;
	} else {
		alert("You have entered an invalid email address!");
		document.form1.text1.focus();
		return false;
	}
}

function submit_form() {
	alert("Login successfully");
}
function create() {
	// window.location = "signup.html";
	alert("Submit successfully");
}
function display() {
	var x = document.details.manager.value;
	var y = document.details.email.value;
	var z = document.details.server.value;
	var w = document.details.teamleadname.value;
	alert("NAME:" + x + "     " + "EMAIL:" + y + "     " + "USERNAME:" + z + "TEAMLEAD:" + w);
}

function validatePassword() {
	var password = document.getElementById("password"),
		confirm_password = document.getElementById("confirm_password");

	if (password.value != confirm_password.value) {
		confirm_password.setCustomValidity("Passwords Don't Match");
	} else {
		confirm_password.setCustomValidity("");
	}
}

function myFunction() {
	var element = document.body;
	element.classList.toggle("dark-mode");
}
function dragStartHandler(event) {
	//   e.preventDefault();
	event.dataTransfer.setData("draggedElementId", event.target.id);
	//   console.log(event.target);
}

function dragOverHandler(event) {
	event.preventDefault();
}

function dropHandler(event) {
	event.preventDefault();

	var elementId = event.dataTransfer.getData("draggedElementId");
	event.target.appendChild(document.getElementById(elementId));
}
function finalmsg() {
	var name = document.getElementById("manager").value;
	var email = document.getElementById("email").value;
	var username = document.getElementById("username").value;
	var teamlead = document.getElementById("teamleadname").value;
	var teammember = document.getElementById("tmm").value;

	alert(
		"Name : " +
			name +
			" \n email:   " +
			email +
			" \n  username: " +
			username +
			" \n teamlead: " +
			teamlead +
			" \n team-member:  " +
			teammember
	);
}
window.addEventListener("keypress", (e) => {
	console.log(e);
	if (e.ctrlKey && e.code == "KeyM") {
		myFunction();
	}
});
