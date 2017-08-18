let input = document.getElementById('rating'),
    response = document.getElementById("response"),
    rating = input.value;

if (rating === 10)
    response.innerHTML = "Good job!";
else
    response.innerHTML = 'Close but not perfect.';
