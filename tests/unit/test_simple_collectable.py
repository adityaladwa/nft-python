import pytest
from brownie import accounts, network
from scripts.deploy_and_create import deploy_and_create
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENV, get_accounts


def test_can_create_simple_collectable():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENV:
        pytest.skip()
    simple_collectible = deploy_and_create()
    assert simple_collectible.ownerOf(0) == get_accounts()
