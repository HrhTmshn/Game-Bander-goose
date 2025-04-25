# Changelog

## [v_0.1.3] - 2025-04-25
### Added
- Created and embedded a gameplay GIF preview into the `README.md`
- Added `LICENSE` file with a custom "Portfolio Only" license

## [v_0.1.2] - 2024-08-11
### Updates
- Improved enemy removal logic to check if enemies have fully exited the screen.
- Updated collision detection to use `colliderect` method for more accurate results.
- Enhanced code readability by reformatting and simplifying some logic.

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