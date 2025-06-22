

function Summary(){
  company=document.getElementById('cmp').value;
  area=document.getElementById('area').value;
  user=document.getElementById('user').value;
  curarea=document.getElementById('curarea').value;
  allarea=document.getElementById('allarea')

  alluser=document.getElementById('alluser')
if(area=='HEAD OFFICE'){
  if(allarea.checked==true){
    fromdt=document.getElementById('from-date').value;
    todt=document.getElementById('to-date').value;
    fetch(`/lossprofitget/?fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'all'}&chkuser=${'all'}&comp=${company}&curarea=${curarea}`)
           .then(response => response.json())
           .then(data => displayrep(data.reportdata)
             
             );
  }
  else{

    if(alluser.checked==true){
      fromdt=document.getElementById('from-date').value;
    todt=document.getElementById('to-date').value;
    fetch(`/lossprofitget/?fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'all'}&comp=${company}&curarea=${curarea}`)
           .then(response => response.json())
           .then(data => displayrep(data.reportdata)
             
             );
    }
    else{
      fromdt=document.getElementById('from-date').value;
    todt=document.getElementById('to-date').value;
    fetch(`/lossprofitget/?fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'no'}&comp=${company}&curarea=${curarea}`)
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
  fetch(`/lossprofitget/?fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'all'}&comp=${company}&curarea=${curarea}`)
         .then(response => response.json())
         .then(data => displayrep(data.reportdata)
           
           );
  }
  else{
    fromdt=document.getElementById('from-date').value;
  todt=document.getElementById('to-date').value;
  fetch(`/lossprofitget/?fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'no'}&comp=${company}&curarea=${curarea}`)
         .then(response => response.json())
         .then(data => displayrep(data.reportdata)
           
           );
  }
}
 
}
function displayrep(report){
  
  const totalsale=document.getElementById('totsale');
  const totalsr=document.getElementById('totsr');
const costrate=document.getElementById('costrate');
const grossprofit=document.getElementById('grossprofit');
const indirectexp=document.getElementById('indirectexp')
const indirectinc=document.getElementById('indirectinc')
const employeeexp=document.getElementById('exployeeexp');
const netprofit=document.getElementById('netprofit');


  report.forEach(reportdata => {


    let opcash= reportdata.opcash;
      let opbank= reportdata.opbank;
      
      
      let totcashpurch=parseFloat( reportdata.totcashpurchase);
      
     

      let totsale=parseFloat( reportdata.totsale);
      let totsalecard=parseFloat( reportdata.totsalecard);
      let totsalecash=parseFloat( reportdata.totsalecash);
     
      let totsr=parseFloat( reportdata.totsr);
      
      let totsrcredit=parseFloat( reportdata.totsrcredit);


    
      let totpayment=parseFloat( reportdata.payment);
      let totreceipt=parseFloat( reportdata.receipt);


    

      

      
      let prtrn=parseFloat( reportdata.totalprwithoutcr);    
  
      let crate=parseFloat( reportdata.crate);  
      let grossp=parseFloat( reportdata.grossprofit); 
      let indexp=parseFloat( reportdata.indirectexpense); 
      let indinc=parseFloat( reportdata.indirectincome); 
      let expemployee=parseFloat( reportdata.employeeexpense);
     
      if(reportdata.indirectexpense==null){
        
       indexp= 0
       indirectexp.value='0.00'
      }
      else{
        indirectexp.value=indexp.toFixed(2)
      }
      if(reportdata.indirectincome==null){
        indinc=0
        indirectinc.value='0.00'
      }
      else{
        indirectinc.value=indinc.toFixed(2) 
      }
      
      if(reportdata.employeeexpense==null){
        
        expemployee=0
        employeeexp.value='0.00'
      }
      else{
        employeeexp.value=expemployee.toFixed(2)
      }
    let saletrn=(totsalecard+totsalecash)
    let srtrn=totsr-totsrcredit
   
    let plusamnt=parseFloat( totreceipt)+parseFloat(prtrn)+parseFloat(opcash)+ parseFloat(saletrn)
    let lessamnt=totpayment+srtrn+totcashpurch
    
    
    
    

     totalsale.value=totsale.toFixed(2);
     totalsr.value=totsr.toFixed(2);
    costrate.value=crate.toFixed(2)
    grossprofit.value=grossp.toFixed(2)
    
    



  
    netprofit.value=((grossp+indinc)-(indexp+expemployee)).toFixed(2)
 
    if(netprofit.value=='NaN'){
      netprofit.value='0.00';
    }
    
  

  });
}