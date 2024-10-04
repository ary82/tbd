all: build run

run:
	@( \
		 echo "making python3 venv"; \
		 python3 -m venv .venv; \
		 echo "sourcing python3 venv"; \
		 source ./.venv/bin/activate; \
		 echo "downloading dependencies"; \
		 pip install -r ./requirements.txt; \
		 echo "starting py-server"; \
		 python3 -m flask --app ./main.py --debug run; \
	)

clean:
	@echo "cleaning python3 server..."
	@rm -rf ./.venv
	@rm -rf ./__pycache__

.PHONY: all build run
