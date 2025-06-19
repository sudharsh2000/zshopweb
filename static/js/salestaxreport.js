

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
    fetch(`/salestaxreportget/?fromdt=${fromdt}&vtype=${vtype}&todt=${todt}&user=${user}&area=${area}&chkarea=${'all'}&chkuser=${'all'}&comp=${company}&curarea=${curarea}`)
           .then(response => response.json())
           .then(data => displayrep(data.reportdata)
             
             );
  }
  else{

    if(alluser.checked==true){
      fromdt=document.getElementById('from-date').value;
    todt=document.getElementById('to-date').value;
    fetch(`/salestaxreportget/?fromdt=${fromdt}&todt=${todt}&vtype=${vtype}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'all'}&comp=${company}&curarea=${curarea}`)
           .then(response => response.json())
           .then(data => displayrep(data.reportdata)
             
             );
    }
    else{
      fromdt=document.getElementById('from-date').value;
    todt=document.getElementById('to-date').value;
    fetch(`/salestaxreportget/?fromdt=${fromdt}&todt=${todt}&vtype=${vtype}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'no'}&comp=${company}&curarea=${curarea}`)
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
  fetch(`/salestaxreportget/?fromdt=${fromdt}&todt=${todt}&vtype=${vtype}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'all'}&comp=${company}&curarea=${curarea}`)
         .then(response => response.json())
         .then(data => displayrep(data.reportdata)
           
           );
  }
  else{
    fromdt=document.getElementById('from-date').value;
  todt=document.getElementById('to-date').value;
  fetch(`/salestaxreportget/?fromdt=${fromdt}&todt=${todt}&vtype=${vtype}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'no'}&comp=${company}&curarea=${curarea}`)
         .then(response => response.json())
         .then(data => displayrep(data.reportdata)
           
           );
  }
}


}
function displayrep(report){
  let rowNumber=1;
  let final1perctex=0;
  let final15perctax=0;
  let final20perctax=0;

  let finaltottaxamt=0;
  let final0taxable=0;
  let final1taxable=0;
  let final15taxable=0;
  let final20taxable=0;
  let finalgrossamt=0;
  let finalnetamt=0;
  
  if(report==""){
    alert("No Sales data found")
  }
  report.forEach(element => {
     final1perctex=final1perctex+ parseFloat(element.onetx);
     final15perctax=final15perctax+ parseFloat(element.fifteentx);
     final20perctax=final20perctax+ parseFloat(element.twentytx);
     finaltottaxamt=finaltottaxamt+parseFloat(element.tottax);
     final0taxable=final0taxable+ 0;
     if(element.onetx==0)
    {
      final1taxable=final1taxable
    } 
    else
    {
      final1taxable=final1taxable+ parseFloat(element.netamt-element.onetx);
    }
    if(element.fifteentx==0)
      {
        final15taxable=final15taxable
      } 
    else{
        final15taxable=final15taxable+ parseFloat(element.netamt-element.fifteentx);

      }
      if(element.twentytx==0)
        {
          final20taxable=final20taxable
        }
      else{
        final20taxable=final20taxable+ parseFloat(element.netamt-element.twentytx);

      } 
     finalgrossamt=finalgrossamt+parseFloat(element.grossamt);
     finalnetamt=finalnetamt+parseFloat(element.netamt);
    // finalamt=finalamt+ parseFloat(element.amount);
    // finalqty=finalqty+ parseFloat(element.qty);
   
  const tableBody = document.getElementById('invoice-form-items-table-body');
  
  rowNumber=rowNumber+1;




    const newRow = document.createElement('tr');
    newRow.innerHTML = `
     <td id="vdate${rowNumber}" ondblclick="Tosale(${element.clnvno})"></td>
    <td id="vno${rowNumber}" ondblclick="Tosale(${element.clnvno})">${element.clnvno}</td>
   
   
    <td id="party${rowNumber}" ondblclick="Tosale(${element.clnvno})"></td>
     <td id="address${rowNumber}" ondblclick="Tosale(${element.clnvno})"></td>

    <td id="1%tax${rowNumber}" ondblclick="Tosale(${element.clnvno})"></td>
    <td id="15%tax${rowNumber}" ondblclick="Tosale(${element.clnvno})"></td>
    <td id="20%tax${rowNumber}" ondblclick="Tosale(${element.clnvno})"></td>
    <td id="totaltax${rowNumber}" ondblclick="Tosale(${element.clnvno})"></td>
    <td id="0%taxable${rowNumber}" ondblclick="Tosale(${element.clnvno})"></td>
    <td id="1%taxable${rowNumber}" ondblclick="Tosale(${element.clnvno})"></td>
    <td id="15%taxable${rowNumber}" ondblclick="Tosale(${element.clnvno})"></td>
    <td id="20%taxable${rowNumber}" ondblclick="Tosale(${element.clnvno})"></td>
    <td id="totalgross${rowNumber}" ondblclick="Tosale(${element.clnvno})"></td>
    <td id="amount${rowNumber}" ondblclick="Tosale(${element.clnvno})"></td>
   
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
let vdatetxt=document.getElementById(`vdate${rowNumber}`)
    let vnotxt=document.getElementById(`vno${rowNumber}`)
    
    
    let partytxt=document.getElementById(`party${rowNumber}`)
    let addresstxt=document.getElementById(`address${rowNumber}`)
   
    let oneperctxt=document.getElementById(`1%tax${rowNumber}`)

    let fifteenperctxt=document.getElementById(`15%tax${rowNumber}`)
    let twentyperctxt=document.getElementById(`20%tax${rowNumber}`)

    let totaltxt=document.getElementById(`totaltax${rowNumber}`)
    let zerotaxabletxt=document.getElementById(`0%taxable${rowNumber}`)
    let onetaxabletxt=document.getElementById(`1%taxable${rowNumber}`)
    let fifteentaxabletxt=document.getElementById(`15%taxable${rowNumber}`)
    let twentytaxabletxt=document.getElementById(`20%taxable${rowNumber}`)
    let totalgrosstaxabletxt=document.getElementById(`totalgross${rowNumber}`)
    let amounttaxabletxt=document.getElementById(`amount${rowNumber}`)



    vdatetxt.innerHTML=element.clndate;
    vnotxt.innerHTML=element.clnvno;
    partytxt.innerHTML=element.party;
    
    oneperctxt.innerHTML=element.onetx.toFixed(2);
    fifteenperctxt.innerHTML=element.fifteentx.toFixed(2);
    twentyperctxt.innerHTML=element.twentytx.toFixed(2);
    totaltxt.innerHTML=element.tottax;
    zerotaxabletxt.innerHTML='0.00';
    if(element.onetx==0){
      onetaxabletxt.innerHTML='0.00'
    }
    else{

    
    onetaxabletxt.innerHTML=parseFloat(element.netamt-element.onetx).toFixed(2);
    }
    if(element.fifteentx==0){
      fifteentaxabletxt.innerHTML='0.00'
    }
    else{
      fifteentaxabletxt.innerHTML=parseFloat(element.netamt-element.fifteentx).toFixed(2);

    }
    if(element.twentytx==0){
      twentytaxabletxt.innerHTML='0.00'

    }
    else{
    twentytaxabletxt.innerHTML=parseFloat(element.netamt-element.twentytx).toFixed(2);
    }
    totalgrosstaxabletxt.innerHTML=element.grossamt.toFixed(2);
    amounttaxabletxt.innerHTML=element.netamt;
 
    fetch(`/getcustomer/?query=${element.clnparty}&comp=${company}`)
    .then(response => response.json())
    .then(data =>data.customers.forEach((cus,index) => {
      
      partytxt.innerHTML=cus.name;

      if(cus.address==''){
        addresstxt.innerHTML='None';

      }
      else{
        addresstxt.innerHTML=cus.address;

      }
      



    })
    
    
    );

  });
  
  const tableBody = document.getElementById('invoice-form-items-table-body');
  
  rowNumber=rowNumber+1;
  




    const finalrw = document.createElement('tr');
    finalrw.innerHTML = `
    <td ></td>
    <td ></td>
    <td ></td>
    <td  style="color:#690000;"></td>
    <td id="final1perc" style="color:#690000;">${final1perctex.toFixed(2)}</td>
    <td id="final15perc" style="color:#690000;">${final15perctax.toFixed(2)}</td>
    <td id="final20perc" style="color:#690000;">${final20perctax.toFixed(2)}</td>
    <td id="finaltottax" style="color:#690000;">${finaltottaxamt.toFixed(2)}</td>
    <td id="final0taxable" style="color:#690000;">${final0taxable.toFixed(2)}</td>
    <td id="final1taxable" style="color:#690000;">${final1taxable.toFixed(2)}</td>
    <td id="final15taxable" style="color:#690000;">${final15taxable.toFixed(2)}</td>
    <td id="final20taxable" style="color:#690000;">${final20taxable.toFixed(2)}</td>
    <td id="finalgrossamt" style="color:#690000;">${finalgrossamt.toFixed(2)}</td>
    <td id="finalnet" style="color:#690000;">${finalnetamt.toFixed(2)}</td>
   
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