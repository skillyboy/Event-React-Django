import React, { Component } from "react";
import SingleEventPage from "./SingleEventPage";
import EventsPage from "./EventsPage";
import NewEventPage from "./NewEventPage";
import MyEventPage from "./MyEventPage";

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";

export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Router>
        <div>
          <nav>
            <ul>
              
              <li>
                <Link to="/">Home</Link>
              </li>

              <li>
                <Link to="/create/event">Create An Event </Link>
              </li>
              <li>
                <Link to="/events">All Events </Link>
              </li>
              <li>
                <Link to="/myevents"> My Events </Link>
              </li>

            </ul>
          </nav>

          <Switch>
            <Route exact path="/">
              <p>This is the home page</p>
            </Route>
            
            <Route path="/events" component={EventsPage} />
            <Route path="/create/event" component={NewEventPage} />
            <Route path="/myevents" component={MyEventPage} />

          </Switch>
        </div>
      </Router>
    );
  }
}

