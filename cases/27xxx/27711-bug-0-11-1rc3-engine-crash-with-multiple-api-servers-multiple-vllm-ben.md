# vllm-project/vllm#27711: [Bug][0.11.1rc3]: Engine crash with multiple API servers + multiple `vllm bench serve` clients

| 字段 | 值 |
| --- | --- |
| Issue | [#27711](https://github.com/vllm-project/vllm/issues/27711) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | shape_align |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][0.11.1rc3]: Engine crash with multiple API servers + multiple `vllm bench serve` clients

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Two conditions for this bug to reproduce (vLLM 0.11.0) 1. API server count > 1 2. `vllm bench serve` client count > 1 For example: ```shell MODEL_PATH="Qwen/Qwen2.5-0.5B-Instruct" MODEL_ID="qw-0.5B" vllm serve "$MODEL_PATH" \ --served-model-name "$MODEL_ID" \ --api-server-count 2 ``` From two different terminals: ```shell MODEL_ID="qw-0.5B" MODEL_PATH="Qwen/Qwen2.5-0.5B-Instruct" vllm bench serve \ --model "$MODEL_PATH" \ --served-model-name "$MODEL_ID" \ ``` Possible errors: 1. ``` (EngineCore_DP0 pid=748303) ERROR 10-28 20:10:56 [v1/engine/core.py:710] File "/home/ray/anaconda3/lib/python3.11/site-packages/vllm/v1/engine/core.py", line 754, in _process_engine_step (EngineCore_DP0 pid=748303) ERROR 10-28 20:10:56 [v1/engine/core.py:710] outputs, model_executed = self.step_fn() (ApiServer_3 pid=748307) INFO: 127.0.0.1:45516 - "POST /v1/completions HTTP/1.1" 200 OK (EngineCore_DP0 pid=748303) ERROR 10-28 20:10:56 [v1/engine/core.py:710] ^^^^^^^^^^^^^^ (ApiServer_15 pid=748319) INFO: 127.0.0.1:48880 - "POST /v1/completions HTTP/1.1" 200 OK (EngineCore_DP0 pid=748303) ERROR 10-28 20:10:56 [v1/engine/core.py:710] File "/home/ray/anac...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: 3.11/site-packages/vllm/v1/engine/core.py", line 325, in step_with_batch_queue (EngineCore_DP0 pid=748303) ERROR 10-28 20:10:56 [v1/engine/core.py:710] scheduler_output = self.scheduler.schedule() (ApiServer_3 pid=74830...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cuda;operator;samp...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: t environment ### 🐛 Describe the bug Two conditions for this bug to reproduce (vLLM 0.11.0) 1. API server count > 1 2. `vllm bench serve` client count > 1 For example: ```shell MODEL_PATH="Qwen/Qwen2.5-0.5B-Instruct" MO...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ore_DP0 pid=748303) ERROR 10-28 20:10:56 [v1/engine/core.py:710] new_blocks = self.kv_cache_manager.allocate_slots( (EngineCore_DP0 pid=748303) ERROR 10-28 20:10:56 [v1/engine/core.py:710] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
