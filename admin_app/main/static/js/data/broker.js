self.addEventListener('load', async e => {
    // TODO - listen for form input
    // TODO take data and send to backend
    let broker_id = document.getElementById('broker_id');
    let broker_code = document.getElementById('broker-code');
    let broker_name = document.getElementById('broker-name');

    document.getElementById('submit-button').addEventListener('click', async e => {
        e.preventDefault();
        let init_post = {
                method: "POST",
                headers: new Headers({'content-type': 'application/json'}),
                mode: "cors",
                body: JSON.stringify({broker_id: broker_id.value, broker_code: broker_code.value, broker_name: broker_name.value}),
                credentials: "same-origin",
                cache: "no-cache"
        }
        let request = new Request(url='/data/broker', init_post);
        let response = await fetch(request);
        let json_data = await response.json();
        console.log(json_data);
        if (json_data.status === true){
            document.getElementById('message').innerHTML = `
            <span>${json_data.message}</span>
            `
        }else{
            document.getElementById('message').innerHTML = `
            <span>${json_data.message}</span>
            `
        }
    })
    document.getElementById('add-broker').addEventListener('click', async e => {
        document.getElementById('form_data').innerHTML = `
                                    <div class="ln_solid"></div>
                                    <form id="demo-form2" data-parsley-validate class="form-horizontal form-label-left">
                                                            <div class="item form-group">
                                    <label class="col-form-label col-md-3 col-sm-3 label-align" for="exchange">Select Exchange <span class="required">*</span>
                                    </label>
                                                                <div class="col-md-6 col-sm-6 ">
                                                                    <select class="form-control">
                                                                        <option> Philippines Stock Exchange </option>
                                                                    </select>
                                                                </div>
                                    
                                                            </div>
                                    <div class="item form-group">
                                    <label class="col-form-label col-md-3 col-sm-3 label-align" for="broker-id">Broker ID <span class="required">*</span>
                                    </label>
                                    <div class="col-md-6 col-sm-6 ">
                                    <input type="text" id="broker-id"  class="form-control ">
                                    </div>
                                    </div>
                                    
                                    <div class="item form-group">
                                    <label class="col-form-label col-md-3 col-sm-3 label-align" for="broker-code">Broker Code <span class="required">*</span>
                                    </label>
                                    <div class="col-md-6 col-sm-6 ">
                                    <input type="text" id="broker-code" required="required" class="form-control ">
                                    </div>
                                    </div>
                                    <div class="item form-group">
                                    <label class="col-form-label col-md-3 col-sm-3 label-align" for="broker-name">Broker Name <span class="required">*</span>
                                    </label>
                                    <div class="col-md-6 col-sm-6 ">
                                    <input type="text" id="broker-name" name="broker-name" required="required" class="form-control">
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
                                    <form action="/uploads/broker" class="dropzone dz-clickable"><div class="dz-default dz-message">
                                    <span>
                                    <p>To Upload Broker Data in CSV Formatted Files, Drop Files Here</p>
                                    <p>Broker Data Format: </p>
                                    <p>format 1: <code>broker_code</code>, <code>broker_name</code></p>
                                    <p>format 2: <code>broker_id</code>, <code>broker_code</code>, <code>broker_name</code></p>
                                        </span>
                                    </div>
                                    </form>
        
        `
    })
    document.getElementById('brokers-list').addEventListener('click', async e => {

        let init_post = {
                method: "POST",
                headers: new Headers({'content-type': 'application/json'}),
                mode: "cors",
                credentials: "same-origin",
                cache: "no-cache"
        }

        let request = new Request('/dashboard/brokers', init_post);
        let response = await fetch(request);
        let json_data = await response.json();
        let brokers_list = json_data.payload;
        let brokers_dom_elements = brokers_list.map(broker => {
            let edit_link = `/data/broker/edit/${broker.broker_id}`
            return (
                `
                    <tr>
                        <td><input type="checkbox" value=${broker.broker_id}></td>
                        <td>${broker.broker_id}</td>
                        <td>${broker.broker_code}</td>
                        <td>${broker.broker_name}</td>
                        <td><a href=${edit_link}> Edit </a></td>
                    </tr>
                `
            )
        })
        document.getElementById('form_data').innerHTML = `
          <div class="row">
              <div class="col-sm-12">
                <div class="card-box table-responsive">
                <p class="text-muted font-13 m-b-30">
                  Click on a broker to edit details
                </p>
                <table id="datatable-checkbox" class="table table-striped table-bordered bulk_action" style="width:100%">
                  <thead>
                    <tr>                                  
                      <th><input type="checkbox" id="check-all" ></th>
                      <th>Broker ID</th>
                      <th>Broker Code</th>
                      <th>Broker Name</th>
                      <td>Action</td>
                    </tr>
                  </thead>
                  <tbody>
                    ${brokers_dom_elements}
                  </tbody>
              </table>
            </div>
          </div>                
        `
    })
});