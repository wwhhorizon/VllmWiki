# vllm-project/vllm#16883: [Bug]: Ngram speculative decoding doesn't work in vLLM 0.8.3/0.8.4 with VLLM_USE_V1 enabled.

| 字段 | 值 |
| --- | --- |
| Issue | [#16883](https://github.com/vllm-project/vllm/issues/16883) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Ngram speculative decoding doesn't work in vLLM 0.8.3/0.8.4 with VLLM_USE_V1 enabled.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM 0.8.3/0.8.4: **In v0 mode, ngram speculative decoding works as expected.** **In v1 mode, ngram speculative decoding does not work.** vLLM 0.7.3: **Both v0/v1 mode work as expected.** Let me know if I missed anything. #### use v0 ```bash export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 vllm serve /data/code/Qwen2.5-Coder-32B-Instruct \ --host 0.0.0.0 \ --port 8080 \ --trust-remote-code \ --gpu-memory-utilization 0.9 \ --dtype auto \ --tensor-parallel-size 4 \ --max-num-batched-tokens 131072 \ --max-model-len 131072 \ --max-num-seqs 8 \ --enable-prefix-caching \ --speculative-config '{"method": "ngram", "prompt_lookup_min": 10, "prompt_lookup_max": 50, "num_speculative_tokens": 300}' \ --rope-scaling '{ "factor": 4.0, "original_max_position_embeddings": 32768, "rope_type": "yarn" }' \ --enforce-eager ``` I can see that SpecDecodeWorker is active in the logs, and the completions are extremely fast. ```bash INFO 04-20 16:25:45 [spec_decode_worker.py:221] [Speculative Decoding] Configuring SpecDecodeWorker with sampler= ``` #### use v1 ```bash export VLLM_USE_V1=1 export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 vllm serve /data/code/Qwen2.5-Coder-3...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Ngram speculative decoding doesn't work in vLLM 0.8.3/0.8.4 with VLLM_USE_V1 enabled. bug;stale ### Your current environment ### 🐛 Describe the bug vLLM 0.8.3/0.8.4: **In v0 mode, ngram speculative decoding works...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: equently asked questions. performance activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding atten...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: w if I missed anything. #### use v0 ```bash export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 vllm serve /data/code/Qwen2.5-Coder-32B-Instruct \ --host 0.0.0.0 \ --port 8080 \ --trust-remote-code \ --gpu-memory-utilization 0.9 \ -...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: port 8080 \ --trust-remote-code \ --gpu-memory-utilization 0.9 \ --dtype auto \ --tensor-parallel-size 4 \ --max-num-batched-tokens 131072 \ --max-model-len 131072 \ --max-num-seqs 8 \ --enable-prefix-caching \ --specul...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
