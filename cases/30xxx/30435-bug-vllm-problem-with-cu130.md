# vllm-project/vllm#30435: [Bug]: vllm problem with cu130

| 字段 | 值 |
| --- | --- |
| Issue | [#30435](https://github.com/vllm-project/vllm/issues/30435) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm problem with cu130

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After successful installation of vllm when I run any command any command, here what I get : \[\e]0;\u@\h: \w\a\]\u@\h:\w$ vllm --help Traceback (most recent call last): File "/opt/conda/bin/vllm", line 5, in from vllm.entrypoints.cli.main import main File "/opt/conda/lib/python3.11/site-packages/vllm/entrypoints/cli/__init__.py", line 3, in from vllm.entrypoints.cli.benchmark.latency import BenchmarkLatencySubcommand File "/opt/conda/lib/python3.11/site-packages/vllm/entrypoints/cli/benchmark/latency.py", line 5, in from vllm.benchmarks.latency import add_cli_args, main File "/opt/conda/lib/python3.11/site-packages/vllm/benchmarks/latency.py", line 17, in from vllm.engine.arg_utils import EngineArgs File "/opt/conda/lib/python3.11/site-packages/vllm/engine/arg_utils.py", line 36, in from vllm.config import ( File "/opt/conda/lib/python3.11/site-packages/vllm/config/__init__.py", line 5, in from vllm.config.compilation import ( File "/opt/conda/lib/python3.11/site-packages/vllm/config/compilation.py", line 18, in from vllm.platforms import current_platform File "/opt/conda/lib/python3.11/site-packages/vllm/platforms/__init__.py",...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ## Your current environment ### 🐛 Describe the bug After successful installation of vllm when I run any command any command, here what I get : \[\e]0;\u@\h: \w\a\]\u@\h:\w$ vllm --help Traceback (most recent call last):...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: entrypoints/cli/__init__.py", line 3, in from vllm.entrypoints.cli.benchmark.latency import BenchmarkLatencySubcommand File "/opt/conda/lib/python3.11/site-packages/vllm/entrypoints/cli/benchmark/latency.py", line 5, in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ^^^^^^^^^ File "/opt/conda/lib/python3.11/site-packages/vllm/platforms/cuda.py", line 16, in import vllm._C # noqa ^^^^^^^^^^^^^^ ImportError: libcudart.so.12: cannot open shared object file: No such file or directory #...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: .11/site-packages/vllm/engine/arg_utils.py", line 36, in from vllm.config import ( File "/opt/conda/lib/python3.11/site-packages/vllm/config/__init__.py", line 5, in from vllm.config.compilation import ( File "/opt/cond...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vllm problem with cu130 bug;stale ### Your current environment ### 🐛 Describe the bug After successful installation of vllm when I run any command any command, here what I get : \[\e]0;\u@\h: \w\a\]\u@\h:\w$ vllm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
