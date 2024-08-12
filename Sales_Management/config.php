<?php
$dbhost = 'localhost'; // Localhost deve ser em letras minúsculas
$dbUsername = 'root';
$dbPassword = '';
$dbName = 'formulario';

// Criando uma nova conexão usando mysqli (não mysql)
$conexao = new mysqli($dbhost, $dbUsername, $dbPassword, $dbName);

// Verificando se há erros de conexão
if ($conexao->connect_errno) {
    echo "Erro: " . $conexao->connect_error; // Exibe a mensagem de erro da conexão
} else {
    echo 'Connection on'; // Removeu os dois-pontos ':' e ajustou a sintaxe
}
