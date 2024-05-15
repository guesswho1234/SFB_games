$(function () {
    checkFunction('session', 'checkAllSessions');
});

$(function () {
    checkFunction('setup', 'checkAllRooms');
});

$('#numParticipants input').change(function () {
    let value = $(this).val()

    // limit number of participants to min, max and multiples of min
	if(!isNaN(value) && value !== null && value !== "") {
		value = Math.max(minParticipants, value);
		value = Math.min(maxParticipants, value);
		value = value - value % minParticipants;

		$(this).val(value);
	} else {
	    $(this).val(minParticipants);
	}
})

function checkFunction(checkName, checkAllName) {
    // code for "checkAll" checkbox
    $('input[name=' + checkAllName + ']:visible').click(function () {
        $('input[name=' + checkName + ']:visible').prop('checked', $(this).prop('checked')).trigger("change")
    });

    // if all checkboxes are selected check also "checkAll" checkbox
    $('input[name=' + checkName + ']').change(function () {
        var check = ($("input[name=" + checkName + "]:checked:visible").length == $("input[name=" + checkName + "]:visible").length);
        $("input[name=" + checkAllName + "]:visible").prop('checked', check);
    })
}

$(function () {
    $('input[type=checkbox]').prop('checked', false);
    $('button').prop('disabled', true);

    // delete sessions
    let progressDivDeleteSessions = $('#delete-sessions-wait');

    $('input[name=session]').change(function () {
        var actionButton = $('#btn-delete-sessions');
        var numCheckedSessions = $('input[name=session]:checked').length;
        if (numCheckedSessions === 0) {
            actionButton.attr('disabled', true);
        } else {
            actionButton.attr('disabled', false);
        }
    })

    let socketDeleteSessions = makeReconnectingWebSocket("/delete_sessions");
    let $btnConfirmDelete = $('#btn-delete-sessions');

    $btnConfirmDelete.click(function (e) {
        progressDivDeleteSessions.show();
        $btnConfirmDelete.prop('disabled', true);

        session_codes = $('input[name="session"]').map(function(){
            if($(this).is(":checked"))
                return $(this).val();
        }).get();

        socketDeleteSessions.send(JSON.stringify(session_codes));
        e.preventDefault();
    });

    socketDeleteSessions.onmessage = function (message) {
        location.reload();
    }

    // reset rooms
    let progressDivSetupRooms = $('#reset-rooms-wait');

    $('input[name=setup]').change(function () {
        var actionButton = $('#reset-rooms-btn');
        var numCheckedSessions = $('input[name=setup]:checked').length;
        if (numCheckedSessions === 0) {
            actionButton.attr('disabled', true);
        } else {
            actionButton.attr('disabled', false);
        }
    })

    let $btnResetRooms = $('#reset-rooms-btn');

    $btnResetRooms.click(function (e) {
        progressDivSetupRooms.show();
        $btnResetRooms.prop('disabled', true);

        // list of sessions to set up
        let setupRoomSessionCallPromises = [];

        // homePage setup
        if ( $('#homePageRoomSettings .roomSession').is(":checked") ) {
            homePage_session_config = $('#homePageRoomSettings .roomSession').data("session-config");
            homePage_room_name = $('#homePageRoomSettings .roomSession').data("room-name");
            homePage_num_participants = parseInt($('#numParticipants input').val());

            setupRoomSessionCallPromises.push(new Promise(function (resolve, reject) {
                setupRoomSession(resolve, reject, homePage_session_config, homePage_room_name, homePage_num_participants);
            }));
        }

        // games setup
        $('.gameRoomSetting').each(function(){
            if ( !$(this).find('.roomSession').is(":checked") )
                return;

            game_session_config = $(this).find('.roomSession').data("session-config");
            game_room_name = $(this).find('.roomSession').data("room-name");
            game_num_participants = parseInt($('#numParticipants input').val());

            // set up sessions and collect promises
            setupRoomSessionCallPromises.push(new Promise(function (resolve, reject) {
                setupRoomSession(resolve, reject, game_session_config, game_room_name, game_num_participants);
            }));
        })

        // reload page once all sessions have been set up (all promises resolved or rejected)
        Promise.all(setupRoomSessionCallPromises).then(values => {
            location.reload();
        }).catch(error => {
            location.reload();
        });

        e.preventDefault();
    });

    // create sessions with websocket
    function setupRoomSession(resolve, reject, session_config, room_name, num_participants) {
        let socketCreateSession = makeReconnectingWebSocket("/create_session");
        let form_data = {
            session_config: session_config,
            room_name: room_name,
            num_participants: num_participants
        }

        socketCreateSession.send(JSON.stringify(form_data));

        socketCreateSession.onmessage = function (message) {
            resolve(true);
        }
    }
});

// minimal view
function minView() {
    $("#top_menu").hide();
    $("#minView").hide();
    $("#fullView").show();
}

// full view
function fullView() {
    $("#top_menu").show();
    $("#minView").show();
    $("#fullView").hide();
}

$('body').on('click', '#minView', function() {
	minView();
});

$('body').on('click', '#fullView', function() {
	fullView();
});
