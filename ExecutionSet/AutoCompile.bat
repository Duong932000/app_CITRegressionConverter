@echo off
echo Activating Anaconda environment: tool...

::Activating Anaconda environment: mcdc...
call activate tool

echo Running PyInstaller ...

:: Use PyInstaller to compile the Python script
pyinstaller --noconfirm --onedir --windowed --icon "D:/sgdcc_tool_sdk_dev/ToolTaskSW/app_Human2Bench/ExecutionSet/icon/CAPLGenerator_icon.ico" ^
--add-data "D:/sgdcc_tool_sdk_dev/ToolTaskSW/app_Human2Bench/ExecutionSet/libs/gui/CTkMessagebox;CTkMessagebox/" ^
--add-data "D:/sgdcc_tool_sdk_dev/ToolTaskSW/app_Human2Bench/ExecutionSet/libs/gui/CTkToolTip;CTkToolTip/" ^
--add-data "D:/sgdcc_tool_sdk_dev/ToolTaskSW/app_Human2Bench/ExecutionSet/libs/capl/capl_libs;capl_libs/" ^
--add-data "D:/sgdcc_tool_sdk_dev/ToolTaskSW/app_Human2Bench/ExecutionSet/docx/UserGuideResource;UserGuideResource/" ^
--add-data "D:/sgdcc_tool_sdk_dev/ToolTaskSW/app_Human2Bench/ExecutionSet/libs/gui/Human2Bench_Installer.exe;." ^
--add-data "D:/sgdcc_tool_sdk_dev/ToolTaskSW/app_Human2Bench/ExecutionSet/libs/gui/version.config;." ^
--distpath "D:/sgdcc_tool_sdk_dev/ToolTaskSW/app_Human2Bench/Release" "D:/sgdcc_tool_sdk_dev/ToolTaskSW/app_Human2Bench/ExecutionSet/src/Human2Bench.py"

call deactivate

pause