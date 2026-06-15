# vllm-project/vllm#35138: [Bug]: Qwen/Qwen3.5-397B-A17B-FP8 and Qwen/Qwen3.5-397B-A17B has accuracy issues when running with Flashinfer Attention backend on Blackwell.

| 字段 | 值 |
| --- | --- |
| Issue | [#35138](https://github.com/vllm-project/vllm/issues/35138) |
| 状态 | closed |
| 标签 | bug;nvidia |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen/Qwen3.5-397B-A17B-FP8 and Qwen/Qwen3.5-397B-A17B has accuracy issues when running with Flashinfer Attention backend on Blackwell.

### Issue 正文摘录

## Workaround!!!: Use Flash-Attn backend for now: ``` --attention-backend FLASH_ATTN ``` ### Your current environment ### 🐛 Describe the bug ```bash vllm serve Qwen/Qwen3.5-397B-A17B-FP8 --tensor-parallel-size 4 --reasoning-parser qwen3 --no-enable-prefix-caching --no-async-scheduling --enforce-eager ``` run the following script "twice", the accuracy for the second and future runs will 100% reproduce the issue. ```bash python tests/evals/gsm8k/gsm8k_eval.py ``` Observations: 1. Qwen/Qwen3-Next-80B-A3B-Instruct (tp2 and tp4) works fine 2. In addition to the prefix cache and chunked prefill, also ruled out FP8 query quantization, trtllm workspace initialization as not the issue. 3. When using FI native for prefill, then I found NaNs in the output of trtllm_batch_decode_with_kv_cache instead. When using FI native for both prefill and decode, there is no issue. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#35219 [BUGFIX][Mamba][Qwen3.5] Zero freed SSM cache blocks on GPU

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: 7B has accuracy issues when running with Flashinfer Attention backend on Blackwell. bug;nvidia ## Workaround!!!: Use Flash-Attn backend for now: ``` --attention-backend FLASH_ATTN ``` ### Your current environment ### 🐛...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: (tp2 and tp4) works fine 2. In addition to the prefix cache and chunked prefill, also ruled out FP8 query quantization, trtllm workspace initialization as not the issue. 3. When using FI native for prefill, then I found...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: 17B-FP8 and Qwen/Qwen3.5-397B-A17B has accuracy issues when running with Flashinfer Attention backend on Blackwell. bug;nvidia ## Workaround!!!: Use Flash-Attn backend for now: ``` --attention-backend FLASH_ATTN ``` ###...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_de...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Qwen/Qwen3.5-397B-A17B-FP8 and Qwen/Qwen3.5-397B-A17B has accuracy issues when running with Flashinfer Attention backend on Blackwell. bug;nvidia ## Workaround!!!: Use Flash-Attn backend for now: ``` --attention-...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35219](https://github.com/vllm-project/vllm/pull/35219) | mentioned | 0.6 | [BUGFIX][Mamba][Qwen3.5] Zero freed SSM cache blocks on GPU | tokens/s within ±2% noise). ### Test plan - **The original issue (#35138) reproduction test passes**: 5 consecutive GSM8K evaluations on Qwen3.5-397B-A17B-FP8 (TP=4, FlashInfer ba… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
