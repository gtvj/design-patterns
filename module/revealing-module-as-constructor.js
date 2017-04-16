var M = function () {

    // Private members
    var message = 'This is a message';

    function logMessage() {
        console.log(message);
    }

    // Public API
    return {
        logMessage: logMessage
    }
};

var module = new M();