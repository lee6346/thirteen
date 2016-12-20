angular.module('ttLobbyApp', []);

angular.module('ttLobbyApp')
    .service('ttLobbyHttpService', function ($http) {
        return {
            getTables: function () {
                return $http({
                    method: 'GET',
                    url: '/gettable'
                });
            },
            createTable: function(tableName) {
                return $http({
                    method: 'POST',
                    url: '/gettable'
                });
            }
        };
    });

angular.module('ttLobbyApp')
    .controller('ttLobbyController', function ($scope, ttLobbyHttpService) {

        $scope.Contents = {
            availableTables: []
        }

        $scope.Functions = {
            createTable: function() {
                console.log('clicked create table');
            }
        }
        //!!ajax call 
        ttLobbyHttpService.getTables()
            .then(function (data) {
                console.log('data returned from call', data);
                $scope.Contents.availableTables = JSON.parse(data.data);  //!!referenced by  ng-repeat
            });

    });

