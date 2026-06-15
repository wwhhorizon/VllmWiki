# vllm-project/vllm#14610: [RFC]: A proper way to deal with 'Ray does not allocate any GPUs on the driver node' && 'No CUDA GPUs are available' problem

| 字段 | 值 |
| --- | --- |
| Issue | [#14610](https://github.com/vllm-project/vllm/issues/14610) |
| 状态 | closed |
| 标签 | RFC;ray;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api |
| 子分类 | race_cond |
| Operator 关键词 | cuda |
| 症状 | mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: A proper way to deal with 'Ray does not allocate any GPUs on the driver node' && 'No CUDA GPUs are available' problem

### Issue 正文摘录

### Motivation. When deploying platforms based on the Ray framework, such as Ray Serve and Ray LLM, together with vLLM's OpenAI server, the errors "No CUDA GPUs are available" or "Ray does not allocate any GPUs on the driver node" have become recurring issues. In this issue, I will provide a detailed analysis of these problems, along with a brief solution, experimental records. I sincerely invite developers from the Ray and vLLM communities to participate in the discussion, point out any shortcomings, and share your suggestions! For Ray LLM and Ray Serve documentation: Ray LLM : Ray LLM Documentation Ray Serve : Ray Serve vLLM Example Introduction The issue can be summarized simply: the framework design of vLLM does not fully accommodate LLMEngine running within a placement group . The process that creates RayDistributedExecutor , which serves as the entry point, must have access to a GPU while not occupying GPU resources within Ray . This conflicts with the typical configuration of Ray Serve . Additionally, since vLLM always requests a whole number of GPUs when world_size &gt; 1 , it is not possible to work around this limitation by allocating fractional GPUs. ![Image](https://gi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: I sincerely invite developers from the Ray and vLLM communities to participate in the discussion, point out any shortcomings, and share your suggestions! For Ray LLM and Ray Serve documentation: Ray LLM : Ray LLM Docume...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: to deal with 'Ray does not allocate any GPUs on the driver node' && 'No CUDA GPUs are available' problem RFC;ray;stale ### Motivation. When deploying platforms based on the Ray framework, such as Ray Serve and Ray LLM,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: GPUs on the driver node' && 'No CUDA GPUs are available' problem RFC;ray;stale ### Motivation. When deploying platforms based on the Ray framework, such as Ray Serve and Ray LLM, together with vLLM's OpenAI server, the...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ntly asked questions. correctness distributed_parallel;frontend_api cuda mismatch env_dependency Motivation.
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: g in Ray Serve ). This explains why the issue has not become a critical blocker—under the current configuration, execution is still possible. TP = 1 with GPU assignment (as mentioned earlier, using an appropriate config...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
