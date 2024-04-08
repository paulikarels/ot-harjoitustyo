from invoke import task

@task
def flask(ctx):
    ctx.run("flask --app src/flask_app.py run", pty=True)

@task
def start(ctx):
    ctx.run("py src/app.py", pty=False)
