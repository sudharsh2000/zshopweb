

  var rowNumber ;
let  aa=2;
let tf=0
let tnet=0;
let ttax=0;
var dltrowid;
var dltrowname;
let incscheck=0;
var myArray = [];
var trntype='';

function calculateTotal(rowNumber) {

  const saleInput = document.getElementById(`srate${rowNumber}`);

  const quantityInput = document.getElementById(`qty${rowNumber}`);
  const totalInput = document.getElementById(`total${rowNumber}`);
  const taxInput = document.getElementById(`tax${rowNumber}`);
  const netamtInput = document.getElementById(`net-amt${rowNumber}`);

  const name1 = document.getElementById(`itemname${rowNumber}`);
  const vattax = document.getElementById(`vat${rowNumber}`);


  const sale = parseFloat(saleInput.value) || 0;
const quantity = parseFloat(quantityInput.value) || 0;
 var tax = parseFloat(taxInput.value) || 0;
 const vatt=parseFloat(vattax.value) || 0;
 var amtt= parseFloat(totalInput.value) || 0;
   var net;
   var total;
   if(incscheck==1){

  
    tax = (sale*vatt)/(100+vatt);
    tax=tax*quantity;
 

    amtt=(sale*quantity)-tax;
    net=tax+amtt;
    
    
    
      }
    else{
    

    
    amtt=quantity*sale;
    tax = (sale*vatt)/(100);
    tax=tax*quantity;
    net=amtt+tax;
    }


    taxInput.value=tax.toFixed(2);
    tf=amtt.toFixed(2);
  tnet=net.toFixed(2);
  
  ttax=tax;
    totalInput.value = amtt.toFixed(2);
    netamtInput.value = net.toFixed(2);

totalfind(rowNumber);
}
function totalfind(rowNumber) {
  const tableBody = document.getElementById('invoice-form-items-table-body');
var finalnet=0;
var finalamt=0;
var finaltax=0;



var rows = tableBody.getElementsByTagName("tr");

for (var i = 0; i < rows.length; i++) {
    var inputs = rows[i].getElementsByTagName('input');
    var netget=inputs[8]
    var amtget=inputs[6]
    var taxget=inputs[7]
    
    finalnet+=parseFloat(netget.value) ||0;


    finalamt+=parseFloat(amtget.value)||0;
    finaltax+=parseFloat(taxget.value)||0;
   
}


// for (let i = 1; i <= tableBody.rows.length; i++) {

// var netget=document.getElementById(`net-amt${i}`);
// var amtget=document.getElementById(`total${i}`);
// var taxget=document.getElementById(`tax${i}`);





// }



var totamt=	document.getElementById('amttotal');
var totnet=	document.getElementById('nettotal');
var tottax=	document.getElementById('taxamt');

totamt.value= finalamt.toFixed(2);
totnet.value= finalnet.toFixed(2);
tottax.value= finaltax.toFixed(2);





}




        function openPopupitem() {
      document.getElementById('overlay2').style.display = 'flex';
    }

    function closePopupitem() {
   
      document.getElementById('overlay2').style.display = 'none';
    }
    let itemlen=0;
    let tempitemname=[];
    let tempbarcode=[];
    let tempsrate=[];
    let temptax=[]
    let ilang=[];
    let tempitemid=[];
    let vat=[];
    let tempitemcode=[];
    const itemresultsContainer = document.getElementById('itemresults');
    const company = document.getElementById('cmp').value;
 function search(rowNumber) {
tempbarcode=[];
tempitemname=[];
tempsrate=[];
temptax=[];
ilang=[];
tempitemid=[];
vat=[];
tempitemcode=[];
const item = document.getElementById(`barcode${rowNumber}`);
 var query=item.value;
 
       fetch(`/searchitem/?query=${query}&comp=${company}`)
                .then(response => response.json())
                .then(data => displayitemResults(data.customers,rowNumber));
        }

        function displayitemResults(customers,rowNumber) {
            openPopupitem();
            itemlen=customers.length;
            const resultsList = document.getElementById('itemresults');

            resultsList.innerHTML = '';

            customers.forEach(customer => {
              const mainlist = document.createElement('tr');
                const listItem = document.createElement('td');
                mainlist.classList.add('result-item2');

                listItem.textContent = customer.name;

                 const listbcode = document.createElement("td");
                 if(customer.bcode==''){

                   }
                   else{
                        listbcode.textContent=customer.bcode;
                   }


                 const listitemcode = document.createElement("td");
                   if(customer.itemcode==''){
                   listitemcode.textContent='00.0';
                   }
                   else{
                   listitemcode.textContent=customer.itemcode;
                   }


                 const listsrate = document.createElement("td");
                 if(customer.srate==0){
                   listsrate.textContent='0.0';

                   }
                   else{
                   listsrate.textContent=customer.srate;
                   }


                   const listilang = document.createElement("td");
                   if(customer.ilang==''){
                   listilang.textContent='Empty';
                   }
                   else{

                   listilang.textContent=customer.ilang;
                   }


                 const listprate = document.createElement("td");

                  if( customer.prate==0){

                   listprate.textContent='00.0';
                   }
                   else{

                    listprate.textContent=customer.prate;
                   }
var tax=(parseFloat(customer.srate)*parseFloat(customer.vat))/115;

tempitemname.push(customer.name);
tempbarcode.push(customer.bcode);
tempsrate.push(customer.srate);
ilang.push(customer.ilang);
tempitemid.push(customer.id);
temptax.push(customer.incs);
vat.push(customer.vat);
tempitemcode.push(customer.itemcode);

listItem.style.width = "220px";
listbcode.style.width = "150px";
listitemcode.style.width = "150px";
listilang.style.width = "220px";
listprate.style.width = "250px";
listsrate.style.width = "200px";
resultsList.style.height='100%';


mainlist.appendChild(listItem);
mainlist.appendChild(listbcode);
mainlist.appendChild(listitemcode);
mainlist.appendChild(listilang);
mainlist.appendChild(listprate);
mainlist.appendChild(listsrate);
mainlist.value=customer.bcode;

resultsList.appendChild(mainlist);

console.log(tempitemid)



                   const divide = document.createElement('hr');

                resultsList.appendChild(divide);
                

                listItem.onclick = () => selectitem(customer.id,customer.name,customer.bcode,customer.ilang, customer.srate,customer.incs,customer.vat,customer.itemcode, rowNumber);


            });
        }

        function selectitem(customerid,customer,barcode,ilang,srate,incs,vat,itemcode, rowNumber) {



        incscheck=incs;
        


var check=0;
bcheck=true;
   myArray=[];
  //  document.getElementById(`barcode${rowNumber}`).value=tempbarcode[index];
   let curbcode=barcode
   
    const tableBody = document.getElementById('invoice-form-items-table-body');

   
      for (let i = 1; i <=tableBody.rows.length ; i++) {
      if(document.getElementById(`barcode${i}`).value==curbcode){
        
        var newqty = document.getElementById(`qty${i}`).value;

        
        document.getElementById(`qty${i}`).value=parseInt(newqty)+1;
        document.getElementById(`barcode${rowNumber}`).value=''
        document.getElementById(`barcode${rowNumber}`).focus();
        calculateTotal(i)
        bcheck=false;
        break;
        
      }
      
      
    
      
  
      
   }  
   if(bcheck){
    document.getElementById(`barcode${rowNumber}`).value=curbcode;
    document.getElementById(`qty${rowNumber}`).focus();
   }
     
                  // Implement logic to handle selected customer (e.g., make an API call, update UI)
     

    
    
      closePopupitem();
      getbarcodeitem(rowNumber)     

        }

