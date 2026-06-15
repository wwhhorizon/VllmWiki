# vllm-project/vllm#33572: [Bug]: GPT-OSS with CPU KV cache offload break with FlashInfer

| 字段 | 值 |
| --- | --- |
| Issue | [#33572](https://github.com/vllm-project/vllm/issues/33572) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPT-OSS with CPU KV cache offload break with FlashInfer

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Serving with this script: ```bash #!/usr/bin/env bash cat > config.yaml << EOF kv-cache-dtype: fp8 compilation-config: '{"pass_config":{"fuse_allreduce_rms":true,"eliminate_noops":true}}' async-scheduling: true max-cudagraph-capture-size: 2048 max-num-batched-tokens: 8192 EOF export TORCH_CUDA_ARCH_LIST="10.0" export VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8=1 export PYTHONNOUSERSITE=1 vllm serve openai/gpt-oss-120b --host 0.0.0.0 --port 8888 \ --config config.yaml \ --gpu-memory-utilization 0.9 \ --tensor-parallel-size 1 \ --max-num-seqs 512 \ --kv_offloading_backend native \ --kv_offloading_size 200 \ --disable-hybrid-kv-cache-manager ``` Note that setting `--attention-backend TRITON_ATTN`, the server runs with the same settings. Full server logs: [server_err.log](https://github.com/user-attachments/files/25024703/server_err.log) Extended trace logs: [server_err_trace.log](https://github.com/user-attachments/files/25024877/server_err_trace.log) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs....

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: script: ```bash #!/usr/bin/env bash cat > config.yaml << EOF kv-cache-dtype: fp8 compilation-config: '{"pass_config":{"fuse_allreduce_rms":true,"eliminate_noops":true}}' async-scheduling: true max-cudagraph-capture-size...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: GPT-OSS with CPU KV cache offload break with FlashInfer bug ### Your current environment ### 🐛 Describe the bug Serving with this script: ```bash #!/usr/bin/env bash cat > config.yaml << EOF kv-cache-dtype: fp8 c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_de...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: GPT-OSS with CPU KV cache offload break with FlashInfer bug ### Your current environment ### 🐛 Describe the bug Serving with this script: ```bash #!/usr/bin/env bash cat > config.yaml << EOF kv-cache-dtype: fp8 c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: GPT-OSS with CPU KV cache offload break with FlashInfer bug ### Your current environment ### 🐛 Describe the bug Serving with this script: ```bash #!/usr/bin/env bash cat > config.yaml << EOF kv-cache-dtype: fp8 co

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
