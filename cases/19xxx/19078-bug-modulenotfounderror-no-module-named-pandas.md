# vllm-project/vllm#19078: [Bug]: ModuleNotFoundError: No module named 'pandas'

| 字段 | 值 |
| --- | --- |
| Issue | [#19078](https://github.com/vllm-project/vllm/issues/19078) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ModuleNotFoundError: No module named 'pandas'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Install** ``` VLLM_USE_PRECOMPILED=1 uv pip install --editable . ``` **ModuleNotFoundError: No module named 'pandas'** in main `0.9.1.dev382+g5bc1ad6ce.d20250603.precompiled`. ``` (workspace) root@nodedev:/workspace# vllm --help INFO 06-03 19:25:55 [__init__.py:243] Automatically detected platform cuda. Traceback (most recent call last): File "/workspace/.venv/bin/vllm", line 4, in from vllm.entrypoints.cli.main import main File "/workspace/vllm/vllm/entrypoints/cli/main.py", line 7, in import vllm.entrypoints.cli.benchmark.main File "/workspace/vllm/vllm/entrypoints/cli/benchmark/main.py", line 5, in import vllm.entrypoints.cli.benchmark.serve File "/workspace/vllm/vllm/entrypoints/cli/benchmark/serve.py", line 4, in from vllm.benchmarks.serve import add_cli_args, main File "/workspace/vllm/vllm/benchmarks/serve.py", line 34, in from vllm.benchmarks.datasets import (AIMODataset, ASRDataset, BurstGPTDataset, File "/workspace/vllm/vllm/benchmarks/datasets.py", line 26, in import pandas as pd ModuleNotFoundError: No module named 'pandas' ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant is...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: d 'pandas' bug ### Your current environment ### 🐛 Describe the bug **Install** ``` VLLM_USE_PRECOMPILED=1 uv pip install --editable . ``` **ModuleNotFoundError: No module named 'pandas'** in main `0.9.1.dev382+g5bc1ad6c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: lp INFO 06-03 19:25:55 [__init__.py:243] Automatically detected platform cuda. Traceback (most recent call last): File "/workspace/.venv/bin/vllm", line 4, in from vllm.entrypoints.cli.main import main File "/workspace/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: m/entrypoints/cli/main.py", line 7, in import vllm.entrypoints.cli.benchmark.main File "/workspace/vllm/vllm/entrypoints/cli/benchmark/main.py", line 5, in import vllm.entrypoints.cli.benchmark.serve File "/workspace/vl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash;import_error env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ed questions. performance ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash;import_error env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
