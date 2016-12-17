angular.module('ttLobbyApp', []);

angular.module('ttLobbyApp')
    .controller('ttLobbyController', function($scope) {

        console.log('loaded the main controller!');

        $scope.test = 'this is a test string';

        $scope.testFunction = function() {
            console.log('logging from a function!');
        }

        $scope.availableTables = [
            {
                Id: 1,
                AvailableSeats: 3,
                Name: 'tiger room'
            },
            {
                Id: 2,
                AvailableSeats: 2,
                Name: 'monkey room'
            },
            {
                Id: 3,
                AvailableSeats: 3,
                Name: 'dragon room'
            }
        ];

        $scope.change = 'this is binded to an input';

    });

