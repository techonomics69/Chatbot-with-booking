import React, { Component } from 'react';
import ScrollableFeed from 'react-scrollable-feed'


class Messages extends Component {
    render() {
        const {messages} = this.props;
        return (
            <ScrollableFeed forceScroll={true}>
                <ul className="Messages-list" id="helo">
                    {messages.map(m => this.renderMsg(m))}
                </ul>
            </ScrollableFeed>
        );
    }

    renderMsg(message) {
        const {member, text} = message;
        //const {currentMember} = this.props;
        const className = member.username === "You" ? "Messages-message currentMember" : "Messages-message currentBot";
        return (
            <li className={className}>
                <span className="avatar" 
                style={{backgroundColor: member.color}}/>
                <div className="Message-content">
                    <div className="username">
                        {member.username}
                    </div>
                    <div className="text" id="text-move">{text}</div>
                </div>
            </li>
        )
    }
}

export default Messages;