

self.addEventListener('load', async e => {
    document.getElementById('update-button').addEventListener('click', async e => {
        e.preventDefault();
        let broker_id = document.getElementById('broker-id');
        let broker_code = document.getElementById('broker-code');
        let broker_name = document.getElementById('broker-name');

        let init_post = {
                method: "POST",
                headers: new Headers({'content-type': 'application/json'}),
                mode: "cors",
                body: JSON.stringify({broker_id: broker_id.value, broker_code: broker_code.value, broker_name: broker_name.value}),
                credentials: "same-origin",
                cache: "no-cache"
        }

        let request = new Request('/')
    });

})