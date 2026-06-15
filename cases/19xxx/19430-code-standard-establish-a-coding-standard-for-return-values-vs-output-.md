# vllm-project/vllm#19430: [Code Standard] Establish a Coding Standard for Return Values vs. Output Parameters in CUDA Kernels

| 字段 | 值 |
| --- | --- |
| Issue | [#19430](https://github.com/vllm-project/vllm/issues/19430) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Code Standard] Establish a Coding Standard for Return Values vs. Output Parameters in CUDA Kernels

### Issue 正文摘录

> I prefer the return, it's more functional, looks more clear, and I think it's a better general c++/CUDA practice, and the compiler is nominally better at optimizing it (in general - here I think everything will be inlined anyway). So I always default to returning. _Originally posted by @ProExpertProg in https://github.com/vllm-project/vllm/pull/19233#discussion_r2136889956_ The vLLM codebase currently employs two different patterns for handling function outputs within our CUDA C++ code: 1. **Return Values**: Functions return the result directly (e.g., `OutType func(InType)`). 2. **Output Parameters**: Functions take a non-const pointer or reference to fill with the result (e.g., `void func(InType, OutType*)`). While both are valid, the lack of a formal standard can lead to inconsistencies. Adopting a clear coding standard would improve readability, maintainability, and make it easier for new contributors to understand and write idiomatic code. I would like to open this topic for discussion with the community. What are your thoughts on this? If we can reach a consensus, we can create a small guide in our contribution documentation and identify existing code that could be refactor...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: more clear, and I think it's a better general c++/CUDA practice, and the compiler is nominally better at optimizing it (in general - here I think everything will be inlined anyway). So I always default to returning. _Or...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ] Establish a Coding Standard for Return Values vs. Output Parameters in CUDA Kernels > I prefer the return, it's more functional, looks more clear, and I think it's a better general c++/CUDA practice, and the compiler...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ed anyway). So I always default to returning. _Originally posted by @ProExpertProg in https://github.com/vllm-project/vllm/pull/19233#discussion_r2136889956_ The vLLM codebase currently employs two different patterns fo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
