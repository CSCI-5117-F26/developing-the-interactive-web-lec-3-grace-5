parent = document.getElementById('form');
form.addEventListener('submit', function(event) {
    event.preventDefault();
    add_guest();
  });

parent = document.getElementById('guestbook');
function add_guest() {
    const firstName = document.getElementById('fname').value;
    const lastName = document.getElementById('lname').value;
    const guest = document.createElement("li");
    guest.textContent = `${firstName} ${lastName}`;
    parent.appendChild(guest);
}