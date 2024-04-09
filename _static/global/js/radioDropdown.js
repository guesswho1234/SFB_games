$('body').on('click', '.dropdown-content li label', function() {
    toggleDropdown(this);
});

$('body').on('click', '.dropdownSelectedPlaceholder', function() {
    $(this).hide();
    toggleDropdown(this);
});

function toggleDropdown(element){
    $(element).closest('.dropdown-wrapper').toggleClass('active');
}
