# vllm-project/vllm#3353: Neuron error: AttributeError: module 'mpmath' has no attribute 'rational'

| 字段 | 值 |
| --- | --- |
| Issue | [#3353](https://github.com/vllm-project/vllm/issues/3353) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Neuron error: AttributeError: module 'mpmath' has no attribute 'rational'

### Issue 正文摘录

Running on AWS on: Instance type: inf2.48xlarge AMI name: Deep Learning AMI Neuron (Ubuntu 22.04) 20240304 Following step 2 and 3 of https://docs.vllm.ai/en/latest/getting_started/neuron-installation.html When running `python examples/offline_inference_neuron.py` I get this error: ``` (aws_neuron_venv_pytorch) ubuntu@ip-172-31-74-175:~/vllm$ python examples/offline_inference_neuron.py Traceback (most recent call last): File "/home/ubuntu/vllm/examples/offline_inference_neuron.py", line 1, in from vllm import LLM, SamplingParams File "/home/ubuntu/aws_neuron_venv_pytorch/lib/python3.10/site-packages/vllm/__init__.py", line 3, in from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs File "/home/ubuntu/aws_neuron_venv_pytorch/lib/python3.10/site-packages/vllm/engine/arg_utils.py", line 6, in from vllm.config import (CacheConfig, DeviceConfig, ModelConfig, File "/home/ubuntu/aws_neuron_venv_pytorch/lib/python3.10/site-packages/vllm/config.py", line 6, in import torch File "/home/ubuntu/aws_neuron_venv_pytorch/lib/python3.10/site-packages/torch/__init__.py", line 1504, in from . import masked File "/home/ubuntu/aws_neuron_venv_pytorch/lib/python3.10/site-packages/torch/masked/_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ng step 2 and 3 of https://docs.vllm.ai/en/latest/getting_started/neuron-installation.html When running `python examples/offline_inference_neuron.py` I get this error: ``` (aws_neuron_venv_pytorch) ubuntu@ip-172-31-74-1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 3.10/site-packages/vllm/engine/arg_utils.py", line 6, in from vllm.config import (CacheConfig, DeviceConfig, ModelConfig, File "/home/ubuntu/aws_neuron_venv_pytorch/lib/python3.10/site-packages/vllm/config.py", line 6,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ntu 22.04) 20240304 Following step 2 and 3 of https://docs.vllm.ai/en/latest/getting_started/neuron-installation.html When running `python examples/offline_inference_neuron.py` I get this error: ``` (aws_neuron_venv_pyt...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: y", line 11, in from torch._prims_common import corresponding_real_dtype File "/home/ubuntu/aws_neuron_venv_pytorch/lib/python3.10/site-packages/torch/_prims_common/__init__.py", line 23, in import sympy File "/home/ubu...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
