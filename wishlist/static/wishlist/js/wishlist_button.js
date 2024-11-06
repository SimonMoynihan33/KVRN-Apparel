document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll('.wishlist-icon-form').forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            const url = this.action;
            const formData = new FormData(this);

            fetch(url, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Toggle the heart icon based on wishlist state
                    const icon = this.querySelector('i');
                    if (data.wishlist_state) {
                        icon.classList.remove('fa-heart-o');
                        icon.classList.add('fa-heart');
                    } else {
                        icon.classList.remove('fa-heart');
                        icon.classList.add('fa-heart-o');
                    }
                } else if (data.redirect_url) {
                    // Redirect if the user is not authenticated
                    window.location.href = data.redirect_url;
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });
});