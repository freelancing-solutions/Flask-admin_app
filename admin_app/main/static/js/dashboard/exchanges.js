self.addEventListener('load', async e => {
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
    let exchange_list = json_response.payload
    let exchange_dom_elements = exchange_list.map(exchange => {
        let exchange_edit = `/data/exchange/edit/${exchange.exchange_id}`
        let exchange_view = `/data/exchange/view/${exchange.exchange_id}`
        return (
            `
                <tr>
                    <td><input type="checkbox" value=${exchange.exchange_id}></td>
                    <td>${exchange.exchange_country}</td>
                    <td>${exchange.exchange_country}</td>
                    <td>
                        <a class="btn btn-sm btn-warning" href=${exchange_edit}> Edit </a>
                        <a class="btn btn-sm btn-primary" href=${exchange_view}> View </a>
                    </td>
                </tr>
            `
        )
    })
    /*** loading the datatable **/
    document.getElementById('exchanges_list').innerHTML = `
      <div class="row">
          <div class="col-sm-12">
            <div class="card-box table-responsive">
            <p class="text-muted font-13 m-b-30">
              Exchange Dashboard
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
});