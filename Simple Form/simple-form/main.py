"""
Name: MATT HICKS
Class: Design Patterns for Web Programming
Assignment: Simple Form
Date: 06/11/15
"""

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # Header section for top portion of form
        page_head = '''

        <!DOCTYPE html>
        <html>
        <head>
	        <link href="css/style.css" rel="stylesheet" type="text/css">
	        <link href='http://fonts.googleapis.com/css?family=Oxygen' rel='stylesheet' type='text/css'>
	        <title>Order New System</title>
        </head>
        <body>

        '''

        # My actual HTML form goes here
        page_form = '''
        <div class="container">
  	    <h1>HVAC Order Form</h1>

	    <form method="GET" action="">

	    	<label>Brand:</label>
	       	<input class="textfield" type="text" name="brand" placeholder="Brand">
	       	<label>Size:</label>
	       	<input class="textfield" type="size" name="size" input="size" placeholder="Size">
	       	<label>SEER Rating:</label>
	       	<input class="textfield" type="text" name="seer" placeholder="SEER Rating">
	       	<label>System Type:</label>
	       	<select name="system_type" id="system_type" style="height:33px;">
	            <option value="Heat Pump">Heat Pump</option>
	            <option value="Straight Cool">Straight Cool</option>
	            <option value="Gas Furnace">Gas Furnace</option>
	       	</select>
	       	<label>Heat Kit:</label>
            <label class="checkbox_label"><input type="checkbox" name="heat_kit" value="14 Kilowatt">14 Kilowatt</label><br>
  			<label class="comments">Additional Comments: </label><br>
			<textarea class="message-box" name="comments" placeholder="Additional Comments"></textarea>
	       <input type="submit" value="Submit" id="Submit">

    	</form>
        '''

        # This is the closing section with footer
        page_close = '''
            <footer align='center'>
		        <p>&copy;Copyright 2015 - All Rights Reserved.</p>
	        </footer>
        </div>
        </body>
        </html>
        '''

        # A confirmation that data was processed
        form_confirm_open = '''
        <div class="container">
	        <h2>Your Request has been submitted!</h2>
               <ul>
                 <li><strong>Brand: </strong>{brand}</li><br>
                 <li><strong>Size: </strong>{size}</li><br>
                 <li><strong>SEER Rating: </strong>{seer}</li><br>
                 <li><strong>System Type: </strong>{system_type}</li><br>
                <ul><br>
                <ul><li><strong>Heat Kit: </strong>{heat_option}</li></ul><br><br>
         '''

        # End of confirmation page
        form_confirm_close = '''
                <ul><li><strong>Additional Comments: </strong><br><p style='align:center;'>{comments}<p></li>
                </ul>
        </div>
        '''

        # Check to see if form is filled
        if self.request.GET:
            # Data assigned to variables
            brand = self.request.GET['brand']
            size = self.request.GET['size']
            seer = self.request.GET['seer']
            system_type = self.request.GET['system_type']
            heat_kit = self.request.get_all('heat_kit')
            comments = self.request.GET['comments']

            heat_option = '''
'''

            # A Loop for the check boxes
            for i in range(len(heat_kit)):
                heat_option = heat_kit[i]

            # Formats the form variables
            form_confirm_open = form_confirm_open.format(**locals())
            form_confirm_close = form_confirm_close.format(**locals())

            # Stores form data to a variable
            form_submitted = form_confirm_open + form_confirm_close

            # Prints page with the form data
            self.response.write(page_head + form_submitted + page_close)

            # Do this if no data present
        else:
            self.response.write(page_head + page_form + page_close)


# DON'T TOUCH
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
