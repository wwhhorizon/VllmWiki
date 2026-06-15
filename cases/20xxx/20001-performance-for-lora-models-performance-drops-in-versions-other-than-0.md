# vllm-project/vllm#20001: [Performance]: For LoRA models, performance drops in versions other than 0.8.2.

| 字段 | 值 |
| --- | --- |
| Issue | [#20001](https://github.com/vllm-project/vllm/issues/20001) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: For LoRA models, performance drops in versions other than 0.8.2.

### Issue 正文摘录

### Proposal to improve performance On LoRA models, It's very strange. The performance difference between vllm version 0.8.2 and other versions is extremely significant. With the same input and model, the outputs of vllm 0.8.2 and 0.9.1 are completely different—0.9.1 directly produces garbled output. Based on current testing, 0.8.2 is the most stable and delivers the best results. ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text vllm 0.9.1 ============================== System Info ============================== OS : Ubuntu 22.04.3 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.0 | packaged by conda-forge | (default, Nov 20 2021, 02:24:10) [GCC 9.4.0] (64-bit ru...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Performance]: For LoRA models, performance drops in versions other than 0.8.2. performance;stale ### Proposal to improve performance On LoRA models, It's very strange. The performance difference between vllm version 0....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.0 |...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Performance]: For LoRA models, performance drops in versions other than 0.8.2. performance;stale ### Proposal to improve performance On LoRA models, It's very strange. The performance difference between vllm version 0....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: LoRA models, performance drops in versions other than 0.8.2. performance;stale ### Proposal to improve performance On LoRA models, It's very strange. The performance difference between vllm version 0.8.2 and other versi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: etely different—0.9.1 directly produces garbled output. Based on current testing, 0.8.2 is the most stable and delivers the best results. ### Report of performance regression _No response_ ### Misc discussion on perform...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
