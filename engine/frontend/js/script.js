document.addEventListener('DOMContentLoaded', (event) => {
    let currentTemplateKey = 'start';

    const fetchTemplate = (templateKey, status) => {
        fetch(`/fetch_template/${templateKey}/${status}`)
            .then(response => response.json())
            .then(data => {
                if (data.end) {
                    document.getElementById('content').innerHTML = '<p>All templates rendered.</p>';
                } else {
                    document.getElementById('content').innerHTML = data.template;
                    currentTemplateKey = data.next_key;
                    setupButtons();
                }
            })
            .catch(error => {
                console.error('Error fetching template:', error);
            });
    };

    const setupButtons = () => {
        document.getElementById('next-button').addEventListener('click', () => {
            fetchTemplate(currentTemplateKey, 'next');
        });

        document.getElementById('error-button').addEventListener('click', () => {
            fetchTemplate(currentTemplateKey, 'error');
        });
    };

    // Start with the initial template
    fetchTemplate(currentTemplateKey, 'next');  
});