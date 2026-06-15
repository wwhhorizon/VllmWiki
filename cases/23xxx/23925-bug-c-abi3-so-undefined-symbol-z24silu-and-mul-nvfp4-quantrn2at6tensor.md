# vllm-project/vllm#23925: [Bug]: _C.abi3.so: undefined symbol: _Z24silu_and_mul_nvfp4_quantRN2at6TensorES1_S1_S1_

| 字段 | 值 |
| --- | --- |
| Issue | [#23925](https://github.com/vllm-project/vllm/issues/23925) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: _C.abi3.so: undefined symbol: _Z24silu_and_mul_nvfp4_quantRN2at6TensorES1_S1_S1_

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I build vllm from source, however, when I start a server, error happens as below: ```bash nohup: ignoring input INFO 08-29 17:41:42 [__init__.py:241] Automatically detected platform cuda. Traceback (most recent call last): File "/root/paddlejob/workspace/env_run/xuruihao/miniconda3/envs/vllm/bin/vllm", line 4, in from vllm.entrypoints.cli.main import main File "/root/paddlejob/workspace/env_run/xuruihao/projects/vllm/vllm/entrypoints/cli/__init__.py", line 3, in from vllm.entrypoints.cli.benchmark.latency import BenchmarkLatencySubcommand File "/root/paddlejob/workspace/env_run/xuruihao/projects/vllm/vllm/entrypoints/cli/benchmark/latency.py", line 5, in from vllm.benchmarks.latency import add_cli_args, main File "/root/paddlejob/workspace/env_run/xuruihao/projects/vllm/vllm/benchmarks/latency.py", line 18, in from vllm.engine.arg_utils import EngineArgs File "/root/paddlejob/workspace/env_run/xuruihao/projects/vllm/vllm/engine/arg_utils.py", line 24, in from vllm.config import (BlockSize, CacheConfig, CacheDType, CompilationConfig, File "/root/paddlejob/workspace/env_run/xuruihao/projects/vllm/vllm/config/__init__.py", line 36,...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: _C.abi3.so: undefined symbol: _Z24silu_and_mul_nvfp4_quantRN2at6TensorES1_S1_S1_ bug;stale ### Your current environment ### 🐛 Describe the bug I build vllm from source, however, when I start a server, error happe...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: _C.abi3.so: undefined symbol: _Z24silu_and_mul_nvfp4_quantRN2at6TensorES1_S1_S1_ bug;stale ### Your current environment ### 🐛 Describe the bug I build vllm from source, however, when I start a server, error happe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: entrypoints/cli/__init__.py", line 3, in from vllm.entrypoints.cli.benchmark.latency import BenchmarkLatencySubcommand File "/root/paddlejob/workspace/env_run/xuruihao/projects/vllm/vllm/entrypoints/cli/benchmark/latenc...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: , line 36, in from vllm.config.parallel import (DistributedExecutorBackend, EPLBConfig, File "/root/paddlejob/workspace/env_run/xuruihao/projects/vllm/vllm/config/parallel.py", line 17, in from vllm.platforms import cur...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ut INFO 08-29 17:41:42 [__init__.py:241] Automatically detected platform cuda. Traceback (most recent call last): File "/root/paddlejob/workspace/env_run/xuruihao/miniconda3/envs/vllm/bin/vllm", line 4, in from vllm.ent...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23926: Should have ROCm label: NO (0 matches) #23925: Should have ROCm label: NO (0 matches) #23923: Should have ROCm label: NO (0 matches) #23922: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
