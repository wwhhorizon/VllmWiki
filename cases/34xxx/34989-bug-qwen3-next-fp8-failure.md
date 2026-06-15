# vllm-project/vllm#34989: [Bug]: Qwen3-Next-FP8 failure

| 字段 | 值 |
| --- | --- |
| Issue | [#34989](https://github.com/vllm-project/vllm/issues/34989) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Next-FP8 failure

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I hit a new problem when trying run benchmark performance of Qwen3-Next using prefix caching and MTP: **Server:** ``` vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 \ --tensor-parallel-size 4 \ --max-model-len 262144 \ --enable-prefix-caching \ --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens":2}' ``` **Benchmark:** ``` vllm bench serve --model Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 --ignore_eos --dataset-name sharegpt --dataset-path ShareGPT_V3_unfiltered_cleaned_split.json ``` **Error:** ``` (Worker_TP2 pid=27181) ERROR 02-20 21:24:42 [multiproc_executor.py:867] File "/workspace/vllm/vllm/v1/worker/gpu_model_runner.py", line 1888, in _build_attention_metadata (Worker_TP0 pid=27179) ERROR 02-20 21:24:42 [multiproc_executor.py:867] File "/workspace/vllm/vllm/v1/worker/gpu_model_runner.py", line 3485, in execute_model (Worker_TP2 pid=27181) ERROR 02-20 21:24:42 [multiproc_executor.py:867] _build_attn_group_metadata(kv_cache_gid, attn_gid, cm) (Worker_TP0 pid=27179) ERROR 02-20 21:24:42 [multiproc_executor.py:867] self._build_attention_metadata( (Worker_TP2 pid=27181) ERROR 02-20 21:24:42 [multiproc_executor....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ile "/workspace/vllm/vllm/v1/worker/gpu_model_runner.py", line 1888, in _build_attention_metadata (Worker_TP0 pid=27179) ERROR 02-20 21:24:42 [multiproc_executor.py:867] File "/workspace/vllm/vllm/v1/worker/gpu_model_ru...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Qwen3-Next-FP8 failure bug ### Your current environment ### 🐛 Describe the bug I hit a new problem when trying run benchmark performance of Qwen3-Next using prefix caching and MTP: **Server:** ``` vllm serve Qwen...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3-Next-FP8 failure bug ### Your current environment ### 🐛 Describe the bug I hit a new problem when trying run benchmark performance of Qwen3-Next using prefix caching and MTP: **Server:** ``` vllm serve Qwen...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 42 [multiproc_executor.py:867] File "/workspace/vllm/vllm/v1/attention/backends/gdn_attn.py", line 310, in build (Worker_TP0 pid=27179) ERROR 02-20 21:24:42 [multiproc_executor.py:867] attn_metadata_i = builder.build( (...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ore ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
