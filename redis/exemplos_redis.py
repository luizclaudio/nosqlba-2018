#coding: utf-8

import redis

banco = redis.Redis(
    host='127.0.0.1',
    port=6379,
    password='')
    
    
# -- INSERIR (CREATE) ------------------------------
banco.set('chave_1', 'novo valor')
# ---
banco.set('chave_2', 5)


# -- RECUPERAR/BUSCAR (RETREIVE) ------------------------------
valor = banco.get('chave_busca')
print(valor)


# -- ATUALIZAR (UPDATE) ------------------------------
banco.set('chave_existente', 'novo valor')


# -- EXCLUIR (DELETE) ------------------------------
resultado = banco.delete('chave')


# -- CHAVES ------------------------------
chaves = banco.keys()
# ---
chaves = banco.keys('partedo*')


# -- CONTADORES ------------------------------
banco.set('meu_contador', 5)
banco.incr('meu_contador')
banco.incr('meu_contador', 2)
banco.decr('meu_contador')
banco.decr('meu_contador', 3)
valor = banco.get('meu_contador')
print(value)


# -- LISTAS ------------------------------
resultado = banco.rpush('numeros', 'um')
resultado = banco.rpush('numeros', 'dois')
resultado = banco.rpush('numeros', 'três')
resultado = banco.rpush('numeros', 'quatro')
print(banco.llen('numeros'))
print(banco.lindex('numeros', 3))


# -- HASHES ('DOCUMENTOS') ------------------------------
banco.hset('documento_1', 'nome', 'alice')
banco.hset('documento_1', 'idade', 5)
valor = banco.hget('documento_1', 'nome')
print(valor)
todos = banco.hgetall('documento_1')
print(todos)
r.hmset('outro_documento', {'nome': 'maria', 'idade': 23})
todos = r.hgetall('outro_documento')
print(todos)









