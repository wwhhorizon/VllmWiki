# vllm-project/vllm#973: Deployment stuck when using kuberay to scale Multi-GPU LLM on Kubernetes

| 字段 | 值 |
| --- | --- |
| Issue | [#973](https://github.com/vllm-project/vllm/issues/973) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | operator;sampling |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Deployment stuck when using kuberay to scale Multi-GPU LLM on Kubernetes

### Issue 正文摘录

I want to use kuberay to serve and horizontaly-scale my LLM on Kubernetes. The python code i want to deploy looks somewhat like this: ``` import json import logging from typing import AsyncGenerator import ray from fastapi import BackgroundTasks from huggingface_hub import login from ray import serve from starlette.requests import Request from starlette.responses import StreamingResponse, Response from vllm.engine.arg_utils import AsyncEngineArgs from vllm.engine.async_llm_engine import AsyncLLMEngine from vllm.sampling_params import SamplingParams from vllm.utils import random_uuid logger = logging.getLogger("ray.serve") @serve.deployment() class VLLMPredictDeployment: def __init__(self, **kwargs): """ Construct a VLLM deployment. Refer to https://github.com/vllm-project/vllm/blob/main/vllm/engine/arg_utils.py for the full list of arguments. Args: model: name or path of the huggingface model to use download_dir: directory to download and load the weights, default to the default cache dir of huggingface. use_np_weights: save a numpy copy of model weights for faster loading. This can increase the disk usage by up to 2x. use_dummy_weights: use dummy values for model weights. dtype:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ernetes. The python code i want to deploy looks somewhat like this: ``` import json import logging from typing import AsyncGenerator import ray from fastapi import BackgroundTasks from huggingface_hub import login from...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: port AsyncGenerator import ray from fastapi import BackgroundTasks from huggingface_hub import login from ray import serve from starlette.requests import Request from starlette.responses import StreamingResponse, Respon...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: tensor_parallel_size: number of tensor parallel replicas. block_size: token block size. swap_space: CPU swap space size (GiB) per GPU. gpu_memory_utilization: the percentage of GPU memory to be used for the model execut...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Deployment stuck when using kuberay to scale Multi-GPU LLM on Kubernetes I want to use kuberay to serve and horizontaly-scale my LLM on Kubernetes. The python code i want to deploy looks somewhat like this: ``` import j...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: weights and activations. The "auto" option will use FP16 precision for FP32 and FP16 models, and BF16 precision. for BF16 models. seed: random seed. worker_use_ray: use Ray for distributed serving, will be

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
