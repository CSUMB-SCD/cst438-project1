
function myFunction() {

    var popup = document.getElementById("myPopup");
    popup.classList.toggle("show");
}


var display = function(ourData) {
    var recipe;
    // var show=document.getElementById("tablePrint");
    var myTable = '<table class="highlight">';
    // myTable+='<caption>Recipes</caption>';
    // let displayText = '';
    myTable += '<thead>';
    myTable += '<tr>';
    myTable += '<th>';
    myTable += 'title';
    myTable += '</th>';
    myTable += '<th>';
    myTable += 'Save Recipe';
    myTable += '</th>';
    myTable += '<th>';
    myTable += 'ingredients';
    myTable += '</th>';
    myTable += '<th>';
    myTable += 'thumbnail';
    myTable += '</th>';
    myTable += '</tr>';
    myTable += '</thead>';
    myTable += '<tbody>';

    //alert(ourData['results']['results'].length);
    for (var i = 0; i < ourData['results']['results'].length; i++) {
        recipe = ourData['results']['results'][i]['href'];
        myTable += '<tr>';
        myTable += '<td>';
        myTable += '<a href=' + '"' + ourData['results']['results'][i]['href'] + '"' + '>' + ourData['results']['results'][i]['title'] + '</a>';
        myTable += '</td>';
        myTable += '<td>';
        myTable += '<button class="btn btn-primary btn-sm" type="button" id="save">Save Recipe</button>';
        myTable += '</td>';
        myTable += '<td>';
        myTable += ourData['results']['results'][i]['ingredients'];
        myTable += '</td>';
        myTable += '<td>';
        // myTable+=ourData['results']['results'][i]['thumbnail'];
        myTable += '<img src=' + '"' + ourData['results']['results'][i]['thumbnail'] + '"' + '>';
        myTable += '</td>';
        myTable += '</tr>';
    }
    myTable += '</tbody>';

    myTable += '</table>';
    document.getElementById('tablePrint').innerHTML = myTable;

};
var loadResults = function() {
    let userValue = document.getElementById("query").value;
    console.log("userValue ", userValue);

    var ourRequest = new XMLHttpRequest();
    // ourRequest.open('GET','http://www.recipepuppy.com/api/?i=onions,garlic&q=omelet&p=3')
    ourRequest.open('GET', '/todo/api/v0.1/results/' + userValue);
    // ourRequest.open('GET',url);
    ourRequest.send();
    ourRequest.onreadystatechange = function() {
        if (ourRequest.readyState == XMLHttpRequest.DONE && ourRequest.status == 200) {
            var ourData = ourRequest.responseText;
            console.log("ourData ", ourData);
            var json = JSON.parse(ourData);

            display(json);
        }
    };

};
window.onload = function() {
    $('#loader').css('display', 'none');
    //alert(key);
    //   document.getElementById("button").style.display='none';
    // document.getElementById("query2").style.display='none';
};
var display2 = function(ourData) {
    //var clear='';
    // document.getElementById('tablePrint').innerHTML=clear;
    var myTable = '<table class="highlight">';
    // myTable+='<caption>Nutrition Facts</caption>';
    myTable += '<thead>';
    myTable += '<tr bgcolor="#FF0000">';
    myTable += '<th>';
    myTable += 'Item Name';
    myTable += '</th>';
    // myTable+='<th>';
    // myTable+='Item Description';
    // myTable+='</th>';
    // myTable+='<th>';
    // myTable+='updated time';
    // myTable+='</th>';
    myTable += '<th>';
    myTable += 'calories';
    myTable += '</th>';
    myTable += '<th>';
    myTable += 'calories from fat';
    myTable += '</th>';
    myTable += '<th>';
    myTable += 'Total Fat';
    myTable += '</th>';
    myTable += '<th>';
    myTable += 'Saturated Fat';
    myTable += '</th>';
    myTable += '<th>';
    myTable += 'Cholesterol';
    myTable += '</th>';
    myTable += '<th>';
    myTable += 'Sugars';
    myTable += '</th>';
    myTable += '<th>';
    myTable += 'Protein';
    myTable += '</th>';
    myTable += '</tr>';
    myTable += '</thead>';

    myTable += '<tbody>';
    myTable += '<tr>';
    myTable += '<td>';
    myTable += ourData['item_name'];
    myTable += '</td>';
    // myTable+='<td>';
    // myTable+=ourData['item_description'];
    // myTable+='</td>';
    // myTable+='<td>';
    // myTable+=ourData['updated_at'];
    // myTable+='</td>';
    myTable += '<td>';
    myTable += ourData['nf_calories'];
    myTable += '</td>';
    myTable += '<td>';
    myTable += ourData['nf_calories_from_fat'];
    myTable += '</td>';
    myTable += '<td>';
    myTable += ourData['nf_total_fat'];
    myTable += '</td>';
    myTable += '<td>';
    myTable += ourData['nf_saturated_fat'];
    myTable += '</td>';
    myTable += '<td>';
    myTable += ourData['nf_cholesterol'];
    myTable += '</td>';
    myTable += '<td>';
    myTable += ourData['nf_sugars'];
    myTable += '</td>';
    myTable += '<td>';
    myTable += ourData['nf_protein'];
    myTable += '</td>';
    myTable += '</tr>';
    myTable += '</tbody>';


    myTable += '</table>';
    document.getElementById('tablePrint2').innerHTML = myTable;
};
var getID = function() {
    //alert("inside");
    document.getElementById('query2')
    var id;
    $(function() {
        $('.info_link').click(function() {
            //alert($(this).text());
            id = $(this).val();
            getNutritionFacts(id);
            // $("#query2").val(id);
            // or alert($(this).hash();
        });
    });

}
var getNutritionFacts = function(id) {
    // let userValue = document.getElementById("query2").value;
    // console.log("userValue ", userValue);
    var ourRequest = new XMLHttpRequest();
    //https://api.nutritionix.com/v1_1/item?id=5707e580a613d0d10ed33608&appId=62a70248&appKey=4c6269d3d4c26690f9511d2103eccc48
    ourRequest.open('GET', 'https://api.nutritionix.com/v1_1/item?id=' + id + '&&appId=' + app + '&&appKey=' + key);
    // ourRequest.open('GET',url);
    ourRequest.send();
    ourRequest.onreadystatechange = function() {
        if (ourRequest.readyState == XMLHttpRequest.DONE && ourRequest.status == 200) {
            var ourData = ourRequest.responseText;
            console.log("ourData ", ourData);
            var json = JSON.parse(ourData);

            display2(json);
        }
    };
}


