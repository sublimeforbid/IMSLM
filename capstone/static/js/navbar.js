const userNav = document.querySelector(".user-nav");
const userBtn = document.querySelector("#user");
const userDropdown = document.querySelector(".user-dropdown");

const handleUserDropdown = () => {
  userDropdown.classList.toggle("hide");
  // console.log("clicked");
};

userBtn.addEventListener("click", handleUserDropdown);

const notifyBtn = document.querySelector("#notify");
const notifyDropdown = document.querySelector(".notify-dropdown");

const handleNotifyDropdown = () => {
  notifyDropdown.classList.toggle("hide");
  // console.log("clicked");
};

notifyBtn.addEventListener("click", handleNotifyDropdown);

const messageBtn = document.querySelector("#message");
const messageDropdown = document.querySelector(".message-dropdown");

const handleMessageDropdown = () => {
  messageDropdown.classList.toggle("hide");
  // console.log("clicked");
};

messageBtn.addEventListener("click", handleMessageDropdown);

const settingsBtn = document.querySelector("#settings");
const settingsDropdown = document.querySelector(".settings-dropdown");

const handleSettingsDropdown = () => {
  settingsDropdown.classList.toggle("hide");
  // console.log("clicked");
};

settingsBtn.addEventListener("click", handleSettingsDropdown);

document.getElementById('notify').addEventListener('click', function() {
  var dropdown = document.querySelector('.notify-dropdown');
  dropdown.classList.toggle('show'); 
});
