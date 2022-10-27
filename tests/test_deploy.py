import pytest
import fake_mii

def test_deploy():
    engine = fake_mii.deploy("gpt")
    assert engine.policy.mii_version == engine.policy.ds_version, "mismatched version"
