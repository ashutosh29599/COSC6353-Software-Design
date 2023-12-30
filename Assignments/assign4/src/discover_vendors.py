import importlib.util
import inspect
import pkgutil


def discover_vendors():
    package = __import__("vendors")

    return sum(
        [vendor_annotated_functions_in_a_module(importer, module_name) for importer, module_name, _ in
         pkgutil.walk_packages(package.__path__)], [])


def vendor_annotated_functions_in_a_module(importer, module_name):
    module_spec = importer.find_spec(module_name)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)

    return [member for _, member in inspect.getmembers(module)
            if inspect.isfunction(member) and member.__module__ == module_name]
