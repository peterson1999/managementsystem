
            $(document).ready(function () {
              var oTable= $('#dtBasicExample').DataTable({  
                "oLanguage": {
                  "sSearch": "Filter Data"
                },
                "iDisplayLength": -1,
                "sPaginationType": "full_numbers",
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
            // oTable.buttons().container().addClass('btn btn-danger');
            Table(oTable);

              $('.dataTables_length').addClass('bs-select');
              });


            function Table(  oTable) {
              // var oTable = $('#dtBasicExample').DataTable({
              //   "oLanguage": {
              //     "sSearch": "Filter Data"
              //   },
              //   "iDisplayLength": -1,
              //   "sPaginationType": "full_numbers",
            
              // });

              $("#datepicker_from").datepicker({
                showOn: "button",
                buttonImage: "/static/resources/calendar.png",
                buttonImageOnly: false,
                "onSelect": function(date) {
                  minDateFilter = new Date(date).getTime();
                  oTable.draw();
                }
              }).keyup(function() {
                minDateFilter = new Date(this.value).getTime();
                oTable.draw();
              });
            
              $("#datepicker_to").datepicker({
                showOn: "button",
                buttonImage: "/static/resources/calendar.png",
                buttonImageOnly: false,
                "onSelect": function(date) {
                  maxDateFilter = new Date(date).getTime();
                  oTable.draw();
                }
              }).keyup(function() {
                maxDateFilter = new Date(this.value).getTime();
                oTable.draw();
              });
            
            }
            
            // Date range filter
            minDateFilter = "";
            maxDateFilter = "";
            
            $.fn.dataTableExt.afnFiltering.push(
              function(oSettings, aData, iDataIndex) {
                if (typeof aData._date == 'undefined') {
                  aData._date = new Date(aData[0]).getTime();
                }
            
                if (minDateFilter && !isNaN(minDateFilter)) {
                  if (aData._date < minDateFilter) {
                    return false;
                  }
                }
            
                if (maxDateFilter && !isNaN(maxDateFilter)) {
                  if (aData._date > maxDateFilter) {
                    return false;
                  }
                }
            
                return true;
              }
            );
