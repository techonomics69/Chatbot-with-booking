import React from 'react';
import Login from './Login';

const Header = () => {

    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0');
    var yyyy = today.getFullYear();

    today = dd + '/' + mm + '/' + yyyy;
    return (
      <div className="ui pointing menu App-header" id="header">
        <div class="header item">
            Dentist Appointment
        </div>
        <Login/>
        <div class="header item">
            Today is
            <br/>
            {today}
        </div>
      </div>
    );
  };
  
export default Header;