//enter and grid select


        
myArray=[];
var bcheck=true;
     var tembcode;  
     var bscanner=true; 
  function selectResultitem(index,rowNumber) {
bcheck=true;

   let curbcode=tembcode
   
    const tableBody = document.getElementById('invoice-form-items-table-body');
    var rows = tableBody.getElementsByTagName('tr');
   
      for (let i = 1; i <=tableBody. rows.length ; i++) {
        var inputs = rows[i-1].getElementsByTagName('input');
     
      if(inputs[0].value==curbcode){
       
        var newqty = inputs[4].value;

        
       inputs[4].value=parseInt(newqty)+1;
        document.getElementById(`barcode${rowNumber}`).value=''
        document.getElementById(`barcode${rowNumber}`).focus();
        calculateTotal(i)
        bcheck=false;
        break;
        
      }
      
      
    
      
  
      
   }  
   if(bcheck){
    // getbcode=curbcode;
    bscanner=false;
    document.getElementById(`barcode${rowNumber}`).value=curbcode
    document.getElementById(`qty${rowNumber}`).focus();
   }
     
                  // Implement logic to handle selected customer (e.g., make an API call, update UI)
     

    
    
      closePopupitem();
                   
 
  }
  function qtykeydown(event,rowNumber){
    if (event.key === 'Enter') {

    event.preventDefault();
        document.getElementById(`srate${rowNumber}`).focus()
    }
  }
  function handleKeyDown(event,rowNumber) {
  
  
    
    if (event.key === 'ArrowDown') {
      
      event.preventDefault();
      selectedResultIndex = Math.min(selectedResultIndex + 1, itemlen );
      highlightSelectedResult();
    } else if (event.key === 'ArrowUp') {
      event.preventDefault();
      selectedResultIndex = Math.max(selectedResultIndex -1,0);
      highlightSelectedResult();
    } else if (event.key === 'Enter') {
   
     
      if (selectedResultIndex !== -1) {
      
        event.preventDefault();
        selectResultitem(selectedResultIndex,rowNumber);
        selectedResultIndex = -1;
      }
      else{
        event.preventDefault();
        document.getElementById(`qty${rowNumber}`).focus()
      }
    }

    }
  function highlightSelectedResult() {
   
    
    const resultItems = document.querySelectorAll('.result-item2');

    resultItems.forEach((item, index) => {
        
      if (index === selectedResultIndex) {
        item.style.backgroundColor = '#e0e0e0';
        item.scrollIntoView({ behavior: 'smooth', block: 'center' });
        tembcode=item.value
      } else {
        item.style.backgroundColor = '';
      }
    });
  }
  
  // Handle keyboard events
  

  // Hide results when clicking outside the input and results container
  document.addEventListener('click', (event) => {
    const isClickInsideInput = searchInput.contains(event.target);
    const isClickInsideResults = itemresultsContainer.contains(event.target);

    if (!isClickInsideInput && !isClickInsideResults) {
      closePopupitem();
    }
  });

  


