# vllm-project/vllm#31199: [Bug]: UnpicklingError during concurrent model compilation on multiple GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#31199](https://github.com/vllm-project/vllm/issues/31199) |
| 状态 | open |
| 标签 | bug;torch.compile;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;model_support;quantization |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;fp8;operator |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: UnpicklingError during concurrent model compilation on multiple GPUs

### Issue 正文摘录

### Your current environment - vLLM Version: 0.10.2+cu129 (Running V1 Engine) - Model: Qwen/Qwen3-32B-FP8 - GPU: NVIDIA H200 (x3) - CUDA Version: 12.9 - Python Version: 3.12.12 - OS: Linux (HPC Cluster) - Install Method: uv package manager ### 🐛 Describe the bug When launching multiple vLLM instances concurrently (one per GPU) on the same node, failures occur during the TorchInductor model compilation phase. **Observed Behavior:** -Sequential launch: Works fine. -Concurrent launch: 2 out of 3 instances fail with UnpicklingError. The error implies that the compilation cache file might be corrupted or read partially while being written by another process. ### Reproduction Script: #!/bin/bash **Common Configuration** MODEL="Qwen/Qwen3-32B-FP8" KV_CONFIG='{"kv_connector":"NixlConnector","kv_role":"kv_both"}' **--- 1. Launch Prefiller (GPU 0) ---** CUDA_VISIBLE_DEVICES=0 \ UCX_NET_DEVICES=all \ VLLM_NIXL_SIDE_CHANNEL_PORT=5605 \ vllm serve $MODEL \ --port 8105 \ --kv-transfer-config "$KV_CONFIG" & **--- 2. Launch Decoder 1 (GPU 1) ---** CUDA_VISIBLE_DEVICES=1 \ UCX_NET_DEVICES=all \ VLLM_NIXL_SIDE_CHANNEL_PORT=5705 \ vllm serve $MODEL \ --port 8205 \ --kv-transfer-config "$KV_CONFIG" &...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: lingError during concurrent model compilation on multiple GPUs bug;torch.compile;stale ### Your current environment - vLLM Version: 0.10.2+cu129 (Running V1 Engine) - Model: Qwen/Qwen3-32B-FP8 - GPU: NVIDIA H200 (x3) -...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: UnpicklingError during concurrent model compilation on multiple GPUs bug;torch.compile;stale ### Your current environment - vLLM Version: 0.10.2+cu129 (Running V1 Engine) - Model: Qwen/Qwen3-32B-FP8 - GPU: NVIDIA...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: - vLLM Version: 0.10.2+cu129 (Running V1 Engine) - Model: Qwen/Qwen3-32B-FP8 - GPU: NVIDIA H200 (x3) - CUDA Version: 12.9 - Python Version: 3.12.12 - OS: Linux (HPC Cluster) - Install Method: uv package manager ### 🐛 De...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: r during concurrent model compilation on multiple GPUs bug;torch.compile;stale ### Your current environment - vLLM Version: 0.10.2+cu129 (Running V1 Engine) - Model: Qwen/Qwen3-32B-FP8 - GPU: NVIDIA H200 (x3) - CUDA Ver...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: mine_available_memory (EngineCore_DP0 pid=3835890) self.model_runner.profile_run() (EngineCore_DP0 pid=3835890) File ".../site-packages/vllm/v1/worker/gpu_model_runner.py", line 3031, in profile_run (EngineCore_DP0 pid=...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
