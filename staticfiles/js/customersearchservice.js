 function openPopup() {
      document.getElementById('overlay').style.display = 'flex';
    }

    function closePopup() {
      document.getElementById('overlay').style.display = 'none';
    }

    function selectboxclick(){
      
     
        document.getElementById('searchInput').value='';
        
        
        document.getElementById('searchInput').focus();
      
    
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


            id=18;
            fetch(`/search/?query=${query}&id=${id}&comp=${company}`)
                .then(response => response.json())
                .then(data => displayResults(data.customers));
        }

        function displayResults(customers) {
          tempname=[];
            tempid=[];
            tempmob=[];
      

       
        openPopup();
        
     



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
            document.getElementById('mobile').value =mobile;



        }
        
  function selectcusResult(index) {
    
console.log(tempmob)
    searchInput.value =tempname[index];
    document.getElementById('customerid').value =tempid[index];
    document.getElementById('mobile').value =tempmob[index];
    
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