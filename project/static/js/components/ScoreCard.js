var React = require("react");
var HoleScore = require("./HoleScore");

var ScoreCard = React.createClass({
    render: function() {
        var card = this.props.card;
        var holeNums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18];
        var holes = holeNums.map(function(holeNumber){
            return <HoleScore num={holeNumber} />
        });

        return (
            <div>
                <li>Scorecard: <small>{card.date.toLocaleString()}</small></li>
                {holes}
            </div>
        );
    }
});

module.exports = ScoreCard;