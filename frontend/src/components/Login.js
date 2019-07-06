import React, { Component } from 'react';
import axios from 'axios';
import './config';
import CryptoJS from "react-native-crypto-js";

class Login extends Component {

    constructor() {
        super();
        this.state = {
            name: "",
            password: ""
        };
        this.handleChange = this.handleChange.bind(this)
    }

    handleChange(event) {
        const {name, value} = event.target;
        this.setState({
            [name]: value
        })
    }

    onSubmit(e) {
        e.preventDefault(); // Prevent default so it doesn't refresh
        var password = CryptoJS.MD5(this.state.password);

        axios.post('http://localhost:2000/login', {
                user: this.state.name,
                password: password
            })
            .then(function (response) {
                if (response.data.token){
                    global.constants.token = response.data.token;
                    alert('You hvae successfully log in, now you can start to talk with Bot')
                }else{
                    alert(response.data)
                }
            })
            .catch(function (error) {
                alert('The system is under maintenance');
            });
    }

    render() {
        return (
            <div className="Input" id='loginform'>
                <form class='header item'  onSubmit={e => this.onSubmit(e)}>
                    <input type='text'
                           value={this.state.name}
                           name='name'
                           placeholder='name'
                           onChange={ this.handleChange }
                    />
                    <div>&nbsp;&nbsp;&nbsp;</div>
                    <input type='password'
                           value={this.state.password}
                           name='password'
                           placeholder='password'
                           onChange={ this.handleChange }
                    />
                    <button disabled={!this.state.name}>Login</button>
                    <div>&nbsp;&nbsp;&nbsp;</div>
                    Welcome
                    <div>&nbsp;&nbsp;&nbsp;</div>
                    <span>{this.state.name}</span>
                </form>
            </div>
        );
    }
}

export default Login;