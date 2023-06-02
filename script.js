var storedData = localStorage.getItem('formData');
var data = JSON.parse(storedData);
console.log(data.name);     // Output the stored name value
console.log(data.password); // Output the stored password value
