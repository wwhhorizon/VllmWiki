# vllm-project/vllm#24365: [Bug]: high priority not work

| 字段 | 值 |
| --- | --- |
| Issue | [#24365](https://github.com/vllm-project/vllm/issues/24365) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: high priority not work

### Issue 正文摘录

### Your current environment ============================== Environment Variables ============================== NCCL_VERSION=2.25.1-1 NVIDIA_DRIVER_CAPABILITIES=compute,utility NVIDIA_PRODUCT_NAME=CUDA VLLM_USAGE_SOURCE=production-docker-image CUDA_VERSION=12.8.1 LD_LIBRARY_PATH=/usr/local/cuda/lib64 NCCL_CUMEM_ENABLE=0 PYTORCH_NVML_BASED_CUDA_CHECK=1 TORCHINDUCTOR_COMPILE_THREADS=1 CUDA_MODULE_LOADING=LAZY vLLM Version : [0.10.1.1](http://0.10.1.1/) Nvidia driver version : 570.86.10 PyTorch version : 2.7.1+cu128 OS : Ubuntu 22.04.5 LTS (x86_64) ### 🐛 Describe the bug Background: When I started vllm openai_compatible_server (versions 0.8.5 or 0.10.0, etc.), I added the configuration: --scheduling-policy priority I used deepseek v3 (official version) for inference, started and inferred normally, I tried both vllm engines: 0 and 1 (1) I manually sent a request A: Conclusion: Processed in 8 seconds (2) Then: I started running batch tasks, 30 concurrent requests, and continuously sent request B: Added: "priority": 10 or "extra_body":{"priority": 10 } Conclusion: The batch ran normally (3) I manually sent request A again (maybe: high priority request) Added: "priority": 0 or "extra_bo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ========= Environment Variables ============================== NCCL_VERSION=2.25.1-1 NVIDIA_DRIVER_CAPABILITIES=compute,utility NVIDIA_PRODUCT_NAME=CUDA VLLM_USAGE_SOURCE=production-docker-image CUDA_VERSION=12.8.1 LD_L...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: =2.25.1-1 NVIDIA_DRIVER_CAPABILITIES=compute,utility NVIDIA_PRODUCT_NAME=CUDA VLLM_USAGE_SOURCE=production-docker-image CUDA_VERSION=12.8.1 LD_LIBRARY_PATH=/usr/local/cuda/lib64 NCCL_CUMEM_ENABLE=0 PYTORCH_NVML_BASED_CU...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: openai_compatible_server (versions 0.8.5 or 0.10.0, etc.), I added the configuration: --scheduling-policy priority I used deepseek v3 (official version) for inference, started and inferred normally, I tried both vllm en...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: high priority not work bug;stale ### Your current environment ============================== Environment Variables ============================== NCCL_VERSION=2.25.1-1 NVIDIA_DRIVER_CAPABILITIES=compute,utility N...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
