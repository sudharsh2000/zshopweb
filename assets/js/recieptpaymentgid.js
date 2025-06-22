
const tableBody = document.getElementById('invoice-form-items-table-body');
let tablerow=tableBody.rows.length;
var rowNumber = 1;

var rownum2;
let  aa=2;
let tf=0
let tnet=0;
let ttax=0;
var index2;
let incscheck=0;
var trntype='';

//calculations for total amount and related

  function calculateTotal(rowNumber) {
    const amtInput = document.getElementById(`amt${rowNumber}`);
    const taxpercInput = document.getElementById(`taxperc${rowNumber}`);
    const taxamtInput = document.getElementById(`taxamt${rowNumber}`);
    



    const sale = parseFloat(amtInput.value) || 0;
    const quantity = parseFloat(taxpercInput.value) || 0;
     
    const taxamt=(sale*quantity)/100

    
    taxamtInput.value=parseFloat(taxamt).toFixed(2);
  

	// tf=total.toFixed(2);;
	// tnet=net.toFixed(2);

	
totalfind(rowNumber);
  }


  function totalfind(rowNumber) {

var finalnet=0;
var finalamt=0;
var finaltax=0;
const tableBody = document.getElementById('invoice-form-items-table-body');

const rowlength=tableBody.rows.length

for (let i = 1; i <= rowlength; i++) {

let amt=document.getElementById(`amt${i}`);
let taxperc=document.getElementById(`taxperc${i}`);
let taxamt=document.getElementById(`taxamt${i}`);


finalnet+=parseFloat( amt.value);


finalamt+=parseFloat(taxperc.value);
finaltax+=parseFloat( taxamt.value);


}



	var totamt=	document.getElementById('totalamt');
	// var totnet=	document.getElementById('nettotal');
	// var tottax=	document.getElementById('taxamt');
 
if(isNaN(finalnet)){
  
  finalnet=parseFloat(0)
}
else{
  
}
	totamt.value=finalnet.toFixed(2);
	





  }


//opening and closing popup

        function openPopupitem() {
      document.getElementById('overlay2').style.display = 'flex';
    }

    function closePopupitem() {
      document.getElementById('overlay2').style.display = 'none';
    }
    let ledgerlen=0;
    let templedname=[];
    let templedid=[];
    let tempaliasnm=[];
    let selectedResultIndex = -1;
    const itemresultsContainer = document.getElementById('item-tbl-body');

    const company = document.getElementById('cmp').value;

//grid search ledger

 function search(rowNumber) {



  templedname=[];
  templedid=[];
  tempaliasnm=[];
   
  const item = document.getElementById(`ledname${rowNumber}`);
  var query=item.value;
  let vtype=document.getElementById('vtype').value;
  id=20;
 
  fetch(`/search/?query=${query}&id=${id}&comp=${company}`)
       .then(response => response.json())
       .then(data => displayResults(data.customers,rowNumber));
        }

   ///Display grid     
        function displayResults(customers,rowNumber) {
          
            openPopupitem();
            ledgerlen=customers.length;
            const tableBody = document.getElementById('item-tbl-body');
             tableBody.innerHTML = '';

            customers.forEach(customer => {
              const mainlist = document.createElement('tr');
                const listItem = document.createElement('td');
                mainlist.classList.add('result-item2');

                listItem.textContent = customer.name;
                listItem.value=customer.id

                 const listalias = document.createElement("td");
                 if(customer.alias==''){
                    listalias.textContent='';
                   }
                   else{
                    listalias.textContent=customer.alias;
                   }


                 
                   templedname.push(customer.name);
templedid.push(customer.id);
tempaliasnm.push(customer.alias);


listItem.style.width = "280px";
listalias.style.width = "150px";



mainlist.appendChild(listItem);
mainlist.appendChild(listalias);

mainlist.value=customer.id;


tableBody.appendChild(mainlist);




            
                

                mainlist.onclick = () => selectitem(customer.id,customer.name,customer.alias,rowNumber);


            });
        }

        function selectitem(customerid,customernm,aliasnm,rowNumber) {
          



            document.getElementById(`ledname${rowNumber}`).value = customernm;
               document.getElementById(`ledid${rowNumber}`).value = customerid;
               
               document.getElementById(`note${rowNumber}`).focus()
              


closePopupitem();

        }

