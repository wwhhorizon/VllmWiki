# vllm-project/vllm#29528: [CI Failure]: mi325_8: Distributed Tests (8 GPUs)

| 字段 | 值 |
| --- | --- |
| Issue | [#29528](https://github.com/vllm-project/vllm/issues/29528) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;moe |
| 子分类 |  |
| Operator 关键词 | cuda;moe |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: mi325_8: Distributed Tests (8 GPUs)

### Issue 正文摘录

### Name of failing test `torchrun --nproc-per-node=8 ../examples/offline_inference/torchrun_dp_example.py --tp-size=2 --pp-size=1 --dp-size=4 --enable-ep` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **Failing Test:** `torchrun_dp_example.py` with data-parallel inference **Configuration:** - 8 processes (nproc-per-node=8) - tp-size=2, dp-size=4, pp-size=1 - Expert parallel enabled - External launcher (torchrun) **Failure:** `c10::DistBackendError` with `hipErrorStreamCaptureUnsupported` - "operation not permitted when stream is capturing" **Error location:** ProcessGroupNCCL watchdog thread at `finishedGPUExecutionInternal()` during stream capture **Symptoms:** - Multiple ranks (0, 1, 2+) receive SIGABRT (-6) - Rank 0 fails first at PID 75 - Shared memory leaks detected during cleanup **Likely cause:** ROCm HIP stream capture incompatibility with NCCL ProcessGroup watchdog. The watchdog thread attempts to query work completion status during CUDA graph capture, triggering HIP operations that are prohibited while stream capturing is active. This suggests CUDA graph...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: External launcher (torchrun) **Failure:** `c10::DistBackendError` with `hipErrorStreamCaptureUnsupported` - "operation not permitted when stream is capturing" **Error location:** ProcessGroupNCCL watchdog thread at `fin...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_8: Distributed Tests (8 GPUs) ci-failure ### Name of failing test `torchrun --nproc-per-node=8 ../examples/offline_inference/torchrun_dp_example.py --tp-size=2 --pp-size=1 --dp-size=4 --enable-ep` ##
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: example.py --tp-size=2 --pp-size=1 --dp-size=4 --enable-ep` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing t...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ** - 8 processes (nproc-per-node=8) - tp-size=2, dp-size=4, pp-size=1 - Expert parallel enabled - External launcher (torchrun) **Failure:** `c10::DistBackendError` with `hipErrorStreamCaptureUnsupported` - "operation no...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: parallel enabled - External launcher (torchrun) **Failure:** `c10::DistBackendError` with `hipErrorStreamCaptureUnsupported` - "operation not permitted when stream is capturing" **Error location:** ProcessGroupNCCL watc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
