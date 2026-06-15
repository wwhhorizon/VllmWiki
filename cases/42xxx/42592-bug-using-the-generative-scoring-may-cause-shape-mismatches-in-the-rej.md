# vllm-project/vllm#42592: [Bug]: Using the /generative_scoring may cause shape mismatches in the rejection sampler, causing vllm serve to crash

| 字段 | 值 |
| --- | --- |
| Issue | [#42592](https://github.com/vllm-project/vllm/issues/42592) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Using the /generative_scoring may cause shape mismatches in the rejection sampler, causing vllm serve to crash

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Description When sending a `/generative_scoring` request to a vLLM server running `DeepSeek-V4-Flash` with speculative decoding (MTP) enabled, the server crashes with a shape mismatch error inside the rejection sampler. The service becomes completely unresponsive and requires a restart. The error occurs while processing a batch that mixes generative scoring requests and ongoing chat completions. The rejection sampler tries to assign bonus logits with shape `[14, 3]` to a tensor of shape `[14, 129280]`, which is incompatible. **Expected behavior:** `/generative_scoring` should return scoring results without crashing the server, even when speculative decoding and other concurrent requests are active. ### Reproduction 1. **Start vLLM server** with the following command: ```bash vllm/vllm-openai:v0.20.2-cu129 \ --host 0.0.0.0 \ --port 8000 \ --model /models \ --trust-remote-code \ --max-num-batched-tokens 4096 \ --served-model-name deepseek-v4-flash \ --enable-chunked-prefill \ --enable-prefix-caching \ --kv-cache-dtype fp8 \ --block-size 256 \ --max-num-seqs 30 \ --tensor-parallel-size 4 \ --tokenizer-mode deepseek_v4 \ --tool-c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: th a `RuntimeError` in the rejection sampler. ### Environment - **vLLM version**: 0.20.2 (Docker image `vllm/vllm-openai:v0.20.2-cu129`) - **Model**: DeepSeek-V4-Flash (`deepseek-v4`) - **Hardware**: 4x NVIDIA H20-3e GP...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: \ --enable-chunked-prefill \ --enable-prefix-caching \ --kv-cache-dtype fp8 \ --block-size 256 \ --max-num-seqs 30 \ --tensor-parallel-size 4 \ --tokenizer-mode deepseek_v4 \ --tool-call-parser deepseek_v4 \ --enable-au...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Describe the bug ### Description When sending a `/generative_scoring` request to a vLLM server running `DeepSeek-V4-Flash` with speculative decoding (MTP) enabled, the server crashes with a shape mismatch error inside t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Using the /generative_scoring may cause shape mismatches in the rejection sampler, causing vllm serve to crash bug ### Your current environment ### 🐛 Describe the bug ### Description When sending a `/generative_s...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: unked-prefill \ --enable-prefix-caching \ --kv-cache-dtype fp8 \ --block-size 256 \ --max-num-seqs 30 \ --tensor-parallel-size 4 \ --tokenizer-mode deepseek_v4 \ --tool-call-parser deepseek_v4 \ --enable-auto-tool-choic...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