//enter and grid select


        
       ///select and display ledgers
 var ledgid;       
  function selectResultled(index,rowNumber) {
    let query=ledgid;
    fetch(`/getcustomer/?query=${query}&comp=${company}`)
    .then(response => response.json())
    .then(data =>displayled(data.customers));
     
    function displayled(customers){
      customers.forEach(customer => {
        
        document.getElementById(`ledname${rowNumber}`).value =customer. name;
        document.getElementById(`ledid${rowNumber}`).value =customer. id;
        document.getElementById(`note${rowNumber}`).focus()
      })
     
    }
                   closePopupitem();
                
  }

//keyboard function

  function handleKeyDown(event,rowNumber) {
    // alert(ledgerlen)
    
    if (event.key === 'ArrowDown') {
      
      event.preventDefault();
      selectedResultIndex = Math.min(selectedResultIndex + 1, ledgerlen);
      highlightSelectedResult();
    } else if (event.key === 'ArrowUp') {
      event.preventDefault();
      selectedResultIndex = Math.max(selectedResultIndex - 1,0);
      highlightSelectedResult();
    } else if (event.key === 'Enter') {
      if (selectedResultIndex !== -1) {
        event.preventDefault();
        selectResultled(selectedResultIndex,rowNumber);
        selectedResultIndex = -1;
      }
    }

    }
  function highlightSelectedResult() {
   
    
    const tableBody = document.getElementById('item-tbl-body').children;

    Array.from(tableBody).forEach((item, index)  => {
        
      if (index === selectedResultIndex) {
        item.style.backgroundColor = '#e0e0e0';
        item.scrollIntoView({ behavior: 'smooth', block: 'center' });
       ledgid=item.value;
      } else {
        item.style.backgroundColor = '';
      }
    });
  }
  
  // Handle keyboard events
  

  // Hide results when clicking outside the input and results container
  document.addEventListener('click', (event) => {
    // const isClickInsideInput = searchInput.contains(event.target);
    const isClickInsideResults = itemresultsContainer.contains(event.target);

    if ( !isClickInsideResults) {
      closePopupitem();
    }
  });


//add newrow


  function addRow(e) {
    
    
    

    const tableBody = document.getElementById('invoice-form-items-table-body');
    let tablerow=tableBody.rows.length;
     rowNumber = tablerow+1;
    rownum2=rowNumber;
    
    const newRow = document.createElement('tr');
    newRow.innerHTML = `
    <td class="">${aa}</td>
    <td ><input name="ledname" style="min-width:14rem;"  onkeydown="handleKeyDown(event,${rowNumber});getrow(${index2},event)" onclick="getrow(${index2},event)"  oninput="search(${rowNumber});getrow(${index2},event)" onclick="getrow(${index2},event)" onblur="checkundef(${rowNumber})" id="ledname${rowNumber}" class="form-control"  type="text" ></td>
		
			  <td><input type="text" name="note" style="min-width:13rem;" id="note${rowNumber}" onclick="getrow(${index2},event)" class="form-control"  ></td>
			  <td><input type="number" name="taxperc" style="min-width:12rem;" placeholder="0.00" id="taxperc${rowNumber}" onclick="getrow(${index2},event)" oninput="calculateTotal(${rowNumber})"  class="form-control"  ></td>
			  <td><input type="number" name="taxamt" style="min-width:12rem;" placeholder='0.00' id="taxamt${rowNumber}" onclick="getrow(${index2},event)" class="form-control" readonly ></td>
			  <td><input type="number" name="amt" style="min-width:12rem;" id="amt${rowNumber}" placeholder="0.00" oninput="calculateTotal(${rowNumber})" onclick="getrow(${index2},event)" class="form-control"  onkeydown="nextrowkey(event)"></td>
				 <td>
         <input type="text" name="ledid" style="min-width:12rem;" id="ledid${rowNumber}" hidden="true" class="form-control"  >
         0</td>
				
     `;

    tableBody.appendChild(newRow);
   
   document.getElementById(`ledname${rowNumber}`).focus();
 
    rowNumber++;
    aa++;



  }
  //add new row when
