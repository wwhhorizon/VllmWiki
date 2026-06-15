# vllm-project/vllm#17966: [Bug]: import TypedDict from typing does not work for python<3.12

| 字段 | 值 |
| --- | --- |
| Issue | [#17966](https://github.com/vllm-project/vllm/issues/17966) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: import TypedDict from typing does not work for python<3.12

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Launching openai serving engine will face the issue: ``` ... File "/home/xxx/rh/vllm/vllm/entrypoints/cli/main.py", line 7, in import vllm.entrypoints.cli.benchmark.main File "/home/xxx/rh/vllm/vllm/entrypoints/cli/benchmark/main.py", line 6, in import vllm.entrypoints.cli.benchmark.throughput File "/home/xxx/rh/vllm/vllm/entrypoints/cli/benchmark/throughput.py", line 4, in from vllm.benchmarks.throughput import add_cli_args, main File "/home/xxx/rh/vllm/vllm/benchmarks/throughput.py", line 26, in from vllm.entrypoints.openai.api_server import ( File "/home/xxx/rh/vllm/vllm/entrypoints/openai/api_server.py", line 75, in from vllm.entrypoints.openai.serving_chat import OpenAIServingChat File "/home/xxx/rh/vllm/vllm/entrypoints/openai/serving_chat.py", line 29, in from vllm.entrypoints.openai.serving_engine import (OpenAIServing, File "/home/xxx/rh/vllm/vllm/entrypoints/openai/serving_engine.py", line 102, in class RequestProcessingMixin(BaseModel): ... pydantic.errors.PydanticUserError: Please use typing_extensions.TypedDict instead of typing.TypedDict on Python = 3.12 or `typing_extensions` for python < 3.12. ### Before submittin...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: import TypedDict from typing does not work for python<3.12 bug ### Your current environment ### 🐛 Describe the bug Launching openai serving engine will face the issue: ``` ... File "/home/xxx/rh/vllm/vllm/entrypo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: m/entrypoints/cli/main.py", line 7, in import vllm.entrypoints.cli.benchmark.main File "/home/xxx/rh/vllm/vllm/entrypoints/cli/benchmark/main.py", line 6, in import vllm.entrypoints.cli.benchmark.throughput File "/home/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 12. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: vllm/vllm/entrypoints/openai/serving_engine.py", line 102, in class RequestProcessingMixin(BaseModel): ... pydantic.errors.PydanticUserError: Please use typing_extensions.TypedDict instead of typing.TypedDict on Python...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf;slowdown env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
