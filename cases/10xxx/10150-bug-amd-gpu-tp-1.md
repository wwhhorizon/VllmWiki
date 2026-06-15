# vllm-project/vllm#10150: [Bug]: AMD GPU tp>1 模型上线卡住

| 字段 | 值 |
| --- | --- |
| Issue | [#10150](https://github.com/vllm-project/vllm/issues/10150) |
| 状态 | closed |
| 标签 | bug;rocm;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AMD GPU tp>1 模型上线卡住

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug tp>1，模型上线卡住，显存占用但是利用率为0， ruijie:849:1185 [0] NCCL INFO Connected all rings comm 0x55a968d59160 nRanks 02 busId 3000 ruijie:849:1185 [0] NCCL INFO Connected all trees ruijie:849:1185 [0] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 256 | 256 ruijie:849:1185 [0] NCCL INFO 64 coll channels, 0 nvls channels, 64 p2p channels, 2 p2p channels per peer ruijie:1122:1186 [1] NCCL INFO Connected all rings comm 0x557519a97630 nRanks 02 busId c3000 ruijie:1122:1186 [1] NCCL INFO Connected all trees ruijie:1122:1186 [1] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 256 | 256 ruijie:1122:1186 [1] NCCL INFO 64 coll channels, 0 nvls channels, 64 p2p channels, 2 p2p channels per peer ruijie:849:1185 [0] NCCL INFO comm 0x55a968d59160 rank 0 nranks 2 cudaDev 0 busId 3000 commId 0xdf38d22419fae72b localSize 192 used 134323280 bytes - Init COMPLETE ruijie:1122:1186 [1] NCCL INFO comm 0x557519a97630 rank 1 nranks 2 cudaDev 1 busId c3000 commId 0xdf38d22419fae72b localSize 192 used 134323280 bytes - Init COMPLETE ruijie:1122:1663 [1] NCCL INFO Channel 32 : 1[c3000] -> 0[3000] via SHM/direct/direct comm 0x557519a97630...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ning out of memory, consider decreasing `gpu_memory_utilization` or enforcing eager mode. You can also reduce the `max_num_seqs` as needed to decrease memory usage. (VllmWorkerProcess pid=1122) INFO 11-08 09:37:40 model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: AMD GPU tp>1 模型上线卡住 bug;rocm;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug tp>1，模型上线卡住，显存占用但是利用率为0， ruijie:849:1185 [0] NCCL INFO Connected all rings comm 0x55a968d...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: AMD GPU tp>1 模型上线卡住 bug;rocm;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug tp>1，模型上线卡住，显存占用但是利用率为0， ruijie:849:1185 [0] NCCL INFO Connected all rings comm 0x55a968d...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf;oom env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: i_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf;oom env_dependency Your current e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
