///////////////////////////////////////////////////////////////////////////////
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
//=============================================================================
///////////////////////////////////////////////////////////////////////////////
//
//    Copyright (C) 2015 Kushagra Singh
//
///////////////////////////////////////////////////////////////////////////////

var prev_req;

$('#searchquery').keyup(function () {

    var q = $("#searchquery").val()
    var $results = $("#results");

    // Google API key
    var key = "AIzaSyB0BvPaPRqLZxgsO_8z7xGB1-SRcBvZB-8";

    // API URL
    var urlcall = "https://www.googleapis.com/youtube/v3/search?"

    // max results
    var maxResults = "12";
    
    // API url
    urlcall = urlcall + "type=video&part=snippet&fields=items(id,snippet)"
    urlcall = urlcall + "&maxResults=" + maxResults;
    urlcall = urlcall + "&q=" + q;
    urlcall = urlcall + '&key=' + key;


    var html;
    var count = 0;

    try
    {
        console.log("okk")
        prev_req.abort();
        console.log("aborted");
    }
    catch(e)
    {
        console.log(e);
    }

    prev_req = $.ajax({ 
        type: 'GET', 
        url: urlcall, 
        success: function (data) {

            var items = data["items"];
            html = "<br><div class = 'row'>";
            
            items.forEach(function (item) {
            
                html = html + '<div class = "col-md-3">';
                html += '<a href="http://youtu.be/' + item.id.videoId + '">';
                html += "<center>";
                html += '<img height="180px" width="180px" src="http://i.ytimg.com/vi/' + item.id.videoId + '/hqdefault.jpg">';
                html += "<br>"
                html = html + "<p>" + item.snippet.title + "</p>";
                html += "</a>";

                html += '<form action = "/add/' + item.id.videoId + '" method = "POST">'
                html += "<input type = 'submit' class = 'btn btn-md btn-default' value = 'Add to Q' />";
                html += "<input type = 'hidden' name = 'title' value = '" + item.snippet.title + "' />";
                html += "</form>"

                html += "</center>";
                html += "</div>";

                // Total results displayed
                count++;

                if (count % 4 == 0)
                    html += "</div><br><div class = 'row'>";
            });

            html += "</div><br>";

            // Did YouTube return any search results?
            if (count === 0)
                $results.html("No videos found");
            else 
              // Display the YouTube search results
                $results.html(html);

            $('#results').css('display', 'inline-block');
        }
    });

});
