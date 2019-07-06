import React, {Component} from 'react';
import axios from 'axios';
import './config';

class Input extends Component {
    state = {
        text: ""
    };

    render() {
        return (
            <div className="Input">
                <form onSubmit={e => this.onSubmit(e)}>
                    <input
                        onChange={e => this.onChange(e)}
                        value={this.state.text}
                        type="text"
                        placeholder="Ask here and press ENTER to send"
                        autoFocus="true"
                    />
                    <button disabled={!this.state.text}>Send</button>
                </form>
            </div>
        );
    }

    /* Events */
    onChange(e) {
        this.setState({text: e.target.value});
    }


    onSubmit(e) {
        var _this = this;
        e.preventDefault(); // Prevent default so it doesn't refresh
        this.setState({text: ""});
        var reg = /~/;
        var result = reg.test(this.state.text);
        if (result) {
            var time = this.state.text.split("~")[0];
            var confirms = window.confirm("Are you sure to cancel " + time + " ?");
            if (confirms) {
                axios.post('http://localhost:2000/webhook', {
                        text: this.state.text,
                        token: global.constants.token
                    })
                    .then(function (response) {
                        var __this = _this;
                        __this.props.onSendMessage(response.data, "Bot");
                    })
                    .catch(function (error) {
                        var __this = _this;
                        __this.props.onSendMessage("The system is under maintenance.....", "Bot");
                    });
                _this.props.onSendMessage(this.state.text, "User");
            }
        }else{
            axios.post('http://localhost:2000/webhook', {
                    text: this.state.text,
                    token: global.constants.token
                })
                .then(function (response) {
                    var __this = _this;
                    __this.props.onSendMessage(response.data, "Bot");
                })
                .catch(function (error) {
                    var __this = _this;
                    __this.props.onSendMessage("The system is under maintenance.....", "Bot");
                });
            _this.props.onSendMessage(this.state.text, "User");
        }
    }
}

export default Input;