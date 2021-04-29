self.addEventListener('load', async e => {
    document.getElementById('submit_butt').addEventListener('submit', async e => {
        e.preventDefault();
        const plan_name = document.getElementById('plan_name').value;
        const description = document.getElementById('description').value;
        const schedule_day = parseInt(document.getElementById('schedule_day').value);
        const schedule_term = document.getElementById('schedule_term').value;
        const payment_amount = parseInt(document.getElementById('payment_amount').value);
        const registration_amount = parseInt(document.getElementById('registration_amount').value);

        const init_post = {
                method: "POST",
                headers: new Headers({'content-type': 'application/json'}),
                mode: "cors",
                body: JSON.stringify({
                    plan_name: plan_name, description: description,
                    schedule_day: schedule_day,
                    schedule_term: schedule_term, payment_amount: payment_amount,
                    registration_amount: registration_amount
                }),
                credentials: "same-origin",
                cache: "no-cache"
        }
        const request = new Request('/create-membership_plan', init_post);
        const response = await fetch(request);
        const json_data = await response.json();
        if (response.ok){
            document.getElementById('message').innerHTML = `
                <span class="info"> ${json_data.message}</span>
            `
        }else{
            document.getElementById('message').innerHTML = `
                <span class="danger"> ${json_data.message}</span>
            `
        }
    })
})