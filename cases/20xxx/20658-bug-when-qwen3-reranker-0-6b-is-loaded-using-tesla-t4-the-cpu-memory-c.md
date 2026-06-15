# vllm-project/vllm#20658: [Bug]: When qwen3-reranker-0.6B is loaded using Tesla T4, the CPU memory continues to grow until the system crashes

| 字段 | 值 |
| --- | --- |
| Issue | [#20658](https://github.com/vllm-project/vllm/issues/20658) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When qwen3-reranker-0.6B is loaded using Tesla T4, the CPU memory continues to grow until the system crashes

### Issue 正文摘录

### Your current environment The graphics card is Tesla T4, and NVIDIA-SMI 525.105.17 Driver Version: 525.105.17 CUDA Version: 12.0 [pip-requirements-all.txt](https://github.com/user-attachments/files/21133901/pip-requirements-all.txt) ### 🐛 Describe the bug The machine is a single card machine with 32G memory. When executed using the following code, the memory grows until it crashes,： [https://github.com/QwenLM/Qwen3-Embedding/blob/main/examples/qwen3_reranker_vllm.py](url) I think it's the distributed parameter: distributed_executor_backend='ray'. This doesn't happen when I load it like this： ``` self.lm = LLM( model=model_name_or_path, # tensor_parallel_size=number_of_gpu, max_model_len=self.max_length, # enable_prefix_caching=True, # distributed_executor_backend='ray', enforce_eager=True, Gpu_memory_utilization = 0.5, dtype=kwargs.get('dtype', 'float16'), ) ``` enable_prefix_caching is not used, presumably because triton is not yet compatible with T4 ``` import logging import json import logging from collections import defaultdict from contextlib import nullcontext from dataclasses import dataclass, field from pathlib import Path from tqdm import tqdm from typing import Union,...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: nment The graphics card is Tesla T4, and NVIDIA-SMI 525.105.17 Driver Version: 525.105.17 CUDA Version: 12.0 [pip-requirements-all.txt](https://github.com/user-attachments/files/21133901/pip-requirements-all.txt) ### 🐛...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ### Your current environment The graphics card is Tesla T4, and NVIDIA-SMI 525.105.17 Driver Version: 525.105.17 CUDA Version: 12.0 [pip-requirements-all.txt](https://github.com/user-attachments/files/21133901/pip-requi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: When qwen3-reranker-0.6B is loaded using Tesla T4, the CPU memory continues to grow until the system crashes bug;stale ### Your current environment The graphics card is Tesla T4, and NVIDIA-SMI 525.105.17 Driver...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: lm.py](url) I think it's the distributed parameter: distributed_executor_backend='ray'. This doesn't happen when I load it like this： ``` self.lm = LLM( model=model_name_or_path, # tensor_parallel_size=number_of_gpu, ma...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: xecutor_backend='ray', enforce_eager=True, Gpu_memory_utilization = 0.5, dtype=kwargs.get('dtype', 'float16'), ) ``` enable_prefix_caching is not used, presumably because triton is not yet compatible with T4 ``` import...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
