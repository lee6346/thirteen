angular.module('ttModalApp', []);

angular.module('ttModalApp')
    .controller('ttCreateTableModalController', function ($scope, $uibModalInstance, $http) {

        $scope.Contents = {
            Name: ''   
        }
        $scope.Functions = {
            Create: function () {
                $http.post('/CreateTable/', $scope.Contents.Name)
                    .then(function(){

                    });
            },
            Cancel: function () {
                $uibModalInstance.dismiss();
            }
        }

        

    });