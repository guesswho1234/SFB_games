$('#id_result input').prop("checked",false);

$('.resultButton').click(function() {
    $('#id_result input[value="' + $(this).attr('id') + '"]').prop("checked",true);
    $('#next').click();
});

let segments = [];
for (var i = 0; i < numSegments; i++) {
    segments.push({
        // available fields: fillStyle, text, textFontSize, textFillStyle
        'fillStyle' : '#' + colors[i % colors.length],
        'text' : ''
    });
}

// Create new wheel object specifying the parameters at creation time.
let theWheel = new Winwheel({
    'outerRadius'     : 124,//212,                                                                              // Set outer radius so wheel fits inside the background.
    'innerRadius'     : 10,                                                                                     // Make wheel hollow so segments don't go all way to center.
    'textFontSize'    : 24,                                                                                     // Set default font size for the segments.
    'textOrientation' : 'vertical',                                                                             // Make text vertial so goes down from the outside of wheel.
    'textAlignment'   : 'outer',                                                                                // Align text to outside of wheel.
    'numSegments'     : numSegments,                                                                            // Specify number of segments.
    'segments'        : segments,                                                                               // Define segments including colour and text.
    'animation' :                                                                                               // Specify the animation to use.
    {
        'type'     : 'spinToStop',
        'duration' : 10,                                                                                        // Duration in seconds.
        'spins'    : 3,                                                                                         // Default number of complete spins.
        'callbackFinished' : result,
        'soundTrigger'     : 'pin'                                                                              // Specify pins are to trigger the sound, the other option is 'segment'.
    },
    'pins' :				                                                                                    // Turn pins on.
    {
        'number'     : numSegments,
        'fillStyle'  : 'silver',
        'outerRadius': 4,
    }
});

let wheelPower    = 0;
let wheelSpinning = false;

function startSpin()
{
    if (wheelSpinning == false) {
        $('#spin').addClass("disabled");
        theWheel.animation.spins = Math.max(1, Math.floor(Math.random() * 10));
        theWheel.startAnimation();
        wheelSpinning = true;
    }
}

function resetWheel()
{
    theWheel.stopAnimation(false);      // Stop the animation, false as param so does not call callback function.
//    theWheel.rotationAngle = 0;       // Re-set the wheel angle to 0 degrees.
    theWheel.draw();                    // Call draw to render changes to the wheel.
    wheelSpinning = false;              // Reset to false to power buttons and spin can be clicked again.
    $('#spin').removeClass("disabled");
}

function result(indicatedSegment)
{
//    resetWheel();
    $('#id_result input[value="' + indicatedSegment.fillStyle.substring(1) + '"]').prop("checked",true);
    $('#next').click();
}
