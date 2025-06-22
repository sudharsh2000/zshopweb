

function Summary(){
  

  const tableBody = document.getElementById('invoice-form-items-table-body');
  tableBody.innerHTML='';
  
  company=document.getElementById('cmp').value;
  area=document.getElementById('area').value;
  user=document.getElementById('user').value;
  curarea=document.getElementById('curarea').value;
  allarea=document.getElementById('allarea');
  let agrouplist=[];
  fromdt=document.getElementById('from-date').value;
  todt=document.getElementById('to-date').value;

  alluser=document.getElementById('alluser')
if(area=='HEAD OFFICE'){
      if(allarea.checked==true){
            if(document.getElementById('allledchk').checked==true){
              let ttype='all';
              fetch(`/ledgergrpget/?type=${ttype}&fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'all'}&chkuser=${'all'}&comp=${company}&curarea=${curarea}`)
              .then(response => response.json())
              .then(data => displayrep(data.reportdata)
                
                );
            }
            else{
              let ttype=''
              if(document.getElementById('cuschk').checked==true){
                let ttype='cus';
                agrouplist.push('18')
              }
              if(document.getElementById('supchk').checked==true){
                let ttype='sup';
                agrouplist.push('19')
              }
              if(document.getElementById('empchk').checked==true){
                let ttype='cus';
                agrouplist.push('22')
              }
            
            
                fetch(`/ledgergrpget/?type=${ttype}&agrp=${agrouplist}&fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'all'}&chkuser=${'all'}&comp=${company}&curarea=${curarea}`)
                .then(response => response.json())
                .then(data => displayrep(data.reportdata)
                  
                  );
            
            }
      
      }
  else{
        if(alluser.checked==true){

         


        if(allarea.checked==true){
          alert('primary5')
          fromdt=document.getElementById('from-date').value;
          todt=document.getElementById('to-date').value;
          if(document.getElementById('allledchk').checked==true){
            let ttype='all';
            fetch(`/ledgergrpget/?type=${ttype}&fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'all'}&comp=${company}&curarea=${curarea}`)
            .then(response => response.json())
            .then(data => displayrep(data.reportdata)
              
              );
          }
          else{
            let ttype=''
            if(document.getElementById('cuschk').checked==true){
              let ttype='cus';
              agrouplist.push('18')
            }
            if(document.getElementById('supchk').checked==true){
              let ttype='sup';
              agrouplist.push('19')
            }
            if(document.getElementById('empchk').checked==true){
              let ttype='cus';
              agrouplist.push('22')
            }
          
          
              fetch(`/ledgergrpget/?type=${ttype}&agrp=${agrouplist}&fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'all'}&comp=${company}&curarea=${curarea}`)
              .then(response => response.json())
              .then(data => displayrep(data.reportdata)
                
                );
          
          }
      
        }
      
        else{

        if(document.getElementById('allledchk').checked==true){
          let ttype='all';
          fetch(`/ledgergrpget/?type=${ttype}&fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'no'}&comp=${company}&curarea=${curarea}`)
          .then(response => response.json())
          .then(data => displayrep(data.reportdata)
            
            );
        }
        else{
          let ttype=''
          if(document.getElementById('cuschk').checked==true){
            let ttype='cus';
            agrouplist.push('18')
          }
          if(document.getElementById('supchk').checked==true){
            let ttype='sup';
            agrouplist.push('19')
          }
          if(document.getElementById('empchk').checked==true){
            let ttype='cus';
            agrouplist.push('22')
          }
        
        
            fetch(`/ledgergrpget/?type=${ttype}&agrp=${agrouplist}&fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'no'}&comp=${company}&curarea=${curarea}`)
            .then(response => response.json())
            .then(data => displayrep(data.reportdata)
              
              );
        
        }

        
      }
        }

      }  
    }
else{
  if(alluser.checked==true){



  if(document.getElementById('allledchk').checked==true){
    let ttype='all';
    fetch(`/ledgergrpget/?type=${ttype}&fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'all'}&comp=${company}&curarea=${curarea}`)
    .then(response => response.json())
    .then(data => displayrep(data.reportdata)
      
      );
  }
  else{
    let ttype=''
    if(document.getElementById('cuschk').checked==true){
      let ttype='cus';
      agrouplist.push('18')
    }
    if(document.getElementById('supchk').checked==true){
      let ttype='sup';
      agrouplist.push('19')
    }
    if(document.getElementById('empchk').checked==true){
      let ttype='cus';
      agrouplist.push('22')
    }
   
   
      fetch(`/ledgergrpget/?type=${ttype}&agrp=${agrouplist}&fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'all'}&comp=${company}&curarea=${curarea}`)
      .then(response => response.json())
      .then(data => displayrep(data.reportdata)
        
        );
  
  }


  }
  else{
 

  
  if(document.getElementById('allledchk').checked==true){
    let ttype='all';
    fetch(`/ledgergrpget/?type=${ttype}&fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'no'}&comp=${company}&curarea=${curarea}`)
    .then(response => response.json())
    .then(data => displayrep(data.reportdata)
      
      );
  }
  else{
    let ttype=''
    if(document.getElementById('cuschk').checked==true){
      let ttype='cus';
      agrouplist.push('18')
    }
    if(document.getElementById('supchk').checked==true){
      let ttype='sup';
      agrouplist.push('19')
    }
    if(document.getElementById('empchk').checked==true){
      let ttype='cus';
      agrouplist.push('22')
    }
   
   
      fetch(`/ledgergrpget/?type=${ttype}&agrp=${agrouplist}&fromdt=${fromdt}&todt=${todt}&user=${user}&area=${area}&chkarea=${'no'}&chkuser=${'no'}&comp=${company}&curarea=${curarea}`)
      .then(response => response.json())
      .then(data => displayrep(data.reportdata)
        
        );
  
  }


  }
}
}


