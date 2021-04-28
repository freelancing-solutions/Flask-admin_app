
self.addEventListener('load', async e => {
    document.getElementById('submit_button').addEventListener( 'submit', async e => {
        e.preventDefault();
        const website_name = document.getElementById('website-name').value;
        const target_uri = document.getElementById('target-uri').value;
        const schedule = document.getElementById('edit-schedule').value;
        const schedule_type = document.getElementById('schedule-type').value;
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        const login_uri = document.getElementById('login-uri').value;

        const init_post = {
                method: "POST",
                headers: new Headers({'content-type': 'application/json'}),
                mode: "cors",
                credentials: "same-origin",
                body: JSON.stringify({
                    'website_name': website_name, 'target_uri': target_uri, 'schedule': schedule,
                    'schedule_type': schedule_type, 'username': username, 'password': password,
                    'login_uri': login_uri}),
                cache: "no-cache"
        }

        const request = new Request('/settings/scrapper', init_post)
        const response = await fetch(request)
        const json_data = await response.json()
        if (response.ok){
            document.getElementById('message').innerHTML = json_data.message
        }
    })
})