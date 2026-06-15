# vllm-project/vllm#11638: [Feature]: Avoid KV Cache and offload Model weights in RL workloads

| 字段 | 值 |
| --- | --- |
| Issue | [#11638](https://github.com/vllm-project/vllm/issues/11638) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Avoid KV Cache and offload Model weights in RL workloads

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Thanks for the awesome inference library! I'm writing to request two features that would be beneficial to RL post-training workloads. In online PPO (or GRPO, online DPO), the policy model will perform auto-regressive generation (using vLLM or other inference engines) and fwd + bwd computation with training infrastructure. Therefore, in the training stage, we hope to free the KVCache and even offload the model parameter stored in the vLLM (as the model parallel strategies during generation and training could be different). Therefore, we propose two sets of APIs in the `Worker`, `GPUExecutor`, `LLMEngine`, and `LLM` classes and one model init choice: - **`free_cache_engine()` and `init_cache_engine()`**: The users can call the `free_cache_engine` from an instance of `LLM` and the calling chain could be `LLM.free_cache_engine() -> LLMEngine.free_cache_engine() -> GPUExecutor.free_cache_engine() -> Worker.free_cache_engine()`. A similar calling chain applies to `init_cache_engine()` while the `Worker.init_cache_engine()` will simply call the `_init_cache_engine()` in the Worker class. After generation, the RL framework can call the `llm.free_cac...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ference library! I'm writing to request two features that would be beneficial to RL post-training workloads. In online PPO (or GRPO, online DPO), the policy model will perform auto-regressive generation (using vLLM or o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: `free_cache_engine` and `offload_model_weights`, we have to disable the _CUDAGraph_, which could reduce the generation throughput. One issue in SGLang observes a similar problem: https://github.com/sgl-project/sglang/is...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Feature]: Avoid KV Cache and offload Model weights in RL workloads feature request ### 🚀 The feature, motivation and pitch Thanks for the awesome inference library! I'm writing to request two features that would be ben...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Avoid KV Cache and offload Model weights in RL workloads feature request ### 🚀 The feature, motivation and pitch Thanks for the awesome inference library! I'm writing to request two features that would be ben...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: `, we have to disable the _CUDAGraph_, which could reduce the generation throughput. One issue in SGLang observes a similar problem: https://github.com/sgl-project/sglang/issues/2542 Currently, in veRL, we simply set `e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
