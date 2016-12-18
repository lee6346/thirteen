// declare a new angular module
// second argument is an array that contains other angular modules
// in this particular case, the 3rd party library 'ui router'
angular.module('ttMainApp', [
    'ui.router',
    'ttLobbyApp', 'ttTableApp'
]);

// optional configuration, in this case, routing
angular.module('ttMainApp')
    .config([
        '$stateProvider', '$urlRouterProvider',
        function ($stateProvider, $urlRouterProvider) {

            // declare all the states (think URLs) we'll need here
            // with angular and ui router, each URL is associated to a 
            // separate HTML template
            var states = [
                {
                    name: 'lobby',
                    url: '/lobby',
                    templateUrl: '/partials/lobby',
                    controller: 'ttLobbyController'
                },
                {
                    name: 'table',
                    url: '/table/:id',
                    template: '<h1>welcome to a table</h1>'
                }
            ];

            // registering the state with ui router
            states.forEach(function (state) {
                $stateProvider.state(state);
            });

            // redirects
            $urlRouterProvider.when('', '/lobby');
        }]);