function getbarcodeitem(rowNumber){
 
if(bscanner){
  bcheck=true;
  let curbcode= document.getElementById(`barcode${rowNumber}`).value
 if(curbcode!=''){  
  const tableBody = document.getElementById('invoice-form-items-table-body');
  var rows = tableBody.getElementsByTagName('tr');
 
    for (let i = 1; i <= rows.length ; i++) {
      var inputs = rows[i-1].getElementsByTagName('input');
      
  if(dltrowid!=i){
    if(inputs[0].value==curbcode){
     
      var newqty = inputs[4].value;

      
      inputs[4].value=parseInt(newqty)+1;
      document.getElementById(`barcode${rowNumber}`).value=''
      document.getElementById(`barcode${rowNumber}`).focus();
      calculateTotal(i)
      bcheck=false;
    
      break;
      
    }
 else{

 }
    
  
  }   

    
 } 
 
}
   
  

}

  if(bcheck){
    bscanner=true;
  const item = document.getElementById(`barcode${rowNumber}`);
 var query=item.value;
// query=getbcode;

 if(query=='undefined'){
  document.getElementById(`barcode${rowNumber}`).value='';
  document.getElementById(`barcode${rowNumber}`).focus();
 }
 else{
if(query!==''){

const typ='bcode'
       fetch(`/getitem/?query=${query}&type=${typ}&comp=${company}`)
                .then(response => response.json())
                .then(data => displaybarcodeitem(data.customers,rowNumber));
              
            }
        }
      }
      else{
        closePopupitem();
      }
    }
    function displaybarcodeitem(items,rowNumber) {
      
   
          
          items.forEach((item,index) => {
         
    const tableBody = document.getElementById('invoice-form-items-table-body'); 
          
            document.getElementById(`qty${rowNumber}`).focus()
            document.getElementById(`barcode${rowNumber}`).value=item.bcode;
            document.getElementById(`itemname${rowNumber}`).value =item.name;
               document.getElementById(`itemcode${rowNumber}`).value = item.itemcode;
              
               document.getElementById(`ilang${rowNumber}`).value = item.ilang;
                            document.getElementById(`srate${rowNumber}`).value = item.srate;
                              incscheck =item.incs;
                               document.getElementById(`itemid${rowNumber}`).value = item.id;
                              document.getElementById(`vat${rowNumber}`).value = item.vat;
          // 
          

                         // Implement logic to handle selected customer (e.g., make an API call, update UI)
          });
     
             closePopupitem();
                          
        
         }
         function getRow2(event,rowid) {
         
          var row = event.target.closest("tr");
          var rowIndex = Array.from(row.parentNode.children).indexOf(row);
          dltrowid=rowIndex+1;
          dltrowval=rowid;
      }
  var dltrowval;
function getrow(rowid,event){
 getRow2(event,rowid)

dltrowname=  document.getElementById(`itemname${dltrowval}`).value;
}

function deleterow(){
 
  const tableBody = document.getElementById('invoice-form-items-table-body');
  if(tableBody.rows.length==1){
    location.reload();
  }
  else{
    
   
    myArray.slice()
    const deleterw=dltrowid-1
  if(myArray.includes(dltrowname)){
   
 myArray.splice(deleterw,1)
  }
   
      tableBody.deleteRow(deleterw);
  
  }
  totalfind(dltrowval)
  
}

function Loaddata(){

  const type = document.getElementById('type').value;
  const prevno = document.getElementById('prevno').value;

  const setvno = document.getElementById('vno');
  if(type=='report'){
   
    setvno.value=parseInt( prevno);
  
      jumpdata()
  }
}

const tableBody = document.getElementById('invoice-form-items-table-body');
rowNumber=1;
  function addRow() {

    const type = document.getElementById('type');
    if(type=='report'){

    }
rowNumber+=1;

    const newRow = document.createElement('tr');
    newRow.innerHTML = `


    <td class="">${rowNumber}</td>
    <td class="form-input-td"><input name="barcode" style="width:150px;"  onkeydown="handleKeyDown(event,${rowNumber});getrow(${rowNumber},event)" oninput="search(${rowNumber}) "  onblur="getbarcodeitem(${rowNumber})"  onclick="getrow(${rowNumber},event)" id="barcode${rowNumber}" type="text" class="form-control"   placeholder="Barcode"></td>
    <td class="form-input-td"><input name="itemcode" style="width:150px;" id="itemcode${rowNumber}" type="text" class="form-control"   placeholder="Itemcode" onclick="getrow(${rowNumber},event)" readonly></td>
    	<td class="form-input-td"><input name="itemname" style="width:350px;"    id="itemname${rowNumber}"  class="form-control"  type="text" placeholder="Itemname" onclick="getrow(${rowNumber},event)" readonly></td>

<td class="form-input-td"><input name="ilang" id="ilang${rowNumber}"  style="width:150px;" type="text" class="form-control"   placeholder="second lang" onclick="getrow(${rowNumber},event)" readonly></td>
<td class="form-input-td"><input type="number" name="qty" style="width:100px;" class="form-control"  id="qty${rowNumber}" style="width:100px;" oninput="calculateTotal(${rowNumber})" onkeydown="qtykeydown(event,${rowNumber})" placeholder="0.0" onclick="getrow(${rowNumber},event)" required ></td>     
<td class="form-input-td"><input type="number" name="srate" id="srate${rowNumber}" style="width:100px;" oninput="calculateTotal(${rowNumber})" class="form-control" placeholder="0.0" onclick="getrow(${rowNumber},event)" onkeydown="nextrowkey(event,${rowNumber})" required ></td>

      <td class="form-input-td"><input type="text" name="amt" style="width:100px;" class="form-control"   id="total${rowNumber}" placeholder="0.0" onclick="getrow(${rowNumber},event)" readonly></td>
      <td class="form-input-td"><input type="text" name="tax" style="width:100px;" id="tax${rowNumber}"   class="form-control" oninput="calculateTotal(${rowNumber})"   placeholder="0.0" onclick="getrow(${rowNumber},event)" required></td>

      <td><input type="text" name="netamt" style="width:100px;" id="net-amt${rowNumber}"  class="form-control" placeholder="0.0"  onclick="getrow(${rowNumber},event)" readonly></td>
         <td><input type="text" name="itemid" style="width:100px;" id="itemid${rowNumber}" hidden="true" class="form-control"  ></td>
            <td><input type="text" name="vat" style="width:100px;" id="vat${rowNumber}" hidden="true" class="form-control"  ></td>
            <td><input type="text" name="validate" style="width:100px;" id="validate${rowNumber}" hidden="true" class="form-control"  ></td>
   `;

    tableBody.appendChild(newRow);
   
   document.getElementById(`barcode${rowNumber}`).focus();
 
    aa++;



  }

