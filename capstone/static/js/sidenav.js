var logoutLink = document.getElementById('logout');

  logoutLink.addEventListener('click', function (e) {
    e.preventDefault();

    var confirmLogout = confirm('Are you sure you want to log out?');

    if (!confirmLogout) return;

    if (confirmLogout) {
      window.location.href = logoutLink.href;
    }

  });
