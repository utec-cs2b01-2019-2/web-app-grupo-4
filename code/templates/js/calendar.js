$(function(){
    var date = new Date(2018, 9, 16, 15, 8, 12);
​​
    $("#constant").dxDateBox({
        placeholder: "10/16/2018",
        showClearButton: true,
        useMaskBehavior: true,
        displayFormat: "shortdate",
        type: "date",
        value: date
    });
​
});
