$('#HSQr').click(function () {
    hideShow('qr');
});

$('#qr .popupClose').click(function () {
    hideShow('qr');
});

$('#HSSettings').click(function () {
    hideShow('settings');
});

$('#settings .popupClose').click(function () {
    hideShow('settings');
});

$(document).keyup(function(e) {
    if(e.key === "Escape") {
        $('.popupContainer').hide();
    }
});

hideShow = function(id) {
    let x = document.getElementById(id)
    if (x.style.display === "none") {
        x.style.display = "grid";
        $('body').css('overflow', 'hidden');
    } else {
        x.style.display = "none";
        $('body').css('overflow', 'auto');
    }
}

$('#participantLabel input').prop('checked', false);

$('#participantLabel input').filter(function() {
    return $(this).val() == colorCodeSelected;
}).prop('checked', true);

