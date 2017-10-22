/**
 * Created by Платон on 17.10.2017.
 */
$(document).ready(function() {
    $('#id_edition_date').attr('type', 'date');
    $('#id_edition_date').attr('value', '2017-10-22');
    $('#search-btn').click(function(e) {
        search = $('#search').val();
        var re = new RegExp(/^.*\//);
        var url = re.exec(window.location.href);
        window.location = url + 'catalog/search/' + search;
});
    $('.preview').hover(function(){
        var src = $(this).attr('src');
        $('#bigimage').attr('src', src);
    });


});