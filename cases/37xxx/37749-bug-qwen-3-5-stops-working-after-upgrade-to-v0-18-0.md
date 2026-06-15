# vllm-project/vllm#37749: [Bug]: Qwen 3.5 stops working after upgrade to v0.18.0

| 字段 | 值 |
| --- | --- |
| Issue | [#37749](https://github.com/vllm-project/vllm/issues/37749) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen 3.5 stops working after upgrade to v0.18.0

### Issue 正文摘录

### Your current environment Model: cyankiwi/Qwen3.5-27B-AWQ-BF16-INT4 + QuantTrio/Qwen3.5-27B-AWQ Inference Framework: vLLM 0.18.0 GPU Hardware: Multiple A100 40GB (one model / card) Deployment Mode: vLLM as Docker Parameter: ` --gpu-memory-utilization 0.90 --reasoning-parser qwen3 --enable-auto-tool-choice --tool-call-parser qwen3_coder --language-model-only --max-model-len 65536 --max-num-batched-tokens 12288 --kv-cache-dtype fp8 --max-num-seqs 8 --enable-chunked-prefill --enable-prefix-caching` ### 🐛 Describe the bug After upgrading from 0.17.1 to v0.18.0, all my qwen 3.5 model-container didnt start anymore. They just restarting without an error. When i use 0.17.1 everything works again. qwen3-embedding and qwen3-reranker works on version 18. it looks like an qwen 3.5 problem. When I use the latest nightly build, I see the same behavior, but at least I get the following error `(APIServer pid=1) INFO 03-21 14:13:50 [utils.py:297] (APIServer pid=1) INFO 03-21 14:13:50 [utils.py:297] █ █ █▄ ▄█ (APIServer pid=1) INFO 03-21 14:13:50 [utils.py:297] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.17.2rc1.dev201+g0d50fa1db (APIServer pid=1) INFO 03-21 14:13:50 [utils.py:297] █▄█▀ █ █ █ █ model /root/.cac...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: 0.18.0 bug ### Your current environment Model: cyankiwi/Qwen3.5-27B-AWQ-BF16-INT4 + QuantTrio/Qwen3.5-27B-AWQ Inference Framework: vLLM 0.18.0 GPU Hardware: Multiple A100 40GB (one model / card) Deployment Mode: vLLM as...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Bug]: Qwen 3.5 stops working after upgrade to v0.18.0 bug ### Your current environment Model: cyankiwi/Qwen3.5-27B-AWQ-BF16-INT4 + QuantTrio/Qwen3.5-27B-AWQ Inference Framework: vLLM 0.18.0 GPU Hardware: Multiple A100...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Hardware: Multiple A100 40GB (one model / card) Deployment Mode: vLLM as Docker Parameter: ` --gpu-memory-utilization 0.90 --reasoning-parser qwen3 --enable-auto-tool-choice --tool-call-parser qwen3_coder --language-mod...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: --kv-cache-dtype fp8 --max-num-seqs 8 --enable-chunked-prefill --enable-prefix-caching` ### 🐛 Describe the bug After upgrading from 0.17.1 to v0.18.0, all my qwen 3.5 model-container didnt start anymore. They just resta...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: orks on version 18. it looks like an qwen 3.5 problem. When I use the latest nightly build, I see the same behavior, but at least I get the following error `(APIServer pid=1) INFO 03-21 14:13:50 [utils.py:297] (APIServe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