function nextrowkey(){


  if (event.key === 'Enter'|event.key=='Tab') {
    event.preventDefault();
    addRow();
    }
    if (event.key === 'F5') {
      event.preventDefault();
      
      }
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
function checkundef(rowNumber){

let lednm=document.getElementById(`ledname${rowNumber}`).value;
let ledid=document.getElementById(`ledid${rowNumber}`).value;

if(lednm=='undefined' ||ledid==''){
  document.getElementById(`ledname${rowNumber}`).focus();
  document.getElementById(`ledname${rowNumber}`).value=''

}


}
function Loaddata(){
  
  // if (navigator.userAgent.match(/Mobile/)) {
  //   document.getElementById('landscapetbl').innerHTML = '';
  //   }
  //   else{
  //     document.getElementById('table-responsive').innerHTML = '';

  //   }
  const type = document.getElementById('type').value;
  const prevno = document.getElementById('prevno').value;
  
  const setvno = document.getElementById('vno');
  if(type=='report'){
    setvno.value=parseInt( prevno)+1;
    previousdata();

  }
  
}
///save data 

document.addEventListener("keydown", keyDownTextField, false);
let salesform = document.getElementById('invoice-form');
let submitbutton = document.getElementById('subtmit');
let table = document.getElementById('invoice-form-items-table');
let tablemain =document.getElementById('invoice-form-items-table-body');
let printsave =document.getElementById('printssave');
var valid=true;
function keyDownTextField(e) {
let rowlength=tableBody.rows.length;
  if(event.key === 'F5') {

    event.preventDefault()
    validform();
   if(valid) {

  

    
    
      const vno = document.getElementById(`vno`).value;
      const vtyp = document.getElementById(`vtype`).value;
      const company = document.getElementById(`cmp`).value;
        fetch(`/getvno/?type=${vtyp}&company=${company}`)
        .then(response => response.json())
        .then(data => savecurfn(data.vno)
        
        );
  function savecurfn(vnomax){
   
    if(trntype==''){
      document.getElementById(`vno`).value=vnomax;
    }
    
 
    document.getElementById("invoice-form").submit();
    if(printsave.checked==true){
      printa4();
    }
    
    
   
  
  }

    

    
    }

  } 
  if(event.key === 'F12') {
    event.preventDefault()
    document.getElementById(`ledname${rowlength}`).focus();
  }
  if(event.key === 'Enter') {
    event.preventDefault()
    
  }

}
function validform(){
 

  valid=true;

  // Start loop at 1 to skip table header
  for (let i = 1; i <=tablemain.rows.length; i++) {
    
       
    if(document.getElementById(`ledname${i}`).value!=''){
  
  
      

      if (   document.getElementById(`amt${i}`).value=='' || document.getElementById(`amt${i}`).value==0 ) {
      alert("Total amount is empty")    
        valid = false;
          break;
      }
     
    }
    if(document.getElementById(`amt${i}`).value!=''){
  
  
      

      if (   document.getElementById(`ledname${i}`).value=='' ) {
      alert("Please select ledger name")    
        valid = false;
          break;
      }
     
    }

   
 
  }




}

salesform.addEventListener("submit", (e) => {
  e.preventDefault();
    validform();
  if(valid) {

    

    
  
      const vno = document.getElementById(`vno`).value;
      const vtyp = document.getElementById(`vtype`).value;
      const company = document.getElementById(`cmp`).value;
        fetch(`/getvno/?type=${vtyp}&company=${company}`)
        .then(response => response.json())
        .then(data => savecurfn(data.vno)
        
        );
    function savecurfn(vnomax){
     
      if(trntype==''){
        document.getElementById(`vno`).value=vnomax;
      }
      
    
    
      document.getElementById("invoice-form").submit();
      
        if(printsave.checked==true){
      printa4();
    }
      
     
    
    }
    


    }

  // handle submit
});

  function removerow(this_,rowNumber){
 var tr = $(this_).closest("tr");

rowindex = tr.index();

// document.getElementById("invoice-form-items-table-body").deleteRow(rowNumber);
  }

  async function jumpdata(){
    var maxvno=await getmaxvvno();
    const vno = document.getElementById(`vno`);
   let query= parseInt(vno.value);
   if(query>0){
    if(maxvno<=query){
      location.reload()
    }
    else{
      addprevious(query);
  
    }
   }
   else{
    alert("Invalid transaction");
   }

  
    }
    function numberToWords(number) {
      const units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
      const teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"];
      const tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"];
  
      function convertToWordsLessThanThousand(num) {
          if (num === 0) return "";
  
          let words = "";
  
          if (num >= 100) {
              words += units[Math.floor(num / 100)] + " hundred";
              num %= 100;
              if (num > 0) {
                  words += " and ";
              }
          }
  
          if (num >= 11 && num <= 19) {
              words += teens[num - 10];
          } else {
              words += tens[Math.floor(num / 10)];
              num %= 10;
              if (num > 0) {
                  words += " " + units[num];
              }
          }
  
          return words;
      }
  
      if (number === 0) {
          return "zero";
      }
  
      const lakhs = Math.floor(number / 100000);
      const thousands = Math.floor((number % 100000) / 1000);
      const remaining = number % 1000;
  
      let result = "";
  
      if (lakhs > 0) {
          result += convertToWordsLessThanThousand(lakhs) + " lakh";
          if (thousands > 0 || remaining > 0) {
              result += " ";
          }
      }
  
      if (thousands > 0) {
          result += convertToWordsLessThanThousand(thousands) + " thousand";
          if (remaining > 0) {
              result += " ";
          }
      }
  
      if (remaining > 0) {
          result += convertToWordsLessThanThousand(remaining);
      }
  
      return result;
  }
  
  

   function printa4(){
    let vno=document.getElementById('vno').value;
    let ledger=document.getElementById('ledname1').value;
    let narration=document.getElementById('note1').value;
    let sdate=document.getElementById('sdate').value;
    let totalamt=document.getElementById('totalamt').value;

    let wordsamt=numberToWords(totalamt)


      var printWindow = window.open('', '_blank');
      printWindow.document.write('<html><head><title>A4 Printout</title><style> </style></head><body>');
    
      // Add table with headers
      printWindow.document.write('<div style="border: 1px solid black;height:1250px;width:1000px;border-radius:20px;">')  
      printWindow.document.write('<div style="background-color: afc2b3;margin: auto;margin-top:100px;">')          
        
      printWindow.document.write('<label style="margin-left:350px;font-size:30;font-weight:bold;">Receipt bill (فاتورة الاستلام)</label>')          
              

      printWindow.document.write('</div>')          
     printWindow.document.write('<table style="margin-top:100px;">')  
     printWindow.document.write('<tr >')         
      printWindow.document.write('<td><h3 style="margin-left:50px;">Date (تاريخ):&nbsp;&nbsp;&nbsp; '+sdate+' </h3></td>') 
                
      printWindow.document.write('<td ><h4 style="margin-left:300px;">Invoice No (رقم الفاتورة): &nbsp;&nbsp;&nbsp; '+vno+' </h4></td>')           
      printWindow.document.write('</tr>') 
      printWindow.document.write('<tr >')         
      printWindow.document.write('<td><h3 style="margin-left:50px;margin-top:60px" >Ledger (موازنة): &nbsp;&nbsp;&nbsp; '+ledger+' </h3></td>')          
      printWindow.document.write('</tr>') 
      printWindow.document.write('<tr >')         
      printWindow.document.write('<td><h3 style="margin-left:50px;margin-top:60px" >Narration (السرد): &nbsp;&nbsp;&nbsp; '+narration+' </h3></td>')          
      printWindow.document.write('</tr>') 
      printWindow.document.write('<tr >')         
      printWindow.document.write('<td><h3 style="margin-left:50px;margin-top:60px" >Amount in Words (المبلغ بالكلمات): &nbsp;&nbsp;&nbsp; '+wordsamt+'</h3></td>')          
      printWindow.document.write('</tr>') 
      printWindow.document.write('<tr >')         
      printWindow.document.write('<td><h3 style="margin-left:50px;margin-top:60px" >Amount in Rupees(المبلغ بالروبية) : &nbsp;&nbsp;&nbsp; '+totalamt+'</h3></td>')          
      printWindow.document.write('</tr>') 
      printWindow.document.write('</table>')  
    
     
      printWindow.document.write('</body></html>');
      if ('serviceWorker' in navigator) {
        if (window.matchMedia('(display-mode: standalone)').matches) {
          printWindow.print()
        } else if (window.navigator.standalone) {
          printWindow.print();
           
        } else {
          printWindow.onafterprint = function() {
            printWindow.close();  // Close the window after print
      };
      printWindow.print()
        }
    } else {
        alert('This is a website, not a PWA.');
    }
      
    }
    

    async function getmaxvvno() {
      const vtyp = document.getElementById('vtype').value;
      
      
      try {
        const response = await fetch(`/getvno/?type=${vtyp}`);
        const data = await response.json();
        return data.vno; // Return the fetched vno value
      } catch (error) {
        console.error("Error fetching max vno:", error);
        return null; // Return null if there's an error
      }
    }
  async function previousdata(){
  var maxvno=await getmaxvvno();
  const vno = document.getElementById(`vno`);
 let query= parseInt(vno.value)-1;
 if(query>0){
  if(maxvno==query){
    location.reload()
  }
  else{
    addprevious(query);

  }
 }
 else{
  alert("Minimum sale Reached");
 }
  }
 async function nextdata(){
    var maxvno=await getmaxvvno();

  const vno = document.getElementById(`vno`);
 let query= parseInt(vno.value)+1;
 if (query>=maxvno){
  location.reload()
}
else{
  addprevious(query);

}
  }





  function addprevious(vno){
 trntype='pre';
 let vtype=document.getElementById('vtype').value;
 
    var Table = document.getElementById("invoice-form-items-table-body");
Table.innerHTML = "";


       fetch(`/getpreviouspaymentreceipt/?query=${vno}&vtype=${vtype}&comp=${company}`)
                .then(response => response.json())
                .then(data => displayprevious(vno,data.data1,data.lvno)
                  
                  );

  }




  function displayprevious(curvno,generalledger,lvno){
   

  if(lvno==0){
    document.getElementById(`vno`).value=curvno
    addRow()
   	document.getElementById('amttotal').value='0.00';
document.getElementById('nettotal').value='0.00';
	document.getElementById('taxamt').value='0.00';
  }
 


  receiptpaydetailsprev(generalledger);
    
    

  }
  
 

  function receiptpaydetailsprev(generalledger){
    indexmain=0
    const tableBody = document.getElementById('invoice-form-items-table-body');

    generalledger.forEach((customer,index) => {
      
    
 
 
    
  
    const ledvno=customer.vno;
    const ledvdate=customer.vdate;
    const ledledcode=customer.ledcode;
    const ledcramt=customer.cramt;
    const leddbamt=customer.dbamt;
    const ledtaxamt=customer.rptaxamt;
    const ledtaxperc=customer.rptaxperc;
    const vtype = document.getElementById('vtype').value;
   
    var datetimeString = customer.vdate;
    var date = new Date(datetimeString);
    
    var year = date.getUTCFullYear();
    var month = ('0' + (date.getUTCMonth() + 1)).slice(-2); // Adding 1 because months are zero-based
    var day = ('0' + date.getUTCDate()).slice(-2);
    var hours = ('0' + date.getUTCHours()).slice(-2);
    var minutes = ('0' + date.getUTCMinutes()).slice(-2);
    var seconds = ('0' + date.getUTCSeconds()).slice(-2);
    
    var formattedDatetime = year + "-" + month + "-" + day;

if(vtype=='R'){
    if(leddbamt>0){
      

      
      
      // Output: 2024-04-06 11:48:00
      
      

    
      document.getElementById(`vno`).value=customer.vno;
      document.getElementById(`sdate`).value=formattedDatetime;
      document.getElementById(`payment`).value=ledledcode;
     

    }
    else{


      index2=index+1;
    indexmain=indexmain+1
         const newRow = document.createElement('tr');
         newRow.innerHTML = `
         <td class="" >${index2}</td>
         <td><input name="ledname" style="min-width:14rem;"  onkeydown="handleKeyDown(event,${index2});getrow(${index2},event)" onclick="getrow(${index2},event)" oninput="search(${index2});getrow(${index2},event)" id="ledname${index2}" class="form-control"  type="text" placeholder="Itemname"></td>
   
         <td><input type="text" name="note" style="min-width:13rem;" id="note${index2}"  class="form-control"  ></td>
         <td><input type="text" name="taxperc" style="min-width:12rem;" id="taxperc${index2}" oninput="calculateTotal(${index2})"  class="form-control"  ></td>
         <td><input type="text" name="taxamt" style="min-width:12rem;" placeholder='0.00' id="taxamt${index2}"  class="form-control" readonly  ></td>
         <td><input type="text" name="amt" style="min-width:12rem;" id="amt${index2}" placeholder="0.00" oninput="calculateTotal(${index2})"  class="form-control"  onkeydown="nextrowkey(event)"></td>
            <td>
            <input type="text" name="ledid" style="min-width:12rem;" id="ledid${index2}" hidden="true" class="form-control"  >
   
            </td>
       `;
     
     tableBody.appendChild(newRow);
     let  rownum=index2;




query=customer.ledcode;

      fetch(`/getcustomer/?query=${query}&comp=${company}`)
          .then(response => response.json())
          .then(data =>getcus(data.customers,rownum)
          
          
          );
   

      

       document.getElementById(`taxperc${index2}`).value = customer.taxperc;
       document.getElementById(`taxamt${index2}`).value = customer.taxamt;
       document.getElementById(`amt${index2}`).value=customer.cramt;
       document.getElementById(`note${index2}`).value=customer.naration2;
       
       calculateTotal(index2);
    }
  }

else{

  if(ledcramt>0){
    document.getElementById(`vno`).value=customer.vno;
    document.getElementById(`sdate`).value=formattedDatetime;
    document.getElementById(`payment`).value=ledledcode;

  }
  else{


    index2=index+1;
    
    // rowNumber=index2;
       const newRow = document.createElement('tr');
       newRow.innerHTML = `
       <td class="" >${index2}</td>
       <td ><input name="ledname" style="min-width:14rem;"  onkeydown="handleKeyDown(event,${index2});getrow(${index2},event)" onclick="getrow(${index2},event)" oninput="search(${index2});getrow(${index2},event)" id="ledname${index2}" class="form-control"  type="text" placeholder="Itemname"></td>
 
       <td><input type="text" name="note" style="min-width:13rem;" id="note${index2}" onclick="getrow(${index2},event)" class="form-control"  ></td>
       <td><input type="text" name="taxperc" style="min-width:12rem;" id="taxperc${index2}" onclick="getrow(${index2},event)" oninput="calculateTotal(${index2})"  class="form-control" ></td>
       <td><input type="text" name="taxamt" style="min-width:12rem;" value='0.00' id="taxamt${index2}" onclick="getrow(${index2},event)" class="form-control"  readonly ></td>
       <td><input type="text" name="amt" style="min-width:12rem;" id="amt${index2}" placeholder="0.00" oninput="calculateTotal(${index2})" onclick="getrow(${index2},event)" class="form-control"  onkeydown="nextrowkey(event)"></td>
          <input type="text" name="ledid" style="min-width:12rem;" id="ledid${index2}" hidden="true" class="form-control"  >
             
      </td>
     `;
   
   tableBody.appendChild(newRow);
   let  rownum=index2;




query=customer.ledcode;


    fetch(`/getcustomer/?query=${query}&comp=${company}`)
        .then(response => response.json())
        .then(data =>getcus(data.customers,rownum)
        
        
        );
 

    

     document.getElementById(`taxperc${index2}`).value = customer.taxperc;
     document.getElementById(`taxamt${index2}`).value = customer.taxamt;
     document.getElementById(`amt${index2}`).value=customer.dbamt;
     document.getElementById(`note${index2}`).value=customer.naration2;
     
     calculateTotal(index2);
  }


  
}




  
  
  });
  function getcus(abcin,rownum){
   
    
    abcin.forEach((cus,index) => {

      document.getElementById(`ledname${rownum}`).value=cus.name;
        document.getElementById(`ledid${rownum}`).value=cus.id;


    });

  }
  }
  
  