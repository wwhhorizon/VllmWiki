# vllm-project/vllm#5726: [Usage]: qwen2-1.5b-gptq-in4 single gpu multiprocessing deployment fail

| 字段 | 值 |
| --- | --- |
| Issue | [#5726](https://github.com/vllm-project/vllm/issues/5726) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | quantization |
| 症状 | oom |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: qwen2-1.5b-gptq-in4 single gpu multiprocessing deployment fail

### Issue 正文摘录

I try to deploy qwen2-1.5b-gptq-in4 model on one A100-80G gpu with multiprocessing, the number of process is 2, but always failed when inferencing, reporting OOM. 1.5b-gptq-int4 model should not use such amount of gpu memory. Any suggestions? Here is my argument: LLM(model="./qwen2_1.5b_int4", trust_remote_code=True, quantization='gptq', gpu_memory_utilization=0.5, max_model_len=512, enforce_eager=True)

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ocess is 2, but always failed when inferencing, reporting OOM. 1.5b-gptq-int4 model should not use such amount of gpu memory. Any suggestions? Here is my argument: LLM(model="./qwen2_1.5b_int4", trust_remote_code=True,...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: he number of process is 2, but always failed when inferencing, reporting OOM. 1.5b-gptq-int4 model should not use such amount of gpu memory. Any suggestions? Here is my argument: LLM(model="./qwen2_1.5b_int4", trust_rem...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: qwen2-1.5b-gptq-in4 single gpu multiprocessing deployment fail usage;stale I try to deploy qwen2-1.5b-gptq-in4 model on one A100-80G gpu with multiprocessing, the number of process is 2, but always failed when...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ltiprocessing, the number of process is 2, but always failed when inferencing, reporting OOM. 1.5b-gptq-int4 model should not use such amount of gpu memory. Any suggestions? Here is my argument: LLM(model="./qwen2_1.5b_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: oyment fail usage;stale I try to deploy qwen2-1.5b-gptq-in4 model on one A100-80G gpu with multiprocessing, the number of process is 2, but always failed when inferencing, reporting OOM. 1.5b-gptq-int4 model should not...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
