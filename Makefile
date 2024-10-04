all: build run

run:
	@( \
		 echo "making python venv"; \
		 python -m venv .venv; \
		 echo "sourcing python venv"; \
		 source ./.venv/bin/activate; \
		 echo "downloading dependencies"; \
		 pip install -r ./requirements.txt; \
		 echo "starting py-server"; \
		 python ./main.py; \
	)

clean:
	@echo "cleaning Python server..."
	@rm -rf ./.venv

.PHONY: all build run
