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
        '$stateProvider', '$urlRouterProvider', '$httpProvider',
        function ($stateProvider, $urlRouterProvider, $httpProvider) {

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
                    templateUrl: '/partials/table',
                    controller: 'ttTableController'
                }
            ];

            // registering the state with ui router
            states.forEach(function (state) {
                $stateProvider.state(state);
            });

            // redirects
            $urlRouterProvider.when('', '/lobby');

            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
            $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        }]);