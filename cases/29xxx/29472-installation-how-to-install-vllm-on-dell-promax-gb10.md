# vllm-project/vllm#29472: [Installation]: how to Install vllm on dell promax gb10

| 字段 | 值 |
| --- | --- |
| Issue | [#29472](https://github.com/vllm-project/vllm/issues/29472) |
| 状态 | open |
| 标签 | installation;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;gemm_linear |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda |
| 症状 | build_error;crash;import_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: how to Install vllm on dell promax gb10

### Issue 正文摘录

### Your current environment I failed to install vllm on dell promax gb10 , mesages as followed nvcc --version nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2025 NVIDIA Corporation Built on Wed_Aug_20_01:57:39_PM_PDT_2025 Cuda compilation tools, release 13.0, V13.0.88 Build cuda_13.0.r13.0/compiler.36424714_0 pip install vllm Successfully installed torch-2.9.0 torchaudio-2.9.0 torchvision-0.24.0 vllm-0.11.2 ``` (py312) dell@promaxgb10-0843:~/test/vllm/Qwen$ vllm -V Traceback (most recent call last): File "/home/dell/miniconda3/envs/py312/bin/vllm", line 3, in from vllm.entrypoints.cli.main import main File "/home/dell/miniconda3/envs/py312/lib/python3.12/site-packages/vllm/entrypoints/cli/__init__.py", line 3, in from vllm.entrypoints.cli.benchmark.latency import BenchmarkLatencySubcommand File "/home/dell/miniconda3/envs/py312/lib/python3.12/site-packages/vllm/entrypoints/cli/benchmark/latency.py", line 5, in from vllm.benchmarks.latency import add_cli_args, main File "/home/dell/miniconda3/envs/py312/lib/python3.12/site-packages/vllm/benchmarks/latency.py", line 17, in from vllm.engine.arg_utils import EngineArgs File "/home/dell/miniconda3/envs/py312/lib/python3.12/s...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Installation]: how to Install vllm on dell promax gb10 installation;stale ### Your current environment I failed to install vllm on dell promax gb10 , mesages as followed nvcc --version nvcc: NVIDIA (R) Cuda compiler dr
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: 2.9.0 torchvision-0.24.0 vllm-0.11.2 ``` (py312) dell@promaxgb10-0843:~/test/vllm/Qwen$ vllm -V Traceback (most recent call last): File "/home/dell/miniconda3/envs/py312/bin/vllm", line 3, in from vllm.entrypoints.cli.m...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: dell promax gb10 , mesages as followed nvcc --version nvcc: NVIDIA (R) Cuda compiler driver Copyright (c) 2005-2025 NVIDIA Corporation Built on Wed_Aug_20_01:57:39_PM_PDT_2025 Cuda compilation tools, release 13.0, V13.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: hvision-0.24.0 vllm-0.11.2 ``` (py312) dell@promaxgb10-0843:~/test/vllm/Qwen$ vllm -V Traceback (most recent call last): File "/home/dell/miniconda3/envs/py312/bin/vllm", line 3, in from vllm.entrypoints.cli.main import...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ackages/vllm/engine/arg_utils.py", line 35, in from vllm.attention.backends.registry import AttentionBackendEnum File "/home/dell/miniconda3/envs/py312/lib/python3.12/site-packages/vllm/attention/__init__.py", line 4, i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
