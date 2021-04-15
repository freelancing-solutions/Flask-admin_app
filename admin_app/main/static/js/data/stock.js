
self.addEventListener('load', e => {
    // TODO - listen for form input
    // TODO take data and send to backend
    let stock_id = document.getElementById('stock-id')
    let stock_code = document.getElementById('stock-code')
    let stock_name = document.getElementById('stock-name')
    let symbol = document.getElementById('symbol')
    document.getElementById('submit-button').addEventListener('click', async e => {
        e.preventDefault();
        let init_post = {
                method: "POST",
                headers: new Headers({'content-type': 'application/json'}),
                mode: "cors",
                body: JSON.stringify({stock_id: stock_id.value, stock_code: stock_code.value, stock_name: stock_name.value, symbol:symbol.value}),
                credentials: "same-origin",
                cache: "no-cache"
        }
        let response = await fetch(new Request(url='/data/stock', init_post));
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

    document.getElementById('add-stock').addEventListener('click', async e => {
        document.getElementById('form_data').innerHTML = `
                                        <br />
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
                                            <label class="col-form-label col-md-3 col-sm-3 label-align" for="stock-id">Stock ID <span class="required">*</span></label>
                                            <div class="col-md-6 col-sm-6 ">
                                                <input type="text" id="stock-id"  class="form-control ">
                                            </div>
                                        </div>
                                        
                                        <div class="item form-group">
                                            <label class="col-form-label col-md-3 col-sm-3 label-align" for="stock-code">Stock Code <span class="required">*</span></label>
                                            <div class="col-md-6 col-sm-6 ">
                                                <input type="text" id="stock-code" required="required" class="form-control ">
                                            </div>
                                        </div>
                                        <div class="item form-group">
                                            <label class="col-form-label col-md-3 col-sm-3 label-align" for="stock-name">Stock Name <span class="required">*</span></label>
                                            <div class="col-md-6 col-sm-6 ">
                                                <input type="text" id="stock-name" name="broker-name" required="required" class="form-control">
                                            </div>
                                        </div>
                                        <div class="item form-group">
                                            <label class="col-form-label col-md-3 col-sm-3 label-align" for="symbol">Symbol <span class="required">*</span></label>
                                            <div class="col-md-6 col-sm-6 ">
                                                <input type="text" id="symbol" name="symbol" required="required" class="form-control">
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
                                        </form>
                                        <div class="ln_solid"></div>
                                        <div class="item form-group" id="message">                                        
                                        </div>
                                        <div class="ln_solid"></div>
                                            <form action="/uploads/stock" class="dropzone dz-clickable">
                                                <div class="dz-default dz-message">
                                                <span>
                                                    <p>To Upload Stock Data in CSV Formatted Files, Drop Files Here..</p>
                                                    <p>Stock Data Format</p>
                                                    <p>Format 1: <code>stock_code</code>, <code>stock_name</code>, <code>symbol</code></p>
                                                    <p>Format 2: <code>stock_id</code>, <code>stock_code</code>, <code>stock_name</code>, <code>symbol</code></p>
                                                </span>
                                                </div>
                                            </form>
        
        `
    })
    document.getElementById('stocks-list').addEventListener('click', async e => {
        let init_post = {
                method: "POST",
                headers: new Headers({'content-type': 'application/json'}),
                mode: "cors",
                credentials: "same-origin",
                cache: "no-cache"
        }
        let reguest = new Request('/dashboard/stocks', init_post);
        let response = await fetch(reguest);
        let json_response = await response.json();
        let stocks_list = []
        if (json_response.status){
            stocks_list = json_response.payload;
        }
        let stocks_dom_list = stocks_list.map(stock => {
            let stock_edit = `/data/stock/edit/${stock.stock_id}`
            return (
                `
                    <tr>
                        <td><input type="checkbox" value=${stock.stock_id} /></td>
                        <td>${stock.stock_id}</td>
                        <td>${stock.stock_name}</td>
                        <td>${stock.stock_code}</td>
                        <td>${stock.symbol}</td>
                        <td><a href=${stock_edit}> Edit </a></td>
                    </tr>
                `
            )
        });

        document.getElementById('form_data').innerHTML = `
                      <div class="row">
                          <div class="col-sm-12">
                            <div class="card-box table-responsive">
                            <p class="text-muted font-13 m-b-30">
                              Click on a Stock to edit details
                            </p>
                            <table id="datatable-checkbox" class="table table-striped table-bordered bulk_action" style="width:100%">
                              <thead>
                                <tr>                                  
                                  <th><input type="checkbox" id="check-all" ></th>
                                  <th>Stock ID</th>
                                  <th>Stock Name</th>
                                  <th>Stock Code</th>
                                  <td>Symbol</td>
                                  <td>Action</td>
                                </tr>
                              </thead>
                              <tbody>
                                ${stocks_dom_list}
                              </tbody>
                          </table>
                        </div>
                      </div>                        
        
        `


    })
});