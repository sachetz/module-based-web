document.addEventListener('DOMContentLoaded', (event) => {
    let index = 0;

    const fetchTemplate = (index, status) => {
        fetch(`/fetch_template/${index}/${status}`)
            .then(response => response.json())
            .then(data => {
                if (data.end) {
                    document.getElementById('content').innerHTML = '<p>All templates rendered.</p>';
                } else {
                    document.getElementById('content').innerHTML = data.template;
                    setupButtons(index);
                }
            })
            .catch(error => {
                console.error('Error fetching template:', error);
            });
    };

    const setupButtons = (index) => {
        document.getElementById('next-button').addEventListener('click', () => {
            fetchTemplate(index + 1, 'success');
        });

        document.getElementById('error-button').addEventListener('click', () => {
            fetchTemplate(index + 1, 'error');
        });
    };

    fetchTemplate(index, 'success');  // Start fetching templates
});