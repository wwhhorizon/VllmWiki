# vllm-project/vllm#23023: [Bug]: FlashInfer Sampler is broken on nightly vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#23023](https://github.com/vllm-project/vllm/issues/23023) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;operator |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FlashInfer Sampler is broken on nightly vLLM

### Issue 正文摘录

### Your current environment ``` /pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:144: operator(): block: [0,0,0], thread: [0,0,0] Assertion `idx_dim >= 0 && idx_dim = 0 && idx_dim = 0 && idx_dim = 0 && idx_dim < index_size && "index out of bounds"` failed. tcpxResult_t tcpxInit(tcpxDebugLogger_t):379 NET/GPUDirectTCPX : GPUDirectTCPX enable: 1Warning: please use at least NVCC 12.9 for the best DeepGEMM performancetcpxResult_t tcpxInit(tcpxDebugLogger_t):379 NET/GPUDirectTCPX : GPUDirectTCPX enable: 1Warning: please use at least NVCC 12.9 for the best DeepGEMM performancetcpxResult_t tcpxInit(tcpxDebugLogger_t):379 NET/GPUDirectTCPX : GPUDirectTCPX enable: 1Warning: please use at least NVCC 12.9 for the best DeepGEMM performancetcpxResult_t tcpxInit(tcpxDebugLogger_t):379 NET/GPUDirectTCPX : GPUDirectTCPX enable: 1Warning: please use at least NVCC 12.9 for the best DeepGEMM performance(VllmWorker TP0 pid=406) ERROR 08-16 01:07:56 [multiproc_executor.py:596] WorkerProc hit an exception. (VllmWorker TP0 pid=406) ERROR 08-16 01:07:56 [multiproc_executor.py:596] Traceback (most recent call last): (VllmWorker TP0 pid=406) ERROR 08-16 01:07:56 [multiproc_executor.py:596] File "...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: VllmWorker TP0 pid=406) ERROR 08-16 01:07:56 [multiproc_executor.py:596] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. (VllmWorker TP0 pid=406) ERROR 08-16 01:07:56 [multiproc_executor.py:596] (Vll...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: vLLM bug ### Your current environment ``` /pytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:144: operator(): block: [0,0,0], thread: [0,0,0] Assertion `idx_dim >= 0 && idx_dim = 0 && idx_dim = 0 && idx_dim = 0 &...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ytorch/aten/src/ATen/native/cuda/ScatterGatherKernel.cu:144: operator(): block: [0,0,0], thread: [0,0,0] Assertion `idx_dim >= 0 && idx_dim = 0 && idx_dim = 0 && idx_dim = 0 && idx_dim < index_size && "index out of boun...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: on3.12/dist-packages/vllm/v1/worker/gpu_worker.py", line 362, in execute_model (VllmWorker TP0 pid=406) ERROR 08-16 01:07:56 [multiproc_executor.py:596] output = self.model_runner.execute_model(scheduler_output, (VllmWo...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ectTCPX enable: 1Warning: please use at least NVCC 12.9 for the best DeepGEMM performancetcpxResult_t tcpxInit(tcpxDebugLogger_t):379 NET/GPUDirectTCPX : GPUDirectTCPX enable: 1Warning: please use at least NVCC 12.9 for...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
