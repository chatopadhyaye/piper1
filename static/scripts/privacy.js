//PRIVACY DROPDOWN 


	$('.pvt_btn').off('click').on('click', function(){

		var dropdown = $(this).siblings('div');
		var pri_down = $('.pri_down');

		pri_down.not(dropdown).hide();		// hide all other privacy dropdown

		window.container = $(this).parents('.indicator');	//Global variable for hiding privacy dropdown 

		dropdown.toggle();	//Toggle the pivacy dropdown

		var n = 0;
		dropdown.children('ul').children('li').off('click').on('click', function(){

			var cls = $(this).attr('class');

			var icon = $(this).siblings('li').children('.icon');
			var privacy = $(this).parents('div').siblings('.pvt_btn').children('.privacy');
			var sprite_1 = $(this).parents('div').siblings('.pvt_btn').children('.sprite_1');
			var pvt_btn = $(this).parents('div').siblings('.pvt_btn');

			function pub() {
				icon.removeClass('checked');
				privacy.removeClass('on');
				sprite_1.removeClass('hide fork lock').addClass('globe');	
			}

			function con() {
				icon.removeClass('checked');
				privacy.removeClass('on');
				sprite_1.removeClass('hide globe lock').addClass('fork');	
			}

			function me() {
				icon.removeClass('checked');
				privacy.removeClass('on');
				sprite_1.removeClass('hide fork globe').addClass('lock');	
			}



			if ($(this).hasClass('public')) {
				pri_down.hide();
				pub();
			}

			else if ($(this).hasClass('connection')) {
				pri_down.hide();
				con();
			}

			else if ($(this).hasClass('private')) {
				pri_down.hide();
				me();
			}

			else {
				$(this).children('.icon').toggleClass('checked');
				pvt_btn.children('.'+cls).toggleClass('on');
				pvt_btn.children('.sprite_1').addClass('hide');


				if (pvt_btn.children('.'+cls).hasClass('on')) {
					n++;
				}	
				else if (!pvt_btn.children('.'+cls).hasClass('on')) {
						n--;
				}

				if (n==6) {
					con();
					$(this).children('.icon').removeClass('checked'); 
					n=0;
				}
				else if (n<1) {
					me();
					$(this).children('.icon').removeClass('checked'); 
					n=0;
				}


			}



		});
	});




//close privacy dropdown
$(document).click(function(e) {

	container = window.container;

		// if the target of the click isn't the descendant of the container
		if (container.has(e.target).length === 0 ) 
		{
			container.children(".pri_down").hide();
		}
});

