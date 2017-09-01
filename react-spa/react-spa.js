var destination = document.querySelector("#container");
var { Router,
      Route,
      IndexRoute,
      IndexLink,
      Link } = ReactRouter;

var Home = React.createClass({
  render: () =>
        <div>
          <h3>Welcome to the home page!</h3>
        </div>
});

let Contact = React.createClass({
  render: function() {
      return (
        <div>
          <div className="friendbuy-bje-dmg"></div>
        </div>
      );
    },

  componentDidMount: () => {
    const script = document.createElement("script");

    script.innerHTML = 'window["friendbuy"].push(["widget", "bje-dmg"]);';
    script.async = true;

    document.body.appendChild(script);
  }
});

var Stuff = React.createClass({
  render: () => <span className="stuff"><div><h3>There’s stuff on this page!</h3></div></span>
});

let App = React.createClass({
  render: function() {
    return (
      <div>
        <h1>Simple React-Based Single-Page Application</h1>
        <ul className="header">
          <li><IndexLink to="/" activeClassName="active">Home</IndexLink></li>
          <li><Link to="/stuff" activeClassName="active">Stuff</Link></li>
          <li><Link to="/contact" activeClassName="active">Contact</Link></li>
        </ul>
        <div className="content">
          <p>This single-page app is implemented with React. You should see a widget on
            the <Link to="/contact">Contact</Link> page regardless of how you get to it
            (whether by direct load or by clicking a link).</p>

          {this.props.children}
        </div>
      </div>
    )
  }
});

ReactDOM.render(
  <Router>
    <Route path="/" component={App}>
      <IndexRoute component={Home}/>
      <Route path="stuff" component={Stuff} />
      <Route path="contact" component={Contact} />
    </Route>
  </Router>,
  destination
);
