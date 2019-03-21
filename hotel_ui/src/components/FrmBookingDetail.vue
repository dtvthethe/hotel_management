<template>
  <form role="form">
    <!-- Nav tabs -->
    <ul class="nav nav-tabs" role="tablist">
      <li role="presentation" class="active">
        <a
          href="#reservation"
          aria-controls="reservation"
          role="tab"
          data-toggle="tab"
        >Reservation Info</a>
      </li>
      <li role="presentation">
        <a href="#extracharge" aria-controls="extracharge" role="tab" data-toggle="tab">Extra Charge</a>
      </li>
      <li role="presentation">
        <a href="#foliodetail" aria-controls="foliodetail" role="tab" data-toggle="tab">Folio Detail</a>
      </li>
    </ul>

    <!-- Tab panes -->
    <div class="tab-content">
      <!-- reservation -->
      <div role="tabpanel" class="tab-pane active" id="reservation">
        <div class="row">
          <div class="col-md-6 col-sm-12">
            <fieldset>
              <legend class>Booking Infomation</legend>
              <div class="form-group col-md-6">
                <label for="booking-code">Booking Code</label>
                <input type="text" class="form-control m-bot15" id="booking-code" maxlength="20">
              </div>
              <div class="form-group col-md-6">
                <label for="client">Client</label>
                <select class="form-control m-bot15" id="client">
                  <option>Option 1</option>
                  <option>Option 2</option>
                  <option>Option 3</option>
                </select>
              </div>
              <div class="form-group col-md-6">
                <label for="room-type">Room Type</label>
                <select class="form-control m-bot15" id="room-type">
                  <option>Option 1</option>
                  <option>Option 2</option>
                  <option>Option 3</option>
                </select>
              </div>
              <div class="form-group col-md-6">
                <label for="room">Room</label>
                <select class="form-control m-bot15" id="room">
                  <option>Option 1</option>
                  <option>Option 2</option>
                  <option>Option 3</option>
                </select>
              </div>
              <div class="form-group col-md-6">
                <label for="adult">Adult</label>
                <input
                  class="form-control m-bot15"
                  type="number"
                  min="1"
                  max="100"
                  value="1"
                  id="adult"
                >
              </div>
              <div class="form-group col-md-3">
                <label for="child">Child</label>
                <input
                  class="form-control m-bot15"
                  type="number"
                  min="1"
                  value="1"
                  max="100"
                  id="child"
                >
              </div>
              <div class="checkbox col-md-3">
                <label>
                  <input type="checkbox" value>
                  Breakfast
                </label>
              </div>
              <div class="form-group col-md-6">
                <label for="room-rate">Room Rate</label>
                <input class="form-control m-bot15" type="number" min="0" value="0" id="room-rate">
              </div>
              <div class="form-group col-md-6">
                <i>25,000 (VND)</i>
              </div>
              <div class="form-group col-md-12">
                <label for="note">Note</label>
                <textarea class="form-control" rows="3" id="note" maxlength="500"></textarea>
              </div>
            </fieldset>
          </div>
          <div class="col-md-6 col-sm-12">
            <fieldset>
              <legend class>Stay Infomation</legend>
              <div class="form-group col-md-6">
                <label id="dt-arrive-date">Arrive Date</label>
                <Datepicker
                  id="dt-arrive-date"
                  format="dd/MM/yyyy"
                  @selected="onSelectDateArrive"
                  :disabledDates="disabledDatesArrive"
                ></Datepicker>
              </div>
              <div class="form-group col-md-6">
                <label for="dt-depart-date">DepartDate</label>
                <Datepicker
                  id="dt-depart-date"
                  format="dd/MM/yyyy"
                  @selected="onSelectDateDepart"
                  :disabledDates="disabledDatesDepart"
                ></Datepicker>
              </div>
              <div class="form-group col-md-12">
                <div class="form-group">
                  <label for="night">Night(s)</label>
                  <input
                    class="form-control m-bot15"
                    disabled
                    type="number"
                    min="0"
                    value="0"
                    id="night"
                  >
                </div>
              </div>
            </fieldset>
            <fieldset>
              <legend class>Guest Infomation</legend>
              <div class="form-group col-md-12">
                <label for="fullname">Full Name</label>
                <input type="text" class="form-control m-bot15" id="fullname" maxlength="150">
              </div>
            </fieldset>
          </div>
        </div>
      </div>
      <!-- //reservation -->
      <!-- extracharge -->
      <div role="tabpanel" class="tab-pane" id="extracharge">
        <button data-toggle="modal" class="btn btn-sm btn-default">Add</button>

        <table class="table table-fixed table-minibar">
          <thead>
            <tr>
              <th class="col-md-2">Date</th>
              <th class="col-md-2">Product</th>
              <th class="col-md-2">Quantity</th>
              <th class="col-md-2">Price</th>
              <th class="col-md-2">Total</th>
              <th class="col-md-2">Option</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">johndoe@email.com</td>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">
                a
                a
              </td>
            </tr>
            <tr>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">johndoe@email.com</td>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">
                a
                a
              </td>
            </tr>
            <tr>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">johndoe@email.com</td>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">
                a
                a
              </td>
            </tr>
            <tr>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">johndoe@email.com</td>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">
                a
                a
              </td>
            </tr>
            <tr>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">johndoe@email.com</td>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">
                a
                a
              </td>
            </tr>
            <tr>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">johndoe@email.com</td>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">
                a
                a
              </td>
            </tr>
            <tr>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">johndoe@email.com</td>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">
                a
                a
              </td>
            </tr>
            <tr>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">johndoe@email.com</td>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">
                a
                a
              </td>
            </tr>
            <tr>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">johndoe@email.com</td>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">
                a
                a
              </td>
            </tr>
            <tr>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">johndoe@email.com</td>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">
                a
                a
              </td>
            </tr>
            <tr>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">johndoe@email.com</td>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">
                a
                a
              </td>
            </tr>
            <tr>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">johndoe@email.com</td>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">
                a
                a
              </td>
            </tr>
            <tr>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">johndoe@email.com</td>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">
                a
                a
              </td>
            </tr>
            <tr>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">johndoe@email.com</td>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">
                a
                a
              </td>
            </tr>
            <tr>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">johndoe@email.com</td>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">
                a
                a
              </td>
            </tr>
            <tr>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">johndoe@email.com</td>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">
                a
                a
              </td>
            </tr>
            <tr>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">johndoe@email.com</td>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">
                a
                a
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <!-- //extracharge -->
      <!-- foliodetail -->
      <div role="tabpanel" class="tab-pane" id="foliodetail">
        <fieldset>
          <legend class>Payment</legend>
          <div class="col-md-12"> 
            <input type="button" class="btn btn-default" value="Add Payment" @click="controlModal"/>
          </div>
          <div class="col-md-10">
            <table class="table table-fixed table-payment">
              <thead>
                <tr>
                  <th class="col-md-2">Date</th>
                  <th class="col-md-2">Product</th>
                  <th class="col-md-2">Quantity</th>
                  <th class="col-md-2">Price</th>
                  <th class="col-md-2">Total</th>
                  <th class="col-md-2">Option</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="col-md-2">
            <p>
              Balance:
              <i>0</i>
            </p>
          </div>
        </fieldset>

        <fieldset>
          <legend class>All Guest Transactions</legend>
          <button data-toggle="modal" class="btn btn-warning btn-sm">Add Room Charge</button>
          <button data-toggle="modal" class="btn btn-default btn-sm">Folio Tranfer</button>
          <table class="table table-fixed table-transaction">
            <thead>
              <tr>
                <th class="col-md-2">Date</th>
                <th class="col-md-2">Product</th>
                <th class="col-md-2">Quantity</th>
                <th class="col-md-2">Price</th>
                <th class="col-md-2">Total</th>
                <th class="col-md-2">Option</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">johndoe@email.com</td>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">
                  a
                  a
                </td>
              </tr>
              <tr>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">johndoe@email.com</td>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">
                  a
                  a
                </td>
              </tr>
              <tr>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">johndoe@email.com</td>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">
                  a
                  a
                </td>
              </tr>
              <tr>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">johndoe@email.com</td>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">
                  a
                  a
                </td>
              </tr>
              <tr>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">johndoe@email.com</td>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">
                  a
                  a
                </td>
              </tr>
              <tr>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">johndoe@email.com</td>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">
                  a
                  a
                </td>
              </tr>
              <tr>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">johndoe@email.com</td>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">
                  a
                  a
                </td>
              </tr>
              <tr>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">johndoe@email.com</td>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">
                  a
                  a
                </td>
              </tr>
              <tr>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">johndoe@email.com</td>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">
                  a
                  a
                </td>
              </tr>
              <tr>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">johndoe@email.com</td>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">
                  a
                  a
                </td>
              </tr>
              <tr>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">johndoe@email.com</td>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">
                  a
                  a
                </td>
              </tr>
              <tr>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">johndoe@email.com</td>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">
                  a
                  a
                </td>
              </tr>
              <tr>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">johndoe@email.com</td>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">
                  a
                  a
                </td>
              </tr>
              <tr>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">johndoe@email.com</td>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">
                  a
                  a
                </td>
              </tr>
              <tr>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">johndoe@email.com</td>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">
                  a
                  a
                </td>
              </tr>
              <tr>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">johndoe@email.com</td>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">
                  a
                  a
                </td>
              </tr>
              <tr>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">johndoe@email.com</td>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">
                  a
                  a
                </td>
              </tr>
            </tbody>
          </table>
        </fieldset>
      </div>
      <!-- foliodetail -->
    </div>

    <button type="submit" class="btn btn-info">Submit</button>

    <!-- Modal -->
