// total = document.getElementById("total").value;
// document.getElementById("netWorth").innerHTML = total;

// function entry(){
//   total = document.getElementById("total").value;
//   document.getElementById("entry").value = total;
// }

function finishTable(){
  var totalColumn1 = tableColumnTotal("sumTable",1);
  var totalColumn2 = tableColumnTotal("sumTable",3);
  var totalColumn3 = tableColumnTotal("sumTable",4);
  var totalColumn4 = tableColumnTotal("sumTable",5);
  var totalColumn5 = tableColumnTotal("sumTable",7);
  var totalColumn6 = tableColumnTotal("sumTable",9);
  var totalColumn7 = tableColumnTotal("sumTable",10);
  var totalColumn1Elem = window.document.getElementById("totalColumn1id");
  totalColumn1Elem.innerHTML = totalColumn1;
  var totalColumn2Elem = window.document.getElementById("totalColumn2id");
  totalColumn2Elem.innerHTML = totalColumn2;
  var totalColumn3Elem = window.document.getElementById("totalColumn3id");
  totalColumn3Elem.innerHTML = totalColumn3;
  var totalColumn4Elem = window.document.getElementById("totalColumn4id");
  totalColumn4Elem.innerHTML = totalColumn4;
  var totalColumn5Elem = window.document.getElementById("totalColumn5id");
  totalColumn5Elem.innerHTML = totalColumn5;
  var totalColumn6Elem = window.document.getElementById("totalColumn6id");
  totalColumn6Elem.innerHTML = totalColumn6;
  var totalColumn7Elem = window.document.getElementById("totalColumn7id");
  totalColumn7Elem.innerHTML = totalColumn7;
  var sum = 1500 - totalColumn1 + totalColumn2 - totalColumn3 + totalColumn4 - totalColumn5 + totalColumn6 + totalColumn7
  document.getElementById("total").innerHTML = sum;
  document.getElementById("total2").innerHTML = sum;
  return;
 }
function tableColumnTotal(thisTable,colNumber){
  var tableElem = document.getElementById(thisTable);
  var tableBody = document.getElementsByTagName("tbody").item(0);
  var i;
  var howManyRows = tableBody.rows.length;
  result = 0;
  for(i=0; i<howManyRows-1; i++){
    var thisTrElem = tableBody.rows[i];
    var thisTdElem = thisTrElem.cells[colNumber];
    var thisTextNode = thisTdElem.childNodes.item(0);
    if (thisTextNode == null) {
      thisNumber = 0;
    }
    else{
      var thisNumber = parseFloat(thisTextNode.data);
    }
    result += thisNumber;
  }
  return result;
}

function displayScore(){
  var totalColumn1 = tableColumnTotal("sumTable",1);
  var totalColumn2 = tableColumnTotal("sumTable",3);
  var totalColumn3 = tableColumnTotal("sumTable",4);
  var totalColumn4 = tableColumnTotal("sumTable",5);
  var totalColumn5 = tableColumnTotal("sumTable",7);
  var totalColumn6 = tableColumnTotal("sumTable",9);
  var totalColumn7 = tableColumnTotal("sumTable",10);
  var sum = 1500 - totalColumn1 + totalColumn2 - totalColumn3 + totalColumn4 - totalColumn5 + totalColumn6 + totalColumn7
  document.getElementById("alert").style.display = "block";
  document.getElementById("entry").style.display = "block";
  document.getElementById("section").style.display = "none";
}
