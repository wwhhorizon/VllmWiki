# vllm-project/vllm#23662: [Bug]:  RuntimeError: operator _C::marlin_qqq_gemm does not exist

| 字段 | 值 |
| --- | --- |
| Issue | [#23662](https://github.com/vllm-project/vllm/issues/23662) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  RuntimeError: operator _C::marlin_qqq_gemm does not exist

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` nvidia-smi ``` Wed Aug 27 20:18:39 2025 +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 575.64.03 Driver Version: 575.64.03 CUDA Version: 12.9 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+========================+======================| | 0 NVIDIA GeForce RTX 3090 Off | 00000000:32:00.0 Off | N/A | | 0% 29C P8 35W / 420W | 11MiB / 24576MiB | 0% Default | | | | N/A | +-----------------------------------------+------------------------+----------------------+ | 1 NVIDIA GeForce RTX 3090 Off | 00000000:98:00.0 Off | N/A | | 97% 25C P8 44W / 420W | 11MiB / 24576MiB | 0% Default | | | | N/A | +-----------------------------------------+------------------------+----------------------+ +-----------------------------------------------------------------------------------------+ | Processes: | | GPU GI CI PID Type Process name GPU Memory | | ID...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ----------------------------+ | NVIDIA-SMI 575.64.03 Driver Version: 575.64.03 CUDA Version: 12.9 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M |...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: tale ### Your current environment ### 🐛 Describe the bug ``` nvidia-smi ``` Wed Aug 27 20:18:39 2025 +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 575.64.03 Dri...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ) main ``` VLLM_USE_PRECOMPILED=1 uv pip install --editable . --torch-backend="cu128" ``` ``` pip show torch ``` Name: torch Version: 2.7.1+cu128 Summary: Tensors and Dynamic neural networks in Python with strong GPU ac...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: roughput and memory-efficient inference and serving engine for LLMs ``` HF_ENDPOINT=https://hf-mirror.com torchrun --nproc-per-node=1 torchrun_example.py ``` ```text DEBUG 08-27 20:07:41 [__init__.py:30] No plugins for...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: RuntimeError: operator _C::marlin_qqq_gemm does not exist bug;stale ### Your current environment ### 🐛 Describe the bug ``` nvidia-smi ``` Wed Aug 27 20:18:39 2025 +-----------------------------------------------...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23667: Should have ROCm label: NO (0 matches) #23662: Should have ROCm label: NO (0 matches) #23661: Should have ROCm label: NO (0 matches) #23655: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
