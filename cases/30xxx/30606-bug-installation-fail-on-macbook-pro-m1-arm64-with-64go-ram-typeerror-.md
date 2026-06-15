# vllm-project/vllm#30606: [Bug]: Installation fail on Macbook Pro M1 ARM64 with 64Go RAM: TypeError: unsupported operand type(s) for |: 'type' and 'NoneType'

| 字段 | 值 |
| --- | --- |
| Issue | [#30606](https://github.com/vllm-project/vllm/issues/30606) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;hardware_porting |
| 子分类 | latency_reg |
| Operator 关键词 | cuda |
| 症状 | build_error;crash;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Installation fail on Macbook Pro M1 ARM64 with 64Go RAM: TypeError: unsupported operand type(s) for \|: 'type' and 'NoneType'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug following the process to install mistral locally: https://docs.mistral.ai/mistral-vibe/local it fail during the vllm installation ``` # vllm serve mistralai/Devstral-Small-2-24B-Instruct-2512 --tool-call-parser mistral --enable-auto-tool-choice --port 8080 INFO 12-13 11:30:12 [__init__.py:216] Automatically detected platform cpu. Traceback (most recent call last): File "/Users/smerle/.asdf/installs/python/3.9.18/bin/vllm", line 5, in from vllm.entrypoints.cli.main import main File "/Users/smerle/.asdf/installs/python/3.9.18/lib/python3.9/site-packages/vllm/entrypoints/cli/__init__.py", line 3, in from vllm.entrypoints.cli.benchmark.latency import BenchmarkLatencySubcommand File "/Users/smerle/.asdf/installs/python/3.9.18/lib/python3.9/site-packages/vllm/entrypoints/cli/benchmark/latency.py", line 5, in from vllm.benchmarks.latency import add_cli_args, main File "/Users/smerle/.asdf/installs/python/3.9.18/lib/python3.9/site-packages/vllm/benchmarks/latency.py", line 18, in from vllm.engine.arg_utils import EngineArgs File "/Users/smerle/.asdf/installs/python/3.9.18/lib/python3.9/site-packages/vllm/engine/arg_utils.py", line 42, in...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Installation fail on Macbook Pro M1 ARM64 with 64Go RAM: TypeError: unsupported operand type(s) for |: 'type' and 'NoneType' bug;stale ### Your current environment ### 🐛 Describe the bug following the process to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: fail during the vllm installation ``` # vllm serve mistralai/Devstral-Small-2-24B-Instruct-2512 --tool-call-parser mistral --enable-auto-tool-choice --port 8080 INFO 12-13 11:30:12 [__init__.py:216] Automatically detect...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: entrypoints/cli/__init__.py", line 3, in from vllm.entrypoints.cli.benchmark.latency import BenchmarkLatencySubcommand File "/Users/smerle/.asdf/installs/python/3.9.18/lib/python3.9/site-packages/vllm/entrypoints/cli/be...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: te-packages/vllm/entrypoints/chat_utils.py", line 48, in from vllm.model_executor.models import SupportsMultiModal File "/Users/smerle/.asdf/installs/python/3.9.18/lib/python3.9/site-packages/vllm/model_executor/models/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: TypeError: unsupported operand type(s) for |: 'type' and 'NoneType' bug;stale ### Your current environment ### 🐛 Describe the bug following the process to install mistral locally: https://docs.mistral.ai/mistral-vibe/lo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
