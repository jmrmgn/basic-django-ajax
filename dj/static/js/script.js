$(function() {

   const clearFields = () => {
      
   }
   
   const getTotalUser = () => {
      let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
      $.ajax({
         url: 'get_user/',
         method: 'POST',
         dataType: 'JSON',
         data: {
            csrfmiddlewaretoken: csrfmiddlewaretoken
         },
         success: (data) => {
            document.getElementById('userCount').innerHTML = data.number;
         }
      });
   }
   
   
   getTotalUser();

   $("#btnAdd").on('click', (e) => {
      let firstname = $("#id_firstname").val();
      let lastname = $("#id_lastname").val();
      let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
      e.preventDefault();
      $.ajax({
         url: 'insert/',
         method: 'POST',
         dataType: 'JSON',
         data: {
            firstname: firstname,
            lastname: lastname,
            csrfmiddlewaretoken: csrfmiddlewaretoken
         },
         success: (data) => {
            if ( data.msg )  {
               alert(`${firstname} added successfully!`);
               getTotalUser();
            }
            else {
               alert('Error!')
            }
         }
      })      
   });

});