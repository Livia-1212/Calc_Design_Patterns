import importlib
import pkgutil

class PluginLoader:
    """Dynamically loads all command plugins from the specified plugins package."""

    loaded_plugins = set()  # Track loaded plugins to avoid duplicate registrations

    @staticmethod
    def load_plugins(command_handler, plugins_package, calculator):
        """
        Load all plugins from the specified package and register their commands.

        Args:
            command_handler (CommandHandler): The command handler to register commands with.
            plugins_package (str): The root package path to load plugins from (e.g., 'plugins').
            calculator (Calculator): The calculator instance.
        """
        package_path = plugins_package.replace('.', '/')
        registered_plugins = []  # Track successfully registered plugins

        print(f"🔍 Searching for plugins in: {plugins_package} ...")

        # Discover and iterate through all submodules in the specified plugins directory
        for _, plugin_name, _ in pkgutil.iter_modules([package_path]):
            module_name = f"{plugins_package}.{plugin_name}"

            if module_name in PluginLoader.loaded_plugins:
                continue

            try:
                # Dynamically import the plugin module
                module = importlib.import_module(module_name)

                if hasattr(module, 'register_commands'):
                    register_func = getattr(module, 'register_commands')
                    register_func(command_handler, calculator)
                    PluginLoader.loaded_plugins.add(module_name)
                    registered_plugins.append(plugin_name)  # Track registered plugins
                else:
                    print(f"⚠️  No `register_commands` function found in: {module_name}. Skipping...")

            except ImportError as e:
                print(f"❌ Failed to import plugin: {module_name}. Error: {e}")

        # Print a consolidated success message for registered plugins
        if registered_plugins:
            print(f"✅ Successfully imported plugins: {', '.join(registered_plugins)}")
        else:
            print("⚠️ No plugins were successfully imported.")
