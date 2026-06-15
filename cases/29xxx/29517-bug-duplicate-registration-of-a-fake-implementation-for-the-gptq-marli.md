# vllm-project/vllm#29517: [Bug]: Duplicate registration of a fake implementation for the gptq_marlin_repack operator causing vllm serve to fail.

| 字段 | 值 |
| --- | --- |
| Issue | [#29517](https://github.com/vllm-project/vllm/issues/29517) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Duplicate registration of a fake implementation for the gptq_marlin_repack operator causing vllm serve to fail.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug A duplicate registration was added, a Python @register_fake for gptq_marlin_repack when the C++ code already provides a Meta implementation. While doing a normal VLLM serve, I faced this issue where it threw me this error. ``` Traceback (most recent call last): File "/home/ubuntu/contribute/vllm/.venv/bin/vllm", line 4, in from vllm.entrypoints.cli.main import main File "/home/ubuntu/contribute/vllm/vllm/entrypoints/cli/__init__.py", line 3, in from vllm.entrypoints.cli.benchmark.latency import BenchmarkLatencySubcommand File "/home/ubuntu/contribute/vllm/vllm/entrypoints/cli/benchmark/latency.py", line 5, in from vllm.benchmarks.latency import add_cli_args, main File "/home/ubuntu/contribute/vllm/vllm/benchmarks/latency.py", line 17, in from vllm.engine.arg_utils import EngineArgs File "/home/ubuntu/contribute/vllm/vllm/engine/arg_utils.py", line 35, in from vllm.attention.backends.registry import AttentionBackendEnum File "/home/ubuntu/contribute/vllm/vllm/attention/__init__.py", line 4, in from vllm.attention.backends.abstract import ( File "/home/ubuntu/contribute/vllm/vllm/attention/backends/abstract.py", line 9, in from vll...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: te/vllm/.venv/bin/vllm", line 4, in from vllm.entrypoints.cli.main import main File "/home/ubuntu/contribute/vllm/vllm/entrypoints/cli/__init__.py", line 3, in from vllm.entrypoints.cli.benchmark.latency import Benchmar...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: te/vllm/vllm/engine/arg_utils.py", line 35, in from vllm.attention.backends.registry import AttentionBackendEnum File "/home/ubuntu/contribute/vllm/vllm/attention/__init__.py", line 4, in from vllm.attention.backends.ab...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: entrypoints/cli/__init__.py", line 3, in from vllm.entrypoints.cli.benchmark.latency import BenchmarkLatencySubcommand File "/home/ubuntu/contribute/vllm/vllm/entrypoints/cli/benchmark/latency.py", line 5, in from vllm....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ine 25, in from vllm.model_executor.layers.utils import dispatch_unquantized_gemm File "/home/ubuntu/contribute/vllm/vllm/model_executor/layers/utils.py", line 9, in from vllm import _custom_ops as ops File "/home/ubunt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: r examination, I discovered that a C++ implementation already exists for CUDA as well as Meta, so we don't require a fake, which was the case with `gptq_marlin_gemm`. I have tested it post-removing the duplicate code, a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
