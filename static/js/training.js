function updateProgress(moduleName, userId, progress) {
    fetch('/update-progress', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ module_name: moduleName, user_id: userId, progress: progress })
    })
    .then(response => response.json())
    .then(data => {
        if(data.success) {
            console.log('Progress updated successfully');
        } else {
            console.error('Error updating progress');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}