function displayrep(report){
  let rowNumber=1;
  let slno=0;
  let finaltaxamt=0;
  let finalamt=0;
  let finalnetamt=0;
  let finalbalance=0;
  if(report==""){
    alert("No  data found")
  }

  

  report.forEach(element => {
    
    const tb = document.getElementById('reportwindow');
    
   

    tb.style.visibility='visible'
    
   

   

  //   finaltaxamt=finaltaxamt+ parseFloat(element.taxamt);
  //   finalamt=finalamt+ parseFloat(element.amount);
  //   finalqty=finalqty+ parseFloat(element.qty);
   const tableBody = document.getElementById('invoice-form-items-table-body');
  
  rowNumber=rowNumber+1;
slno=slno+1;



    const newRow = document.createElement('tr');
    newRow.innerHTML = `
    <td id="slno${rowNumber}" ondblclick="Toledger(${rowNumber})"></td>
    <td id="party${rowNumber}" ondblclick="Toledger(${rowNumber})"></td>
   
    <td id="debit${rowNumber}" ondblclick="Toledger(${rowNumber})"></td>

    <td id="credit${rowNumber}" ondblclick="Toledger(${rowNumber})"></td>
    <td id="total${rowNumber}" ondblclick="Toledger(${rowNumber})"></td>


   `;
   tableBody.appendChild(newRow);



   
    let vnotxt=document.getElementById(`slno${rowNumber}`)
    let partyxt=document.getElementById(`party${rowNumber}`)
  
    let debittxt=document.getElementById(`debit${rowNumber}`)
    let credittxt=document.getElementById(`credit${rowNumber}`)

    let balancetxt=document.getElementById(`total${rowNumber}`)
    
   
    
   
    vnotxt.innerHTML=slno;
    
    debittxt.innerHTML=parseFloat(element.dbamt).toFixed(2);
    credittxt.innerHTML=parseFloat(element.cramt).toFixed(2);
    balancetxt.innerHTML=(parseFloat(element.dbamt)-parseFloat(element.cramt)).toFixed(2)
    finalamt=parseFloat( balancetxt.innerHTML)
     finalbalance=parseFloat(finalamt+finalbalance).toFixed(2);
     

    fetch(`/getcustomer/?query=${element.ledcode}&comp=${company}`)
    .then(response => response.json())
    .then(data =>data.customers.forEach((cus,index) => {

      
      
      if(element.vno==''|| element.vno==null){
        partyxt.innerHTML=cus.name;
      }
    
    
    })
    );

  });
  const tableBody = document.getElementById('invoice-form-items-table-body');
  
  
  

  rowNumber=rowNumber+1;


    const finalrw = document.createElement('tr');
    finalrw.innerHTML = `
    
    <td ></td>
   
    <td  style="color:#504646;"></td>
    <td id="finaldebit" style="color:#504646;"></td>
\
    <td id="finalamt" style="color:#504646;">Balance</td>
    <td id="finalnetbal" style="color:#504646;">${finalbalance}</td>
   
   `;
   tableBody.appendChild(finalrw);
  
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






    




// Handle keyboard events


// Hide results when clicking outside the input and results container
