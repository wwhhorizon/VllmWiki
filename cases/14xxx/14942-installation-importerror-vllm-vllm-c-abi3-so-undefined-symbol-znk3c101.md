# vllm-project/vllm#14942: [Installation]: ImportError: vllm/vllm/_C.abi3.so: undefined symbol: _ZNK3c1011StorageImpl27throw_data_ptr_access_errorEv

| 字段 | 值 |
| --- | --- |
| Issue | [#14942](https://github.com/vllm-project/vllm/issues/14942) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | crash;import_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: ImportError: vllm/vllm/_C.abi3.so: undefined symbol: _ZNK3c1011StorageImpl27throw_data_ptr_access_errorEv

### Issue 正文摘录

### Your current environment ```text Collecting environment information... INFO 03-17 17:16:30 [__init__.py:256] Automatically detected platform cuda. Traceback (most recent call last): File "/mnt/workspace/sea/longli/Latent_RL/collect_env.py", line 765, in main() File "/mnt/workspace/sea/longli/Latent_RL/collect_env.py", line 744, in main output = get_pretty_env_info() ^^^^^^^^^^^^^^^^^^^^^ File "/mnt/workspace/sea/longli/Latent_RL/collect_env.py", line 739, in get_pretty_env_info return pretty_str(get_env_info()) ^^^^^^^^^^^^^^ File "/mnt/workspace/sea/longli/Latent_RL/collect_env.py", line 568, in get_env_info vllm_version = get_vllm_version() ^^^^^^^^^^^^^^^^^^ File "/mnt/workspace/sea/longli/Latent_RL/collect_env.py", line 273, in get_vllm_version from vllm import __version__, __version_tuple__ File "/mnt/workspace/sea/longli/vllm/vllm/__init__.py", line 11, in from vllm.engine.arg_utils import AsyncEngineArgs, EngineArgs File "/mnt/workspace/sea/longli/vllm/vllm/engine/arg_utils.py", line 21, in from vllm.executor.executor_base import ExecutorBase File "/mnt/workspace/sea/longli/vllm/vllm/executor/executor_base.py", line 16, in from vllm.model_executor.layers.sampler import...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Installation]: ImportError: vllm/vllm/_C.abi3.so: undefined symbol: _ZNK3c1011StorageImpl27throw_data_ptr_access_errorEv installation ### Your current environment ```text Collecting environment information... INFO 03-17
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .. INFO 03-17 17:16:30 [__init__.py:256] Automatically detected platform cuda. Traceback (most recent call last): File "/mnt/workspace/sea/longli/Latent_RL/collect_env.py", line 765, in main() File "/mnt/workspace/sea/l...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tallation ### Your current environment ```text Collecting environment information... INFO 03-17 17:16:30 [__init__.py:256] Automatically detected platform cuda. Traceback (most recent call last): File "/mnt/workspace/se...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: vllm/model_executor/layers/sampler.py", line 23, in from vllm.spec_decode.metrics import SpecDecodeWorkerMetrics File "/mnt/workspace/sea/longli/vllm/vllm/spec_decode/metrics.py", line 9, in from vllm.model_executor.lay...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build cuda crash;import_error Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
