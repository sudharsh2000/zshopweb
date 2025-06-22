

function Summary(){
  

  const tableBody = document.getElementById('invoice-form-items-table-body');
  tableBody.innerHTML='';
  openingbalence();
  company=document.getElementById('cmp').value;
  area=document.getElementById('area').value;
  user=document.getElementById('user').value;
  curarea=document.getElementById('curarea').value;
  allarea=document.getElementById('allarea')
  customerid=document.getElementById('customerid').value;

  alluser=document.getElementById('alluser')
if(area=='HEAD OFFICE'){
  if(allarea.checked==true){
    fromdt=document.getElementById('from-date').value;
    todt=document.getElementById('to-date').value;
    fetch(`/ledgerget/?lid=${customerid}&fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'all'}&chkuser=${'all'}&comp=${company}&curarea=${curarea}`)
           .then(response => response.json())
           .then(data => displayrep(data.reportdata)
             
             );
  }
  else{

    if(alluser.checked==true){
      fromdt=document.getElementById('from-date').value;
    todt=document.getElementById('to-date').value;
    fetch(`/ledgerget/?lid=${customerid}&fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'all'}&comp=${company}&curarea=${curarea}`)
           .then(response => response.json())
           .then(data => displayrep(data.reportdata)
             
             );
    }
    else{
      fromdt=document.getElementById('from-date').value;
    todt=document.getElementById('to-date').value;
    fetch(`/ledgerget/?lid=${customerid}&fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'no'}&comp=${company}&curarea=${curarea}`)
           .then(response => response.json())
           .then(data => displayrep(data.reportdata)
             
             );
    }

  }
}
else{
  if(alluser.checked==true){
    fromdt=document.getElementById('from-date').value;
  todt=document.getElementById('to-date').value;
  fetch(`/ledgerget/?lid=${customerid}&fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'all'}&comp=${company}&curarea=${curarea}`)
         .then(response => response.json())
         .then(data => displayrep(data.reportdata)
           
           );
  }
  else{
    fromdt=document.getElementById('from-date').value;
  todt=document.getElementById('to-date').value;
  fetch(`/ledgerget/?lid=${customerid}&fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'no'}&comp=${company}&curarea=${curarea}`)
         .then(response => response.json())
         .then(data => displayrep(data.reportdata)
           
           );
  }
}
 
}
var rowNumber;
function displayrep(report){
 
  let finaltaxamt=0;
  let finalamt=0;
  let finalnetamt=0;
  let finalbalance=0;
  if(report==""){
    alert("No  data found")
   
  }
else{
  report.forEach(element => {
    
    const tb = document.getElementById('reportwindow');
    const searchwindow = document.getElementById('searchInput');
    
   

    tb.style.visibility='visible'

  //   finaltaxamt=finaltaxamt+ parseFloat(element.taxamt);
  //   finalamt=finalamt+ parseFloat(element.amount);
  //   finalqty=finalqty+ parseFloat(element.qty);
   const tableBody = document.getElementById('invoice-form-items-table-body');
  
  rowNumber=rowNumber+1;




    const newRow = document.createElement('tr');
    newRow.innerHTML = `
    <td id="vdate${rowNumber}" ondblclick="Toledger(${rowNumber})"></td>
    <td id="particular${rowNumber}" ondblclick="Toledger(${rowNumber})"></td>
    <td id="voucher${rowNumber}" ondblclick="Toledger(${rowNumber})"></td>
    <td id="vno${rowNumber}" ondblclick="Toledger(${rowNumber})"></td>

    <td id="notes${rowNumber}" ondblclick="Toledger(${rowNumber})"></td>
    <td id="debit${rowNumber}" ondblclick="Toledger(${rowNumber})"></td>

    <td id="credit${rowNumber}" ondblclick="Toledger(${rowNumber})"></td>
    <td id="balance${rowNumber}" ondblclick="Toledger(${rowNumber})"></td>
   
    <td id="vtype${rowNumber}" hidden="true">${element.vtype}</td>

   `;
   tableBody.appendChild(newRow);


   var dtdate=new Date(element.vdate)

// Get day, month, and year components
var day = dtdate.getDate();
var month = dtdate.getMonth() + 1; // Month is zero-based, so add 1
var year = dtdate.getFullYear() % 100; // Get last two digits of the year

// Pad single digit day or month with leading zero
day = (day < 10) ? '0' + day : day;
month = (month < 10) ? '0' + month : month;

// Formatted date string in "dd mm yy" format
var formattedDate = day + '/' + month + '/' + year;
   
    let vnotxt=document.getElementById(`vno${rowNumber}`)
    let vdatetxt=document.getElementById(`vdate${rowNumber}`)
    let particulartxt=document.getElementById(`particular${rowNumber}`)
    let vouchertxt=document.getElementById(`voucher${rowNumber}`)
    let notstxt=document.getElementById(`notes${rowNumber}`)
    let debittxt=document.getElementById(`debit${rowNumber}`)
    let credittxt=document.getElementById(`credit${rowNumber}`)

    let balancetxt=document.getElementById(`balance${rowNumber}`)
    
    vdatetxt.innerHTML=formattedDate;
    if(element.vno==''|| element.vno==null){
      particulartxt.innerHTML=element.particulars;
    }
    else{
      particulartxt.innerHTML=element.user;
      if(element.vtype=='PI'){
        vouchertxt.innerHTML='PURCHASE'
      }
      else if(element.vtype=='SI'){
        vouchertxt.innerHTML='SALES'
      }
      else if(element.vtype=='SR'){
        vouchertxt.innerHTML='SALES RETURN'
      }
      else if(element.vtype=='PR'){
        vouchertxt.innerHTML='PURCHASE RETURN'
      }
      else if(element.vtype=='R'){
        vouchertxt.innerHTML='RECEIPT'
      }
      else if(element.vtype=='P'){
        vouchertxt.innerHTML='PAYMENT'
      }
      else if(element.vtype=='SO'){
        vouchertxt.innerHTML='SALES ORDER'
      }
      else if(element.vtype=='PO'){
        vouchertxt.innerHTML='PURCHASE ORDER'
      }
      
    }
    
    vnotxt.innerHTML=element.vno;
    notstxt.innerHTML=element.note;
    debittxt.innerHTML=parseFloat(element.dbamt).toFixed(2);
    credittxt.innerHTML=parseFloat(element.cramt).toFixed(2);
    balancetxt.innerHTML=(parseFloat(element.dbamt)-parseFloat(element.cramt)).toFixed(2)
    const bal = document.getElementById(`balance${rowNumber}`);
    for(i=1;i<=tableBody.rows.length;i++){
    
var curbal=document.getElementById(`bal${i}`).innerHTML;
finalbalance=finalbalance+parseFloat(curbal);
    }
  
    fetch(`/getcustomer/?query=${element.ledcode}&comp=${company}`)
    .then(response => response.json())
    .then(data =>data.customers.forEach((cus,index) => {

      
      
      if(element.vno==''|| element.vno==null){
        vouchertxt.innerHTML=cus.name;
      }
      else{
        
        if(element.vtype=='PI'){
          vouchertxt.innerHTML='PURCHASE'
        }
        else if(element.vtype=='SI'){
          vouchertxt.innerHTML='SALES'
        }
        else if(element.vtype=='SR'){
          vouchertxt.innerHTML='SALES RETURN'
        }
        else if(element.vtype=='SO'){
          vouchertxt.innerHTML='SALES ORDER'
        }
        else if(element.vtype=='PO'){
          vouchertxt.innerHTML='PURCHASE ORDER'
        }
        else if(element.vtype=='PR'){
          vouchertxt.innerHTML='PURCHASE RETURN'
        }
        else if(element.vtype=='R'){
          vouchertxt.innerHTML='RECEIPT'
        }
        else if(element.vtype=='P'){
          vouchertxt.innerHTML='PAYMENT'
        }
        
      }
      
     



    })
    
    
    );

  });
}
  const tableBody = document.getElementById('invoice-form-items-table-body');
  
  
  

  



    const finalrw = document.createElement('tr');
    finalrw.innerHTML = `
    <td ></td>
    <td ></td>
    <td ></td>
    <td  style="color:#504646;"></td>
    <td id="finaldebit" style="color:#504646;"></td>
    <td id="finalcredit" style="color:#504646;"></td>
    <td id="finalamt" style="color:#504646;">Balance</td>
    <td id="finalnetbal" style="color:#504646;">${finalbalance.toFixed(2)}</td>
   
   `;
   tableBody.appendChild(finalrw);
 
}
function openingbalence(){
  
  const tb = document.getElementById('reportwindow');
  const searchwindow = document.getElementById('searchInput');
  
 

  tb.style.visibility='visible'

//   finaltaxamt=finaltaxamt+ parseFloat(element.taxamt);
//   finalamt=finalamt+ parseFloat(element.amount);
//   finalqty=finalqty+ parseFloat(element.qty);
 const tableBody = document.getElementById('invoice-form-items-table-body');





  const newRow = document.createElement('tr');
  newRow.innerHTML = `
  <td id="vdate${1}" ></td>
  <td id="particular${1}" >Opening Balence</td>
  <td id="voucher${1}" ></td>
  <td id="vno${1}" >OB</td>

  <td id="notes${1}" ></td>
  <td id="debit${1}" ></td>

  <td id="credit${1}" ></td>
  <td id="balance${1}" ></td>
 
  <td id="vtype${1}" hidden="true">OB</td>

 `;
 tableBody.appendChild(newRow);
  company=document.getElementById('cmp').value;
  area=document.getElementById('area').value;
  user=document.getElementById('user').value;
  curarea=document.getElementById('curarea').value;
  allarea=document.getElementById('allarea')
  customerid=document.getElementById('customerid').value;

  alluser=document.getElementById('alluser')
if(area=='HEAD OFFICE'){
  if(allarea.checked==true){
    fromdt=document.getElementById('from-date').value;
    todt=document.getElementById('to-date').value;
    fetch(`/opget/?lid=${customerid}&fromdt=${fromdt}&user=${user}&area=${area}&chkarea=${'all'}&chkuser=${'all'}&comp=${company}&curarea=${curarea}`)
           .then(response => response.json())
           .then(data =>{
           alert(data.reportdata)
           document.getElementById(`debit${1}`).innerHTML=data.reportdata
            document.getElementById(`balance${1}`).innerHTML=data.reportdata
            
           } 
             
             );
  }
  else{

    if(alluser.checked==true){
      fromdt=document.getElementById('from-date').value;
    todt=document.getElementById('to-date').value;
    fetch(`/ledgerget/?lid=${customerid}&fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'all'}&comp=${company}&curarea=${curarea}`)
           .then(response => response.json())
           .then(data => displayrep(data.reportdata)
             
             );
    }
    else{
      fromdt=document.getElementById('from-date').value;
    todt=document.getElementById('to-date').value;
    fetch(`/ledgerget/?lid=${customerid}&fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'no'}&comp=${company}&curarea=${curarea}`)
           .then(response => response.json())
           .then(data => displayrep(data.reportdata)
             
             );
    }

  }
}
else{
  if(alluser.checked==true){
    fromdt=document.getElementById('from-date').value;
  todt=document.getElementById('to-date').value;
  fetch(`/ledgerget/?lid=${customerid}&fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'all'}&comp=${company}&curarea=${curarea}`)
         .then(response => response.json())
         .then(data => displayrep(data.reportdata)
           
           );
  }
  else{
    fromdt=document.getElementById('from-date').value;
  todt=document.getElementById('to-date').value;
  fetch(`/ledgerget/?lid=${customerid}&fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'no'}&comp=${company}&curarea=${curarea}`)
         .then(response => response.json())
         .then(data => displayrep(data.reportdata)
           
           );
  }
}

}
function Toledger(rown){
  let currown=parseInt(rown)-1;

  company=document.getElementById('cmp').value;
  area=document.getElementById('area').value;
  user=document.getElementById('user').value;
  let vnopre=document.getElementById(`vno${rown}`).innerHTML;
  let avtype=document.getElementById(`vtype${rown}`).innerHTML;
  
  if(avtype=='PI'){
    var windowop= window.open('/purchase/?type=report&prevno='+vnopre+'&comp='+company+'&user='+user+'&area='+area+'')

  }
  if(avtype=='SI'){
    var windowop= window.open('/sale/?type=report&prevno='+vnopre+'&comp='+company+'&user='+user+'&area='+area+'')

  }
  if(avtype=='PR'){
    var windowop= window.open('/purchasereturn/?type=report&prevno='+vnopre+'&comp='+company+'&user='+user+'&area='+area+'')

  }
  if(avtype=='SR'){
    var windowop= window.open('/salereturn/?type=report&prevno='+vnopre+'&comp='+company+'&user='+user+'&area='+area+'')

  }
  if(avtype=='P'){
    var windowop= window.open('/payment/?type=report&prevno='+vnopre+'&comp='+company+'&user='+user+'&area='+area+'')

  }
  if(avtype=='R'){
    var windowop= window.open('/receipt/?type=report&prevno='+vnopre+'&comp='+company+'&user='+user+'&area='+area+'')

  }
  if(avtype=='OB'){
    var windowop= window.open('/receipt/?type=report&prevno='+vnopre+'&comp='+company+'&user='+user+'&area='+area+'')

  }
}
function openPopup() {
  document.getElementById('overlay').style.display = 'flex';
}

