var React = require("react");

var ScoreCard = React.createClass({
    render: function() {
        var card = this.props.card;

        return (
            <li>Scorecard: <small>{card.date.toLocaleString()}</small></li>
        );
    }
});

module.exports = ScoreCard;