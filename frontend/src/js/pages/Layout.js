import React from "react";
import { Link } from "react-router-dom";

export default class Layout extends React.Component {
    render(){
        return (
            <div>
                {this.props.children}
                <Link to="/">Home</Link>
                <Link to="/#about"> About</Link>
                <Link to="/#contact"> Contact</Link>
                <Link to="/#pictures"> Pictures</Link>
                <Link to="/#videos"> Videos</Link>
                <Link to="/#customers"> Customers</Link>
                <Link to="/#profiles"> Profiles</Link>
            </div>
        );
    }
}