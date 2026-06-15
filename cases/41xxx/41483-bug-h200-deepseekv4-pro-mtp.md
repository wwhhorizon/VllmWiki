# vllm-project/vllm#41483: [Bug]: h200 deepseekv4 pro mtp

| 字段 | 值 |
| --- | --- |
| Issue | [#41483](https://github.com/vllm-project/vllm/issues/41483) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;scheduler_memory;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;moe;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: h200 deepseekv4 pro mtp

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## server command full command here https://github.com/SemiAnalysisAI/InferenceX/pull/1222/changes closely following official vllm recipes https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro?features=tool_calling%2Creasoning%2Cspec_decoding&hardware=h200 #### the only difference is i have additoaonlly set `--no-enable-prefix-caching` & `--max-model-len 9472` ``` export VLLM_ENGINE_READY_TIMEOUT_S=3600 export VLLM_MEMORY_PROFILER_ESTIMATE_CUDAGRAPHS=0 # Per the recipe, run with EP + DP=8 (no --tensor-parallel-size flag). TP # from the search space is used only for GPU allocation by the runner and # as the DP size. set -x vllm serve $MODEL --host 0.0.0.0 --port $PORT \ --trust-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --no-enable-prefix-caching \ --enable-expert-parallel \ --data-parallel-size 8 \ --max-model-len 9472 \ --gpu-memory-utilization 0.95 \ --max-num-seqs 512 \ --max-num-batched-tokens 512 \ --no-enable-flashinfer-autotune \ --compilation-config '{"mode":0,"cudagraph_mode":"FULL_DECODE_ONLY"}' \ --speculative-config '{"method":"mtp","num_speculative_tokens":1}' \ --tokenizer-mode deepseek_v4 \ --tool-call-p...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: hinfer-autotune \ --compilation-config '{"mode":0,"cudagraph_mode":"FULL_DECODE_ONLY"}' \ --speculative-config '{"method":"mtp","num_speculative_tokens":1}' \ --tokenizer-mode deepseek_v4 \ --tool-call-parser deepseek_v...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: b.com/SemiAnalysisAI/InferenceX/pull/1222/changes closely following official vllm recipes https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Pro?features=tool_calling%2Creasoning%2Cspec_decoding&hardware=h200 #### the only...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ve $MODEL --host 0.0.0.0 --port $PORT \ --trust-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --no-enable-prefix-caching \ --enable-expert-parallel \ --data-parallel-size 8 \ --max-model-len 9472 \ --gpu-memor...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: en 9472` ``` export VLLM_ENGINE_READY_TIMEOUT_S=3600 export VLLM_MEMORY_PROFILER_ESTIMATE_CUDAGRAPHS=0 # Per the recipe, run with EP + DP=8 (no --tensor-parallel-size flag). TP # from the search space is used only for G...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: st 0.0.0.0 --port $PORT \ --trust-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --no-enable-prefix-caching \ --enable-expert-parallel \ --data-parallel-size 8 \ --max-model-len 9472 \ --gpu-memory-utilization...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
