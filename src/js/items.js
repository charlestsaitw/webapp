function getList() {
    $.ajax({
        method: "get",
        url: "/list",
    }).done(function(data) {
        alert('done');
        console.log(data);
    })
}