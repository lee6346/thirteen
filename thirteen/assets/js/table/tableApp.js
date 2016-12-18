angular.module('ttTableApp', []);

angular.module('ttTableApp')
    .controller('ttTableController', function($scope, $http){

        console.log('loaded the table controller!');

        var cards = [
            {
                suit: 0,
                rank: 0
            },
            {
                suit: 0,
                rank: 1
            },
            {
                suit: 0,
                rank: 2
            },
        ];

        var cardSpriteMapper = function(cardsList){
            cardsList.forEach(function(card){
                card.x = card.rank*58;
                card.y = card.suit*77;
            })
        };

        cardSpriteMapper(cards);

        $scope.cards = cards;
    });