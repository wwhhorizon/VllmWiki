# vllm-project/vllm#26594: [Bug]: ngram speculator throughput is low on Qwen3-30B-coder-MOE and Qwen3-32B models

| 字段 | 值 |
| --- | --- |
| Issue | [#26594](https://github.com/vllm-project/vllm/issues/26594) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ngram speculator throughput is low on Qwen3-30B-coder-MOE and Qwen3-32B models

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm able to observe a considerable gain with ngram speculation on llama8B model (on InstructCoder, balzedit datasets). However, the same gain is not observed in Qwen3-coder-30B-MOE and Qwen3-32B models. llama8B-instruct Qwen3-coder-30B-MOE (TP1, H200) Qwen3-32B (TP4. H200) Commands used: **ngram-speculation** ``` vllm serve $target_model_path \ --disable-log-requests \ --tensor-parallel-size 4 \ --enable-chunked-prefill \ --no-enable-prefix-caching \ --max-num-seqs 16 \ --speculative_config '{"method": "ngram", "num_speculative_tokens": 4, "prompt_lookup_max": 4, "prompt_lookup_min": 2, "disable_padded_drafter_batch": true}", "prompt_lookup_max": 5, "prompt_lookup_min": 5}' \ --compilation-config '{"compile_sizes": [1, 2, 4, 8, 16]}' ``` **no-speculation** vllm serve $target_model_path \ --disable-log-requests \ --tensor-parallel-size 4 \ --enable-chunked-prefill \ --no-enable-prefix-caching \ --max-num-seqs 16 \ --compilation-config '{"compile_sizes": [1, 2, 4, 8, 16]}' ``` ``` Running tests: ``` vllm bench serve --port 8000 --save-result --save-detailed \ --model $target_model_path \ --endpoint-type openai-chat \ --endpoint /v1...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: ngram speculator throughput is low on Qwen3-30B-coder-MOE and Qwen3-32B models bug ### Your current environment ### 🐛 Describe the bug I'm able to observe a considerable gain with ngram speculation on llama8B mod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: okup_max": 5, "prompt_lookup_min": 5}' \ --compilation-config '{"compile_sizes": [1, 2, 4, 8, 16]}' ``` **no-speculation** vllm serve $target_model_path \ --disable-log-requests \ --tensor-parallel-size 4 \ --enable-chu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ulation** ``` vllm serve $target_model_path \ --disable-log-requests \ --tensor-parallel-size 4 \ --enable-chunked-prefill \ --no-enable-prefix-caching \ --max-num-seqs 16 \ --speculative_config '{"method": "ngram", "nu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: ngram speculator throughput is low on Qwen3-30B-coder-MOE and Qwen3-32B models bug ### Your current environment ### 🐛 Describe the bug I'm able to observe a considerable gain with ngram speculation on llama8B mod...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