var display3 = function(ourData) {
    //var show=document.getElementById("tablePrint");
    var myTable = '<table class ="highlight">';
    // myTable+='<caption>Nutrition</caption>';
    // let displayText = '';
    myTable += '<thead>';
    myTable += '<tr>';
    myTable += '<th>';
    myTable += 'Click to Expand';
    myTable += '</th>';
    myTable += '<th>';
    myTable += 'Item Name';
    myTable += '</th>';
    myTable += '<th>';
    myTable += 'Brand Name';
    myTable += '</th>';
    myTable += '<th>';
    myTable += 'Serving size qty';
    myTable += '</th>';
    myTable += '<th>';
    myTable += 'Serving size Unit';
    myTable += '</th>';
    myTable += '</tr>';
    myTable += '</thead>';
    myTable += '<tbody>';
    // <a href="#" onclick="someFunction();"
    //alert(ourData['hits'].length);

    for (var i = 0; i < ourData['hits'].length; i++) {
        myTable += '<tr>';
        myTable += '<td>';
        myTable += '<button class="info_link" value="'+ourData['hits'][i]['fields']['item_id']+ '"onclick="getID();" class="mdl-button mdl-js-button mdl-button--fab mdl-button--colored"><i class="material-icons">add</i></button>';
        // myTable += '<a class="info_link"' + 'onclick="getID();"' + '>' + ourData['hits'][i]['fields']['item_id'] + '</a>';
        myTable += '</td>';
        myTable += '<td>';
        myTable += ourData['hits'][i]['fields']['item_name'];
        myTable += '</td>';
        myTable += '<td>';
        myTable += ourData['hits'][i]['fields']['brand_name'];
        myTable += '</td>';
        myTable += '<td>';
        myTable += ourData['hits'][i]['fields']['nf_serving_size_qty'];
        myTable += '</td>';
        myTable += '<td>';
        myTable += ourData['hits'][i]['fields']['nf_serving_size_unit'];
        myTable += '</td>';
        myTable += '</tr>';
    }
    myTable += '</tbody>';

    myTable += '</table>';
    document.getElementById('tablePrint').innerHTML = myTable;

};

// var url="http://www.recipepuppy.com/api/?i=onions,garlic&q=omelet&p=3"