function nextrowkey(event,rownum){
  
  const tableBody = document.getElementById('invoice-form-items-table-body');
  let rowlen=tableBody.rows.length
  

  if (event.key === 'Enter'|event.key=='Tab') {
    
    event.preventDefault();
    if(dltrowid==rowlen){
      addRow();
      }
      else{
        let nxtrownum=dltrowval+1;
        document.getElementById(`barcode${nxtrownum}`).focus();
      }
    }
    if (event.key === 'F5') {
      event.preventDefault();
      
      }
}
function generateThermalPrintout() {


  let table = document.getElementById('invoice-form-items-table');

  var printWindow = window.open('', '_blank');
  printWindow.document.write('<html><head><title>Thermal Printout</title></head><body>');

  // Add table with headers
  printWindow.document.write('<table>');
  printWindow.document.write('<tr><th>Item ID</th><th>Item Name</th><th>Rate</th></tr>');

  // Add table rows with data
  for(i=1;i<=table.tBodies[0].rows.length;i++){
    const itemname=document.getElementById(`itemname${i}`)
    const itemid=document.getElementById(`itemid1`)
    const barcode=document.getElementById(`barcode1`)
   
    printWindow.document.write('<tr>');
    printWindow.document.write('<td>' + itemname.value+ '</td>');
    printWindow.document.write('<td style="width:200px;">' +'sss'+ '</td>');
    printWindow.document.write('<td>' + 'ssss'+ '</td>');
    printWindow.document.write('</tr>');
  
  }
  printWindow.document.write('</table>');
  printWindow.document.write('</body></html>');
  printWindow.document.close();
  printWindow.print();
}


function generateprintA4() {



  const pass= document.getElementById('pass').value
 
    const imei= document.getElementById('imei').value	
    const apdate= document.getElementById('apdate').value
 
    const battery= document.getElementById('btry').value
  
   const fcid= document.getElementById('fcid').value
  
  
  
   const bcid= document.getElementById('bcid').value
  
  
   const mmcid= document.getElementById('mmcid').value;

 
   const sim= document.getElementById('sim').value;
  
  
   const charger= document.getElementById('charger').value;
  


  
   const ns=  document.getElementById('ns').value;
  
  
   const mnw= document.getElementById('mnw').value;
  
  
   const snw= document.getElementById('snw').value;
  

  const nc =  document.getElementById('nc').value;
  
  
   const cnw=  document.getElementById('cnw').value;
  
  
   const knw= document.getElementById('knw').value;
  

 
   const np= document.getElementById('np').value;
  
  
   const fnw= document.getElementById('fnw').value;
  
  
   const lcd= document.getElementById('lcd').value;
  

  // window.open("printtrn")
  const printtype=document.getElementById('printssave')
  const vno=document.getElementById('vno')
  const mobile=document.getElementById('mobile')
  

  const customer=document.getElementById('searchInput')
  const date=document.getElementById('sdate')
  const vtype=document.getElementById('hvtype')
  const taxamt=document.getElementById('taxamt')
  const totalamt=document.getElementById('nettotal')
  
     led=customer.value;
  
let itemarray=[];
let slangarray=[];
let qtyarray=[];
let pricearray=[]
let grossarray=[];
let taxarray=[];
let amountarray=[];
  let table = document.getElementById('invoice-form-items-table');
  for(i=1;i<=table.tBodies[0].rows.length;i++){
    const itemname=document.getElementById(`itemname${i}`)
    const slang=document.getElementById(`ilang${i}`)
    const qty=document.getElementById(`qty${i}`)
    const Price=document.getElementById(`srate${i}`)
    const gross=document.getElementById(`total${i}`)
    const tax=document.getElementById(`tax${i}`)
    const amount=document.getElementById(`net-amt${i}`)
    if(itemname.value!=''){
      itemarray.push(itemname.value)
      qtyarray.push(qty.value)
      pricearray.push(Price.value)
      grossarray.push(gross.value)
      taxarray.push(tax.value)
      amountarray.push(amount.value)
      slangarray.push(slang.value)
    }
    


  }
 var itemar= JSON.stringify(itemarray);
 var slangar=JSON.stringify(slangarray);
 var qtyar= JSON.stringify(qtyarray);
 var pricear= JSON.stringify(pricearray);
 var grossar= JSON.stringify(grossarray);
 var taxar= JSON.stringify(taxarray);
 var amountar= JSON.stringify(amountarray);
 
 if (printtype.checked==true){
 
  var printWindow = window.open('/printtrn/?voucher='+vno.value+'&mobile='+mobile.value+'&cus='+led+'&date='+date.value+'&vtype='+vtype.value+'&item='+itemar+'&qty='+qtyar+'&price='+pricear+'&tax='+taxar+'&gross='+grossar+'&amount='+amountar+'&taxamt='+taxamt.value+'&totalamt='+totalamt.value+'&comp='+company+'&printtype=a4&battery='+battery+'&bcid='+bcid+'&fcid='+fcid+'&mmcid='+mmcid+'&sim='+sim+'&charger='+charger+'&ns='+ns+'&mnw='+mnw+'&nc='+nc+'&cnw='+cnw+'&snw='+snw+'&knw='+knw+'&np='+np+'&fnw='+fnw+'&lcd='+lcd+'&pass='+pass+'&imei='+imei+'&apdate='+apdate+'     ');


 }
 else{
  
  var printWindow = window.open('/printtrn/?voucher='+vno.value+'&mobile='+mobile.value+'&cus='+led+'&date='+date.value+'&vtype='+vtype.value+'&item='+itemar+'&slang='+slangar+'&qty='+qtyar+'&price='+pricear+'&tax='+taxar+'&gross='+grossar+'&amount='+amountar+'&taxamt='+taxamt.value+'&totalamt='+totalamt.value+'&comp='+company+'&printtype=thermal&battery='+battery+'&bcid='+bcid+'&fcid='+fcid+'&mmcid='+mmcid+'  ');

 }



}


