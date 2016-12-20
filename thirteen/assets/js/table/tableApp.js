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
                card.backgroundPosition = (card.rank * 58) + 'px ' + (card.suit * 77) + 'px';
            })
        };

        cardSpriteMapper(cards);

        $scope.cards = cards;
    });