angular.module('ttLobbyApp', []);

angular.module('ttLobbyApp')
    .controller('ttLobbyController', function($scope, $http) {

        console.log('loaded the main controller!');

        $scope.test = 'this is a test string';

        $scope.testFunction = function() {
            console.log('logging from a function!');
        }

        $scope.availableTables = [];

        $scope.change = 'this is binded to an input';
        //!!ajax call 
        $http({
            method: 'GET',
            url: '/gettable'
        })
            .then(function(data) {
                console.log('data returned from call', data);
                $scope.availableTables = data.data;  //!!referenced by  ng-repeat


            });

    });

