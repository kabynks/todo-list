var initialize = function () {
    // console.log('initialize called')
    $('input[name="text"]').on('keypress', function() {
        console.log('list.js loaded')
        $('.has-error').hide();
    });
};
// console.log('list.js loaded')