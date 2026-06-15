# vllm-project/vllm#19499: [Performance]: performance of v0 engine vs v1 engine on Qwen/Qwen2.5-1.5B-Instruct model

| 字段 | 值 |
| --- | --- |
| Issue | [#19499](https://github.com/vllm-project/vllm/issues/19499) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: performance of v0 engine vs v1 engine on Qwen/Qwen2.5-1.5B-Instruct model

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression Hi Team, we're comparing the performance of vllm 0.9.0.1 (with v1 engine) and vllm 0.6.4.post1 (with v0 engine) serving Qwen/Qwen2.5-1.5B-Instruct model. We're seeing performance downgrade however with the newer version and v1 engine. Could you please suggest what might be the reasons? For example, what settings that we are not using are recommended to boost performance? what settings we're using cause performance downgrade? Thank you! Environment: GCP g2-standard-16 machine with NVIDIA 1 L4 GPUs vllm 0.9.0.1 serve command: `vllm serve Qwen/Qwen2.5-1.5B-Instruct --dtype="float16" --max-model-len 3072 --max-num-seqs 256 --kv-cache-dtype auto --tensor-parallel-size 1 --gpu-memory-utilization 0.88 --disable-log-requests --disable-custom-all-reduce --disable-sliding-window --swap-space 2` vllm 0.6.4.post1 serve command: `vllm serve Qwen/Qwen2.5-1.5B-Instruct --dtype="float16" --max-model-len 3072 --max-num-seqs 256 --kv-cache-dtype auto --tensor-parallel-size 1 --gpu-memory-utilization 0.88 --disable-log-requests --disable-custom-all-reduce --disable-sliding-window --swap-space 2 --num-scheduler-ste...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: nstruct model. We're seeing performance downgrade however with the newer version and v1 engine. Could you please suggest what might be the reasons? For example, what settings that we are not using are recommended to boo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: roposal to improve performance _No response_ ### Report of performance regression Hi Team, we're comparing the performance of vllm 0.9.0.1 (with v1 engine) and vllm 0.6.4.post1 (with v0 engine) serving Qwen/Qwen2.5-1.5B...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ``` NFO 06-11 09:57:07 [__init__.py:243] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Performance]: performance of v0 engine vs v1 engine on Qwen/Qwen2.5-1.5B-Instruct model performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression Hi Team, we're comparing...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: f v0 engine vs v1 engine on Qwen/Qwen2.5-1.5B-Instruct model performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression Hi Team, we're comparing the performance of vllm 0.9....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
