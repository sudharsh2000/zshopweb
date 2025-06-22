
function searchsales() {
    selectindex=11;
    
    var query='SI';
    let curarea=document.getElementById('curarea').value;
    
          fetch(`/getedit/?query=${query}&comp=${area}&area=${curarea}`)
                   .then(response => response.json())
                   .then(data => displaytransaction(data.data));
    
    
    
    
               
    
           }
           function searchsalesreturn() {
            selectindex=12;
            
            var query='SR';
            let curarea=document.getElementById('curarea').value;
            
                  fetch(`/getedit/?query=${query}&comp=${area}&area=${curarea}`)
                           .then(response => response.json())
                           .then(data => displaytransactionpurchase(data.data));
           }
           function searchpurchase() {
            selectindex=13;
            
            var query='PI';
            let curarea=document.getElementById('curarea').value;
            
                  fetch(`/getedit/?query=${query}&comp=${area}&area=${curarea}`)
                           .then(response => response.json())
                           .then(data => displaytransactionpurchase(data.data));
             }
             function searchpurchasereturn() {
                selectindex=14;
                
                var query='PR';
                let curarea=document.getElementById('curarea').value;
                
                      fetch(`/getedit/?query=${query}&comp=${area}&area=${curarea}`)
                               .then(response => response.json())
                               .then(data => displaytransaction(data.data));
                  }
           function displaytransaction(customers) {
    
    
    
             
               itemlen=customers.length;
               const resulttable = document.getElementById('tablemain');
    
               resulttable.innerHTML = '';
               var thead = document.createElement('thead');
       var headerRow = thead.insertRow();
       
       // Add header cells
     
       var headerCell = document.createElement('th');
         headerCell.textContent = 'Vno';
         headerCell.style.width='50px';
         headerRow.appendChild(headerCell);
         var headerCell = document.createElement('th');
         headerCell.textContent = 'Vdate';
         headerCell.style.width='200px';
         headerRow.appendChild(headerCell);
         var headerCell = document.createElement('th');
         headerCell.textContent = 'BillAmount';
         headerCell.style.width='200px';
         headerRow.appendChild(headerCell);
         var headerCell = document.createElement('th');
         headerCell.textContent = 'Party';
         headerCell.style.width='200px';
         headerRow.appendChild(headerCell);
         
    
    
    
    
       // Append the header to the table
       resulttable.appendChild(thead);
    
       const tbody = document.createElement('tbody');
       tbody.textContent='';
    if(customers.length==0){
    
      const mainlist = document.createElement('tr');
                   const listvno = document.createElement('td');
                   const listdate = document.createElement("td");
                   const listamount = document.createElement("td");
                   const listparty = document.createElement("td");
                   
                   listvno.textContent='None';
    
                   listdate.textContent='None'
                   listamount.textContent='None'
                   listparty.textContent='None'
                   
                   
    mainlist.appendChild(listvno);
    mainlist.appendChild(listdate);
    mainlist.appendChild(listamount);
    mainlist.appendChild(listparty);
  
    tbody.appendChild(mainlist);   
    }
    var categrownum=0;
    
               customers.forEach(customer => {
    
                
                categrownum+=1;
                 const mainlist = document.createElement('tr');
                   const listvno = document.createElement('td');
                   mainlist.classList.add('result-item2categ');
    
                   listvno.id=`vno${categrownum}`;
    
                   listvno.textContent = customer.vno;
    
                    const listdate = document.createElement("td");
                    listdate.id=`date${categrownum}`;
                    if(customer.date==''){
    
                      }
                      else{
                           listdate.textContent=customer.date;
                      }
    
    
                    const listamount = document.createElement("td");
                    listamount.id=`amount${categrownum}`;
                      if(customer.amount==''){
                        listamount.textContent='None';
                      }
                      else{
                        listamount.textContent=customer.amount;
                      }
    
                    
                      
                               const listparty = document.createElement("td");
                               listparty.id=`party${categrownum}`; 
                               
    var query=customer.party;
   
    if(query==0){
        listparty.textContent='None';
                    }
                      else{
                        fetch(`/getcustomer/?query=${query}&comp=${area}`)
             .then(response => response.json())
             .then(data =>getcus(data.customers)
             
             
             );
                    
                    function getcus(c){
    
                      c.forEach(category => {
                       
                        
                        listparty.textContent=category.name;
                      
                        
                      });
                    }
                  }
    mainlist.appendChild(listvno);
    mainlist.appendChild(listdate);
    mainlist.appendChild(listamount);
    mainlist.appendChild(listparty);
    
    
    
    
    
    
    
    
    
    tbody.appendChild(mainlist);   
    
    mainlist.addEventListener('dblclick', function () {
      
      getid(customer.vno)
      editdata();
    });       
                  // mainlist.onclick = () =>getid(customer.id,this)
                  
                    mainlist.addEventListener('click', function () {
                        // Change color when a row is clicked
                        var rows = document.querySelectorAll('#tablemain tbody tr');
                        rows.forEach(function (item) {
              item.style.backgroundColor = 'rgb(166, 225, 210)';
                
            });
                        this.style.backgroundColor = '#c6ccca';
                        getid(customer.vno)
                    });
               
    
               });
               
               resulttable.appendChild(tbody)  
              
              }
              function displaytransactionpurchase(customers) {
    
    
    
             
                itemlen=customers.length;
                const resulttable = document.getElementById('tablemain');
     
                resulttable.innerHTML = '';
                var thead = document.createElement('thead');
        var headerRow = thead.insertRow();
        
        // Add header cells
      
        var headerCell = document.createElement('th');
          headerCell.textContent = 'Vno';
          headerCell.style.width='50px';
          headerRow.appendChild(headerCell);
          var headerCell = document.createElement('th');
          headerCell.textContent = 'Vdate';
          headerCell.style.width='200px';
          headerRow.appendChild(headerCell);
          var headerCell = document.createElement('th');
          headerCell.textContent = 'BillAmount';
          headerCell.style.width='200px';
          headerRow.appendChild(headerCell);
          var headerCell = document.createElement('th');
          headerCell.textContent = 'Party';
          headerCell.style.width='200px';
          headerRow.appendChild(headerCell);
          
     
     
     
     
        // Append the header to the table
        resulttable.appendChild(thead);
     
        const tbody = document.createElement('tbody');
        tbody.textContent='';
     if(customers.length==0){
     
       const mainlist = document.createElement('tr');
                    const listvno = document.createElement('td');
                    const listdate = document.createElement("td");
                    const listamount = document.createElement("td");
                    const listparty = document.createElement("td");
                    
                    listvno.textContent='None';
     
                    listdate.textContent='None'
                    listamount.textContent='None'
                    listparty.textContent='None'
                    
                    
     mainlist.appendChild(listvno);
     mainlist.appendChild(listdate);
     mainlist.appendChild(listamount);
     mainlist.appendChild(listparty);
   
     tbody.appendChild(mainlist);   
     }
     var categrownum=0;
     
                customers.forEach(customer => {
     
                 
                 categrownum+=1;
                  const mainlist = document.createElement('tr');
                    const listvno = document.createElement('td');
                    mainlist.classList.add('result-item2categ');
     
                    listvno.id=`vno${categrownum}`;
     
                    listvno.textContent = customer.vno;
     
                     const listdate = document.createElement("td");
                     listdate.id=`date${categrownum}`;
                     if(customer.date==''){
     
                       }
                       else{
                            listdate.textContent=customer.date;
                       }
     
     
                     const listamount = document.createElement("td");
                     listamount.id=`amount${categrownum}`;
                       if(customer.amount==''){
                         listamount.textContent='None';
                       }
                       else{
                         listamount.textContent=customer.amount;
                       }
     
                     
                       
                                const listparty = document.createElement("td");
                                listparty.id=`party${categrownum}`; 
                                
     var query=customer.party;
     
     if(query==0){
         listparty.textContent='None';
                         }
                       else{
                       fetch(`/getcustomer/?query=${query}&comp=${area}`)
                     .then(response => response.json())
                     .then(data => getcateg(data.customers));
                     function getcateg(categories){
     
                       categories.forEach(category => {
                        
                         
                         listparty.textContent=category.name;
                       
                         
                       });
                     }
                   }
     mainlist.appendChild(listvno);
     mainlist.appendChild(listdate);
     mainlist.appendChild(listamount);
     mainlist.appendChild(listparty);
     
     
     
     
     
     
     
     
     
     tbody.appendChild(mainlist);   
     
     mainlist.addEventListener('dblclick', function () {
       
       getid(customer.vno)
       editdata();
     });       
                   // mainlist.onclick = () =>getid(customer.id,this)
                   
                     mainlist.addEventListener('click', function () {
                         // Change color when a row is clicked
                         var rows = document.querySelectorAll('#tablemain tbody tr');
                         rows.forEach(function (item) {
               item.style.backgroundColor = 'rgb(166, 225, 210)';
                 
             });
                         this.style.backgroundColor = '#c6ccca';
                         getid(customer.vno)
                     });
                
     
                });
                
                resulttable.appendChild(tbody)  
               
               }
               function searchpayment() {
                selectindex=15;
                
                var query='P';
                let curarea=document.getElementById('curarea').value;
                
                      fetch(`/getedit/?query=${query}&comp=${area}&area=${curarea}`)
                               .then(response => response.json())
                               .then(data => displaypayreceipt(data.data));
                  }
                  function searchreceipt() {
                    selectindex=16;
                    
                    var query='R';
                    let curarea=document.getElementById('curarea').value;
                    
                          fetch(`/getedit/?query=${query}&comp=${area}&area=${curarea}`)
                                   .then(response => response.json())
                                   .then(data => displaypayreceipt(data.data));
                      }
           function displaypayreceipt(customers) {
    
    
    
             
               itemlen=customers.length;
               const resulttable = document.getElementById('tablemain');
    
               resulttable.innerHTML = '';
               var thead = document.createElement('thead');
       var headerRow = thead.insertRow();
       
       // Add header cells
     
       var headerCell = document.createElement('th');
         headerCell.textContent = 'Vno';
         headerCell.style.width='50px';
         headerRow.appendChild(headerCell);
         var headerCell = document.createElement('th');
         headerCell.textContent = 'Vdate';
         headerCell.style.width='200px';
         headerRow.appendChild(headerCell);
         var headerCell = document.createElement('th');
         headerCell.textContent = 'Amount';
         headerCell.style.width='200px';
         headerRow.appendChild(headerCell);
         var headerCell = document.createElement('th');
         headerCell.textContent = 'Narration';
         headerCell.style.width='200px';
         headerRow.appendChild(headerCell);
         
    
    
    
    
       // Append the header to the table
       resulttable.appendChild(thead);
    
       const tbody = document.createElement('tbody');
       tbody.textContent='';
    if(customers.length==0){
    
      const mainlist = document.createElement('tr');
                   const listvno = document.createElement('td');
                   const listdate = document.createElement("td");
                   const listamount = document.createElement("td");
                   const listnarration = document.createElement("td");
                   
                   listvno.textContent='None';
    
                   listdate.textContent='None'
                   listamount.textContent='None'
                   listnarration.textContent='None'
                   
                   
    mainlist.appendChild(listvno);
    mainlist.appendChild(listdate);
    mainlist.appendChild(listamount);
    mainlist.appendChild(listnarration);
  
    tbody.appendChild(mainlist);   
    }
    var categrownum=0;
    
               customers.forEach(customer => {
    
                
                categrownum+=1;
                 const mainlist = document.createElement('tr');
                   const listvno = document.createElement('td');
                   mainlist.classList.add('result-item2categ');
    
                   listvno.id=`vno${categrownum}`;
    
                   listvno.textContent = customer.vno;
    
                    const listdate = document.createElement("td");
                    listdate.id=`date${categrownum}`;
                    if(customer.date==''){
    
                      }
                      else{
                           listdate.textContent=customer.date;
                      }
    
    
                    const listamount = document.createElement("td");
                    listamount.id=`amount${categrownum}`;
                      if(customer.amount==''){
                        listamount.textContent='None';
                      }
                      else{
                        listamount.textContent=customer.amount;
                      }
    
                    
                      
                               const listnarration = document.createElement("td");
                               listnarration.id=`narration${categrownum}`; 
                         if(customer.narration==''){
                      listnarration.textContent='None';
                                  }
                                    else{
                                      listnarration.textContent=customer.narration;
                                }
    mainlist.appendChild(listvno);
    mainlist.appendChild(listdate);
    mainlist.appendChild(listamount);
    mainlist.appendChild(listnarration);
    
    
    
    
    
    
    
    
    
    tbody.appendChild(mainlist);   
    
    mainlist.addEventListener('dblclick', function () {
      
      getid(customer.vno)
      editdata();
    });       
                  // mainlist.onclick = () =>getid(customer.id,this)
                  
                    mainlist.addEventListener('click', function () {
                        // Change color when a row is clicked
                        var rows = document.querySelectorAll('#tablemain tbody tr');
                        rows.forEach(function (item) {
              item.style.backgroundColor = 'rgb(166, 225, 210)';
                
            });
                        this.style.backgroundColor = '#c6ccca';
                        getid(customer.vno)
                    });
               
    
               });
               
               resulttable.appendChild(tbody)  
              
              }


