window.onload = function () {

    $('.basket_list').on('click', 'input[type="number"]', function () {
        var t_href = event.target;

        if (t_href) {
            $.ajax({
                url: "/basket/edit/" + t_href.name + "/" + t_href.value + "/",

                success: function (data) {
                    $('.basket_list').html(data.result);
                    console.log('ajax done');
                },
            });

        }
        event.preventDefault();
    });

}