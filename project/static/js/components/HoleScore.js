var React = require("react");


var HoleScore = React.createClass({
  render: function() {
     return(<span>
       <label for={this.props.num}>Hole {this.props.num}</label>
       <input type="number" min="1" name={this.props.num} />

       </span>)
  }

});

module.exports = HoleScore;