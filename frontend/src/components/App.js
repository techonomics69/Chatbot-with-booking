import React from 'react';
import Header from './Header';
import Messages from './Messages';
import Input from './Input';
import './App.css';


class App extends React.Component {
  state = {
    messages: [],
    member: {
      username: "You",
      color: "#fb7f0a"
    },
    Bot: {
      username: "Bot",
      color: "rgb(38, 126, 204)"
    }
  }

  onSendMessage = (message, auth) => {
    const messages = this.state.messages;
    if (auth === "User") {
        messages.push({
          text: message,
          member: this.state.member
      })
    }
    if (auth === "Bot") {
        messages.push({
          text: message,
          member: this.state.Bot
        })
    }
    this.setState({messages: messages})
  }

  render() {
    return (
      <div className="App">
        <Header/>
        <Messages
          messages={this.state.messages}
          currentMember={this.state.member}
        />
        <Input
          onSendMessage={this.onSendMessage}
        />
      </div>
    );
  }
}

export default App;
