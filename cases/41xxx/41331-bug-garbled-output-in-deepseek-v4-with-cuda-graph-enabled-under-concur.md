# vllm-project/vllm#41331: [Bug]: Garbled Output in DeepSeek-V4 with CUDA Graph Enabled Under Concurrent Identical Input Requests

| 字段 | 值 |
| --- | --- |
| Issue | [#41331](https://github.com/vllm-project/vllm/issues/41331) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Garbled Output in DeepSeek-V4 with CUDA Graph Enabled Under Concurrent Identical Input Requests

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We deploy the model using the following script and send concurrent requests with identical inputs via `claude code -p`. When `cudagraph_mode` is set to `FULL_DECODE_ONLY`, some requests produce garbled output, while single-request (non-concurrent) inference works fine. When `cudagraph_mode` is set to `None`, the garbled output under concurrency disappears. ```Bash IMAGE=vllm/vllm-openai:nightly docker run -d \ --gpus all \ --name vllm-deepseek_v4 \ -p 8000:8000 \ --restart unless-stopped \ -e VLLM_ENGINE_READY_TIMEOUT_S=3600 \ -e VLLM_API_KEY=xxxx \ -v $PROJ/models/deepseek-ai/DeepSeek-V4-Pro:/model \ $IMAGE \ --enable-prefix-caching \ --enable-chunked-prefill \ --model /model \ --served-model-name inner-deepseek_v4 \ --enable-expert-parallel \ --tensor-parallel-size 8 \ --host 0.0.0.0 \ --port 8000 \ --trust-remote-code \ --gpu-memory-utilization 0.95 \ --max-num-seqs 128 \ --kv-cache-dtype fp8 \ --block-size 256 \ --compilation-config '{"mode":0,"cudagraph_mode":"FULL_DECODE_ONLY"}' \ --attention_config.use_fp4_indexer_cache=True \ --tokenizer-mode deepseek_v4 \ --tool-call-parser deepseek_v4 \ --enable-auto-tool-choice \ --rea...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: t under concurrency disappears. ```Bash IMAGE=vllm/vllm-openai:nightly docker run -d \ --gpus all \ --name vllm-deepseek_v4 \ -p 8000:8000 \ --restart unless-stopped \ -e VLLM_ENGINE_READY_TIMEOUT_S=3600 \ -e VLLM_API_K...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: \ --gpu-memory-utilization 0.95 \ --max-num-seqs 128 \ --kv-cache-dtype fp8 \ --block-size 256 \ --compilation-config '{"mode":0,"cudagraph_mode":"FULL_DECODE_ONLY"}' \ --attention_config.use_fp4_indexer_cache=True \ --...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: in DeepSeek-V4 with CUDA Graph Enabled Under Concurrent Identical Input Requests bug ### Your current environment ### 🐛 Describe the bug We deploy the model using the following script and send concurrent requests with i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: g ### Your current environment ### 🐛 Describe the bug We deploy the model using the following script and send concurrent requests with identical inputs via `claude code -p`. When `cudagraph_mode` is set to `FULL_DECODE_...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: --model /model \ --served-model-name inner-deepseek_v4 \ --enable-expert-parallel \ --tensor-parallel-size 8 \ --host 0.0.0.0 \ --port 8000 \ --trust-remote-code \ --gpu-memory-utilization 0.95 \ --max-num-seqs 128 \ --...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
