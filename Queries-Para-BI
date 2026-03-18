-- Quantos filmes e quantas séries há no catalogo
SELECT type, 
COUNT(*) AS quantidade_de_obras
FROM netflix_limpo4
GROUP BY type
ORDER BY quantidade_de_obras DESC;

-- Quais são os gêneros que dominam a plataforma 
SELECT TOP 10 listed_in,
COUNT(*) AS categoria_presente
FROM netflix_limpo4
GROUP BY listed_in
ORDER BY categoria_presente DESC;

-- Entender para qual público a Netflix produz mais conteúdo
SELECT rating,
COUNT(*) AS obras
FROM netflix_limpo4
GROUP BY rating
ORDER BY obras DESC;

-- Volume de Lançamentos por Ano
SELECT release_year,
COUNT (*) as obras_lancadas
FROM netflix_limpo4
GROUP BY release_year
ORDER BY obras_lancadas DESC;


