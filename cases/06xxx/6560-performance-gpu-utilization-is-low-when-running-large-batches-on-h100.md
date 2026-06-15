# vllm-project/vllm#6560: [Performance]: GPU utilization is low when running large batches on H100

| 字段 | 值 |
| --- | --- |
| Issue | [#6560](https://github.com/vllm-project/vllm/issues/6560) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | fp8 |
| 症状 |  |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: GPU utilization is low when running large batches on H100

### Issue 正文摘录

### Proposal to improve performance Hi all, I'm running vicuna 13B on H100 using fp8, and I find when batch size is large, say 64 or 96, the gpu utilization is low, about 60%, this is an important cause for the low performance. I did some analysis, part of this is caused by the schedule and post process of requests. Do you have any plans for improving this? ![image](https://github.com/user-attachments/assets/958fb6f3-baef-417b-ba9b-92f39d4bb0db) ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ```

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: sal to improve performance Hi all, I'm running vicuna 13B on H100 using fp8, and I find when batch size is large, say 64 or 96, the gpu utilization is low, about 60%, this is an important cause for the low performance....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: s large, say 64 or 96, the gpu utilization is low, about 60%, this is an important cause for the low performance. I did some analysis, part of this is caused by the schedule and post process of requests. Do you have any...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ]: GPU utilization is low when running large batches on H100 performance;stale ### Proposal to improve performance Hi all, I'm running vicuna 13B on H100 using fp8, and I find when batch size is large, say 64 or 96, the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Performance]: GPU utilization is low when running large batches on H100 performance;stale ### Proposal to improve performance Hi all, I'm running vicuna 13B on H100 using fp8, and I find when batch size is large, say 6...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: /assets/958fb6f3-baef-417b-ba9b-92f39d4bb0db) ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
