<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
		<title>Карта Артека</title>
    </head>
    <body>
		<canvas id="canvas" width="4096" height="2160"> </canvas>
        <script>
            //var ws = new WebSocket("ws://127.0.0.1:5678/")
			var ws = new WebSocket("ws://{{ip}}:5678/")
			ctx = document.getElementById("canvas").getContext("2d");
			map = new Image();
			map.src = "map.png";
			red = new Image();
			red.src = "red.png";
			green = new Image();
			green.src = "green.png";
			map.onload = function() {
				ctx.drawImage(map,0,0,4096,2160);
			}
            ws.onmessage = function (event) {
				var pings = JSON.parse(event.data);
				for (key in pings) {
					let ping = pings[key][0];
					let x = pings[key][1];
					let y = pings[key][2];
					if (ping === -1) {
						ctx.drawImage(red,x, y, 30, 30);
					} else {
						ctx.drawImage(green, x, y, 30, 30);
					}
					ctx.fillStyle = "blue";
					ctx.font = "italic 30pt Arial";
					ctx.fillText(key, x-40, y-10);

				}
            };
        </script>
    </body>
</html>