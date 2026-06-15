# vllm-project/vllm#39678: [RFC]: Async parallel startup for EngineCore processes in DP/TP scenarios

| 字段 | 值 |
| --- | --- |
| Issue | [#39678](https://github.com/vllm-project/vllm/issues/39678) |
| 状态 | open |
| 标签 | rocm;RFC |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;hardware_porting;model_support |
| 子分类 | race_cond |
| Operator 关键词 | cuda |
| 症状 | slowdown |
| 根因提示 | env_dependency;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Async parallel startup for EngineCore processes in DP/TP scenarios

### Issue 正文摘录

### Motivation. In multi-GPU deployments using Data Parallelism (DP) or Tensor Parallelism (TP), vLLM starts subprocess workers **sequentially**. Each `proc.start()` / `WorkerProc.make_worker_process()` call takes approximately 12 seconds on H100 (NCCL init + device setup), so total startup time grows linearly with the number of processes: | Configuration | Sequential startup time | |---|---| | DP=8, TP=1 (8 EngineCore procs) | ~96 s | | DP=1, TP=8 (8 Worker procs per EngineCore) | ~96 s | This O(N) startup latency is a significant barrier for large-scale production deployments, especially in elastic scaling scenarios where new DP shards need to come online quickly. **Correctness bug on non-CUDA platforms.** The current implementation temporarily patches `CUDA_VISIBLE_DEVICES` (or the platform equivalent) in the **parent** process via `patch.dict(os.environ, ...)` before calling `proc.start()`. When multiple EngineCore processes are started concurrently (or even sequentially with tight timing), this creates a race condition: a child process may inherit the environment variable intended for a different child. This affects Ascend NPU (`ASCEND_RT_VISIBLE_DEVICES`), ROCm (`HIP_VISIBLE...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: RFC]: Async parallel startup for EngineCore processes in DP/TP scenarios rocm;RFC ### Motivation. In multi-GPU deployments using Data Parallelism (DP) or Tensor Parallelism (TP), vLLM starts subprocess workers **sequent...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ncy is a significant barrier for large-scale production deployments, especially in elastic scaling scenarios where new DP shards need to come online quickly. **Correctness bug on non-CUDA platforms.** The current implem...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ), so total startup time grows linearly with the number of processes: | Configuration | Sequential startup time | |---|---| | DP=8, TP=1 (8 EngineCore procs) | ~96 s | | DP=1, TP=8 (8 Worker procs per EngineCore) | ~96...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: DP=1, TP=8 (8 Worker procs per EngineCore) | ~96 s | This O(N) startup latency is a significant barrier for large-scale production deployments, especially in elastic scaling scenarios where new DP shards need to come on...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: | ~96 s | This O(N) startup latency is a significant barrier for large-scale production deployments, especially in elastic scaling scenarios where new DP shards need to come online quickly. **Correctness bug on non-CUDA...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
