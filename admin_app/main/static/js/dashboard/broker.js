

self.addEventListener('load', async e => {
    let init_post = {
            method: "POST",
            headers: new Headers({'content-type': 'application/json'}),
            mode: "cors",
            credentials: "same-origin",
            cache: "no-cache"
    }
    let reguest = new Request('/dashboard/brokers', init_post);
    let response = await fetch(reguest);
    let json_data = await response.json();
    let brokers_list = json_data.payload;
    let brokers_dom_elements = brokers_list.map(broker => {
        let edit_link = `/data/broker/edit/${broker.broker_id}`
        let view_link = `/data/broker/view/${broker.broker_id}`
        return (
            `
                <tr>
                    <td><input type="checkbox" value=${broker.broker_id}></td>
                    <td>${broker.broker_id}</td>
                    <td>${broker.broker_code}</td>
                    <td>${broker.broker_name}</td>
                    <td><a class="btn btn-warning btn-sm" href=${edit_link}> Edit </a> <a class="btn btn-sm btn-primary"  href=${view_link}> View</a></td>
                </tr>
            `
        )
    })
    document.getElementById('brokers_list').innerHTML = `
              <div class="row">
                  <div class="col-sm-12">
                    <div class="card-box table-responsive">
                    <p class="text-muted font-13 m-b-30">
                      The information above is for all brokers / stats for single brokers are accessible on view
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
});