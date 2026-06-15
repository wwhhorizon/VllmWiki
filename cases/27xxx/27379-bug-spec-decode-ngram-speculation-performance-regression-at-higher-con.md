# vllm-project/vllm#27379: [Bug]: [Spec Decode] ngram speculation performance regression at higher concurrany

| 字段 | 值 |
| --- | --- |
| Issue | [#27379](https://github.com/vllm-project/vllm/issues/27379) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [Spec Decode] ngram speculation performance regression at higher concurrany

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have benchmarked ngram-speculation decoding on Qwen3-30B-MOE model. I observe there is a regression in throughput (throughput lower than no-speculation decoding) on some datasets as concurrency increases. However, I observe that token acceptance rate is staying more or less the same when concurrency is. Therefore, this is likely not an algorithmic issue. The drop in performance is most noticeable on Blazedit dataset - which is expected to have stronger performance in ngram decoding (over no-speculation). Code to reproduce: ``` VLLM_FLASH_ATTN_VERSION=3 vllm serve $target_model_path --speculative_config '{"method": "ngram", "num_speculative_tokens": 5, "prompt_lookup_max": 5, "prompt_lookup_min": 2, "disable_padded_drafter_batch": true}' --disable-log-requests --enable-chunked-prefill --max-num-seqs 16 --no-enable-prefix-caching --tensor-parallel-size 4 --compilation-config {\"compile_sizes\":[1,2,4,8,16]} ``` ``` vllm bench serve --port 8000 --save-result --save-detailed \ --model "$target_model_path" \ --backend openai-chat \ --endpoint /v1/chat/completions \ --dataset-name hf \ --dataset-path vdaita/edit_5k_char \ --blazedit-...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: [Spec Decode] ngram speculation performance regression at higher concurrany bug;stale ### Your current environment ### 🐛 Describe the bug I have benchmarked ngram-speculation decoding on Qwen3-30B-MOE model. I ob...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: oding (over no-speculation). Code to reproduce: ``` VLLM_FLASH_ATTN_VERSION=3 vllm serve $target_model_path --speculative_config '{"method": "ngram", "num_speculative_tokens": 5, "prompt_lookup_max": 5, "prompt_lookup_m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ### 🐛 Describe the bug I have benchmarked ngram-speculation decoding on Qwen3-30B-MOE model. I observe there is a regression in throughput (throughput lower than no-speculation decoding) on some datasets as concurrency...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: [Spec Decode] ngram speculation performance regression at higher concurrany bug;stale ### Your current environment ### 🐛 Describe the bug I have benchmarked ngram-speculation decoding on Qwen3-30B-MOE model. I ob...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: save-detailed \ --model "$target_model_path" \ --backend openai-chat \ --endpoint /v1/chat/completions \ --dataset-name hf \ --dataset-path vdaita/edit_5k_char \ --blazedit-min-distance 0.01 \ --blazedit-max-d

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
