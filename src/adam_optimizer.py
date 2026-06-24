import numpy as np

from scipy.special import (
    softmax
)


class AdamAlphaOptimizer:

    def __init__(
        self,
        num_tasks,
        lr=0.05,
        beta1=0.9,
        beta2=0.999,
        eps=1e-8
    ):

        self.lr = lr

        self.beta1 = beta1

        self.beta2 = beta2

        self.eps = eps

        self.t = 0

        self.logits = np.zeros(
            num_tasks
        )

        self.m = np.zeros(
            num_tasks
        )

        self.v = np.zeros(
            num_tasks
        )

    def alpha(self):

        return softmax(
            self.logits
        )

    def step(
        self,
        reward
    ):

        self.t += 1

        g = reward

        self.m = (
            self.beta1*self.m
            + (1-self.beta1)*g
        )

        self.v = (
            self.beta2*self.v
            + (1-self.beta2)*(g**2)
        )

        m_hat = (
            self.m
            /
            (1-self.beta1**self.t)
        )

        v_hat = (
            self.v
            /
            (1-self.beta2**self.t)
        )

        self.logits += (
            self.lr
            *
            m_hat
            /
            (
                np.sqrt(
                    v_hat
                )
                + self.eps
            )
        )

        return self.alpha()