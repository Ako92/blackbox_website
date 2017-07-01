import React from 'react';
import ReactDOM from 'react-dom';
import Layout from "./pages/Layout";
import About from "./pages/About";
import Contact from "./pages/Contact";
import Customers from "./pages/Customers";
import Profiles from "./pages/Profiles";
import Pictures from "./pages/Pictures";
import Videos from "./pages/Videos";

import {Router, Route, Link,BrowserRouter } from "react-router-dom";

const app = document.getElementById('app');

ReactDOM.render(
    <BrowserRouter>

        <Route history={BrowserRouter} path="/" component={Layout}>
        </Route>
    
        </BrowserRouter>
    ,app);