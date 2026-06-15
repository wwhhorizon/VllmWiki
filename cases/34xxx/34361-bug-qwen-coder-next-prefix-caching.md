# vllm-project/vllm#34361: [Bug]: Qwen Coder Next prefix caching

| 字段 | 值 |
| --- | --- |
| Issue | [#34361](https://github.com/vllm-project/vllm/issues/34361) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen Coder Next prefix caching

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug VLLM crashes with error ``` (EngineCore_DP0 pid=2525901) ERROR 02-11 20:37:49 [core.py:1008] EngineCore encountered a fatal error. (EngineCore_DP0 pid=2525901) ERROR 02-11 20:37:49 [core.py:1008] Traceback (most recent call last): (EngineCore_DP0 pid=2525901) ERROR 02-11 20:37:49 [core.py:1008] File "/home/gleb/llm/env_vllm/lib/python3.13/site-packages/vllm/v1/engine/core.py", line 999, in run_engine_core (EngineCore_DP0 pid=2525901) ERROR 02-11 20:37:49 [core.py:1008] engine_core.run_busy_loop() (EngineCore_DP0 pid=2525901) ERROR 02-11 20:37:49 [core.py:1008] ~~~~~~~~~~~~~~~~~~~~~~~~~^^ (EngineCore_DP0 pid=2525901) ERROR 02-11 20:37:49 [core.py:1008] File "/home/gleb/llm/env_vllm/lib/python3.13/site-packages/vllm/v1/engine/core.py", line 1026, in run_busy_loop (EngineCore_DP0 pid=2525901) ERROR 02-11 20:37:49 [core.py:1008] self._process_engine_step() (EngineCore_DP0 pid=2525901) ERROR 02-11 20:37:49 [core.py:1008] ~~~~~~~~~~~~~~~~~~~~~~~~~^^ (EngineCore_DP0 pid=2525901) ERROR 02-11 20:37:49 [core.py:1008] File "/home/gleb/llm/env_vllm/lib/python3.13/site-packages/vllm/v1/engine/core.py", line 1060, in _process_engine_step (Engi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cuda;o...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: (EngineCore_DP0 pid=2525901) ERROR 02-11 20:37:49 [core.py:1008] new_blocks = self.kv_cache_manager.allocate_slots( (EngineCore_DP0 pid=2525901) ERROR 02-11 20:37:49 [core.py:1008] request, (EngineCore_DP0 pid=2525901)...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: tep (EngineCore_DP0 pid=2525901) ERROR 02-11 20:37:49 [core.py:1008] scheduler_output = self.scheduler.schedule() (EngineCore_DP0 pid=2525901) ERROR 02-11 20:37:49 [core.py:1008] File "/home/gleb/llm/env_vllm/lib/python...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 387 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen Coder Next prefix caching bug ### Your current environment ### 🐛 Describe the bug VLLM crashes with error ``` (EngineCore_DP0 pid=2525901) ERROR 02-11 20:37:49 [core.py:1008] EngineCore encountered a fatal e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