///save data 

document.addEventListener("keydown", keyDownTextField, false);
let salesform = document.getElementById('invoice-form');
let submitbutton = document.getElementById('subtmit');
let tablemain = document.getElementById('invoice-form-items-table-body');
var chk2=1;
 let valid = true;
function keyDownTextField(e) {

  if(event.key === 'F5') {
    
    event.preventDefault()
    validform();
  
   if(valid) {


    const vno = document.getElementById(`vno`).value;
  const vtyp = document.getElementById(`hvtype`).value;
  const company = document.getElementById(`cmp`).value;
    fetch(`/getvno/?type=${vtyp}&company=${company}`)
    .then(response => response.json())
    .then(data => savecurfn(data.vno)
    
    );
function savecurfn(vnomax){
 
 
  if(document.getElementById('btry').checked==true){
    document.getElementById('btry').value=1;	
  }
  else{
    document.getElementById('btry').value=-1;
  }
  if(document.getElementById('fcid').checked==true){
    document.getElementById('fcid').value=1;	
  }
 else{
    document.getElementById('fcid').value=5;
  }
  
  if(document.getElementById('bcid').checked==true){
    document.getElementById('bcid').value=1;	
  }
  else{
    document.getElementById('bcid').value=-1;
  }
  if(document.getElementById('mmcid').checked==true){
    document.getElementById('mmcid').value=1;	
  }
  else{
    document.getElementById('mmcid').value=-1;
  }
  if(document.getElementById('sim').checked==true){
    document.getElementById('sim').value=1;	
  }
  else{
    document.getElementById('sim').value=-1;
  }
  if(document.getElementById('charger').checked==true){
    document.getElementById('charger').value=1;	
  }
  else{
    document.getElementById('charger').value=-1;
  }


  if(document.getElementById('ns').checked==true){
    document.getElementById('ns').value=1;	
  }
  else{
    document.getElementById('ns').value=-1;
  }
  if(document.getElementById('mnw').checked==true){
    document.getElementById('mnw').value=1;	
  }
  else{
    document.getElementById('mnw').value=-1;
  }
  if(document.getElementById('snw').checked==true){
    document.getElementById('snw').value=1;	
  }
  else{
    document.getElementById('snw').value=-1;
  }
  if(document.getElementById('nc').checked==true){
    document.getElementById('nc').value=1;	
  }
  else{
    document.getElementById('nc').value=-1;
  }
  if(document.getElementById('cnw').checked==true){
    document.getElementById('cnw').value=1;	
  }
  else{
    document.getElementById('cnw').value=-1;
  }
  if(document.getElementById('knw').checked==true){
    document.getElementById('knw').value=1;	
  }
  else{
    document.getElementById('knw').value=-1;
  }

  if(document.getElementById('np').checked==true){
    document.getElementById('np').value=1;	
  }
  else{
    document.getElementById('np').value=-1;
  }
  if(document.getElementById('fnw').checked==true){
    document.getElementById('fnw').value=1;	
  }
  else{
    document.getElementById('fnw').value=-1;
  }
  if(document.getElementById('lcd').checked==true){
    document.getElementById('lcd').value=1;	
  }
  else{
    document.getElementById('lcd').value=-1;
  }


  document.getElementById("invoice-form").submit();
  const printcheck=document.getElementById('printssave')
  
var printsale=0;
var rows = tableBody.getElementsByTagName('tr');
for(i=0;i<tablemain.rows.length;i++){
  var inputs = rows[i].getElementsByTagName('input');
  alert(inputs[11].value)
  if(inputs[11].value==1){
    
    printsale=1;
  }
}

  if(printcheck.checked==true ){
    if(printsale==1){

   
  generateprintA4()
}
  }
 

}
}
    

    
    

  } 
  if(event.key=='Enter'){
   
    event.preventDefault()
  }

  if(event.key === 'F12') {
    event.preventDefault()
    document.getElementById(`barcode${1}`).focus()
  }
 
}
function validform(){
  valid=true;
  
  var checkindex;

    if(document.getElementById('searchInput').value==='' ){
      alert("Please select Customer");
      document.getElementById('searchInput').focus();
      valid= false;
    }
    if(document.getElementById('customerid').value===''){
      alert("Please select valid Customer");
      document.getElementById('searchInput').focus();
      valid= false;
   
    }

    const tableBody = document.getElementById('invoice-form-items-table-body');
    var rows = tableBody.getElementsByTagName('tr');
   
      for (let i = 0; i <tableBody. rows.length ; i++) {
        var inputs = rows[i].getElementsByTagName('input');
     
      const vtyp = document.getElementById(`hvtype`).value;
      if(inputs[2].value!=''){
       
        
   
         
        inputs[11].value=1;
        
        

        if (   inputs[8].value=='' || inputs[8].value==0 ) {
        alert("Total amount is empty")    
          valid = false;
            break;
        }
        if (   inputs[4].value=='' || inputs[4].value==0 ) {
          alert("Please Enter Quantity")    
            valid = false;
              break;
          }
      }

      else{
       
        
          inputs[11].value=-1;
          
      }
      if((inputs[8].value!='' && inputs[2].value=='')||(inputs[4].value!='' && inputs[2]=='') )
      {
       alert("Please Select Item")    
       valid = false;
         break;
      }


    }

   
    
}
function SAvefn(){

  validform();
   
 
  if(valid) {
   
    const vno = document.getElementById(`vno`).value;
    const vtyp = document.getElementById(`hvtype`).value;
    const company = document.getElementById(`cmp`).value;
      fetch(`/getvno/?type=${vtyp}&company=${company}`)
      .then(response => response.json())
      .then(data => savecurfn(data.vno)
      
      );
  function savecurfn(vnomax){
   
 
    if(document.getElementById('btry').checked==true){
      document.getElementById('btry').value=1;	
    }
    else{
      document.getElementById('btry').value=-1;
    }
    if(document.getElementById('fcid').checked==true){
      document.getElementById('fcid').value=1;	
    }
   else{
      document.getElementById('fcid').value=5;
    }
    
    if(document.getElementById('bcid').checked==true){
      document.getElementById('bcid').value=1;	
    }
    else{
      document.getElementById('bcid').value=-1;
    }
    if(document.getElementById('mmcid').checked==true){
      document.getElementById('mmcid').value=1;	
    }
    else{
      document.getElementById('mmcid').value=-1;
    }
    if(document.getElementById('sim').checked==true){
      document.getElementById('sim').value=1;	
    }
    else{
      document.getElementById('sim').value=-1;
    }
    if(document.getElementById('charger').checked==true){
      document.getElementById('charger').value=1;	
    }
    else{
      document.getElementById('charger').value=-1;
    }
  
  
    if(document.getElementById('ns').checked==true){
      document.getElementById('ns').value=1;	
    }
    else{
      document.getElementById('ns').value=-1;
    }
    if(document.getElementById('mnw').checked==true){
      document.getElementById('mnw').value=1;	
    }
    else{
      document.getElementById('mnw').value=-1;
    }
    if(document.getElementById('snw').checked==true){
      document.getElementById('snw').value=1;	
    }
    else{
      document.getElementById('snw').value=-1;
    }
    if(document.getElementById('nc').checked==true){
      document.getElementById('nc').value=1;	
    }
    else{
      document.getElementById('nc').value=-1;
    }
    if(document.getElementById('cnw').checked==true){
      document.getElementById('cnw').value=1;	
    }
    else{
      document.getElementById('cnw').value=-1;
    }
    if(document.getElementById('knw').checked==true){
      document.getElementById('knw').value=1;	
    }
    else{
      document.getElementById('knw').value=-1;
    }
  
    if(document.getElementById('np').checked==true){
      document.getElementById('np').value=1;	
    }
    else{
      document.getElementById('np').value=-1;
    }
    if(document.getElementById('fnw').checked==true){
      document.getElementById('fnw').value=1;	
    }
    else{
      document.getElementById('fnw').value=-1;
    }
    if(document.getElementById('lcd').checked==true){
      document.getElementById('lcd').value=1;	
    }
    else{
      document.getElementById('lcd').value=-1;
    }

    document.getElementById("invoice-form").submit();
    const printcheck=document.getElementById('printssave')
  
var printsale=0;
var rows = tableBody.getElementsByTagName('tr');
for(i=0;i<tablemain.rows.length;i++){
  var inputs = rows[i].getElementsByTagName('input');
  if(inputs[11].value==1){
    
    printsale=1;
  }
}

  if(printcheck.checked==true ){
    if(printsale==1){

   
  generateprintA4()
}
  }
   
  
  }
} 
     
     else{
alert("invalid")
     }

   

}
// salesform.addEventListener("submit", (e) => {
  
