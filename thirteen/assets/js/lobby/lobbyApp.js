angular.module('ttLobbyApp', ['ui.bootstrap', 'ttModalApp', 'ui.router']);

angular.module('ttLobbyApp')
    .service('ttLobbyHttpService', function ($http) {
        return {
            getTables: function () {
                return $http({
                    method: 'GET',
                    url: '/gettable'
                })
                    .then(function (data) {
                        return JSON.parse(data.data);
                    });
            }
        };
    });

angular.module('ttLobbyApp')
    .controller('ttLobbyController', function ($scope, ttLobbyHttpService, $uibModal, $state) {

        $scope.Contents = {
            availableTables: []
        }

        $scope.Functions = {
            createTable: function () {
                var modalInstance = $uibModal.open({
                    //animation: $ctrl.animationsEnabled,
                    templateUrl: '/partials/CreateTableModal',
                    controller: 'ttCreateTableModalController',
                    //controllerAs: '$ctrl',
                    //size: size,
                    //appendTo: parentElem
                })
                    .result.then(function(tableId) {
                        console.log('tableId in controller after closing', tableId)
                        $state.go('table', {id: tableId})
                    });
            }
        }
        //!!ajax call 
        ttLobbyHttpService.getTables()
            .then(function (tables) {
                $scope.Contents.availableTables = tables;
            });


    });

