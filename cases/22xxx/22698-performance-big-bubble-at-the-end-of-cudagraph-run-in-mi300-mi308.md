# vllm-project/vllm#22698: [Performance]: Big bubble at the end of cudagraph run in MI300/MI308

| 字段 | 值 |
| --- | --- |
| Issue | [#22698](https://github.com/vllm-project/vllm/issues/22698) |
| 状态 | closed |
| 标签 | performance;rocm;unstale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;hardware_porting;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Big bubble at the end of cudagraph run in MI300/MI308

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression In MI300/MI308, I always find this behavior in many models when turning on full_cuda_graph option. There is a big bubble at the end of each cudagraph run, right before the compute_logits method: ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : 19.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-6.4.1 25184 c87081df219c42dc27c5b6d86c0525bc7d01f727) CMake version : version 3.31.6 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+gitf717b2a Is debug build : False CUDA used to build PyTorch : N/A ROCM used to build PyTorch : 6.4.43483-a187df25c ============================== Python Environment ============================== Python version : 3.12.11 (main, Jun 4 2025, 08:56:18) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-5.15.0-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : 19.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-6.4.1 25184 c87081df219c42dc27c5b6d86c0525b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Performance]: Big bubble at the end of cudagraph run in MI300/MI308 performance;rocm;unstale ### Proposal to improve performance _No response_ ### Report of performance regression In MI300/MI308, I always find this beh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: formance regression In MI300/MI308, I always find this behavior in many models when turning on full_cuda_graph option. There is a big bubble at the end of each cudagraph run, right before the compute_logits method: ###...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Big bubble at the end of cudagraph run in MI300/MI308 performance;rocm;unstale ### Proposal to improve performance _No response_ ### Report of performance regression In MI300/MI308, I always find this behavior in many m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression In MI300/MI308, I always find this behavior in many models when turning on full_cuda_graph option. There is a big bubble at the end of ea...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
