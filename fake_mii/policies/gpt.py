import fake_mii

from fake_ds.module_inject.base_policy import BaseInjectionPolicy

class GPTInjectionPolicy(BaseInjectionPolicy):
    def __init__(self):
        super().__init__()
        self.mii_version = fake_mii.__version__

    def attention(self):
        return "gpt attention"
