<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
		<title>Карта Артека</title>
    </head>
    <body>
		<canvas id="canvas" width="1980" height="1020"> </canvas>
        <script>
            //var ws = new WebSocket("ws://127.0.0.1:5678/")
			var ws = new WebSocket("ws://{{ip}}:5678/")
			ctx = document.getElementById("canvas").getContext("2d");
			ctx.font = "italic 10pt Arial";
			map = new Image();
			map.src = "map.png";
			red = new Image();
			red.src = "red.png";
			green = new Image();
			green.src = "green.png";
			map.onload = function() {
				ctx.drawImage(map,0,0,1980,1020);
			}
            ws.onmessage = function (event) {
				var pings = JSON.parse(event.data);
				for (key in pings) {
					let ping = pings[key][0];
					let x = pings[key][1];
					let y = pings[key][2];
					if (ping === -1) {
						ctx.drawImage(red,x, y, 10, 10);
						ctx.fillStyle = "red";
						ctx.fillText(key, x-10, y-2);
					} else {
						ctx.drawImage(green, x, y, 10, 10);
						ctx.fillStyle = "green";
						ctx.fillText(key, x-10, y-2);
					}
					//ctx.fillStyle = "blue";
					//ctx.font = "italic 10pt Arial";
					//ctx.fillText(key, x-40, y-10);

				}
            };
        </script>
    </body>
</html>