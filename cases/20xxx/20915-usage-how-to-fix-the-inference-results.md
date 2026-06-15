# vllm-project/vllm#20915: [Usage]: How to fix the inference results?

| 字段 | 值 |
| --- | --- |
| Issue | [#20915](https://github.com/vllm-project/vllm/issues/20915) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;sampling |
| 症状 | build_error;import_error;nondeterministic |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to fix the inference results?

### Issue 正文摘录

### Your current environment ```text Your output of `python collect_env.py` here ``` ### How would you like to use vllm I use [ais_bench](https://gitee.com/aisbench/benchmark) to evaluate the model inference results, but the score was different each time. How to fix the inference results? **vllm version**: vllm v0.9.1 (python use_existing_torch.py, pip install --no-build-isolation -v -e .) **score**(run 5 times): aime2024: 23.33/20.00/26.67/13.33/16.67 math500: 71.00/71.40/72.00/73.00/70.20 livecodebench: 17.16/16.79/16.42/16.79/16.04 I fix the results in the following way: **env**： ```shell export CUDA_VISIBLE_DEVICES=4,5,6,7 export VLLM_USE_V1=1 export VLLM_VERSION=0.9.1 export LCCL_DETERMINISTIC=1 export NCCL_DETERMINISTIC=1 ``` **seed_all**： Add the following code at the beginning of the `vllm/vllm/entrypoints/llm.py` and `vllm/vllm/entrypoints/openai/api_server.py` files: ```python import os import random import numpy as np import torch from packaging import version try: import torch_npu except ImportError: is_gpu = True else: is_gpu = False def seed_all(seed=1234, mode=False): try: random.seed(seed) os.environ['PYTHONHASHSEED'] = str(seed) np.random.seed(seed) torch.manual_s...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: score was different each time. How to fix the inference results? **vllm version**: vllm v0.9.1 (python use_existing_torch.py, pip install --no-build-isolation -v -e .) **score**(run 5 times): aime2024: 23.33/20.00/26.67...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: would you like to use vllm I use [ais_bench](https://gitee.com/aisbench/benchmark) to evaluate the model inference results, but the score was different each time. How to fix the inference results? **vllm version**: vllm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: I use [ais_bench](https://gitee.com/aisbench/benchmark) to evaluate the model inference results, but the score was different each time. How to fix the inference results? **vllm version**: vllm v0.9.1 (python use_existin...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: VICES=4,5,6,7 export VLLM_USE_V1=1 export VLLM_VERSION=0.9.1 export LCCL_DETERMINISTIC=1 export NCCL_DETERMINISTIC=1 ``` **seed_all**： Add the following code at the beginning of the `vllm/vllm/entrypoints/llm.py` and `v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 6.04 I fix the results in the following way: **env**： ```shell export CUDA_VISIBLE_DEVICES=4,5,6,7 export VLLM_USE_V1=1 export VLLM_VERSION=0.9.1 export LCCL_DETERMINISTIC=1 export NCCL_DETERMINISTIC=1 ``` **seed_all**：...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
