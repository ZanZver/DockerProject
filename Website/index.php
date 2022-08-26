<html>
    <head> 
        <title>Testing API</title>
    </head>

    <body>
        <h1>MyAPI items</h1>
        <ul>
            <?php
                $json = file_get_contents("http://my-api/");
                $obj = json_decode($json);

                $items = $obj -> items;
                foreach($items as $item){
                    echo "<li>$item</li>";
                }
            ?>
        </ul>
    </body>
</html>