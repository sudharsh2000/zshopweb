

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
    fetch(`/summaryget/?fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'all'}&chkuser=${'all'}&comp=${company}&curarea=${curarea}`)
           .then(response => response.json())
           .then(data => displayrep(data.reportdata)
             
             );
  }
  else{

    if(alluser.checked==true){
      fromdt=document.getElementById('from-date').value;
    todt=document.getElementById('to-date').value;
    fetch(`/summaryget/?fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'all'}&comp=${company}&curarea=${curarea}`)
           .then(response => response.json())
           .then(data => displayrep(data.reportdata)
             
             );
    }
    else{
      fromdt=document.getElementById('from-date').value;
    todt=document.getElementById('to-date').value;
    fetch(`/summaryget/?fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'no'}&comp=${company}&curarea=${curarea}`)
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
  fetch(`/summaryget/?fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'all'}&comp=${company}&curarea=${curarea}`)
         .then(response => response.json())
         .then(data => displayrep(data.reportdata)
           
           );
  }
  else{
    fromdt=document.getElementById('from-date').value;
  todt=document.getElementById('to-date').value;
  fetch(`/summaryget/?fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'no'}&comp=${company}&curarea=${curarea}`)
         .then(response => response.json())
         .then(data => displayrep(data.reportdata)
           
           );
  }
}
 
}
function displayrep(report){
  
  const oc=document.getElementById('oc');
  const ob=document.getElementById('ob');
const totalpurchase=document.getElementById('totalpurchase');
const totalcashpurchase=document.getElementById('cashpurchase');
const totalcreditpurchase=document.getElementById('creditpurchase')
const totalpr=document.getElementById('purchasereturn')
const totalsale=document.getElementById('totalsale');
const totalcardamtsale=document.getElementById('totalcardamtbysale');
const totalcashamtsale=document.getElementById('totalcashamtbysale')
const totalcard=document.getElementById('totalcard')
const totalcashsale=document.getElementById('totalcashsale');
const salescredit=document.getElementById('salescredit');
const totalsr=document.getElementById('salesreturn')
const totalsrcash=document.getElementById('salesreturncash')
const totalsrcredit=document.getElementById('salesreturncredit')

const paytx=document.getElementById('Paymenttx');
const saletx=document.getElementById('saletx');
const srtx=document.getElementById('srtx')
const purchasetx=document.getElementById('purchasetx')
const prtx=document.getElementById('prtx');
const sptax=document.getElementById('s-ptax');
const salegross=document.getElementById('salegross')
const purchasegross=document.getElementById('purchasegross')
const totalgross=document.getElementById('totalgross')

const payment=document.getElementById('payment')
const receipt=document.getElementById('receipt')


const totalbank=document.getElementById('totalbank')

const totalcash=document.getElementById('totalcash')
const trnbalance=document.getElementById('trnbalance')

const cashbank=document.getElementById('cashbank')

const cusrem=document.getElementById('c-remain')

const suprem=document.getElementById('s-remain')

  report.forEach(reportdata => {


    let opcash= reportdata.opcash;
      let opbank= reportdata.opbank;
      
      let totpurchase= parseFloat( reportdata.totpurchase);
      let totcashpurch=parseFloat( reportdata.totcashpurchase);
      let totcreditpurch=parseFloat( reportdata.totcreditpurchase);
      let totpr=parseFloat( reportdata.totpr);

      let totsale=parseFloat( reportdata.totsale);
      let totsalecard=parseFloat( reportdata.totsalecard);
      let totsalecash=parseFloat( reportdata.totsalecash);
      let totsalecredit=parseFloat( reportdata.totsalecredit);
      let totsr=parseFloat( reportdata.totsr);
      let totsrcash=parseFloat( reportdata.totsrcash);
      let totsrcredit=parseFloat( reportdata.totsrcredit);


      let paymenttax=parseFloat( reportdata.paymenttax);
      let saletax=parseFloat( reportdata.saletax);
      let srtax=parseFloat( reportdata.srtax);
      let purchasetax=parseFloat( reportdata.purchasetax);

      let prtax=parseFloat( reportdata.prtax);
      let totpayment=parseFloat( reportdata.payment);
      let totreceipt=parseFloat( reportdata.receipt);


      let tottbank=parseFloat( reportdata.totbank);
      let totcash=parseFloat( reportdata.totcash);

      

      let cusremain=parseFloat( reportdata.cusremain);
      let supremain=parseFloat( reportdata.supremain);
      let prtrn=parseFloat( reportdata.totalprwithoutcr);    
  
oc.value=opcash;
ob.value=opbank;
      totalpurchase.value=totpurchase.toFixed(2);
      totalcashpurchase.value=totcashpurch.toFixed(2);
      totalcreditpurchase.value=totcreditpurch.toFixed(2);
      totalpr.value=totpr.toFixed(2);
      totalsale.value=totsale.toFixed(2);
      totalcardamtsale.value=totsalecard.toFixed(2);
      totalcashamtsale.value=totsalecash.toFixed(2);
      totalcard.value=totsalecard.toFixed(2)
      totalcashsale.value=totsalecash.toFixed(2)
      salescredit.value=totsalecredit.toFixed(2)
      totalsr.value=totsr.toFixed(2)
      totalsrcash.value=totsrcash.toFixed(2)
      totalsrcredit.value=totsrcredit.toFixed(2)

      paytx.value=paymenttax.toFixed(2)

      saletx.value=saletax.toFixed(2)
      srtx.value=srtax.toFixed(2)
      purchasetx.value=purchasetax.toFixed(2)
      prtx.value=prtax.toFixed(2)
      sptax.value=(saletax-purchasetax).toFixed(2)
      salegross.value=(totsale-saletax).toFixed(2)
      purchasegross.value=(totpurchase-purchasetax).toFixed(2)
      totalgross.value=((purchasegross.value) - (salegross.value)).toFixed(2)
    
      payment.value=totpayment.toFixed(2)
      receipt.value=totreceipt.toFixed(2)

      totalbank.value=tottbank.toFixed(2)
      totalcash.value=totcash.toFixed(2)
    let saletrn=(totsalecard+totsalecash)
    let srtrn=totsr-totsrcredit
   
    let plusamnt=parseFloat( totreceipt)+parseFloat(prtrn)+parseFloat(opcash)+ parseFloat(saletrn)
    let lessamnt=totpayment+srtrn+totcashpurch
    
    
    const trnamnt=plusamnt-lessamnt

      trnbalance.value=trnamnt.toFixed(2)
      cashbank.value=(tottbank+totcash).toFixed(2)
      cusrem.value=cusremain.toFixed(2)
      suprem.value=supremain.toFixed(2)


    

    


  });
}