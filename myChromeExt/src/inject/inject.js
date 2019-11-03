var overlay_html = '<div id="overlay" class="overlay">' +
		'<div id="my_awesome_iframe_container">' +
		'<iframe id="1click_iframe" width=100% height=100% frameborder=0></iframe>' +
		'</div>' +
		'</div>';

//need to get the name of the extension
var download_links = document.getElementById("add-to-cart-button");
var price = document.getElementsByClassName("a-size-medium a-color-price header-price")[0].innerText;



	var p = document.createElement('p');
		p.innerHTML = '<a href="#">Donate or Retire with more than 10 times money Instead</a>';
		p.className = "button special-plugin-button";
		download_links.parentElement.insertAdjacentElement('beforebegin',p);
		p.querySelector('a').addEventListener('click',clickHandler,true);

document.querySelector('body').insertAdjacentHTML('beforeend',overlay_html);


function clickHandler(e){
	window.open("https://1-dot-hacktx19.appspot.com/?price="+price);

//	window.onfocus = removeOverlay;


}

