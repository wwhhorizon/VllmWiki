# vllm-project/vllm#35390: [Bug]: Qwen3.5 (NVIDIA H200) Pointer argument (at 0) cannot be accessed from Triton

| 字段 | 值 |
| --- | --- |
| Issue | [#35390](https://github.com/vllm-project/vllm/issues/35390) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5 (NVIDIA H200) Pointer argument (at 0) cannot be accessed from Triton

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug CC @haosdent just in case. Container: `vllm/vllm-openai:nightly-4a9c07a0a2b8308a045476b48be29e37c349274b` Command: `python3 -m vllm.entrypoints.openai.api_server --port 5000 --host 0.0.0.0 --download-dir /workspace/.cache/huggingface/hub --model Qwen/Qwen3.5-397B-A17B-FP8 --tensor-parallel-size 2 --pipeline-parallel-size 2 --trust-remote-code --enable-chunked-prefill --enable-prefix-caching --max-num-seqs 128 --gpu-memory-utilization 0.95 --max-model-len 1010000 --hf-overrides '{"text_config": {"max_position_embeddings": 1010000, "rope_parameters": {"mrope_interleaved": true, "mrope_section": [11, 11, 10], "rope_type": "yarn", "rope_theta": 10000000, "partial_rotary_factor": 0.25, "factor": 4.0, "original_max_position_embeddings": 262144}}}' --enable-auto-tool-choice --tool-call-parser qwen3_coder --reasoning-parser qwen3 --mm-processor-cache-gb 0 --mm-encoder-tp-mode data` This is from https://github.com/vllm-project/vllm/pull/35085: (Worker_PP0_TP0 pid=330) WARNING 02-26 09:42:52 [allreduce_rms_fusion.py:771[] AllReduce fusion pass is disabled: flashinfer workspace creation failed: [SymmDeviceMemory] Device does not support mul...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Qwen3.5 (NVIDIA H200) Pointer argument (at 0) cannot be accessed from Triton bug ### Your current environment ### 🐛 Describe the bug CC @haosdent just in case. Container: `vllm/vllm-openai:nightly-4a9c07a0a2b8308...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: upport multicasting.. This is expected on GPUs without NVSwitch (e.g., NVLink bridge-only or PCIe topologies). Falling back to non-fused allreduce. Then: `ValueError: Pointer argument (at 0) cannot be accessed from Trit...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: oad-dir /workspace/.cache/huggingface/hub --model Qwen/Qwen3.5-397B-A17B-FP8 --tensor-parallel-size 2 --pipeline-parallel-size 2 --trust-remote-code --enable-chunked-prefill --enable-prefix-caching --max-num-seqs 128 --...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: l-size 2 --pipeline-parallel-size 2 --trust-remote-code --enable-chunked-prefill --enable-prefix-caching --max-num-seqs 128 --gpu-memory-utilization 0.95 --max-model-len 1010000 --hf-overrides '{"text_config": {"max_pos...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ]: Qwen3.5 (NVIDIA H200) Pointer argument (at 0) cannot be accessed from Triton bug ### Your current environment ### 🐛 Describe the bug CC @haosdent just in case. Container: `vllm/vllm-openai:nightly-4a9c07a0a2b8308a045...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
