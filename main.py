import click
import time
from fan import SetFan, ReedFan, get_cpu_temp, get_fun_speed


@click.group()
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def fan(ctx, debug):
    click.echo("Debug mode is {}".format('on' if debug else 'off'))
    ctx.ensure_object(dict)
    ctx.obj['DEBUG'] = debug


@fan.command()
@click.pass_context
def run(ctx):
    """Script for running fan"""
    fan = SetFan()
    while True:
        temp = get_cpu_temp()
        if ctx.obj['DEBUG']:
            click.echo("Temperatura {}".format(temp))
            
        fun_speed = get_fun_speed(temp)
        if ctx.obj['DEBUG']:
            click.echo("Fun speed {}".format(fun_speed))
        
        fan.set_speed(fun_speed)
        time.sleep(1)


@fan.command()
@click.pass_context
def info(ctx):
    """Print fan debug info"""
    fan = ReedFan()
    event = fan.get_turnover()
    if event:
        print("event detected")
    else:
        print("wait for event timed out")
