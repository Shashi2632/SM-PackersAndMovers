$(document).ready(function() {
    if ($.fn.DataTable.isDataTable('#clickableTable')) {
        $('#clickableTable').DataTable().destroy();
    }
    $('#clickableTable').DataTable({
        "order": [[4, "desc"],[3, "desc"]],  // Sort the 4th column in descending order by default
        "columnDefs": [
            { "orderable": false, "targets": 0 }  // Disable sorting for the first column (index 0)
        ]
    });
});


document.addEventListener('DOMContentLoaded', function () {
    var table = document.getElementById('clickableTable');
    var rows = table.getElementsByTagName('tr');

    for (var i = 0; i < rows.length; i++) {
        rows[i].addEventListener('click', function () {
            var href = this.getAttribute('data-href');
            if (href) {

                // Use fetch to make an asynchronous request to the backend
                fetch(href)
                    .then(response => {
                        // Check if the request was successful (status code 200-299)
                        if (response.ok) {
                            console.log('response:-> ', response.text)
                            // Parse the response as needed (JSON, text, etc.)
                            return response.json(); // Change this based on your backend response format
                        } else {
                            throw new Error('Network response was not ok: ' + response.statusText);
                        }
                    })
                    .then(data => {
                        console.log(data)
                        // Update the modal content with the fetched data
                        document.getElementById('unameLabel').textContent = data.specific_booking.name;
                        document.getElementById('uemailLabel').textContent = data.specific_booking.email;
                        document.getElementById('uphoneLabel').textContent = data.specific_booking.phone;
                        document.getElementById('locationLabel').textContent = data.specific_booking.location_city;
                        document.getElementById('servicesLabel').textContent = data.specific_booking.services;
                        document.getElementById('dateLabel').textContent = data.specific_booking.inquirydate;


                        document.getElementById('originAddress').textContent = data.specific_booking.origin_address;
                        document.getElementById('destinationAddress').textContent = data.specific_booking.destination_address;
                        // Update other fields as needed

                        var modalFooter = document.querySelector('.modal-footer');
                        // Clear the modal footer content
                        modalFooter.innerHTML = "";

                        // Check if status is "Booked" to modify the modal footer
                        if (data.specific_booking.status === "Booked") {
                            var bookeddate = data.specific_booking.bookeddate;

                            // Add a class to the modal footer to center its content
                            modalFooter.classList.add('justify-content-center');
                            // Insert the HTML for the booked inquiry message and image
                            modalFooter.innerHTML = `
                            <div class="inquirydone" style="text-align: end;height: 150px;">
                                <h5 id="bookeddateLabel" style="line-height: 3rem;color: green;">${bookeddate}</h5>
                                <h3 style="line-height: 4rem;color: green;">This Inquiry is Already Booked!</h3>
                            </div>
                            <img src="/static/images/checkmark.png" style="width: 120px;height: 150px;">
                            `;
                        } else {

                            // Create form element
                            var form = document.createElement('form');
                            form.method = "post";
                            form.action = "/update-inquiry/";
                            form.style.display = "flex";
                            form.style.alignItems = "flex-end";
                            form.style.width = "100%";
                            form.style.justifyContent = "space-between";

                            var csrfToken = document.createElement('input');
                            csrfToken.type = "hidden";
                            csrfToken.name = "csrfmiddlewaretoken";
                            csrfToken.value = "{{ csrf_token }}";

                            // Append csrfToken input to form
                            form.appendChild(csrfToken);
                            // Insert the form as it is
                            form.innerHTML = `
                            <ul>
                            <li style="margin-bottom: 0.5rem;display: flex;"><img src="/static/images/date-to-30.png"> 
                            <input type="datetime-local" class="form-control" id="date" name="bookeddate" placeholder="2023-12-18" required style="height: 30px;width: 100%;margin-left: 7px;">
                            </li>
                            <li class="d-flex align-items-center">
                            <div class="custom-control custom-switch">
                            <input type="checkbox" class="custom-control-input" id="customSwitch1" name="status" onchange="toggleSwitch()">
                            <label class="custom-control-label" for="customSwitch1">
                            <h5 id="statusLabel" style="color: red;"></h5>
                            </label>
                            </div>
                            </li>
                            <!-- Hidden input field to store the status value -->
                            <input type="hidden" id="statusValue" name="statusValue" required>
                            <input type="hidden" id="inquiryid" name="inquiryid" requied>
                            </ul>
                        
                            <div class="footer-btn">
                            <button type="button" class="btn btn-secondary" data-dismiss="modal" id="closebtn">Close</button>
                            <button type="submit" class="btn btn-primary btn block" id="savebtn">Save changes</button>
                            </div>
                            `;

                            // Append form to modal footer
                            modalFooter.appendChild(form);

                            document.getElementById('statusLabel').textContent = data.specific_booking.status;
                            document.getElementById("inquiryid").value = data.specific_booking.id;
                        }


                        // Show the modal
                        $('#bd-example-modal-lg').modal('show');

                    })
                    .catch(error => {
                        console.error('Fetch error:', error);
                        // Handle errors (display an error message, etc.)
                    });
            }
        });
    }
});


function toggleSwitch() {
    var switchCheckbox = document.getElementById('customSwitch1');
    var statusLabel = document.getElementById('statusLabel');
    var statusValueInput = document.getElementById("statusValue");

    if (switchCheckbox.checked) {
        // If the switch is toggled ON
        statusLabel.textContent = 'Booked';
        statusLabel.style.color = 'green';
        statusValueInput.value = "Booked"; // Update hidden input value
    } else {
        // If the switch is toggled OFF
        statusLabel.textContent = 'Pending';
        statusLabel.style.color = 'red';
        statusValueInput.value = "Pending"; // Update hidden input value
    }
}

// Submit form via AJAX when Save changes button is clicked
$('#bd-example-modal-lg form').submit(function (event) {
    event.preventDefault(); // Prevent default form submission

    // Serialize form data
    var formData = $(this).serialize();

    // Send form data via AJAX
    $.ajax({
        url: $(this).attr('action'), // URL to submit the form to
        type: $(this).attr('method'), // HTTP method (POST in this case)
        data: formData, // Form data to be submitted
        success: function (data) {
            // Close the modal
            $('#bd-example-modal-lg').modal('hide');
            // Display success message
            alert('Form submitted successfully.');
        },
        error: function (xhr, status, error) {
            console.error('AJAX request failed:', error); // Log any errors
            // Display error message
            alert('Failed to submit the form. Please try again later.');
        }
    });
});


window.addEventListener('DOMContentLoaded', function() {
    // Get the table body
    var tbody = document.querySelector('#clickableTable tbody');

    // Get all rows except the first one (header row) and convert them to an array
    var rows = Array.from(tbody.querySelectorAll('tr:not(:first-child)'));

    // Sort rows based on the content of the "Inquiry" column
    rows.sort(function(a, b) {
        var statusA = a.querySelector('.status-cell').textContent.trim().toLowerCase();
        var statusB = b.querySelector('.status-cell').textContent.trim().toLowerCase();
        if (statusA === 'pending' && statusB !== 'pending') {
            return -1;
        } else if (statusA !== 'pending' && statusB === 'pending') {
            return 1;
        } else {
            return 0; // Maintain the original order if both are the same
        }
    });

    // Remove existing rows from the table
    rows.forEach(function(row) {
        row.remove();
    });

    // Append sorted rows back to the table
    rows.forEach(function(row) {
        tbody.appendChild(row);
    });
});



