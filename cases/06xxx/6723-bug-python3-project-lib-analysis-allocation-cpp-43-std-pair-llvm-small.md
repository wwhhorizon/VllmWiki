# vllm-project/vllm#6723: [Bug]: python3: /project/lib/Analysis/Allocation.cpp:43: std::pair<llvm::SmallVector<unsigned int>, llvm::SmallVector<unsigned int> > mlir::triton::getCvtOrder(mlir::Attribute, mlir::Attribute): Assertion `!(srcMmaLayout && dstMmaLayout && !srcMmaLayout.isAmpere()) && "mma -> mma layout conversion is only supported on Ampere"' failed. Aborted (core dumped)

| 字段 | 值 |
| --- | --- |
| Issue | [#6723](https://github.com/vllm-project/vllm/issues/6723) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: python3: /project/lib/Analysis/Allocation.cpp:43: std::pair<llvm::SmallVector<unsigned int>, llvm::SmallVector<unsigned int> > mlir::triton::getCvtOrder(mlir::Attribute, mlir::Attribute): Assertion `!(srcMmaLayout && dstMmaLayout && !srcMmaLayout.isAmpere()) && "mma -> mma layout conversion is only supported on Ampere"' failed. Aborted (core dumped)

### Issue 正文摘录

### Your current environment INFO 07-24 03:31:45 logger.py:36] Received request chat-d9aa01ce9bad4c01a22eb2d07e2c8392: prompt: ' user \n\n你是谁 assistant \n\n', params: SamplingParams(n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=0.7, top_p=1.0, top_k=-1, min_p=0.0, seed=None, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], stop_token_ids=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=None, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None), prompt_token_ids: [128000, 128006, 882, 128007, 271, 57668, 21043, 112471, 128009, 128006, 78191, 128007, 271], lora_request: None, prompt_adapter_request: None. INFO 07-24 03:31:45 async_llm_engine.py:173] Added request chat-d9aa01ce9bad4c01a22eb2d07e2c8392. python3: /project/lib/Analysis/Allocation.cpp:43: std::pair , llvm::SmallVector > mlir::triton::getCvtOrder(mlir::Attribute, mlir::Attribute): Assertion `!(srcMmaLayout && dstMmaLayout && !srcMmaLayout.isAmpere()) && "mma -> mma layout conversion is only supported on Ampere"' failed. Aborted (core dumped)...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: python3: /project/lib/Analysis/Allocation.cpp:43: std::pair<llvm::SmallVector<unsigned int>, llvm::SmallVector<unsigned int> > mlir::triton::getCvtOrder(mlir::Attribute, mlir::Attribute): Assertion `!(srcMmaLayou...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ut && dstMmaLayout && !srcMmaLayout.isAmpere()) && "mma -> mma layout conversion is only supported on Ampere"' failed. Aborted (core dumped) bug ### Your current environment INFO 07-24 03:31:45 logger.py:36] Received re...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: riton::getCvtOrder(mlir::Attribute, mlir::Attribute): Assertion `!(srcMmaLayout && dstMmaLayout && !srcMmaLayout.isAmpere()) && "mma -> mma layout conversion is only supported on Ampere"' failed. Aborted (core dumped) b...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: llvm::SmallVector<unsigned int>, llvm::SmallVector<unsigned int> > mlir::triton::getCvtOrder(mlir::Attribute, mlir::Attribute): Assertion `!(srcMmaLayout && dstMmaLayout && !srcMmaLayout.isAmpere()) && "mma -> mma layou...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ### Your current environment INFO 07-24 03:31:45 logger.py:36] Received request chat-d9aa01ce9bad4c01a22eb2d07e2c8392: prompt: ' user \n\n你是谁 assistant \n\n', params: SamplingParams(n=1, best_of=1, presence_penalty=0.0,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
