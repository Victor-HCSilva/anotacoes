# Makefile para gerenciar a aplicação anotacoes com Docker Compose

# Rodar a aplicação (build + start)
run:
	@docker compose up --build

# Rodar em background (detached)
run-detached:
	@docker compose up --build -d

# Parar containers da aplicação
stop:
	@docker compose down

# Parar e remover containers, volumes e imagens da aplicação (seguro)
clean:
	@echo "Removendo containers, volumes e imagens do projeto em 5 segundos..."
	@sleep 5
	@docker compose down --volumes --rmi all

# Ver logs dos containers da aplicação
logs:
	@docker compose logs -f

# Listar containers ativos
ps:
	@docker ps

# Listar todas as imagens do host
images:
	@docker images

migrate:
	@echo "Executando migrações"
	@python3 manage.py makemigrations
	@python3 manage.py migrate
	@clear

save_all:
	@git add .
	@git commit