///Service


function searchservice() {
  selectindex=17;
  
  var query='SS';
  let curarea=document.getElementById('curarea').value;
  
        fetch(`/getedit/?query=${query}&comp=${area}&area=${curarea}`)
                 .then(response => response.json())
                 .then(data => displaytransaction(data.data));
   }




function displaytransaction(customers) {
    
    
    
             
  itemlen=customers.length;
  const resulttable = document.getElementById('tablemain');

  resulttable.innerHTML = '';
  var thead = document.createElement('thead');
var headerRow = thead.insertRow();

// Add header cells

var headerCell = document.createElement('th');
headerCell.textContent = 'Vno';
headerCell.style.width='50px';
headerRow.appendChild(headerCell);
var headerCell = document.createElement('th');
headerCell.textContent = 'Vdate';
headerCell.style.width='200px';
headerRow.appendChild(headerCell);
var headerCell = document.createElement('th');
headerCell.textContent = 'BillAmount';
headerCell.style.width='200px';
headerRow.appendChild(headerCell);
var headerCell = document.createElement('th');
headerCell.textContent = 'Party';
headerCell.style.width='200px';
headerRow.appendChild(headerCell);





// Append the header to the table
resulttable.appendChild(thead);

const tbody = document.createElement('tbody');
tbody.textContent='';
if(customers.length==0){

const mainlist = document.createElement('tr');
      const listvno = document.createElement('td');
      const listdate = document.createElement("td");
      const listamount = document.createElement("td");
      const listparty = document.createElement("td");
      
      listvno.textContent='None';

      listdate.textContent='None'
      listamount.textContent='None'
      listparty.textContent='None'
      
      
mainlist.appendChild(listvno);
mainlist.appendChild(listdate);
mainlist.appendChild(listamount);
mainlist.appendChild(listparty);

tbody.appendChild(mainlist);   
}
var categrownum=0;

  customers.forEach(customer => {

   
   categrownum+=1;
    const mainlist = document.createElement('tr');
      const listvno = document.createElement('td');
      mainlist.classList.add('result-item2categ');

      listvno.id=`vno${categrownum}`;

      listvno.textContent = customer.vno;

       const listdate = document.createElement("td");
       listdate.id=`date${categrownum}`;
       if(customer.date==''){

         }
         else{
              listdate.textContent=customer.date;
         }


       const listamount = document.createElement("td");
       listamount.id=`amount${categrownum}`;
         if(customer.amount==''){
           listamount.textContent='None';
         }
         else{
           listamount.textContent=customer.amount;
         }

       
         
                  const listparty = document.createElement("td");
                  listparty.id=`party${categrownum}`; 
                  
var query=customer.party;

if(query==0){
listparty.textContent='None';
       }
         else{
           fetch(`/getcustomer/?query=${query}&comp=${area}`)
.then(response => response.json())
.then(data =>getcus(data.customers)


);
       
       function getcus(c){

         c.forEach(category => {
          
           
           listparty.textContent=category.name;
         
           
         });
       }
     }
mainlist.appendChild(listvno);
mainlist.appendChild(listdate);
mainlist.appendChild(listamount);
mainlist.appendChild(listparty);









tbody.appendChild(mainlist);   

mainlist.addEventListener('dblclick', function () {

getid(customer.vno)
editdata();
});       
     // mainlist.onclick = () =>getid(customer.id,this)
     
       mainlist.addEventListener('click', function () {
           // Change color when a row is clicked
           var rows = document.querySelectorAll('#tablemain tbody tr');
           rows.forEach(function (item) {
 item.style.backgroundColor = 'rgb(166, 225, 210)';
   
});
           this.style.backgroundColor = '#c6ccca';
           getid(customer.vno)
       });
  

  });
  
  resulttable.appendChild(tbody)  
 
 }
 