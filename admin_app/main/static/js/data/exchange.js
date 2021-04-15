
self.addEventListener('load', e => {
    // TODO - listen for form input
    // TODO take data and send to backend
    let exchange_name = document.getElementById('exchange-name');
    let country = document.getElementById('country');
    document.getElementById('submit-button').addEventListener('click', async e => {
        e.preventDefault();
        let init_post = {
                method: "POST",
                headers: new Headers({'content-type': 'application/json'}),
                mode: "cors",
                body: JSON.stringify({name: exchange_name.value, country: country.value}),
                credentials: "same-origin",
                cache: "no-cache"
        }
        let response = await fetch(new Request(url='/data/exchange', init_post));
        let json_data = await response.json();
        if (json_data.status === true){
            document.getElementById('message').innerHTML = `
            <span>${json_data.message}</span>
            `
        }else{
            document.getElementById('message').innerHTML = `
            <span>${json_data.message}</span>            `
        }
    })

    document.getElementById('add-exchange').addEventListener('click', async e => {
        e.preventDefault();
        document.getElementById('form_data').innerHTML = `
            <div class="ln_solid"></div>
            <form id="demo-form2" data-parsley-validate class="form-horizontal form-label-left">            
                <div class="item form-group">
                    <label class="col-form-label col-md-3 col-sm-3 label-align" for="exchange-name">Exchange Name <span class="required">*</span></label>
                    <div class="col-md-6 col-sm-6 ">
                        <input type="text" id="exchange-name" required="required" class="form-control ">
                    </div>
                </div>
                <div class="item form-group">
                    <label class="col-form-label col-md-3 col-sm-3 label-align" for="country">Country <span class="required">*</span></label>
                    <div class="col-md-6 col-sm-6 ">
                        <input type="text" id="country" name="country" required="required" class="form-control">
                    </div>
                </div>
                
                <div class="ln_solid"></div>
                <div class="item form-group">
                    <div class="col-md-6 col-sm-6 offset-md-3">
                        <button class="btn btn-primary" type="button">Cancel</button>
                        <button class="btn btn-primary" type="reset">Reset</button>
                        <button id="submit-button" type="button" class="btn btn-success">Submit</button>
                    </div>
                </div>
                <div class="ln_solid"></div>
                <div class="item form-group" id="message">            
                </div>
                <div class="ln_solid"></div>           
            </form>                       
        `
    })

    document.getElementById('exchange-list').addEventListener('click', async e => {

        let init_post = {
                method: "POST",
                headers: new Headers({'content-type': 'application/json'}),
                mode: "cors",
                credentials: "same-origin",
                cache: "no-cache"
        }
        let request = new Request('/dashboard/exchanges', init_post);
        let response = await fetch(request)
        let json_response = await response.json()
        let exchange_list = []
        if (json_response.status === true){
            exchange_list = json_response.payload
        }
        let exchange_dom_elements = exchange_list.map(exchange => {
            console.log(exchange)
            let stocks_list = `/data/exchange/edit/${exchange.exchange_id}`
            return (
                `
                    <tr>
                        <td><input type="checkbox" value=${exchange.exchange_id}></td>
                        <td>${exchange.exchange_country}</td>
                        <td>${exchange.exchange_country}</td>
                        <td><a href=${stocks_list}> Edit </a></td>
                    </tr>
                `
            )

        })
        document.getElementById('form_data').innerHTML = `
                      <div class="row">
                          <div class="col-sm-12">
                            <div class="card-box table-responsive">
                            <p class="text-muted font-13 m-b-30">
                              Click on an exchange to edit the exchange details
                            </p>
                            <table id="datatable-checkbox" class="table table-striped table-bordered bulk_action" style="width:100%">
                              <thead>
                                <tr>                                  
                                  <th><input type="checkbox" id="check-all" ></th>
                                  <th>Exchange Name</th>
                                  <th>Country</th>
                                  <th>Action</th>
                                </tr>
                              </thead>
                              <tbody>
                                ${exchange_dom_elements}
                              </tbody>
                            </table>
                            </div>
                        </div>
                    </div>
        `


    })
});