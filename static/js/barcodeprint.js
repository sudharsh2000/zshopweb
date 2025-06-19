


var rowNumber ;
let  aa=2;
let tf=0
let tnet=0;
let ttax=0;
var dltrowid;
var dltrowname;
let incscheck=0;
var myArray = [];

let selectedResultIndex=-1;


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
    let tempmrp=[];
    let tempprate=[];
    const itemresultsContainer = document.getElementById('itemresults');
    const comp = document.getElementById('cmp').value;
 function search() {
tempbarcode=[];
tempitemname=[];
tempsrate=[];
temptax=[];
ilang=[];
tempitemid=[];
vat=[];
tempitemcode=[];
tempmrp=[];
tempprate=[];


const query = document.getElementById(`itemcode`).value;


       fetch(`/searchitem/?query=${query}&comp=${comp}`)
                .then(response => response.json())
                .then(data => displayitemResults(data.customers,rowNumber));
        }
        function searchitemname() {
          tempbarcode=[];
          tempitemname=[];
          tempsrate=[];
          temptax=[];
          ilang=[];
          tempitemid=[];
          vat=[];
          tempitemcode=[];
          tempmrp=[];
          tempprate=[];
          
          const query = document.getElementById(`itemname`).value;
         
          
                 fetch(`/searchitem/?query=${query}&comp=${comp}`)
                          .then(response => response.json())
                          .then(data => displayitemResults(data.customers,rowNumber));
                  }
                  function searchbarcode() {
                    tempbarcode=[];
                    tempitemname=[];
                    tempsrate=[];
                    temptax=[];
                    ilang=[];
                    tempitemid=[];
                    vat=[];
                    tempitemcode=[];
                    tempmrp=[];
                    tempprate=[];
                    
                    const query = document.getElementById(`bcode`).value;
                    
                    
                           fetch(`/searchitem/?query=${query}&comp=${comp}`)
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
tempmrp.push(customer.mrp)
tempprate.push(customer.prate)
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


resultsList.appendChild(mainlist);

console.log(tempitemid)



                   const divide = document.createElement('hr');

                resultsList.appendChild(divide);
                

                listItem.onclick = () => selectitem(customer.id,customer.name,customer.bcode,customer.srate,customer.prate,customer.itemcode, customer.mrp);


            });
        }

        function selectitem(customerid,customer,barcode,srate,prate,itemcode, mrp) {


          document.getElementById('itemname').value=customer
          document.getElementById('itemcode').value=itemcode;
          document.getElementById('bcode').value=barcode;
          document.getElementById('srate').value=srate;
          document.getElementById('prate').value=prate;
          document.getElementById('mrp').value=mrp;
          document.getElementById('qty').focus();
   

closePopupitem();

        }

//enter and grid select


        
myArray=[];
        
  function selectResultitem(index,rowNumber) {

   document.getElementById('itemname').value=tempitemname[index];
   document.getElementById('itemcode').value=tempitemcode[index];
   document.getElementById('bcode').value=tempbarcode[index];
   document.getElementById('srate').value=tempsrate[index];
   document.getElementById('prate').value=tempprate[index];
   document.getElementById('mrp').value=tempmrp[index];
   document.getElementById('qty').focus();

   closePopupitem();
     

  }
  function handleKeyDown(event) {
  
 
    
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
        selectResultitem(selectedResultIndex);
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
      } else {
        item.style.backgroundColor = '';
      }
    });
  }
  
  // Handle keyboard events
  

  // Hide results when clicking outside the input and results container
  document.addEventListener('click', (event) => {
    const searchInput=document.getElementById('itemcode')
    const isClickInsideInput = searchInput.contains(event.target);
    const isClickInsideResults = itemresultsContainer.contains(event.target);

    if (!isClickInsideInput && !isClickInsideResults) {
      closePopupitem();
    }
  });

  








  

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
    alert(itemname.value)
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
  const itemname=document.getElementById('itemname')
  const itemcode=document.getElementById('itemcode')
  
  const barcode=document.getElementById('bcode')
  const qty=document.getElementById('qty')
  const mrp=document.getElementById('mrp')
  const srate=document.getElementById('srate')
  const prate=document.getElementById('prate')
  

//  var itemar= JSON.stringify(itemarray);
//  var qtyar= JSON.stringify(qtyarray);
//  var pricear= JSON.stringify(pricearray);
//  var grossar= JSON.stringify(grossarray);
//  var taxar= JSON.stringify(taxarray);
//  var amountar= JSON.stringify(amountarray);
   var printWindow = window.open('/printbarcodeview/?iname='+itemname.value+'&bcode='+barcode.value+'&mrp='+mrp.value+'&srate='+srate.value+' ');




}
function printbarcodeviewdisplay(){

const itemname=document.getElementById('itemname').value;
const barcode=document.getElementById('bcode').value;
const qty=document.getElementById('qty').value;

if(itemname=='' | barcode==''|qty==''){
  alert('Please Fill Blank Fields')
}
else{
 
  generateprintA4();
 location.reload()
}


}

///save data 



  
   
     
  