//   e.preventDefault();


//   // handle submit
// });

async function jumpdata(){
  const vtyp = document.getElementById('hvtype').value;
  const vno = document.getElementById('vno');
  const curtype = document.getElementById(`type`).value;
  trntype='pre';
  // Get the current max vno by awaiting getmaxvvno
  const maxvvno = await getmaxvvno(); 
  
  if (maxvvno === null) {
    alert("Failed to fetch max vno");
    return;
  }

  let query = parseInt(vno.value);
  
  if (query > 0) {
    if (curtype == 'report') {
      
      if (query== maxvvno) {
        location.reload()
        // Do something if vno equals maxvvno
      } else {
        
          addprevioussales(query);
        
      }
    } else {
      
      if (query == maxvvno) {
        location.reload();
      } else {
        
          addprevioussales(query);
        
      }
    }
  }
  }
  
  async function getmaxvvno() {
    const vtyp = document.getElementById('hvtype').value;
   
    
    try {
      const response = await fetch(`/getvno/?type=${vtyp}`);
      const data = await response.json();
      return data.vno; // Return the fetched vno value
    } catch (error) {
      console.error("Error fetching max vno:", error);
      return null; // Return null if there's an error
    }
  }
  
  async function previousdata() {
    const vtyp = document.getElementById('hvtype').value;
    const vno = document.getElementById('vno');
    const curtype = document.getElementById(`type`).value;
    trntype='pre';
    // Get the current max vno by awaiting getmaxvvno
    const maxvvno = await getmaxvvno(); 
    
    if (maxvvno === null) {
      alert("Failed to fetch max vno");
      return;
    }
  
    let query = parseInt(vno.value) - 1;
    
    if (query > 0) {
      if (curtype == 'report') {
        
        if (query== maxvvno) {
          location.reload()
          // Do something if vno equals maxvvno
        } else {
          
            addprevioussales(query);
          
        }
      } else {
        
        if (query == maxvvno) {
          location.reload();
        } else {
          
            addprevioussales(query);
          
        }
      }
    } else {
      alert("Minimum sale Reached");
    }
  }
  
 async function nextdata(){
  const company = document.getElementById('cmp').value;
  
    const vtyp = document.getElementById('hvtype').value;
    const vno = document.getElementById('vno');
    const curtype = document.getElementById(`type`).value;
    trntype='pre';
    // Get the current max vno by awaiting getmaxvvno
    const maxvvno = await getmaxvvno(); 
    
    if (maxvvno === null) {
      alert("Failed to fetch max vno");
      return;
    }
  
    let query = parseInt(vno.value) + 1;
   
    if (query > 0) {
      if (curtype == 'report') {
        
        if (query>= maxvvno) {
         if (vtyp == 'SS') {
          window.location.href =`/service`
        
          // Do something if vno equals maxvvno
        } }else {
          
            addprevioussales(query);
          
        
      } 
    }
    else {
        
        if (query >= maxvvno) {
          location.reload();
        } else {
          
            addprevioussales(query, maxvvno);
          
        }
      }
    
  }

 }





  function addprevioussales(vno){
   let vtype='SS'
   
    var Table = document.getElementById("invoice-form-items-table-body");
Table.innerHTML = "";

//   const vno = document.getElementById(`vno`);
//  let query= parseInt(vno.value)-1;

       fetch(`/getprevious/?query=${vno}&vtype=${vtype}&comp=${company}`)
                .then(response => response.json())
                .then(data => displayprevious(vno,data.data2,data.data1,data.data3,data.lvno)
                  
                  );

  }

  function displayprevious(curvno,issuedetails,buisnessissue,complaindetail,lvno){
  
  if(lvno==0){
    document.getElementById(`vno`).value=curvno
    addRow()
   	document.getElementById('amttotal').value='0.00';
document.getElementById('nettotal').value='0.00';
	document.getElementById('taxamt').value='0.00';
  
  }
 
    buisnessissue.forEach((customer,index) => {
      var datetimeString = customer.issuedate;
      var date = new Date(datetimeString);
      
      var year = date.getUTCFullYear();
      var month = ('0' + (date.getUTCMonth() + 1)).slice(-2); // Adding 1 because months are zero-based
      var day = ('0' + date.getUTCDate()).slice(-2);
      var hours = ('0' + date.getUTCHours()).slice(-2);
      var minutes = ('0' + date.getUTCMinutes()).slice(-2);
      var seconds = ('0' + date.getUTCSeconds()).slice(-2);
      
      var formattedDatetime = year + "-" + month + "-" + day 
  
    
    
      document.getElementById(`previous`).value='yes';
     
      document.getElementById(`vno`).value=customer.vno;
      document.getElementById(`sdate`).value=formattedDatetime;
      document.getElementById(`mobile`).value=customer.tmobile;
      document.getElementById(`nettotal`).value=customer.amt;
      document.getElementById(`taxamt`).value=customer.taxamt;
      
      const query=customer.ledcodedr;
      
      
      fetch(`/getcustomer/?query=${query}&comp=${company}`)
          .then(response => response.json())
          .then(data =>getcus(data.customers)
          
          
          );
        
        
      
     

    });

    previousissuedetails(issuedetails);
    prevcomplaintdetails(complaindetail)
    

  }
  function getcus(abcin){
   
    
    abcin.forEach((cus,index) => {
      
      document.getElementById(`searchInput`).value=cus.name;
      document.getElementById(`customerid`).value=cus.id;
     



    });

  }
 

  function previousissuedetails(issuedetails){
    
    const tableBody = document.getElementById('invoice-form-items-table-body');
var index2;
    issuedetails.forEach((customer,index) => {
      
 
   index2=index+1;
   rowNumber=index2;
      const newRow = document.createElement('tr');
      newRow.innerHTML = `
      <td class="" >${rowNumber}</td>
      <td class="form-input-td"><input name="barcode" style="width:150px;" onchange="calculateTotal(${index2})" onkeydown="handleKeyDown(event,${index2});getrow(${index2},event)"   onblur="getbarcodeitem(${index2})"  onclick="getrow(${index2},event)" oninput="search(${index2}) " id="barcode${index2}" type="text" onchange="checkfn()" class="form-control"   placeholder="Barcode"></td>
      <td class="form-input-td"><input name="itemcode" style="width:150px;" id="itemcode${index2}" type="text"  class="form-control" onclick="getrow(${index2},event)" readonly ></td>

        <td class="form-input-td"><input  name="itemname" style="width:350px;"  id="itemname${index2}"  class="form-control" onclick="getrow(${index2},event)"  type="text" placeholder="Itemname" readonly></td>

  <td class="form-input-td"><input name="ilang" id="ilang${index2}"  style="width:150px;" type="text" class="form-control" onclick="getrow(${index2},event)"  placeholder="second lang" readonly></td>
  <td class="form-input-td"><input type="" name="qty" style="width:100px;" class="form-control"  id="qty${index2}" style="width:100px;" onclick="getrow(${index2},event)" onkeydown="qtykeydown(event,${index2})" oninput="calculateTotal(${index2})" required></td>  
  <td class="form-input-td"><input type="" name="srate" id="srate${index2}" style="width:100px;"  oninput="calculateTotal(${index2})" class="form-control" onclick="getrow(${index2},event)" onkeydown="nextrowkey(event,${index2})" required ></td>

        <td class="form-input-td"><input type="text" name="amt" style="width:100px;"  class="form-control" onclick="getrow(${index2},event)" id="total${index2}" readonly></td>
       <td class="form-input-td"><input type="text" name="tax" style="width:100px;" id="tax${index2}" placeholder="tax"  class="form-control" onclick="getrow(${index2},event)" oninput="calculateTotal(${index2})"  required></td>
  
        <td><input type="text" name="netamt" style="width:100px;" id="net-amt${index2}"  class="form-control" onclick="getrow(${index2},event)" readonly></td>
          <td><input type="text" name="itemid" style="width:100px;" id="itemid${index2}" hidden="true" class="form-control"  ></td>
             <td><input type="text" name="vat" style="width:100px;" id="vat${index2}" hidden="true" class="form-control"  ></td>
             <td><input type="text" name="validate" style="width:100px;" id="validate${index2}" hidden="true" class="form-control"  ></td>
    `;
  
  tableBody.appendChild(newRow);
  let query=customer.pcode
  const typ='itemid'
    let  rownum=index2;
  fetch(`/getitem/?query=${query}&type=${typ}&comp=${company}`)
      .then(response => response.json())
      .then(data => setitem(data.customers,rownum)
      
      );
      let amtt=0;
      function setitem(itemdata,rownum){
        itemdata.forEach((item,index) => {
        
       
        document.getElementById(`itemname${rownum}`).value=item.name;

        document.getElementById(`itemcode${rownum}`).value=item.itemcode;
        document.getElementById(`barcode${rownum}`).value=item.bcode;
        document.getElementById(`ilang${rownum}`).value=item.ilang;
        
        incscheck=item.incs;
        var incscheck2= item.incs;
      


        document.getElementById(`itemid${rownum}`).value = customer.pcode;

        document.getElementById(`srate${rownum}`).value = customer.rate;
        document.getElementById(`tax${rownum}`).value = customer.taxrate;
        document.getElementById(`vat${rownum}`).value=customer.taxper;
        document.getElementById(`qty${rownum}`).value = customer.tempqty;
       //  document.getElementById(`total${index2}`).value = customer.tempqty * customer.rate;
        document.getElementById(`net-amt${rownum}`).value = customer.netamt;
        
          
 if(incscheck==1){
 let tax;
 
   tax = (customer.rate*(customer.taxper))/(100+(customer.taxper));
   tax=tax*(customer.tempqty);
   
   amtt=(customer.rate*customer.tempqty)-customer.taxrate;
  
   
   
   
     }
   else{
   
     
   
   amtt=customer.tempqty * customer.rate;
   
   }
   document.getElementById(`total${rownum}`).value=amtt.toFixed(2)


   var totalamt2=0;
   for(let i=1;i<=tableBody.rows.length;i++){
     var totalam=document.getElementById(`total${i}`);
     
     totalamt2+=parseFloat(totalam.value)
     
    
     
 
      }
      document.getElementById(`amttotal`).value =totalamt2.toFixed(2);
        });
      
      
      }

 
  
  });
  


  }
