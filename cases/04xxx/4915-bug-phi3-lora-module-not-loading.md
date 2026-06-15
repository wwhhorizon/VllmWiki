# vllm-project/vllm#4915: [Bug]: Phi3 lora module not loading

| 字段 | 值 |
| --- | --- |
| Issue | [#4915](https://github.com/vllm-project/vllm/issues/4915) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Phi3 lora module not loading

### Issue 正文摘录

ValueError: While loading /data/llm_resume_profiles_phi3_v1, expected target modules in ['q_proj', 'k_proj', 'v_proj', 'o_proj', 'gate_proj', 'up_proj', 'down_proj', 'embed_tokens', 'lm_head'] but received ['qkv_proj', 'gate_up_proj']. Please verify that the loaded LoRA module is correct. I am unable to load LORA module with phi3-128k-instruct version. Can support for this be added? I am using VLLM docker with version 0.4.2 thanks

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ule is correct. I am unable to load LORA module with phi3-128k-instruct version. Can support for this be added? I am using VLLM docker with version 0.4.2 thanks
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Phi3 lora module not loading bug;stale ValueError: While loading /data/llm_resume_profiles_phi3_v1, expected target modules in ['q_proj', 'k_proj', 'v_proj', 'o_proj', 'gate_proj', 'up_proj', 'down_proj', 'embed_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: module not loading bug;stale ValueError: While loading /data/llm_resume_profiles_phi3_v1, expected target modules in ['q_proj', 'k_proj', 'v_proj', 'o_proj', 'gate_proj', 'up_proj', 'down_proj', 'embed_tokens', 'lm_head...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
