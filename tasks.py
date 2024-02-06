from invoke import task, Collection
import glob
import os
import shutil


@task
def clean(ctx):
    """Delete the compiled UI files and the 'dist' directory"""
    # Remove compiled UI files
    if os.path.exists("lib"):
        for ui_compiled_file in glob.glob("src/ui/*.py"):
            print(f"Removing {ui_compiled_file}")
            os.remove(ui_compiled_file)

    # Remove the compiled application and dist directory
    if os.path.exists("dist"):
        print("Removing application files")
        shutil.rmtree("dist")


@task(pre=[clean])
def build(ctx):
    """Compile Qt UI files to python files and place them in the 'src/ui' directory"""
    os.makedirs("lib", exist_ok=True)
    for ui_file in glob.glob("widgets/*.ui"):
        base_dir = os.path.basename(ui_file)
        py_file = f"src/ui/{base_dir[:-3]}.py"
        print(f"Compiling {ui_file} to {py_file}")
        ctx.run(f"pyside6-uic {ui_file} -o {py_file}")


@task(pre=[build])
def start(ctx):
    """Run the app"""
    print("Starting src/main.py...")
    ctx.run("python src/main.py", pty=True)


@task(pre=[build])
def compile(ctx):
    """Create an executable from the application"""
    ctx.run("pyinstaller --onefile --windowed src/main.py")


# Create a collection and add tasks to it
ns = Collection()
ns.add_task(clean)
ns.add_task(build)
ns.add_task(start, default=True)
ns.add_task(compile)