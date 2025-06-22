 function openPopup() {
      document.getElementById('overlay').style.display = 'flex';
    }

    function closePopup() {
      document.getElementById('overlay').style.display = 'none';
    }

    function selectboxclick(){
      
      let paymnt = document.getElementById('payment').value;
      
      if(paymnt==28){
        document.getElementById('searchInput').value='Bank';
        document.getElementById('mobile').value='';

      }
      else if(paymnt==0){
        document.getElementById('searchInput').value='';
        
        
        document.getElementById('searchInput').focus();
      
      }
      else{
        document.getElementById('searchInput').value='';
        document.getElementById('mobile').value='';
      }
    }
    const resultsContainer = document.getElementById('searchResults');
        let rs='';
        let selectedResultIndex = -1;
        let customerlen=0;
        let tempname=[];
let tempid=[];
let tempmob=[];
        function searchCustomer() {
          openPopup();
          
            const query = document.getElementById('searchInput').value;
            
            fetch(`/searchproductset/?query=${query}`)
                .then(response => response.json())
                .then(data => displayResults(data.data));
        }

        function displayResults(customers) {
          tempname=[];
            tempid=[];
            tempvno=[];
           
   



            const resultsList = document.getElementById('searchResults');
            resultsList.innerHTML = '';
            // console.log(customers.length)
            customerlen=customers.length;
            customers.forEach(customer => {
                const listItem = document.createElement('li');
               
                listItem.classList.add('result-item');
                listItem.textContent = customer.name;
                listItem.onclick = () => selectCustomer(customer.name,customer.pid,customer.vno);
 const divide = document.createElement('hr');
                resultsList.appendChild(listItem);
              

                tempname.push(customer.name)
        tempid.push(customer.pid)
        tempvno.push(customer.vno)
      

           
                 console.log(tempid)
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
        function selectCustomer(customername,customerId,vno) {
      
            // Implement logic to handle selected customer (e.g., make an API call, update UI)
            document.getElementById('searchInput').value =customername;
            document.getElementById('productid').value =customerId;
            document.getElementById('voucherid').value =vno;
            

        }
        
  function selectcusResult(index) {
    

    searchInput.value =tempname[index];
    document.getElementById('productid').value =tempid[index];
    document.getElementById('voucherid').value =tempvno[index];
    
    closePopup()
   

 

  }

  function highlightSelectedResultcus() {
    // alert("high");
    
    // const resultsList = document.getElementById('searchResults');
    const resultItems = document.querySelectorAll('.result-item');
    
    resultItems.forEach((item, index) => {
        
      if (index === selectedResultIndex) {
       
        item.style.backgroundColor = '#cac2c2';
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