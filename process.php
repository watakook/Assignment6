<!DOCTYPE html>
<html>

<head>
    <title>Results</title>
</head>

<body>
    <h2>Processing Results:</h2>
    <?php
        $output = shell_exec("python3 /var/www/html/data_management.py " . escapeshellarg($_SERVER['QUERY_STRING']));
        echo $output;
    ?>

</body>

</html>