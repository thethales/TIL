# Consultar usuários inativos no banco de dados

O Maker da Softwell mantém logs de autenticação do usuário na tabela fr_sessao. Por meio disso pode-se determinar ultima data de conexão do usuário.

-2019-11-12 
```SQL
SELECT ses_usuario as usuario_login, max(coalesce(ses_datahora_login,now())) as data_ultimo_login
FROM fr_sessao
RIGHT JOIN 
	fr_usuario ON UPPER(fr_usuario.usr_login) = UPPER(fr_sessao.ses_usuario)
GROUP BY  ses_usuario
HAVING  max(coalesce(ses_datahora_login,now()))  <= now() - INTERVAL '30 DAYS'
```