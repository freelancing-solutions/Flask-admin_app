

self.addEventListener('load', async e => {
    let init_post = {
            method: "POST",
            headers: new Headers({'content-type': 'application/json'}),
            mode: "cors",
            credentials: "same-origin",
            cache: "no-cache"
    }
    let reguest = new Request('/dashboard/stocks', init_post);
    let response = await fetch(reguest);
    console.log(response)
    let json_data = await response.json();
    let stocks_list = json_data.payload;
    let stocks_dom_model = stocks_list.map(stock => {
        let edit_link = `/data/stock/edit/${stock.stock_id}`
        let view_link = `/data/stock/view/${stock.stock_id}`
        return (
            `
                <tr>
                    <td><input type="checkbox" value=${stock.stock_id}></td>
                    <td>${stock.stock_id}</td>
                    <td>${stock.stock_code}</td>
                    <td>${stock.stock_name}</td>
                    <td>${stock.symbol}</td>
                    <td><a href=${edit_link} class="btn btn-sm btn-warning"> Edit </a>  <a href="${view_link}" class="btn btn-sm btn-primary"> View </a></td>
                </tr>
            `
        )
    })
    document.getElementById('stocks_list').innerHTML = `
                      <div class="row">
                          <div class="col-sm-12">
                            <div class="card-box table-responsive">
                            <p class="text-muted font-13 m-b-30">
                              Stocks Dashboard
                            </p>
                            <table id="datatable-checkbox" class="table table-striped table-bordered bulk_action" style="width:100%">
                              <thead>
                                <tr>                                  
                                  <th><input type="checkbox" id="check-all" ></th>
                                  <th>Stock ID</th>
                                  <th>Stock Code</th>
                                  <th>Stock Name</th>
                                  <td>Symbol</td>
                                  <td>Action</td>
                                </tr>
                              </thead>
                              <tbody>
                                ${stocks_dom_model}
                              </tbody>
                          </table>
                        </div>
                      </div>                
        `

});