<div id="secondModal" class="modal fade col-md-6 col-md-offset-3 second-modal" :class="{in:modal.modalShow}" :style="{display:modal.display}" role="dialog">
  <div class="modal-dialog">

    <!-- Modal content-->
    <div class="modal-content">
      <div class="modal-header">
        <input type="button" class="close" value="×" @click="controlModal" />
        <h4 class="modal-title">Modal Header</h4>
      </div>
      <div class="modal-body">
        <p>Some text in the modal.</p>
      </div>
      <div class="modal-footer">
        <input type="button" class="btn btn-default" value="Close" @click="controlModal" />
      </div>
    </div>

  </div>
</div>

  </form>
</template>
<script>
import Datepicker from "vuejs-datepicker";

export default {
  name: "FrmBookingDetail",
  components: {
    Datepicker
  },
  data: function() {
    return {
      disabledDatesArrive: {
        from: null
      },
      disabledDatesDepart: {
        to: null
      },
      modal: {
        modalShow: false,
        display: 'none'
      },
    };
  },
  methods: {
    onSelectDateArrive: function(event) {
      this.disabledDatesDepart.to = event;
    },
    onSelectDateDepart: function(event) {
      this.disabledDatesArrive.from = event;
    },
    controlModal:function(){
      this.modal.modalShow = !this.modal.modalShow;
      if(this.modal.display === 'none'){
        this.modal.display = 'block';
      }
      else{
        this.modal.display = 'none';

      }
    }
  }
};
</script>



<style>
.table-minibar tbody {
  height: 350px;
}
.table-payment tbody {
  height: 100px;
}
.table-transaction tbody {
  height: 130px;
}
.table-fixed {
  width: 100%;
}
.table-fixed tbody {
  overflow-y: auto;
  width: 100%;
}
.table-fixed thead,
.table-fixed tbody,
.table-fixed tr,
.table-fixed td,
.table-fixed th {
  display: block;
}

.table-fixed tbody td {
  float: left;
}
.table-fixed thead tr th {
  float: left;
}
.table td,
.table > tbody > tr > td {
  padding: 7px !important;
}
.table > thead > tr > th {
  padding: 7px !important;
}
.second-modal{
  height: 200px;
}
</style>
