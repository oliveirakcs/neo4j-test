containers:
	@printf "Running containers... \n\n"
	docker-compose -p 12-backend -f docker-compose.yml up --build --abort-on-container-exit