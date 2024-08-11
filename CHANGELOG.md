# Changelog

## [v_0.1.1] - 2024-08-11
### Changed
- Updated the screen initialization to use dynamic system dimensions.
- Corrected the PyInstaller command in the README file.

## [v_0.1.0] - 2024-08-11
### Added
- Created a folder named `exe` containing the game executable and auxiliary files for creating the executable.
- Added `resource_path` function to the script, which checks if the script is running from an executable and returns the appropriate path to resources.

### Changed
- Updated project structure to include executable-related files.

### Notes
- The `resource_path` function ensures compatibility of resource paths when the script is packaged as an executable.

## [v_0.0.0] - 2024-08-11
### Init
- Initial commit. Set up project structure, added basic files and initial configuration.