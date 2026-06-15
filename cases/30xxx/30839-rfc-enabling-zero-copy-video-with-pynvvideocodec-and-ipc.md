# vllm-project/vllm#30839: [RFC]: Enabling Zero-Copy Video with PyNvVideoCodec and IPC

| 字段 | 值 |
| --- | --- |
| Issue | [#30839](https://github.com/vllm-project/vllm/issues/30839) |
| 状态 | open |
| 标签 | RFC;unstale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;multimodal_vlm;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | cache;cuda;gemm |
| 症状 | oom;slowdown |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Enabling Zero-Copy Video with PyNvVideoCodec and IPC

### Issue 正文摘录

### Motivation. This RFC proposes a set of changes for enabling HW-accelerated video decoding and zero-copy transfer to CoreEngine for improving VLM latency/throughput and reducing CPU pressure for (eventual) multi-GPU scaling. These changes are aimed at improving the basic DP=1 case first with future improvements to support more complex DP>1 or TP cases. # Benchmark Data A comparison of throughput for video captioning tasks consistently showed a 2-3% improvement in overall throughput. This testing was performed on a single H100 GPU. All testing performed on ``` CPU Model: AMD EPYC 7413 24-Core Processor System Memory: 256 GB GPU: NVIDIA H100 80GB HBM3 ``` Benchmarking serving was single vLLM instance with 3 API Server Processes. ``` VLLM_VIDEO_LOADER_BACKEND=pynvvideocodec \ VLLM_WORKER_MULTIPROC_METHOD=spawn \ vllm serve nvidia/cosmos-reason1-7b \ --limit-mm-per-prompt '{"video": 1}' \ --allowed-local-media-path / \ --mm-processor-cache-gb \ --trust-remote-code \ --max-model-len 65536 \ --gpu-memory-utilization 0.6 \ --no-enforce-eager \ --max-num-seqs 64 \ --no-enable-prefix-caching \ --api-server-count 3 \ --media-io-kwargs '{"video":{"num_frames":10}}' \ --mm-processor-kwargs...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [RFC]: Enabling Zero-Copy Video with PyNvVideoCodec and IPC RFC;unstale ### Motivation. This RFC proposes a set of changes for enabling HW-accelerated video decoding and zero-copy transfer to CoreEngine for improving VL...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: ed video decoding and zero-copy transfer to CoreEngine for improving VLM latency/throughput and reducing CPU pressure for (eventual) multi-GPU scaling. These changes are aimed at improving the basic DP=1 case first with...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: mprovement in overall throughput. This testing was performed on a single H100 GPU. All testing performed on ``` CPU Model: AMD EPYC 7413 24-Core Processor System Memory: 256 GB GPU: NVIDIA H100 80GB HBM3 ``` Benchmarkin...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: nsures VRAM allocation remains alive API->>ZMQ: ZMQ Send(Request Metadata + Handle) end Note over Core, GPU: 3. Reconstruction & Inference ZMQ->>Core: Recv(Request Metadata + Handle) Core->>Q: Get() -> Returns GPU Tenso...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: copy transfer to CoreEngine for improving VLM latency/throughput and reducing CPU pressure for (eventual) multi-GPU scaling. These changes are aimed at improving the basic DP=1 case first with future improvements to sup...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
