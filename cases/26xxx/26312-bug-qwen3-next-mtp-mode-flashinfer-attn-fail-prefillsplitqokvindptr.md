# vllm-project/vllm#26312: [Bug]: Qwen3-next. MTP mode. FlashInfer attn fail. `PrefillSplitQOKVIndptr`

| 字段 | 值 |
| --- | --- |
| Issue | [#26312](https://github.com/vllm-project/vllm/issues/26312) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-next. MTP mode. FlashInfer attn fail. `PrefillSplitQOKVIndptr`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Qwen3-next in MPT mode fails with FlashInfer attn (this fail is different from ##25811, I explicitly dissable TRT-LLM attn with `VLLM_USE_TRTLLM_ATTENTION=0`). Server run ``` VLLM_USE_TRTLLM_ATTENTION=0 vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct -tp 4 --no-enable-prefix-caching --speculative-config '{"method": "qwen3_next_mtp", "num_speculative_tokens": 2}' ``` Client ``` vllm bench serve --backend vllm --model Qwen/Qwen3-Next-80B-A3B-Instruct --endpoint /v1/completions --dataset-name random --random-input 1024 --random-output 1024 --max-concurrency 256 --num-prompt 256 --ignore-eos ``` Error ``` (Worker_TP2 pid=2828595) ERROR 10-06 21:25:56 [multiproc_executor.py:706] File "/home/scratch.vgimpelson_ent/vllm_qwen2/vllm/v1/worker/gpu_model_runner.py", line 1393, in _prepare_inputs (Worker_TP2 pid=2828595) ERROR 10-06 21:25:56 [multiproc_executor.py:706] attn_metadata_i = builder.build( (Worker_TP2 pid=2828595) ERROR 10-06 21:25:56 [multiproc_executor.py:706] ^^^^^^^^^^^^^^ (Worker_TP2 pid=2828595) ERROR 10-06 21:25:56 [multiproc_executor.py:706] File "/home/scratch.vgimpelson_ent/vllm_qwen2/vllm/v1/attention/backends/flashinfer.p...

## 现有链接修复摘要

#26361 [Bugfix] Fix MTP+FlashInfer crash when trtllm kernels are available but disabled

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Qwen3-next. MTP mode. FlashInfer attn fail. `PrefillSplitQOKVIndptr` bug ### Your current environment ### 🐛 Describe the bug Qwen3-next in MPT mode fails with FlashInfer attn (this fail is different from ##25811,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Qwen3-next. MTP mode. FlashInfer attn fail. `PrefillSplitQOKVIndptr` bug ### Your current environment ### 🐛 Describe the bug Qwen3-next in MPT mode fails with FlashInfer attn (this fail is different from ##25811,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: fails with FlashInfer attn (this fail is different from ##25811, I explicitly dissable TRT-LLM attn with `VLLM_USE_TRTLLM_ATTENTION=0`). Server run ``` VLLM_USE_TRTLLM_ATTENTION=0 vllm serve Qwen/Qwen3-Next-80B-A3B-Inst...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3-next. MTP mode. FlashInfer attn fail. `PrefillSplitQOKVIndptr` bug ### Your current environment ### 🐛 Describe the bug Qwen3-next in MPT mode fails with FlashInfer attn (this fail is different from ##25811,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: _support;sampling_logits;scheduler_memory;speculative_decoding attention;cuda;operator;sampling;triton build_error;nan_inf env_dependency #26361 [Bugfix] Fix MTP+FlashInfer crash when trtllm kernels are available but di...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#26361](https://github.com/vllm-project/vllm/pull/26361) | mentioned | 0.6 | [Bugfix] Fix MTP+FlashInfer crash when trtllm kernels are available but disabled | he mismatch causes incorrect padding leading to the crash observed in #26312 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
