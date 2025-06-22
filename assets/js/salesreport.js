

function Summary(){
  const tableBody = document.getElementById('invoice-form-items-table-body');
  tableBody.innerHTML='';
  
  company=document.getElementById('cmp').value;
  area=document.getElementById('area').value;
  user=document.getElementById('user').value;
  curarea=document.getElementById('curarea').value;
  allarea=document.getElementById('allarea')

  alluser=document.getElementById('alluser')
  vtype=document.getElementById('curvtype').value;
 


if(area=='HEAD OFFICE'){
  if(allarea.checked==true){
    fromdt=document.getElementById('from-date').value;
    todt=document.getElementById('to-date').value;
    fetch(`/salesget/?fromdt=${fromdt}&vtype=${vtype}&todt=${todt}&user=${user}&area=${area}&chkarea=${'all'}&chkuser=${'all'}&comp=${company}&curarea=${curarea}`)
           .then(response => response.json())
           .then(data => displayrep(data.reportdata)
             
             );
  }
  else{

    if(alluser.checked==true){
      fromdt=document.getElementById('from-date').value;
    todt=document.getElementById('to-date').value;
    fetch(`/salesget/?fromdt=${fromdt}&todt=${todt}&vtype=${vtype}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'all'}&comp=${company}&curarea=${curarea}`)
           .then(response => response.json())
           .then(data => displayrep(data.reportdata)
             
             );
    }
    else{
      fromdt=document.getElementById('from-date').value;
    todt=document.getElementById('to-date').value;
    fetch(`/salesget/?fromdt=${fromdt}&todt=${todt}&vtype=${vtype}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'no'}&comp=${company}&curarea=${curarea}`)
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
  fetch(`/salesget/?fromdt=${fromdt}&todt=${todt}&vtype=${vtype}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'all'}&comp=${company}&curarea=${curarea}`)
         .then(response => response.json())
         .then(data => displayrep(data.reportdata)
           
           );
  }
  else{
    fromdt=document.getElementById('from-date').value;
  todt=document.getElementById('to-date').value;
  fetch(`/salesget/?fromdt=${fromdt}&todt=${todt}&vtype=${vtype}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'no'}&comp=${company}&curarea=${curarea}`)
         .then(response => response.json())
         .then(data => displayrep(data.reportdata)
           
           );
  }
}


}
function displayrep(report){
  let rowNumber=1;
  let finaltaxamt=0;
  let finalamt=0;
  let finalnetamt=0;
  let finalqty=0;
  if(report==""){
    alert("No Sales data found")
  }
  report.forEach(element => {
    finaltaxamt=finaltaxamt+ parseFloat(element.taxamt);
    finalamt=finalamt+ parseFloat(element.amount);
    finalqty=finalqty+ parseFloat(element.qty);
   
  const tableBody = document.getElementById('invoice-form-items-table-body');
  
  rowNumber=rowNumber+1;




    const newRow = document.createElement('tr');
    newRow.innerHTML = `
    <td id="vno${rowNumber}" ondblclick="Tosale(${element.vno})">${element.vno}</td>
    <td id="user${rowNumber}" ondblclick="Tosale(${element.vno})"></td>
    <td id="date${rowNumber}" ondblclick="Tosale(${element.vno})"></td>
    <td id="party${rowNumber}" ondblclick="Tosale(${element.vno})"></td>
    <td id="qty${rowNumber}" ondblclick="Tosale(${element.vno})"></td>
    <td id="taxamt${rowNumber}" ondblclick="Tosale(${element.vno})"></td>
    <td id="amount${rowNumber}" ondblclick="Tosale(${element.vno})"></td>
    <td id="netamount${rowNumber}" ondblclick="Tosale(${element.vno})"></td>
   
   `;
   tableBody.appendChild(newRow);



   var dtdate=new Date(element.dat)

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
    let usertxt=document.getElementById(`user${rowNumber}`)
    let datetxt=document.getElementById(`date${rowNumber}`)
    let partytxt=document.getElementById(`party${rowNumber}`)
    let qtytxt=document.getElementById(`qty${rowNumber}`)
    let taxamttxt=document.getElementById(`taxamt${rowNumber}`)
    let amounttxt=document.getElementById(`amount${rowNumber}`)

    let netamttxt=document.getElementById(`netamount${rowNumber}`)
    usertxt.innerHTML=element.user;
    datetxt.innerHTML=formattedDate;
    taxamttxt.innerHTML=parseFloat(element.taxamt);
    qtytxt.innerHTML=element.qty;
    amounttxt.innerHTML=parseFloat(element.amount);
    netamttxt.innerHTML=(parseFloat(element.taxamt)+parseFloat(element.amount)).toFixed(2)
    
    fetch(`/getcustomer/?query=${element.lid}&comp=${company}`)
    .then(response => response.json())
    .then(data =>data.customers.forEach((cus,index) => {
      
      partytxt.innerHTML=cus.name;
      
     



    })
    
    
    );

  });
  
  const tableBody = document.getElementById('invoice-form-items-table-body');
  
  rowNumber=rowNumber+1;
  finalnetamt=finalamt+finaltaxamt;




    const finalrw = document.createElement('tr');
    finalrw.innerHTML = `
    <td ></td>
    <td ></td>
    <td ></td>
    <td  style="color:#504646;">Final:</td>
    <td id="finalqty" style="color:#504646;">${finalqty.toFixed(2)}</td>
    <td id="finaltx" style="color:#504646;">${finaltaxamt.toFixed(2)}</td>
    <td id="finalamt" style="color:#504646;">${finalamt.toFixed(2)}</td>
    <td id="finalnet" style="color:#504646;">${finalnetamt.toFixed(2)}</td>
   
   `;
   tableBody.appendChild(finalrw);

}
function Tosale(vnopre){
  company=document.getElementById('cmp').value;
  area=document.getElementById('area').value;
  user=document.getElementById('user').value;
  vtype=document.getElementById('curvtype').value;
  if(vtype=='SI'){

  
  var windowop= window.open('/sale/?type=report&prevno='+vnopre+'&comp='+company+'&user='+user+'&area='+area+'')
  }
  else if(vtype=='SR'){
    var windowop= window.open('/salereturn/?type=report&prevno='+vnopre+'&comp='+company+'&user='+user+'&area='+area+'')
  }
  else if(vtype=='SS'){
    var windowop= window.open('/service/?type=report&prevno='+vnopre+'&comp='+company+'&user='+user+'&area='+area+'')
  }
else{
  var windowop= window.open('/saleorder/?type=report&prevno='+vnopre+'&comp='+company+'&user='+user+'&area='+area+'')
}
}