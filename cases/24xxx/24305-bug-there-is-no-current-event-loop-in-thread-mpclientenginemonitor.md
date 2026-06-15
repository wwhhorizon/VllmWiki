# vllm-project/vllm#24305: [Bug]: There is no current event loop in thread 'MPClientEngineMonitor'

| 字段 | 值 |
| --- | --- |
| Issue | [#24305](https://github.com/vllm-project/vllm/issues/24305) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: There is no current event loop in thread 'MPClientEngineMonitor'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When EngineCore process crash, APIServer cannot stop, because `loop = self.output_socket._get_loop()` this line code cannot running. ``` (APIServer pid=215332) ERROR 09-05 01:15:59 [core_client.py:562] Engine core proc EngineCore_0 died unexpectedly, shutting down client. (APIServer pid=215332) /usr/lib/python3.12/weakref.py:590: RuntimeWarning: No running event loop. zmq.asyncio should be used from within an asyncio loop. (APIServer pid=215332) return info.func(*info.args, **(info.kwargs or {})) (APIServer pid=215332) Exception in thread MPClientEngineMonitor: (APIServer pid=215332) Traceback (most recent call last): (APIServer pid=215332) File "/usr/lib/python3.12/threading.py", line 1075, in _bootstrap_inner (APIServer pid=215332) self.run() (APIServer pid=215332) File "/usr/lib/python3.12/threading.py", line 1012, in run (APIServer pid=215332) self._target(*self._args, **self._kwargs) (APIServer pid=215332) File "/root/code/vllm/vllm/v1/engine/core_client.py", line 565, in monitor_engine_cores (APIServer pid=215332) _self.shutdown() (APIServer pid=215332) File "/root/code/vllm/vllm/v1/engine/core_client.py", line 517, in shut...

## 现有链接修复摘要

#24422 [Bugfix] Fix 'no event loop' RuntimeError in MPClientEngineMonitor

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ython3.12/weakref.py:590: RuntimeWarning: No running event loop. zmq.asyncio should be used from within an asyncio loop. (APIServer pid=215332) return info.func(*info.args, **(info.kwargs or {})) (APIServer pid=215332)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency #24422 [Bugfix] Fix 'no event loop' RuntimeError in MPClientEngineMonitor Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: . correctness ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency #24422 [Bugfix] Fix 'no...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: of frequently asked questions. correctness ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_depend...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#24422](https://github.com/vllm-project/vllm/pull/24422) | closes_keyword | 0.95 | [Bugfix] Fix 'no event loop' RuntimeError in MPClientEngineMonitor | Resolves #24230 #24305 ## Test Plan 1. Run any model - In my Case: Llama-3.1-8B-Instruct ``` uv run vllm serve meta-llama/Llama-3.1-8B-Instruct --tool-call-parser llama3_json --c |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
