//===============================================================================
//
//    This file is part of muServe.
//
//    muServe is free software; you can redistribute it and/or modify
//    it under the terms of the GNU General Public License as published by
//    the Free Software Foundation; either version 2 of the License, or
//    (at your option) any later version.
//
//    muServe is distributed in the hope that it will be useful,
//    but WITHOUT ANY WARRANTY; without even the implied warranty of
//    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//    GNU General Public License for more details.
//
//    You should have received a copy of the GNU General Public License
//    along with muServe; if not, write to the Free Software
//    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA
//
//=============================================================================*/
//###############################################################################
//
//    Copyright (C) 2015 Kushagra Singh
//
//###############################################################################

var prev_req;

$('#searchquery').keyup(function () {

    var q = $("#searchquery").val()
    var $results = $("#results");

    // API URL
    var urlcall = "https://www.googleapis.com/youtube/v3/search?type=video&part=snippet&fields=items(id,snippet)"

    // max results
    urlcall += "&maxResults=20";
    
    // search query
    urlcall = urlcall + "&q=" + q;

    // API key
    urlcall += '&key=AIzaSyB0BvPaPRqLZxgsO_8z7xGB1-SRcBvZB-8';

    var html = "";
    var count = 0;
        conole.log("okkkk")

    try
    {
        conole.log("okkkk")
        prev_req.abort();
        conole.log("aborted");
    }
    catch(e)
    {
        conole.log(e);
    }

    prev_req = $.ajax({ 
        type: 'GET', 
        url: urlcall, 
        success: function (data) {
            var items = data["items"];

            items.forEach(function (item) {
            
                // Include the YouTube Watch URL youtu.be 
                html += '<p><a href="http://youtu.be/' + item.id.videoId + '">';
     
                // Add the default video thumbnail (default quality)
                html += '<img src="http://i.ytimg.com/vi/' + item.id.videoId + '/hqdefault.jpg">';
     
                count++;

            });

            console.log(html);


            // Did YouTube return any search results?
            if (count === 0)
                $results.html("No videos found");
            else 
              // Display the YouTube search results
                $results.html(html);
        }
    });

});