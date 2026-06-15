# vllm-project/vllm#34956: [RFC]: Overlap weight loading with torch.compile compilation

| 字段 | 值 |
| --- | --- |
| Issue | [#34956](https://github.com/vllm-project/vllm/issues/34956) |
| 状态 | open |
| 标签 | RFC;torch.compile |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Overlap weight loading with torch.compile compilation

### Issue 正文摘录

### Motivation. torch.compile cold starts take some time - O(10s - 1m). We could totally hide a lot of the compilation time behind weight loading. NB: this doesn't mean that we won't make torch.compile faster; in general it's rare that there is a situation where it is possible to overlap compilation with something else. ### Proposed Change. Overlap weight loading with torch.compile compilation. Goto https://docs.google.com/document/d/1hssZeQv_lJlKqOr0vfpoqEUNn4ASGHVRB9a49yhcY6E/edit?tab=t.0 for the latest design. Feel free to comment on that document, or on this issue. ### Feedback Period. until 3/1/2026 ### CC List. cc @ProExpertProg @youkaichao @WoosukKwon @simon-mo @tlrmchlsmth @mgoin ### Any Other Things. Please let us know any roadblocks you think we'll run into here and things to keep in mind! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ## CC List. cc @ProExpertProg @youkaichao @WoosukKwon @simon-mo @tlrmchlsmth @mgoin ### Any Other Things. Please let us know any roadblocks you think we'll run into here and things to keep in mind! ### Before submitting...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: a situation where it is possible to overlap compilation with something else. ### Proposed Change. Overlap weight loading with torch.compile compilation. Goto https://docs.google.com/document/d/1hssZeQv_lJlKqOr0vfpoqEUNn...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [RFC]: Overlap weight loading with torch.compile compilation RFC;torch.compile ### Motivation. torch.compile cold starts take some time - O(10s - 1m). We could totally hide a lot of the compilation time behind weight lo...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: this issue. ### Feedback Period. until 3/1/2026 ### CC List. cc @ProExpertProg @youkaichao @WoosukKwon @simon-mo @tlrmchlsmth @mgoin ### Any Other Things. Please let us know any roadblocks you think we'll run into here...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: nt/d/1hssZeQv_lJlKqOr0vfpoqEUNn4ASGHVRB9a49yhcY6E/edit?tab=t.0 for the latest design. Feel free to comment on that document, or on this issue. ### Feedback Period. until 3/1/2026 ### CC List. cc @ProExpertProg @youkaich...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
