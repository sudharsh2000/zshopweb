

  var rowNumber ;
let  aa=2;
let tf=0
let tnet=0;
let ttax=0;
var dltrowid;
var dltrowname;


var myArray = [];
var trntype='';



function incoiceprofit(){
  openPopupprofit();
}

function openPopupprofit() {
  document.getElementById('overlayprofit').style.display = 'flow';
}

function closePopupprofit() {

  document.getElementById('overlayprofit').style.display = 'none';
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
    selectedResultIndex=-1;
    const itemresultsContainer = document.getElementById('item-tbl-body');
   
 function search(rowNumber) {
tempbarcode=[];
tempitemname=[];
tempsrate=[];
temptax=[];
ilang=[];
tempitemid=[];
vat=[];
tempitemcode=[];
const item = document.getElementById(`itemname${rowNumber}`);
 var query=item.value;
 
       fetch(`/searchstockitem/?query=${query}`)
                .then(response => response.json())
                .then(data => displayitemResults(data.customers,rowNumber));
        }

        function displayitemResults(customers,rowNumber) {
            
            openPopupitem();
            itemlen=customers.length;
            // const resultsList = document.getElementById('itemresults');

         

             const tableBody = document.getElementById('item-tbl-body');
             tableBody.innerHTML = '';
        
            customers.forEach(customer => {
              const tblrow = document.createElement('tr');
                const listItem = document.createElement('td');
                tblrow.classList.add('main-row');

                listItem.textContent = customer.name;

                 


              


                 const listrate = document.createElement("td");
                 if(customer.srate==0){
                   listrate.textContent='0.0';

                   }
                   else{
                   listrate.textContent=customer.srate;
                   }


                 


                 


tempitemname.push(customer.name);

tempsrate.push(customer.srate);

tempitemid.push(customer.id);



listItem.style.width = "220px";

listrate.style.width = "200px";
tableBody.style.height='100%';


tblrow.appendChild(listItem);

tblrow.appendChild(listrate);
tblrow.value=customer.bcode;

tableBody.appendChild(tblrow);





                   
                

                listItem.onclick = () => selectitem(customer.id,customer.name,customer.srate, rowNumber);

                tblrow.onclick = () => selectitem(customer.id,customer.name,customer.srate, rowNumber);

            });
        }

        function selectitem(customerid,customer,srate,rowNumber) {

          
          document.getElementById(`itemname${rowNumber}`).value=customer
          document.getElementById(`srate${rowNumber}`).value=srate
            
          document.getElementById(`itemid${rowNumber}`).value=customerid
        

          document.getElementById(`qty${rowNumber}`).focus()

    
      closePopupitem();
         

        }

//enter and grid select


        
myArray=[];
var bcheck=true;
     var tembcode;  
     var bscanner=true; 
  function selectResultitem(index,rowNumber) {
bcheck=true;


   
document.getElementById(`itemname${rowNumber}`).value=tempitemname[index]
document.getElementById(`srate${rowNumber}`).value=tempsrate[index]
  
document.getElementById(`itemid${rowNumber}`).value=tempitemid[index]

document.getElementById(`qty${rowNumber}`).focus()
      closePopupitem();
                   
 
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
    const tableBody = document.getElementById('item-tbl-body').children; // This is a NodeList or HTMLCollection

    // Convert NodeList/HTMLCollection to Array
    Array.from(tableBody).forEach((item, index) => {
      if (index === selectedResultIndex) {
        item.style.backgroundColor = '#e0e0e0';
        item.scrollIntoView({ behavior: 'smooth', block: 'center' });
    
        // Assuming `item` has a `data` attribute or similar property you want to extract:
        tembcode = item.children[1].innerHTML; 
        // Modify as per your actual property
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
       fetch(`/getitem/?query=${query}&type=${typ}`)
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
    let incscheck = document.getElementById(`incltax${rowNumber}`).value;
            document.getElementById(`qty${rowNumber}`).focus()
            document.getElementById(`qty${rowNumber}`).value=1;
            document.getElementById(`barcode${rowNumber}`).value=item.bcode;
            document.getElementById(`itemname${rowNumber}`).value =item.name;
               document.getElementById(`itemcode${rowNumber}`).value = item.itemcode;
              
               document.getElementById(`ilang${rowNumber}`).value = item.ilang;
                            document.getElementById(`srate${rowNumber}`).value = item.srate;
                            document.getElementById(`incltax${rowNumber}`).value =item.incs;
                               document.getElementById(`itemid${rowNumber}`).value = item.id;
                              document.getElementById(`vat${rowNumber}`).value = item.vat;
          // 
          calculateTotal(rowNumber);

                         // Implement logic to handle selected customer (e.g., make an API call, update UI)
          });
     
             closePopupitem();
                          
        
         }



const tableBody = document.getElementById('invoice-form-items-table-body');
rowNumber=1;
  function addRow() {

    // const type = document.getElementById('type');
    // if(type=='report'){

    // }
rowNumber+=1;

    const newRow = document.createElement('tr');
    newRow.innerHTML = `


    <td class="fixed-column" >${rowNumber}</td>
 	<td class="form-input-td"><input name="itemname"   id="itemname${rowNumber}"  class="form-control itemnameinput"  type="text" oninput="search(${rowNumber});" onkeydown="handleKeyDown(event,${rowNumber});"  placeholder="Itemname" required></td>

<td class="form-input-td"><input type="number" name="qty" style="min-width:100px;" class="form-control"  id="qty${rowNumber}" style="min-width:100px;" onkeydown="qtykeydown(event,${rowNumber})" placeholder="0.0" onclick="getrow(${rowNumber},event)" required ></td>     
<td class="form-input-td"><input type="number" name="srate" id="srate${rowNumber}" style="min-width:100px;"  class="form-control" placeholder="0.0" onclick="getrow(${rowNumber},event)" onkeydown="nextrowkey(event,${rowNumber})" required >

     <input type="text" name="itemid" style="min-width:100px;" id="itemid${rowNumber}" hidden="true" class="form-control"  >
        </td>
   `;

    tableBody.appendChild(newRow);
   
   document.getElementById(`itemname${rowNumber}`).focus();
 
    aa++;



  }
  function qtykeydown(event,rowNumber){
    if (event.key === 'Enter') {

    event.preventDefault();
        document.getElementById(`srate${rowNumber}`).focus()
    }
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
 
  // window.open("printtrn")
  const printtype=document.getElementById('a4')
  const vno=document.getElementById('vno')
  const mobile=document.getElementById('mobile')
  
  const payment=document.getElementById('payment')
  const customer=document.getElementById('searchInput')
  const date=document.getElementById('sdate')
  const vtype=document.getElementById('hvtype')
  const taxamt=document.getElementById('taxamt')
  const totalamt=document.getElementById('nettotal')
  let led=''
  if(payment.value==1){
     led='CASH'
  }
  else if(payment.value==28){
     led='CREDIT'
  }
  else{
     led=customer.value;
  }
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
  
  
  var printWindow = window.open('/printtrn/?voucher='+vno.value+'&mobile='+mobile.value+'&cus='+led+'&date='+date.value+'&vtype='+vtype.value+'&item='+itemar+'&qty='+qtyar+'&price='+pricear+'&tax='+taxar+'&gross='+grossar+'&amount='+amountar+'&taxamt='+taxamt.value+'&totalamt='+totalamt.value+'&printtype=a4');
 
 }
 else{

  var printWindow = window.open('/printtrn/?voucher='+vno.value+'&mobile='+mobile.value+'&cus='+led+'&date='+date.value+'&vtype='+vtype.value+'&item='+itemar+'&slang='+slangar+'&qty='+qtyar+'&price='+pricear+'&tax='+taxar+'&gross='+grossar+'&amount='+amountar+'&taxamt='+taxamt.value+'&totalamt='+totalamt.value+'&printtype=thermal');

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
  
 let maxvno=0;
   if(valid) {


    const vno = document.getElementById(`vno`).value;
  const vtyp = document.getElementById(`hvtype`).value;
 
    fetch(`/getvno/?type=${vtyp}`)
    .then(response => response.json())
    .then(data => savecurfn(data.vno)
    
    );
function savecurfn(vnomax){

  if(trntype==''){
    document.getElementById(`vno`).value=vnomax;
  }
  

  const vtyp = document.getElementById(`hvtype`).value;

  document.getElementById("invoice-form").submit();
  const printcheck=document.getElementById('printssave')
  const printthermal=document.getElementById('thermalprint')
var printsale=0;
var rows = tableBody.getElementsByTagName('tr');
for(i=0;i<tablemain.rows.length;i++){
  var inputs = rows[i].getElementsByTagName('input');
  if(inputs[11].value==1){
    
    printsale=1;
  }
}

  if(printcheck.checked==true ||printthermal.checked==true){
    if(printsale==1){

   
  generateprintA4()
}
  }
  if(vtyp=='SR'){
    if(printcheck.checked==true ){

   
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

    const tableBody = document.getElementById('invoice-form-items-table-body');
    var rows = tableBody.getElementsByTagName('tr');
    var qtypset = document.getElementById(`qtypset1`)
    const curtype=document.getElementById('type').value;
    if(curtype=='finished'){
    if ( qtypset.value=='' ||qtypset.value==null ) {
      alert("Please Fill Quantity in Finished Table ")    
        valid=false;
          
      }
    }
      for (let i = 1; i <=tableBody.rows.length ; i++) {
        
        var qtyinputs = document.getElementById(`qty${i}`)
        
       
        var iteminputs = document.getElementById(`itemname${i}`)
        
       
       if(curtype=='finished'){
        

        var rateinputs = document.getElementById(`amt${i}`)
       }
       else{
        var rateinputs = document.getElementById(`srate${i}`)
       }

        if (rateinputs.value=='' || rateinputs.value==0 ) {
        alert("Total amount is empty")    
          valid = false;
            break;
        }
        if (   qtyinputs.value=='' || qtyinputs.value==0 ) {
          alert("Please Enter Quantity")    
            valid = false;
              break;
          }
          
          if((iteminputs.value=='' ) )
            {
             alert("Please Select Item")    
             valid = false;
               break;
            }
      }

    
   


    }

   
    


function itemedit(rownum){
 const itemidd= document.getElementById(`itemid${rownum}`).value;


 if(itemidd!==''){
  const type='edit'
  // window.location.href =`/itemedit/${itemidd}/`
 var windowop= window.open('/itemad/?itemid='+itemidd+'&type='+type+'')
 }
  
}



function SAvefn(){

  validform();
   
 
  if(valid) {
   
  
    
  

    document.getElementById("invoice-form").submit();
  

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
  const curtype = document.getElementById(`curtype`).value;
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
      
      if (query>= maxvvno) {
        location.reload()
        // Do something if vno equals maxvvno
      } else {
        if (vtyp == 'SI') {
          addprevioussales(query, maxvvno);
        } else if (vtyp == 'SO') {
          addpreviousso(query);
        } else {
          addpreviousSR(query);
        }
      }
    } else {
      
      if (query>= maxvvno) {
        location.reload();
      } else {
        if (vtyp == 'SI') {
          addprevioussales(query, maxvvno);
        } else if (vtyp == 'SO') {
          addpreviousso(query);
        } else {
          addpreviousSR(query);
        }
      }
    }
  }
  }
  
  async function getmaxvvno() {
  
    
    
    try {
      const response = await fetch(`/getmaxproductid`);
      const data = await response.json();
      return data.vno; // Return the fetched vno value
    } catch (error) {
      console.error("Error fetching max vno:", error);
      return null; // Return null if there's an error
    }
  }
  
  async function previousdata() {
    
    const vno = document.getElementById('vno');
    const curtype = document.getElementById('type').value;
    // const curtype = document.getElementById(`curtype`).value;
    trntype='pre';
    // Get the current max vno by awaiting getmaxvvno
    if(curtype=='finished'){
      let query = parseInt(vno.value) - 1;
      previous_productset(query);
    }
    else{

    
    const maxvvno = await getmaxvvno(); 
    let query = parseInt(vno.value) - 1;
     addpreviousproductset(query,maxvvno);
    }
    // if (query > 0) {
    //   if (curtype == 'report') {
        
    //     if (query== maxvvno) {
    //       location.reload()
    //       // Do something if vno equals maxvvno
    //     } else {
    //       if (vtyp == 'SI') {
    //         addprevioussales(query, maxvvno);
    //       } else if (vtyp == 'SO') {
    //         addpreviousso(query);
    //       } else {
    //         addpreviousSR(query);
    //       }
    //     }
    //   } else {
        
    //     if (query == maxvvno) {
    //       location.reload();
    //     } else {
    //       if (vtyp == 'SI') {
    //         addprevioussales(query, maxvvno);
    //       } else if (vtyp == 'SO') {
    //         addpreviousso(query);
    //       } else {
    //         addpreviousSR(query);
    //       }
    //     }
    //   }
    // } else {
    //   alert("Minimum sale Reached");
    // }
  }
  
 async function nextdata(){
  const maxvvno = await getmaxvvno(); 
  let query = parseInt(vno.value) + 1;
  if (query >= maxvvno) {
          location.reload();
        }
        else{
          addpreviousproductset(query,maxvvno);
        }

    // const vtyp = document.getElementById('hvtype').value;
    // const vno = document.getElementById('vno');
    // const curtype = document.getElementById(`curtype`).value;
    // trntype='pre';
    // // Get the current max vno by awaiting getmaxvvno
    // const maxvvno = await getmaxvvno(); 
    
    // if (maxvvno === null) {
    //   alert("Failed to fetch max vno");
    //   return;
    // }
  
    // let query = parseInt(vno.value) + 1;
   
    // if (query > 0) {
    //   if (curtype == 'report') {
        
    //     if (query>= maxvvno) {
    //      if (vtyp == 'SI') {
    //       window.location.href =`/sale/`
    //     } else if (vtyp == 'SO') {
    //       window.location.href =`/saleorder/`
    //     } else {
    //       window.location.href =`/salereturn/`
    //     }
    //       // Do something if vno equals maxvvno
    //     } else {
    //       if (vtyp == 'SI') {
    //         addprevioussales(query, maxvvno);
    //       } else if (vtyp == 'SO') {
    //         addpreviousso(query);
    //       } else {
    //         addpreviousSR(query);
    //       }
    //     }
    //   } else {
        
    //     if (query >= maxvvno) {
    //       location.reload();
    //     } else {
    //       if (vtyp == 'SI') {
    //         addprevioussales(query, maxvvno);
    //       } else if (vtyp == 'SO') {
    //         addpreviousso(query);
    //       } else {
    //         addpreviousSR(query);
    //       }
    //     }
    //   }
    // }
  }





  function addpreviousproductset(vno,maxvno){

   
    var Table = document.getElementById("invoice-form-items-table-body");
Table.innerHTML = "";

//   const vno = document.getElementById(`vno`);
//  let query= parseInt(vno.value)-1;

       fetch(`/getproductset/?query=${vno}`)
                .then(response => response.json())
                .then(data => displayprevious(data.data1,data.data2)
                  
                  );

  }

  function displayprevious(pdetails,pset){
   
console.log(pset)
    pset.forEach((customer,index) => {
  
  
    
    
      document.getElementById(`vno`).value=customer.pid;
     
      
      document.getElementById(`fp`).value=customer.itemid;
      
    } );
    previouspdetails(pdetails)

  }
  function getcus(abcin){
   
    
    abcin.forEach((cus,index) => {
      
      document.getElementById(`searchInput`).value=cus.name;
      document.getElementById(`customerid`).value=cus.id;
     



    });
   
  }
 

  function previouspdetails(pdetails){
    
    const tableBody = document.getElementById('invoice-form-items-table-body');
var index2;
    pdetails.forEach((customer,index) => {
      
 
   index2=index+1;
   rowNumber=index2;
      const newRow = document.createElement('tr');
      newRow.innerHTML = `
      <td class="fixed-column"  >${rowNumber}</td>
     
        <td class="form-input-td"><input  name="itemname"   id="itemname${index2}"  class="form-control itemnameinput" onclick="getrow(${index2},event)"  type="text" placeholder="Itemname" readonly></td>

  <td class="form-input-td"><input type="" name="qty" style="min-width:100px;" class="form-control"  id="qty${index2}" style="min-width:100px;" ondblclick="itemedit(${index2})" onkeydown="qtykeydown(event,${index2})" onclick="getrow(${index2},event)" oninput="calculateTotal(${index2})" required></td>  
  <td class="form-input-td"><input type="" name="srate" id="srate${index2}" style="min-width:100px;"  oninput="calculateTotal(${index2})" class="form-control" onclick="getrow(${index2},event)" onkeydown="nextrowkey(event,${index2})" required ></td>
 <input type="text" name="itemid" style="min-width:100px;" id="itemid${index2}" hidden="true" class="form-control"  >
       </td>
    `;
  
  tableBody.appendChild(newRow);
  let query=customer.item
  const typ='itemid'
    let  rownum=index2;
  fetch(`/getitem/?query=${query}&type=${typ}`)
      .then(response => response.json())
      .then(data => setitem(data.customers,rownum)
      
      );
      let amtt=0;
      function setitem(itemdata,rownum){
        
        itemdata.forEach((item,index) => {
        
       
        document.getElementById(`itemname${rownum}`).value=item.name;

        
        document.getElementById(`itemid${rownum}`).value = customer.pcode;

        document.getElementById(`srate${rownum}`).value = customer.rate;
     
        document.getElementById(`qty${rownum}`).value = customer.qty;
       //  document.getElementById(`total${index2}`).value = customer.tempqty * customer.rate;
       
     
  
        });
      
      
      }

 
  
  });
  


  }
  function calculateTotal(rowNumber) {
  
    let incscheck = document.getElementById(`incltax${rowNumber}`).value;
    const saleInput = document.getElementById(`prate${rowNumber}`);
  
    const quantityInput = document.getElementById(`qty${rowNumber}`);
   
  
    const name1 = document.getElementById(`itemname${rowNumber}`);
    const vattax = document.getElementById(`vat${rowNumber}`);
  
  
    const sale = parseFloat(saleInput.value) || 0;
  const quantity = parseFloat(quantityInput.value) || 0;
 
   const vatt=parseFloat(vattax.value) || 0;
   const tableBody = document.getElementById('invoice-form-items-table-body');
     var net;
     var total;
     var tax;
     var amtt;
     var totamount=0;
    //  if(incscheck==1){
  
    
    //   tax = (sale*vatt)/(100+vatt);
    //   tax=tax*quantity;
   
  
    //   amtt=(sale*quantity)-tax;
    //   net=tax+amtt;
      
      
      
    //     }
    //   else{
      
  
      
      amtt=quantity*sale;
      tax = (sale*vatt)/(100);
      tax=tax*quantity;
      net=amtt;
      // }
     
      document.getElementById(`amt${rowNumber}`).value=net.toFixed(2);
      for(i=1;i<=tableBody.rows.length;i++){
        const amount= parseFloat(document.getElementById(`amt${i}`).value);
        totamount=totamount+amount;
        
       }
     
      document.getElementById(`rowcost`).value=totamount.toFixed(2);
      document.getElementById(`packedcost`).value=totamount.toFixed(2);
      calculateTotal_pset(1);

  }
  function calculateTotal_pset(rowNumber) {
    const raw=document.getElementById(`packedcost`);
    let incscheck = document.getElementById(`incltaxpset${rowNumber}`).value;
    const saleInput = document.getElementById(`pratepset${rowNumber}`);
    const crateInput = document.getElementById(`cratepset${rowNumber}`);
  
    const quantityInput = document.getElementById(`qtypset${rowNumber}`);
   
  
    const name1 = document.getElementById(`itemnamepset${rowNumber}`);
    const vattax = document.getElementById(`vatpset${rowNumber}`);
  
  
    const sale = parseFloat(saleInput.value) || 0;
    const rowcost = parseFloat(raw.value) || 0;
  const quantity = parseFloat(quantityInput.value) || 0;
    const prate=rowcost/quantity;
    saleInput.value=prate.toFixed(2);
    crateInput.value=prate.toFixed(2);
   const vatt=parseFloat(vattax.value) || 0;

  
     var net=0;
     var total;
     var tax;
     var amtt=0;
     
    //  if(incscheck==1){
  
    
    //   tax = (sale*vatt)/(100+vatt);
    //   tax=tax*quantity;
   
  
    //   amtt=(sale*quantity)-tax;
    //   net=tax+amtt;
      
      
      
    //     }
    //   else{
      
  
      
      amtt=quantity*prate;
      
      net=amtt
      // }
    if(net=='' || net==NaN){
      net=0
    }
  
      document.getElementById('amtpset1').value=net.toFixed(2);
  }
  function previous_productset(vno){
    
 
    fetch(`/getfinishproduct/?query=${vno}`)
        .then(response => response.json())
        .then(data =>{ 
          var Table = document.getElementById("invoice-form-items-table-body");
      Table.innerHTML = "";
          displayproductdetails_infinshed(data.data2);
          display_previousproductset(data.data1,1);
    


        }
        
        ); 
  }
function Fill_table(){
  fillproductdetails();
  Fillproductset();

}
  function Fillproductset(){
    
      
     
   
   //   const vno = document.getElementById(`vno`);
   //  let query= parseInt(vno.value)-1;
   
   let query=document.getElementById('productid').value
   const typ='itemid'

   fetch(`/getitem/?query=${query}&type=${typ}`)
       .then(response => response.json())
       .then(data => display_productset(data.customers,1)
       
       );
   
     }
   


    
   
     function display_productset(itemdata,rownum){
       
       const tableBody = document.getElementById('invoice-form-items-table-body');
   
      
          
          itemdata.forEach((item,index) => {
          
         
          document.getElementById(`itemnamepset${rownum}`).value=item.name;
          
          document.getElementById(`itemcodepset${rownum}`).value=item.itemcode;
          
         
          document.getElementById(`incltaxpset${rownum}`).value= item.incs;
          //  let incscheck = document.getElementById(`incltaxpset ${rownum}`);
           document.getElementById(`pratepset${rownum}`).value = item.prate;
          //  document.getElementById(`cratepset${rownum}`).value = item.crate;
          //  document.getElementById(`mrppset${rownum}`).value = item.mrp;
          document.getElementById(`sratepset${rownum}`).value = item.srate;
          


     
          
          });
        
        
        }
        
         // calculateTotal(index2);
   
       
         function display_previousproductset(itemdata,rownum){
       
          const tableBody = document.getElementById('invoice-form-items-table-body');
      
         
             
             itemdata.forEach((item,index) => {
             
              document.getElementById(`vno`).value=item.vno;
              document.getElementById(`sdate`).value=item.vdate;
              document.getElementById(`pdate`).value=item.packdate;
              document.getElementById(`narration`).value=item.narration;
             document.getElementById(`itemnamepset${rownum}`).value=item.name;
             document.getElementById(`qtypset${rownum}`).value=item.qty;
             document.getElementById(`itemcodepset${rownum}`).value=item.itemcode;
             
            
             document.getElementById(`incltaxpset${rownum}`).value= item.incs;
             //  let incscheck = document.getElementById(`incltaxpset ${rownum}`);
              document.getElementById(`pratepset${rownum}`).value = item.prate;
             //  document.getElementById(`cratepset${rownum}`).value = item.crate;
             //  document.getElementById(`mrppset${rownum}`).value = item.mrp;
             document.getElementById(`sratepset${rownum}`).value = item.srate;
             document.getElementById(`productid`).value = item.itemid;
             let query=item.itemid
             const typ='itemid'
         
             fetch(`/getitem/?query=${query}&type=${typ}`)
                 .then(response => response.json())
                 .then(data => setitem(data.customers,rownum)
                 
                 );
                 let amtt=0;
                 function setitem(itemdata,rownum){
                   
                   itemdata.forEach((item,index) => {
                   
                    document.getElementById(`searchInput`).value=item.name;
                   document.getElementById(`itemnamepset${rownum}`).value=item.name;
                   document.getElementById(`itemcodepset${rownum}`).value=item.itemcode;
                   });}
        
             
             });
           
           
           }
     
     
     
     
   
     
     function fillproductdetails(){
      
   const vno =document.getElementById('voucherid').value;
      var Table = document.getElementById("invoice-form-items-table-body");
      Table.innerHTML = "";
      
      //   const vno = document.getElementById(`vno`);
      //  let query= parseInt(vno.value)-1;
      
             fetch(`/getproductset/?query=${vno}`)
                      .then(response => response.json())
                      .then(data => displayproductdetails_infinshed(data.data1)
                        
                        );
      
        }
      
     
       
      
        function displayproductdetails_infinshed(pdetails){
          
          const tableBody = document.getElementById('invoice-form-items-table-body');
      var index2;
          pdetails.forEach((customer,index) => {
            
       
         index2=index+1;
         rowNumber=index2;
            const newRow = document.createElement('tr');
            newRow.innerHTML = `
            <td class="fixed-column"  >${rowNumber}</td>
           
            <td class="form-input-td"><input name="itemcode" style="min-width:300px;" id="itemcode${rowNumber}" type="text" class="form-control" placeholder="Itemcode" readonly></td>
					<td class="form-input-td"><input name="itemname" style="min-width:350px;" id="itemname${rowNumber}" class="form-control" type="text"  placeholder="Itemname" readonly></td>
					<td class="form-input-td"><input type="number" name="qty" style="min-width:100px;" class="form-control" id="qty${rowNumber}" placeholder="0.00" oninput="calculateTotal(${rowNumber})" required></td>
          					<td class="form-input-td"><input type="number" name="crate" id="crate${rowNumber}" style="min-width:100px;" placeholder="0.00"  class="form-control"  required></td>
        
          <td class="form-input-td"><input type="number" name="prate" id="prate${rowNumber}" style="min-width:100px;" placeholder="0.00"  class="form-control" oninput="calculateTotal(${rowNumber})"   ></td>

                    <td class="form-input-td"><input type="number" name="srate" id="srate${rowNumber}" style="min-width:100px;" placeholder="0.00" class="form-control"  required></td>
                    <td class="form-input-td"><input type="number" name="mrp" style="min-width:100px;" id="mrp${rowNumber}" placeholder="0.00" class="form-control"  readonly></td>

                    <td class="form-input-td"><input type="text" name="amt" style="min-width:100px;" class="form-control" placeholder="0.00" id="amt${rowNumber}"  readonly>
						<input type="number" name="itemid"  id="itemid${rowNumber}" hidden="true"  class="form-control">
						<input type="number" name="incl" " id="incltax${rowNumber}" hidden="true" class="form-control">
						<input type="text" name="vat" style="min-width:100px;" id="vat${rowNumber}" hidden="true" class="form-control">

					</td>
          `;
        
        tableBody.appendChild(newRow);
        let query=customer.item
        const typ='itemid'
          let  rownum=index2;
        fetch(`/getitem/?query=${query}&type=${typ}`)
            .then(response => response.json())
            .then(data => setitem(data.customers,rownum)
            
            );
            let amtt=0;
            function setitem(itemdata,rownum){
              
              itemdata.forEach((item,index) => {
              
             
              document.getElementById(`itemname${rownum}`).value=item.name;
      
            
              document.getElementById(`itemid${rownum}`).value = customer.item;
      
              document.getElementById(`prate${rownum}`).value = customer.rate;
           
              document.getElementById(`qty${rownum}`).value = customer.qty;
              document.getElementById(`itemcode${rownum}`).value=item.itemcode;
              document.getElementById(`srate${rownum}`).value=item.srate;
              // document.getElementById(`crate${rownum}`).value=item.crate;
              // document.getElementById(`mrp${rownum}`).value=item.name;
             //  document.getElementById(`total${index2}`).value = customer.tempqty * customer.rate;
             
           
        calculateTotal(rownum)
              });
            
            
            }
      
       
        
        });
        
      
      
        }
   