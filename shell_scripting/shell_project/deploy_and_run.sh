#!/bin/bash
#Author: Mirza
#Shell scripting project to bundle, extract and run python files

#Constants
SCRIPTS_DIR="python_scripts"
EXTRACT_DIR="extracted_scripts"
BUNDLE_NAME="python_scripts.tar.gz"


#Function to check if the required directory exists
check_directory(){
	if [ ! -d "$1" ]; then
		echo "Error: Directory '$1' does not exist. Please ensure the directory is present."
		exit 1
	fi
}


#Function to create the tarball of python scripts
bundle_python_scripts(){
	echo "Creating a bundle of python scripts..."

	#Check if the scripts directory exists
	check_directory "$SCRIPTS_DIR"

	if [ -f "$BUNDLE_NAME" ]; then
		echo "Warning: Existing bundle '$BUNDLE_NAME' found."
		rm -f "$BUNDLE_NAME"
	fi


	tar -czf "python_scripts.tar.gz" -C "$SCRIPTS_DIR" .
	if [ $? -ne 0  ]; then
		echo "Error: Failed to create bundle $BUNDLE_NAME"
		echo "Exiting the script"
		exit 1
	fi

	echo "Bundle created successfully: $BUNDLE_NAME"
	echo ""
}


#Function to extract the tarball

extract_python_scripts(){

	echo "Extracting python scripts from the bundle...."

	if [ ! -f $BUNDLE_NAME ]; then
		echo "Error: Bundle $BUNDLE_NAME does not exist. Please create it first"
		exit 1
	fi
	
	if [ -d $EXTRACT_DIR ]; then
		echo "Warning: Existing directory $EXTRACT_DIR found."
		echo "Removing it..."
		rm -rf $EXTRACT_DIR
	fi

	#Create extraction directory and extract the tarball
	mkdir -p "$EXTRACT_DIR"
	tar -xzf "$BUNDLE_NAME" -C "$EXTRACT_DIR"
	if [ $? -ne 0 ]; then
		echo "Error: Failed to extract the bundle"
		exit 1
	fi

	echo "Scripts extracted successfully to: $EXTRACT_DIR"
	echo ""

}


run_python_scripts(){

	echo "Running Python Scripts..."

	check_directory "$EXTRACT_DIR"

	for script in "$EXTRACT_DIR"/*.py; do
		if [ -f "$script" ]; then
			echo "Executing: $script"
			python3 $script

			if [ $? -ne 0 ]; then
				echo "Error: Failed to execute script"
				exit 1
			fi
			echo ""
		else
			echo "Warning: No python scripts found in $EXTRACT_DIR"
			exit 1
		fi
	done

	echo "All scripts executed successfully"
}

echo "Starting the python script deployment proces..."
echo "================================================"

bundle_python_scripts
extract_python_scripts
run_python_scripts

echo "Deployment and execution process completed successfully"
