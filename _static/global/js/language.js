window.addEventListener('load', function () {
    f_setLanguage();
})

$('#languageSwitchContainer span').click(function () {
    let lang = $(this).text().toLowerCase().trim();

    if (lang == "|")
	    lang = "en"

	setLanguageCookie(lang);
	f_setLanguage();
});

function f_setLanguage() {
	let lang = getLanguageCookie();

	if (lang === null)
	    lang = "en"

    $('.langElement').hide();
	$('html').attr('lang', lang);
	$('html').attr('xml:lang', lang);
	$('[lang="' + lang + '"]').show();
	$('#languageSwitchContainer .langSelector').removeClass('active');
	$('#languageSwitchContainer .langSelector').filter(function(){return $(this).text().trim().toLowerCase() == lang}).addClass('active');

    $('#_otree-title').append($('#proxyTitle [lang="' + lang + '"]'));
    $('#_otree-title').append($('#exitToHomePage'));
}

function setLanguageCookie(lang) {
    document.cookie = 'Games_JS_lang=' + lang + ';path=/;SameSite=Lax';
}

function getLanguageCookie() {
    const name = 'Games_JS_lang';
    const ca = document.cookie.split(';');
    for(let i=0;i < ca.length;i++) {
        let c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(name) == 0) {
			return c.substring(name.length + 1,c.length);
		}
    }
    return null;
}
