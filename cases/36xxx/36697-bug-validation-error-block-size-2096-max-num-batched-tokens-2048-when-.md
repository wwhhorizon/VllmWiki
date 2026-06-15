# vllm-project/vllm#36697: [Bug]: Validation Error: block_size (2096) > max_num_batched_tokens (2048) when enabling prefix caching for Qwen3.5 Mamba architecture

| 字段 | 值 |
| --- | --- |
| Issue | [#36697](https://github.com/vllm-project/vllm/issues/36697) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Validation Error: block_size (2096) > max_num_batched_tokens (2048) when enabling prefix caching for Qwen3.5 Mamba architecture

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug - Bug summary: When running a Mamba-hybrid model (Qwen3_5MoeForConditionalGeneration) with --enable-prefix-caching, vLLM auto-scales the block_size to 2096 to align Mamba and Attention pages. However, it crashes during VllmConfig validation because the default max_num_batched_tokens for chunked prefill is 2048. - Suggested fix: The framework should either automatically scale max_num_batched_tokens to be at least block_size when Mamba align mode forces it, or provide a clearer warning to the user to manually increase --max-num-batched-tokens. - Full Traceback: ```text (vllm) Yifei@lyg1058:~/models$ CUDA_VISIBLE_DEVICES=2,3 vllm serve Qwen3.5-122B-A10B-GPTQ-Int4 --served-model-name Qwen3.5-27B-AWQ-4bit --gpu-memory-utilization 0.9 --port 8848 -tp 2 --max-model-len 131072 --enable-auto-tool-choice --tool-call-parser qwen3_coder --reasoning-parser qwen3 --max-num-seqs 16 --enable-prefix-caching (APIServer pid=913608) INFO 03-11 03:44:50 [utils.py:302] (APIServer pid=913608) INFO 03-11 03:44:50 [utils.py:302] █ █ █▄ ▄█ (APIServer pid=913608) INFO 03-11 03:44:50 [utils.py:302] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.17.0 (APIServer pid=913608) INF...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: d=913608) INFO 03-11 03:44:50 [utils.py:302] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.17.0 (APIServer pid=913608) INFO 03-11 03:44:50 [utils.py:302] █▄█▀ █ █ █ █ model Qwen3.5-122B-A10B-GPTQ-Int4 (APIServer pid=913608) INFO 03-11 03...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: n3_5MoeForConditionalGeneration) with --enable-prefix-caching, vLLM auto-scales the block_size to 2096 to align Mamba and Attention pages. However, it crashes during VllmConfig validation because the default max_num_bat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: (2096) > max_num_batched_tokens (2048) when enabling prefix caching for Qwen3.5 Mamba architecture bug ### Your current environment ### 🐛 Describe the bug - Bug summary: When running a Mamba-hybrid model (Qwen3_5MoeForC...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]: Validation Error: block_size (2096) > max_num_batched_tokens (2048) when enabling prefix caching for Qwen3.5 Mamba architecture bug ### Your current environment ### 🐛 Describe the bug - Bug summary: When running...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Config validation because the default max_num_batched_tokens for chunked prefill is 2048. - Suggested fix: The framework should either automatically scale max_num_batched_tokens to be at least block_size when Mamba alig...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
