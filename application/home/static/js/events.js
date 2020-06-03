// Menu
function menuIconHoverIn() {
    $(this).addClass("hover__green");
    $(this).next().addClass("menu-info_show");
}

function menuIconHoverOut() {
    $(this).removeClass("hover__green");
    $(this).next().removeClass("menu-info_show");
}

$("#navbar.header .menu .icon").hover(menuIconHoverIn, menuIconHoverOut);

// Social
function socialIconHoverIn() {
    $(this).addClass("hover__green");
}

function socialIconHoverOut() {
    $(this).removeClass("hover__green");
}

$("#navbar .social .icon").hover(socialIconHoverIn, socialIconHoverOut);

// Logo
function logoIconHoverIn() {
    $(this).addClass("hover__green");
    $(this).css("color", "#fff")
}

function logoIconHoverOut() {
    $(this).removeClass("hover__green");
}

$("#navbar.header .logo").hover(logoIconHoverIn, logoIconHoverOut);

// About
function headerLinkHoverIn() {
    $(this).addClass("hover__green");
    $(this).css("color", "#fff")
}

function headerLinkHoverOut() {
    $(this).removeClass("hover__green");
}

$("#about>.content>.header>.links a").hover(headerLinkHoverIn, headerLinkHoverOut);