from invoke import task, Collection
import glob
import os


@task
def clean(ctx):
    """Delete compiled UI files from the 'dist' directory"""
    os.makedirs("dist", exist_ok=True)
    for ui_file in glob.glob("widgets/*.ui"):
        base_dir = os.path.basename(ui_file)
        py_file = f"dist/{base_dir[:-3]}.py"
        print(f"Removing {py_file}")
        ctx.run("rm -rf {py_file}")


@task(pre=[clean])
def create(ctx):
    """Compile Qt UI files to python files and place them in the 'dist' directory"""
    os.makedirs("dist", exist_ok=True)
    for ui_file in glob.glob("widgets/*.ui"):
        base_dir = os.path.basename(ui_file)
        py_file = f"dist/{base_dir[:-3]}.py"
        print(f"Compiling {ui_file} to {py_file}")
        ctx.run(f"pyside6-uic {ui_file} -o {py_file}")


@task(pre=[create])
def start(ctx):
    """Run the app"""
    ctx.run("python main.py", pty=True)


# Create a collection and add tasks to it
ns = Collection()
ns.add_task(start, default=True)
