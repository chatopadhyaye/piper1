 

	//Sidebar Rotator	
	$(document).ready(function(){
		$("#rotator").click(function(){
		$(".front").toggleClass('flippedf');
		$(".back").toggleClass('flippedb');
	});

		//setting up cover pic position.
	$(".cover_pic").scrollTop(150);

});



// character count for editing bio
maxCharacters = 160;

$('#count').text(maxCharacters);

$('.edit_bio').bind('input', function() {
		var count = $('#count');
		var save = $('.save');
		var characters = $(this).val().length;
		
		if (characters > maxCharacters) {
				count.addClass('over');
				save.prop("disabled", true);

		} else {
				count.removeClass('over');
				save.prop("disabled", false);
		}
		
		count.text(maxCharacters - characters);
});


//hide the relationship partner search form
	$('.rel_part').hide(); 

//Relationship partner box
	$(document).ready(function(){
		$('.rel_status').change(function(){
				var wth = $('#with');
				var to = $('#to');
				var from = $('#from');
				var status = $('.rel_status')

				if (status.val() == '0'){
						$('.rel_part').hide(); 
						wth.removeClass('dis_inl');
						to.removeClass('dis_inl');
						from.removeClass('dis_inl');
				} else if (status.val() == '11'){
						$('.rel_part').hide(); 
						wth.removeClass('dis_inl');
						to.removeClass('dis_inl');
						from.removeClass('dis_inl');
				} else if (status.val() == '2'){
						$('.rel_part').show(); 
						wth.addClass('dis_inl');
						to.removeClass('dis_inl');
						from.removeClass('dis_inl');
				} else if (status.val() == '3'){
						$('.rel_part').show(); 
						wth.removeClass('dis_inl');
						to.addClass('dis_inl');
						from.removeClass('dis_inl');
				} else if (status.val() == '4'){
						$('.rel_part').show(); 
						wth.removeClass('dis_inl');
						to.addClass('dis_inl');
						from.removeClass('dis_inl');
				} else if (status.val() == '5'){
						$('.rel_part').show(); 
						wth.addClass('dis_inl');
						to.removeClass('dis_inl');
						from.removeClass('dis_inl');
				} else if (status.val() == '6'){
						$('.rel_part').show(); 
						wth.addClass('dis_inl');
						to.removeClass('dis_inl');
						from.removeClass('dis_inl');
				} else if (status.val() == '7'){
						$('.rel_part').show(); 
						wth.addClass('dis_inl');
						to.removeClass('dis_inl');
						from.removeClass('dis_inl');
				} else if (status.val() == '8'){
						$('.rel_part').show(); 
						wth.addClass('dis_inl');
						to.removeClass('dis_inl');
						from.removeClass('dis_inl');
				} else if (status.val() == '10'){
						$('.rel_part').hide(); 
						wth.removeClass('dis_inl');
						to.removeClass('dis_inl');
						from.removeClass('dis_inl');
				} else {
						$('.rel_part').show(); 
						wth.removeClass('dis_inl');
						to.removeClass('dis_inl');
						from.addClass('dis_inl');
				} 
		});


	});



	//slide down and transform chevron 180deg for ***HAVE WORKED AT***


		$("#chev_b_1").click(function(){
				$("#s_down1").slideToggle("fast");
				$("#chev1").toggleClass('chev_180');
		});




		$("#chev_b_2").click(function(){
				$("#s_down2").slideToggle("fast");
				$("#chev2").toggleClass('chev_180');
		});




		$("#chev_b_3").click(function(){
				$("#s_down3").slideToggle("fast");
				$("#chev3").toggleClass('chev_180');
		});



		$("#chev_b_4").click(function(){
				$("#s_down4").slideToggle("fast");
				$("#chev4").toggleClass('chev_180');
		});



		$("#chev_b_5").click(function(){
				$("#s_down5").slideToggle("slow");
				$("#chev5").toggleClass('chev_180');
		});



		$("#chev_b_6").click(function(){
				$("#s_down6").slideToggle("fast");
				$("#chev6").toggleClass('chev_180');
		});


// Disable education "to" year when "from" year is not selected

	$('.to_1').prop("disabled", true);
$(document).ready(function(){
	$('.from_1').change(function(){
		if ($('.from_1').val() == '0'){
			$('.to_1').prop("disabled", true);
		} else {
			$('.to_1').prop("disabled", false);
		}
	});
});


// Disable work "to" year when "from" year is not selecd
$('.to_2').prop("disabled", true);
$(document).ready(function(){
	$('.from_2').change(function(){
		if ($('.from_2').val() == '0'){
			$('.to_2').prop("disabled", true);
		} else {
			$('.to_2').prop("disabled", false);
		}
	});
});


// if workplace checkbox is checked hide "to" year and show "present"
$('#present_work').removeClass('d_inline');
$(document).ready(function(){
	$('.work_check').change(function(){
	if ($('.work_check').is(':checked')) {
		$('.to_2').addClass('d_none');
		$('#present_work').addClass('d_inline');
	} else {
		$('.to_2').removeClass('d_none');
		$('#present_work').removeClass('d_inline');
	}

	});
});






//scrollbar for mozilla

//	var ps = new PerfectScrollbar('.chat_bar');



// chev for photos

$("#chev_p").click(function(){
	$(".photos_view_container").removeClass('h1049');
});


// Add classes to objects based on URL
var photos = $('.id_photo');

switch (window.location.pathname) {
	case '/about/':
		$('.id_abt').addClass('active_border');
		break;
	case '/shared/':
		$('.id_shared').addClass('active_border');
		$('.personal').addClass('active_background');
		break;
	case '/photos/':
		photos.addClass('active_border');
		$('.id_ph').addClass('active_border');
		break;
	case '/videos/':
		photos.addClass('active_border');
		$('.id_vid').addClass('active_border');
		break;
	case '/album/':
		photos.addClass('active_border');
		$('.id_al').addClass('active_border');
		$('.photos_view_container').css('border-top', '1px solid #c5c5c5')
		break;
	case '/public_posts/':
		$('.id_shared').addClass('active_border');
		$('shared_public').addClass('active_border');
		break;
	case '/public/':
		$('.pro_glo').addClass('pro_glo_selected');
}



// Album list toggle 

if ($('.album_cover').length > 5) {
	$('.view_all').addClass('inl_block_i');
}


$('.view_all').on('click', function(){
	$('.alb_container').toggleClass('album_closed');
	$(this).toggleClass('view_all_close');
	if($(this).hasClass('view_all_close')){
		$(this).children('span').html('View All');
	}
	else{
		$(this).children('span').html('Contract');
	}


});



//preview uploaded images 

/*
function readURL(input) {
		if (input.files && input.files[0]) {
			var reader = new FileReader();

			reader.onload = function (e) {
				$(".image_upload_preview").attr('src', e.target.result);
				$(".dsjlk").show();
				$(".up_box").hide();
				$(".pi_caption").show();
			}

			reader.readAsDataURL(input.files[0]);
		}
	}

	$("#single_pic").change(function () {
		readURL(this);
	});
*/


$("#single_pic").change(function () {
	$("#image_upload_preview").attr('src', window.URL.createObjectURL(this.files[0]))
	$(".dsjlk").show();
	$(".up_box").hide();
	$(".pi_caption").show();
	});


$("#reset_hooter_photo").click(function(){
	$(".dsjlk").hide();
	$(".pi_caption").hide();
	$(".up_box").show();
});
