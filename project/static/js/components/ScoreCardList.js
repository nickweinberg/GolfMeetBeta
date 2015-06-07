var React = require("react");
var ScoreCard = require("./ScoreCard");

// a list of last N scorecards
var ScoreCardList = React.createClass({
    getInitialState: function() {
        return {
            data: [{id: 1, date: 123}, {id:2, date:234}, {id: 3, date: 344}],
            page: 1,
            pages: 1
        }
    },
    render: function() {
        var cards = this.state.data.map(function(card) {
            console.log('hi');
           return <ScoreCard key={card.id} card={card} />
        });
        return (
            <div>
                <ul>
                    {cards}
                </ul>
            </div>
        );
    }
});

module.exports = ScoreCardList;