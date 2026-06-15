# vllm-project/vllm#15576: TP4 fails with 5090 in the mix

| 字段 | 值 |
| --- | --- |
| Issue | [#15576](https://github.com/vllm-project/vllm/issues/15576) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;crash;mismatch |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> TP4 fails with 5090 in the mix

### Issue 正文摘录

> I have a system with a 5090 + 2x4090+ A6000 > > I did build as instructions were mentioned, but I have issues when it has to use the 5090 alongside other GPUs. > > Using any pair of 4090 + 4090 or 4090 + A6000 works fine (with TP 2), but when trying to mix the 5090 with any GPU, it fails. So it also happens with TP 4. > > Errors mostly seems to be: > > ``` > (VllmWorkerProcess pid=74788) ERROR 03-23 21:33:26 [multiproc_worker_utils.py:238] Exception in worker VllmWorkerProcess while processing method determine_num_available_blocks. > (VllmWorkerProcess pid=74788) ERROR 03-23 21:33:26 [multiproc_worker_utils.py:238] Traceback (most recent call last): > [rank2]:[E323 21:33:26.170490902 ProcessGroupNCCL.cpp:1896] [PG ID 2 PG GUID 3 Rank 2] Process group watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered > CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. > For debugging consider passing CUDA_LAUNCH_BLOCKING=1 > Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. > ``` > > Log is attached here > > [vllm log.txt](https://github.com/user-attachments/files/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: n the mix stale > I have a system with a 5090 + 2x4090+ A6000 > > I did build as instructions were mentioned, but I have issues when it has to use the 5090 alongside other GPUs. > > Using any pair of 4090 + 4090 or 4090...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: GUID 3 Rank 2] Process group watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered > CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrac...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ci_build;distributed_parallel;frontend_api cuda;kernel build_error;crash;mismatch > I have a system with a 5090 + 2x4090+ A6000
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: worker VllmWorkerProcess while processing method determine_num_available_blocks. > (VllmWorkerProcess pid=74788) ERROR 03-23 21:33:26 [multiproc_worker_utils.py:238] Traceback (most recent call last): > [rank2]:[E323 21...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: TP4 fails with 5090 in the mix stale > I have a system with a 5090 + 2x4090+ A6000 > > I did build as instructions were mentioned, but I have issues when it has to use the 5090 alongside other GPUs. > > Using any pair o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
