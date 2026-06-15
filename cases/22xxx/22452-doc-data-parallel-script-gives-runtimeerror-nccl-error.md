# vllm-project/vllm#22452: [Doc]: Data Parallel script gives `RuntimeError: NCCL error`

| 字段 | 值 |
| --- | --- |
| Issue | [#22452](https://github.com/vllm-project/vllm/issues/22452) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Doc]: Data Parallel script gives `RuntimeError: NCCL error`

### Issue 正文摘录

### 📚 The doc issue I want to implement data paralle with [doc script](https://docs.vllm.ai/en/v0.10.0/examples/offline_inference/data_parallel.html) But the script return the `NCCL error`: > Traceback (most recent call last): > File "/usr/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap > self.run() > File "/usr/lib/python3.10/multiprocessing/process.py", line 108, in run > self._target(*self._args, **self._kwargs) > File "/root/paddlejob/workspace/env_run/scripts/swift-scripts/intent_chengjiao/dp_debug/vllm_dp.py", line 138, in main > llm = LLM( > File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/llm.py", line 273, in __init__ > self.llm_engine = LLMEngine.from_engine_args( > File "/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py", line 497, in from_engine_args > return engine_cls.from_vllm_config( > File "/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py", line 473, in from_vllm_config > return cls( > File "/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py", line 263, in __init__ > self.model_executor = executor_class(vllm_config=vllm_config) > File "/usr/local/lib/python3.10/dist-packages/vllm/exe...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: local/lib/python3.10/dist-packages/vllm/distributed/device_communicators/cuda_communicator.py", line 50, in __init__ > self.pynccl_comm = PyNcclCommunicator( > File "/usr/local/lib/python3.10/dist-packages/vllm/distribu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ine.py", line 497, in from_engine_args > return engine_cls.from_vllm_config( > File "/usr/local/lib/python3.10/dist-packages/vllm/engine/llm_engine.py", line 473, in from_vllm_config > return cls( > File "/usr/local/lib...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: quently asked questions. development distributed_parallel cuda crash env_dependency 📚 The doc issue
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: oc]: Data Parallel script gives `RuntimeError: NCCL error` documentation;stale ### 📚 The doc issue I want to implement data paralle with [doc script](https://docs.vllm.ai/en/v0.10.0/examples/offline_inference/data_paral...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development distributed_parallel cuda crash env_dependency 📚 The doc issue

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
