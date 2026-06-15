# vllm-project/vllm#21326: [Bug]: dsv3 generates all 0s output

| 字段 | 值 |
| --- | --- |
| Issue | [#21326](https://github.com/vllm-project/vllm/issues/21326) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: dsv3 generates all 0s output

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm is colocated with pytorch training environment. It's initialized with LLM() in vllm.entrypoints.llm.py , which tensor_parallel_size=32 and distributed_executor_backend="external_launcher". I'm using vllm for rollout in RL training. After every step, I call llm.sleep() to offload weights to CPU to save memory. I notice that the model (DSv3) often returns all 0s in the llm.generate(). I disabled training completely and the code only performs a cycle of 1. wake up 2. generate 3. sleep The issue still persists. When I comment out the self.reset_prefix_cache() in llm.py, the all 0s outputs occur way less often. This issue is rare on smaller models which we can use tp=8. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: n llm.py, the all 0s outputs occur way less often. This issue is rare on smaller models which we can use tp=8. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rypoints.llm.py , which tensor_parallel_size=32 and distributed_executor_backend="external_launcher". I'm using vllm for rollout in RL training. After every step, I call llm.sleep() to offload weights to CPU to save mem...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: dsv3 generates all 0s output bug;stale ### Your current environment ### 🐛 Describe the bug vllm is colocated with pytorch training environment. It's initialized with LLM() in vllm.entrypoints.llm.py , which tenso...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: vllm for rollout in RL training. After every step, I call llm.sleep() to offload weights to CPU to save memory. I notice that the model (DSv3) often returns all 0s in the llm.generate(). I disabled training completely a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
