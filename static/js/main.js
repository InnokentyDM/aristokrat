/**
 * Created by Платон on 17.10.2017.
 */
$(document).ready(function() {
    $('#search-btn').click(function(e) {
        search = $('#search').val();
        var re = new RegExp(/^.*\//);
        var url = re.exec(window.location.href);
        window.location = url + 'catalog/search/' + search;
});
});