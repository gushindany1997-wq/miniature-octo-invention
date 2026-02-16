<?php

$token = "8189363267:AAEnxvpyikgCgCo-eK7FKL0JrcrsO7WI3Mw";
$chat_id = "6071962920";

$emoji_id = "5222356412876732496";

$text = "🤯 Это кастом эмоджи в тексте";

$data = [
    "chat_id" => $chat_id,
    "text" => $text,

    "entities" => json_encode([
        [
            "type" => "custom_emoji",
            "offset" => 0,
            "length" => 2,
            "custom_emoji_id" => $emoji_id
        ]
    ])
];

file_get_contents(
    "https://api.telegram.org/bot$token/sendMessage?" .
    http_build_query($data)
);

?>