function closePopup() {
  document.getElementById('overlay').style.display = 'none';
}

function selectboxclick(){
  
  
}
const resultsContainer = document.getElementById('searchResults');
    let rs='';
    let selectedResultIndex = -1;
    let customerlen=0;
    let tempname=[];
let tempid=[];
let tempmob=[];
function searchCustomer() {
      const company = document.getElementById('cmp').value;
        const query = document.getElementById('searchInput').value;
        rs=query


        id=20;
        fetch(`/search/?query=${query}&id=${id}&comp=${company}`)
            .then(response => response.json())
            .then(data => displayResults(data.customers));
    }

    function displayResults(customers) {
      openPopup()
      tempname=[];
        tempid=[];
        tempmob=[];
   



        const resultsList = document.getElementById('searchResults');
        resultsList.innerHTML = '';
        // console.log(customers.length)
        customerlen=customers.length;
        customers.forEach(customer => {
            const listItem = document.createElement('li');
            listItem.classList.add('result-item');
            listItem.textContent = customer.name;
            listItem.onclick = () => selectCustomer(customer.name,customer.id,customer.mobile);
const divide = document.createElement('hr');
listItem.style.color='black';
            resultsList.appendChild(listItem);
            resultsList.appendChild(divide);

            tempname.push(customer.name)
    tempid.push(customer.id)
    tempmob.push(customer.mobile)

       
             console.log(customer)
        });
      
    }
    const searchInput = document.getElementById('searchInput')

    searchInput.addEventListener('keydown', (event) => {
        
        if (event.key === 'ArrowDown') {
           
          event.preventDefault();
          selectedResultIndex = Math.min(selectedResultIndex + 1, customerlen );
          highlightSelectedResultcus();
        } else if (event.key === 'ArrowUp') {
          event.preventDefault();
          selectedResultIndex = Math.max(selectedResultIndex - 1, -1);
          highlightSelectedResultcus();
        } else if (event.key === 'Enter') {
          if (selectedResultIndex !== -1) {
            event.preventDefault();
            selectcusResult(selectedResultIndex);
            selectedResultIndex = -1;
          }
        }
      });
    function selectCustomer(customername,customerId,mobile) {
  
        // Implement logic to handle selected customer (e.g., make an API call, update UI)
        document.getElementById('searchInput').value =customername;
        document.getElementById('customerid').value =customerId;
       



    }
    
function selectcusResult(index) {

searchInput.value =tempname[index];
document.getElementById('customerid').value =tempid[index];


closePopup()
}

function highlightSelectedResultcus() {
// alert("high");

// const resultsList = document.getElementById('searchResults');
const resultItems = document.querySelectorAll('.result-item');

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
const isClickInsideInput = searchInput.contains(event.target);
const isClickInsideResults = resultsContainer.contains(event.target);

if (!isClickInsideInput && !isClickInsideResults) {
  closePopup();
}
});