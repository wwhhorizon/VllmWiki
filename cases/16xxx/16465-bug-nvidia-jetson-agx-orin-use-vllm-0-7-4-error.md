# vllm-project/vllm#16465: [Bug]: NVIDIA Jetson AGX Orin use vllm-0.7.4 error

| 字段 | 值 |
| --- | --- |
| Issue | [#16465](https://github.com/vllm-project/vllm/issues/16465) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NVIDIA Jetson AGX Orin use vllm-0.7.4 error

### Issue 正文摘录

### Your current environment ``` ~# python3 collect_env.py INFO 04-11 16:49:01 [__init__.py:256] Automatically detected platform cuda. Traceback (most recent call last): File "/root/collect_env.py", line 17, in from vllm.envs import environment_variables File "/usr/local/lib/python3.10/dist-packages/vllm/__init__.py", line 11, in from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs File "/usr/local/lib/python3.10/dist-packages/vllm/engine/arg_utils.py", line 21, in from vllm.executor.executor_base import ExecutorBase File "/usr/local/lib/python3.10/dist-packages/vllm/executor/executor_base.py", line 16, in from vllm.model_executor.layers.sampler import SamplerOutput File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/sampler.py", line 23, in from vllm.spec_decode.metrics import SpecDecodeWorkerMetrics File "/usr/local/lib/python3.10/dist-packages/vllm/spec_decode/metrics.py", line 9, in from vllm.model_executor.layers.spec_decode_base_sampler import ( File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/spec_decode_base_sampler.py", line 10, in from vllm.platforms import current_platform File "/usr/local/lib/python3.10/dist-package...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: l last): File "/root/collect_env.py", line 17, in from vllm.envs import environment_variables File "/usr/local/lib/python3.10/dist-packages/vllm/__init__.py", line 11, in from vllm.engine.arg_utils import AsyncEngineArg...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: y INFO 04-11 16:49:01 [__init__.py:256] Automatically detected platform cuda. Traceback (most recent call last): File "/root/collect_env.py", line 17, in from vllm.envs import environment_variables File "/usr/local/lib/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: NVIDIA Jetson AGX Orin use vllm-0.7.4 error bug;stale ### Your current environment ``` ~# python3 collect_env.py INFO 04-11 16:49:01 [__init__.py:256] Automatically detected platform cuda. Traceback (most recent...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: st-packages/vllm/executor/executor_base.py", line 16, in from vllm.model_executor.layers.sampler import SamplerOutput File "/usr/local/lib/python3.10/dist-packages/vllm/model_executor/layers/sampler.py", line 23, in fro...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development model_support cuda crash;import_error env_dependency Your current environ...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
