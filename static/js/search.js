
            $(document).ready(function () {
              $('#dtBasicExample').DataTable({  
                dom: 'lBfrtip',
                  buttons: [
                  //{
                //   extend: 'excelHtml5', 
                //   text: 'Excel',}
                'copyHtml5',
                'excelHtml5',
                'csvHtml5',
                'pdfHtml5'
            ]});

              $('.dataTables_length').addClass('bs-select');
              });


