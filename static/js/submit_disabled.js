$(document).ready(function() {
    // Disable submit button initially
    $('#submitBtn').prop('disabled', true);
  
    // Listen for input changes in the form fields
    $('#myForm input').on('input', function() {
      var emptyFields = false;
  
      // Check if any field is empty
      $('#myForm input').each(function() {
        if ($(this).val() === '') {
          emptyFields = true;
          return false;  // Exit the loop if an empty field is found
        }
      });
  
      // Enable/disable submit button based on empty field status
      $('#submitBtn').prop('disabled', emptyFields);
    });
  });