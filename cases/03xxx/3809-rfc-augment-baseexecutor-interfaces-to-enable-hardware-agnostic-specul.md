# vllm-project/vllm#3809: [RFC] Augment BaseExecutor interfaces to enable hardware-agnostic speculative decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#3809](https://github.com/vllm-project/vllm/issues/3809) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC] Augment BaseExecutor interfaces to enable hardware-agnostic speculative decoding

### Issue 正文摘录

# TL;DR: - The core speculative decoding logic is an algorithmic vLLM feature, and should not have different implementations for different backends. - This RFC proposes a BaseWorker interface, so all workers are compatible with speculative decoding. - This RFC proposes adding `init_workers`, `init_cache`, `profile_num_available_blocks` to the ExecutorBase interface - The modification to ExecutorBase will require common logic in NeuronExecutor, GPUExecutor, RayGPUExecutor to move to the LLMEngine. # Motivation At a high level, all speculative decoding consists of three phases: propose tokens, score tokens, and verify tokens. There are various implementations for proposals and verification; we can swap out a draft model for prompt-lookup-decoding or rejection sampling for typical acceptance. ![Screenshot 2024-04-02 at 5 44 44 PM](https://github.com/vllm-project/vllm/assets/950914/48488f98-5cb0-4bc6-ac78-6f2ea2f6a2b6) This level of abstraction (proposer, scorer, verifier) means that we can implement the speculative decoding framework _above_ the Worker level, such that non-GPU workers can fit within the framework. This RFC proposes the interfaces necessary to make this happen. ## Is...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [RFC] Augment BaseExecutor interfaces to enable hardware-agnostic speculative decoding RFC # TL;DR: - The core speculative decoding logic is an algorithmic vLLM feature, and should not have different implementations for...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: RFC proposes adding `init_workers`, `init_cache`, `profile_num_available_blocks` to the ExecutorBase interface - The modification to ExecutorBase will require common logic in NeuronExecutor, GPUExecutor, RayGPUExecutor...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: implementations for proposals and verification; we can swap out a draft model for prompt-lookup-decoding or rejection sampling for typical acceptance. ![Screenshot 2024-04-02 at 5 44 44 PM](https://github.com/vllm-proje...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: tive decoding. - This RFC proposes adding `init_workers`, `init_cache`, `profile_num_available_blocks` to the ExecutorBase interface - The modification to ExecutorBase will require common logic in NeuronExecutor, GPUExe...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: LLM feature, and should not have different implementations for different backends. - This RFC proposes a BaseWorker interface, so all workers are compatible with speculative decoding. - This RFC proposes adding `init_wo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
