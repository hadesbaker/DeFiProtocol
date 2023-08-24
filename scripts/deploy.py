from scripts.helpful_scripts import get_account
from brownie import Token, LendingPool


def deploy():
    account = get_account()
    token = Token.deploy("HadesCoin", "HC", {"from": account})
    lending_pool = LendingPool.deploy(token.address, {"from": account})
    lending_pool.wait(1)


def main():
    deploy()
