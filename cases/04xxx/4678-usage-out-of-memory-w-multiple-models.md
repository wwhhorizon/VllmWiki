# vllm-project/vllm#4678: [Usage]: Out of Memory w/ multiple models

| 字段 | 值 |
| --- | --- |
| Issue | [#4678](https://github.com/vllm-project/vllm/issues/4678) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Out of Memory w/ multiple models

### Issue 正文摘录

### Your current environment ```text torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 224.00 MiB. GPU ``` ### How would you like to use vllm I'm running a eval framework that's evaluating multiple models. vllm doesn't seem to free the gpu memory after initialize the 2nd model (with the same variable name), how to free up gpu memory with each vLLMEngine call ``` llm = LLM(new_model) ```

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: amework that's evaluating multiple models. vllm doesn't seem to free the gpu memory after initialize the 2nd model (with the same variable name), how to free up gpu memory with each vLLMEngine call ``` llm = LLM(new_mod...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: call ``` llm = LLM(new_model) ``` performance model_support cuda oom env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ory w/ multiple models usage ### Your current environment ```text torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 224.00 MiB. GPU ``` ### How would you like to use vllm I'm running a eval framework th...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: Out of Memory w/ multiple models usage ### Your current environment ```text torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 224.00 MiB. GPU ``` ### How would you like to use vllm I'm running...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 224.00 MiB. GPU ``` ### How would you like to use vllm I'm running a eval framework that's evaluating multiple models. vllm doesn't seem to free the gpu memory after initialize the 2nd model (with the same variable name...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
