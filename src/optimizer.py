import numpy as np
from config.settings import ALPHA_TEMPERATURE
from scipy.special import softmax


class AdamAlphaOptimizer:

    def __init__(
            self,
            num_tasks,
            lr=0.05,
            beta1=0.9,
            beta2=0.999,
            eps=1e-8,
            ema_decay=0.9,
            temperature=1.2
    ):
        self.temperature = temperature
        self.num_tasks = num_tasks
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.eps = eps
        self.ema_decay = ema_decay

        self.t = 0
        self.logits = np.zeros(num_tasks, dtype=np.float32)
        self.m = np.zeros(num_tasks, dtype=np.float32)
        self.v = np.zeros(num_tasks, dtype=np.float32)
        self.running_score = np.zeros(num_tasks, dtype=np.float32)

    def alpha(self):
        return softmax(
            self.logits /
            self.temperature
        )

    def update_running_average(self, scores):
        self.running_score = (
                self.ema_decay * self.running_score
                + (1 - self.ema_decay) * scores
        )

    def compute_advantage(self, scores):
        return scores - self.running_score

    def step(self, scores):
        scores = np.array(scores, dtype=np.float32)

        self.update_running_average(scores)
        advantage = self.compute_advantage(scores)

        self.t += 1
        g = advantage

        # Adam updates using the advantage as the gradient
        self.m = self.beta1 * self.m + (1 - self.beta1) * g
        self.v = self.beta2 * self.v + (1 - self.beta2) * (g ** 2)

        m_hat = self.m / (1 - self.beta1 ** self.t)
        v_hat = self.v / (1 - self.beta2 ** self.t)

        self.logits += (
                self.lr * m_hat / (np.sqrt(v_hat) + self.eps)
        )

        return {
            "alpha": self.alpha(),
            "advantage": advantage,
            "scores": scores
        }

    def state_dict(self):
        return {

            "t": self.t,

            "logits":
                self.logits,

            "m":
                self.m,

            "v":
                self.v,

            "running_score":
                self.running_score
        }

    def load_state_dict(
            self,
            state
    ):
        self.t = state["t"]

        self.logits = state["logits"]

        self.m = state["m"]

        self.v = state["v"]

        self.running_score = (
            state["running_score"]
        )