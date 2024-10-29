PYTHON_PATH=`which python`

reinstall:
	$(PYTHON_PATH) -m pip uninstall metagpt-simple -y
	$(PYTHON_PATH) -m poetry build
	$(PYTHON_PATH) -m pip install dist/*.whl