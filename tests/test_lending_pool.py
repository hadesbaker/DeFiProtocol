from brownie import accounts, LendingPool, Token
import pytest

INITIAL_BALANCE = 10000
DEPOSIT_AMOUNT = 1000
BORROW_AMOUNT = 500


@pytest.fixture(scope="module")

# Deploy Token and LendingPool contracts
def setup():
    deployer = accounts[0]
    token = Token.deploy("MyToken", "MTK", {"from": deployer})
    lending_pool = LendingPool.deploy(token.address, {"from": deployer})
    return token, lending_pool


# Test deposit and borrow functionality
def test_lending_pool(setup):
    token, lending_pool = setup
    user1 = accounts[1]

    # Ensure the user's initial balance is zero
    assert lending_pool.balances(user1) == 0

    # User deposits tokens into the lending pool
    token.approve(lending_pool.address, DEPOSIT_AMOUNT, {"from": user1})
    lending_pool.deposit(DEPOSIT_AMOUNT, {"from": user1})

    # Check user's balance after deposit
    assert lending_pool.balances(user1) == DEPOSIT_AMOUNT

    # User attempts to borrow tokens
    lending_pool.borrow(BORROW_AMOUNT, {"from": user1})

    # Check user's balance after borrowing
    assert lending_pool.balances(user1) == DEPOSIT_AMOUNT - BORROW_AMOUNT

    # Check the lending pool's balance (should have the borrowed amount)
    assert token.balanceOf(lending_pool.address) == BORROW_AMOUNT

    # Check user's token balance (should have the borrowed amount)
    assert token.balanceOf(user1) == BORROW_AMOUNT
