angular.module('ttTableApp', []);

angular.module('ttTableApp')
    .controller('ttTableController', function($scope, $http){

        console.log('loaded the table controller!');

        var cards = [
            {
                suit: 0,
                rank: 1
            }
        ];

        var cardSpriteMapper = function(cardsList){
            cardsList.forEach(function(card){
                card.x = rank*58;
                card.y = suit*77;
            })
        };

        cardSpriteMapper(cards);
    });