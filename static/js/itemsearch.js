
        function openPopupitem() {
      document.getElementById('overlay').style.display = 'flex';
    }

    function closePopupitem() {
      document.getElementById('overlay2').style.display = 'none';
    }
        let rs='';
        function searchitem() {
            const query = document.getElementById('itemname').value;

            rs=query
            fetch(`/searchitem/?query=${query}`)
                .then(response => response.json())
                .then(data => displayResults(data.customers));
        }

        function displayResults(customers) {
        openPopupitem();

            const resultsList = document.getElementById('itemresults');

            resultsList.innerHTML = '';

            customers.forEach(customer => {
                const listItem = document.createElement('li');

                listItem.textContent = customer.name;

                 const listbcode = document.createElement("label");
                   listbcode.textContent=customer.bcode;
                    listbcode.style.marginLeft = '100px';

                 const listitemcode = document.createElement("label");
                   listitemcode.textContent=customer.itemcode;
                 listitemcode.style.marginLeft = '100px';

                 const listsrate = document.createElement("label");
                 if(customer.srate==''){
                   listsrate.textContent=customer.srate;

                   }
                   else{
                   listsrate.textContent='50.0';
                   }
                    listsrate.style.marginLeft = '100px';

                   const listilang = document.createElement("label");
                   if(customer.ilang==''){
                   listilang.textContent='Null';
                   }
                   else{

                   listilang.textContent=customer.ilang;
                   }
                    listilang.style.marginLeft = '100px';

                 const listprate = document.createElement("label");
                  if(customer.prate=='' || customer.prate==null){

                   listprate.textContent=='00.0';
                   }
                   else{

                    listprate.textContent=customer.prate;
                   }
                    listprate.style.marginLeft = '50px';


                   listItem.appendChild(listbcode);
                   listItem.appendChild(listitemcode);
                   listItem.appendChild(listilang);
                   listItem.appendChild(listprate);
                   listItem.appendChild(listsrate);








                   const divide = document.createElement('hr');
resultsList.appendChild(listItem);
                resultsList.appendChild(divide);

                listItem.onclick = () => selectitem(customer.name);


            });
        }

        function selectitem(customerId) {
            // Implement logic to handle selected customer (e.g., make an API call, update UI)
            document.getElementById('itemname').value =customerId;
            alert(rs);
            alert(`Selected customer with ID: ${customerId}`);
        }

