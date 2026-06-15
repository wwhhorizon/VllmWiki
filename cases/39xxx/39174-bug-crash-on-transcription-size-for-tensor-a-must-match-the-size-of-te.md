# vllm-project/vllm#39174: [Bug]: Crash on Transcription (size for tensor a must match the size of tensor b)

| 字段 | 值 |
| --- | --- |
| Issue | [#39174](https://github.com/vllm-project/vllm/issues/39174) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Crash on Transcription (size for tensor a must match the size of tensor b)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Output from console: (EngineCore pid=47271) Process EngineCore: (EngineCore pid=47271) Traceback (most recent call last): (APIServer pid=47229) INFO: 192.168.1.5:46152 - "POST /v1/audio/transcriptions HTTP/1.1" 500 Internal Server Error (EngineCore pid=47271) File "/opt/miniconda3/envs/vllm_nightly/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (EngineCore pid=47271) self.run() (EngineCore pid=47271) File "/opt/miniconda3/envs/vllm_nightly/lib/python3.12/multiprocessing/process.py", line 108, in run (EngineCore pid=47271) self._target(*self._args, **self._kwargs) (EngineCore pid=47271) File "/root/Develop/vllm/vllm/v1/engine/core.py", line 1112, in run_engine_core (EngineCore pid=47271) raise e (EngineCore pid=47271) File "/root/Develop/vllm/vllm/v1/engine/core.py", line 1101, in run_engine_core (EngineCore pid=47271) engine_core.run_busy_loop() (EngineCore pid=47271) File "/root/Develop/vllm/vllm/v1/engine/core.py", line 1142, in run_busy_loop (EngineCore pid=47271) self._process_engine_step() (EngineCore pid=47271) File "/root/Develop/vllm/vllm/v1/engine/core.py", line 1181, in _process_engine_step (EngineC...

## 现有链接修复摘要

#39184 Log warning for scheduled token mismatch

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;ope...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: )) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: (EngineCore pid=47271) outputs, model_executed = self.step_fn() (EngineCore pid=47271) ^^^^^^^^^^^^^^
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: /root/Develop/vllm/vllm/v1/engine/core.py", line 451, in step_with_batch_queue (EngineCore pid=47271) exec_future = self.model_executor.execute_model(
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency;shape #39184 Log warning for scheduled token mismatch Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39184](https://github.com/vllm-project/vllm/pull/39184) | closes_keyword | 0.95 | Log warning for scheduled token mismatch | fix the issue of: - #39174 ## Test Plan Because I'm running on a MacBook, which doesn't have a GPU nor CUDA, I can't run the test normally. Instead I'm running manually. I crea |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
