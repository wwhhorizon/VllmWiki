# vllm-project/vllm#20484: [Bug]: Since  #18437 can't serve any Dual Chunked attention model

| 字段 | 值 |
| --- | --- |
| Issue | [#20484](https://github.com/vllm-project/vllm/issues/20484) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Since  #18437 can't serve any Dual Chunked attention model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Since commit 5d6d1adf15aca59cb135853d0f11308af4bbd6e3 and PR #18437 Using Dual Chunked Attention with Qwen 1M makes the first prompt request hangs and crashes the `vllm serve` server. ```txt INFO 07-04 11:32:50 [engine.py:317] Added request chatcmpl-0ff807c9e8744e56b2e69fb3687499a6. ERROR 07-04 11:33:12 [client.py:307] RuntimeError('Engine process (pid 3607156) died.') ERROR 07-04 11:33:12 [client.py:307] NoneType: None INFO: Shutting down INFO: Waiting for connections to close. (CTRL+C to force quit) ERROR 07-04 11:33:15 [serving_chat.py:897] Error in chat completion stream generator. ERROR 07-04 11:33:15 [serving_chat.py:897] Traceback (most recent call last): ERROR 07-04 11:33:15 [serving_chat.py:897] File "/home/pierre/idextend/vllm_repo/vllm/entrypoints/openai/serving_chat.py", line 481, in chat_completion_stream_generator ERROR 07-04 11:33:15 [serving_chat.py:897] async for res in result_generator: ERROR 07-04 11:33:15 [serving_chat.py:897] File "/home/pierre/idextend/vllm_repo/vllm/engine/multiprocessing/client.py", line 671, in _process_request ERROR 07-04 11:33:15 [serving_chat.py:897] raise request_output ERROR 07-04 11...

## 现有链接修复摘要

#18437 [KERNEL] Sampler. CUDA kernel for applying repetition penalty | #20488 fix crash when empty sequence is sent to cuda penalty kernel

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding attention;cuda;operator;sampling;tr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: 18437 Using Dual Chunked Attention with Qwen 1M makes the first prompt request hangs and crashes the `vllm serve` server. ```txt INFO 07-04 11:32:50 [engine.py:317] Added request chatcmpl-0ff807c9e8744e56b2e69fb3687499a...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: `VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 CUDA_VISIBLE_DEVICES=1,2 VLLM_ATTENTION_BACKEND=DUAL_CHUNK_FLASH_ATTN vllm serve Qwen/Qwen2.5-7B-Instruct-1M --max-model-len 140000 --max-num-seqs 1 --port 2483 --enforce-eager --gpu-mem...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Finished server process [3607080] ``` `VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 CUDA_VISIBLE_DEVICES=1,2 VLLM_ATTENTION_BACKEND=DUAL_CHUNK_FLASH_ATTN vllm serve Qwen/Qwen2.5-7B-Instruct-1M --max-model-len 140000 --max-num-seqs 1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Since #18437 can't serve any Dual Chunked attention model bug ### Your current environment ### 🐛 Describe the bug Since commit 5d6d1adf15aca59cb135853d0f11308af4bbd6e3 and PR #18437 Using Dual Chunked Attention w...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#18437](https://github.com/vllm-project/vllm/pull/18437) | mentioned | 0.45 | [KERNEL] Sampler. CUDA kernel for applying repetition penalty | the bug since commit 5d6d1adf15aca59cb135853d0f11308af4bbd6e3 and pr #18437 using dual chunked attention with qwen 1m makes the first prompt request hangs and crashes the `vllm se… |
| [#20488](https://github.com/vllm-project/vllm/pull/20488) | closes_keyword | 0.95 | fix crash when empty sequence is sent to cuda penalty kernel | Fixes #20484 Debug code that allowed me to find the issue : ```python print('before apply_repetition_penalties') # Apply repetition penalties as a custom op from vllm. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
