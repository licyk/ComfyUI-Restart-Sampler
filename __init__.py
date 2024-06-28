from . import restart_sampling
from .restart_sampling import sample_restart


if not restart_sampling.INITIALIZED:
    from comfy.k_diffusion import sampling as k_diffusion_sampling
    from comfy.samplers import SAMPLER_NAMES

    setattr(k_diffusion_sampling, "sample_restart", sample_restart)
    SAMPLER_NAMES.append("restart")
    restart_sampling.INITIALIZED = True


NODE_CLASS_MAPPINGS = {}