function prevcomplaintdetails(complaint){
  
  complaint.forEach((comp,index) => {
    var datetimeString = comp.addate;
    var date = new Date(datetimeString);
    
    var year = date.getUTCFullYear();
    var month = ('0' + (date.getUTCMonth() + 1)).slice(-2); // Adding 1 because months are zero-based
    var day = ('0' + date.getUTCDate()).slice(-2);
    var hours = ('0' + date.getUTCHours()).slice(-2);
    var minutes = ('0' + date.getUTCMinutes()).slice(-2);
    var seconds = ('0' + date.getUTCSeconds()).slice(-2);
    
    var formattedDatetimefinal = year + "-" + month + "-" + day ;

    document.getElementById(`apdate`).value=formattedDatetimefinal;
    document.getElementById(`pass`).value=comp.passw;
    document.getElementById(`imei`).value=comp.imei;

    if(comp.battery==1){
      document.getElementById('btry').checked=true;
    }
    if(comp.facecover==1){
      document.getElementById('fcid').checked=true;
    }
    if(comp.backcover==1){
      document.getElementById('bcid').checked=true;
    }
    if(comp.mmc==1){
      document.getElementById('mmcid').checked=true;
    }
    if(comp.sim==1){
      document.getElementById('sim').checked=true;
    }if(comp.charger==1){
      document.getElementById('charger').checked=true;
    }if(comp.nsignal==1){
      document.getElementById('ns').checked=true;
    }if(comp.ncharge==1){
      document.getElementById('nc').checked=true;
    }
    if(comp.npower==1){
      document.getElementById('np').checked=true;
    }if(comp.mnt==1){
      document.getElementById('mnw').checked=true;
    }if(comp.cnt==1){
      document.getElementById('cnw').checked=true;
    }if(comp.fnt==1){
      document.getElementById('fnw').checked=true;
    }if(comp.snt==1){
      document.getElementById('snw').checked=true;
    }if(comp.keypadnt==1){
      document.getElementById('knw').checked=true;
    }if(comp.lcdprob==1){
      document.getElementById('lcd').checked=true;
    }
  });
}