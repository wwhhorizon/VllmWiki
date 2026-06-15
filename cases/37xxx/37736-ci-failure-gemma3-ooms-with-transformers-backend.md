# vllm-project/vllm#37736: [CI Failure]:  Gemma3 OOMs with transformers backend

| 字段 | 值 |
| --- | --- |
| Issue | [#37736](https://github.com/vllm-project/vllm/issues/37736) |
| 状态 | open |
| 标签 | rocm;ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  Gemma3 OOMs with transformers backend

### Issue 正文摘录

### Test group mi250_1: Multi-Modal Models (Standard) 2: qwen3 + gemma ### Describe the failing test This is not exactly a test failure, but it has been recommended to investigate further the OOMing event of Gemma3, which is a 4B model. The intuition here is that the fake tensor that is used for profiling is large enough that exceeds the 64 GB of MI250 GPUs. However, it has been suggested that this is still weird. ### 📝 History of failing test https://github.com/vllm-project/vllm/pull/37610#issuecomment-4102286515 ### CC List. @DarkLight1337 (for transparency)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: Gemma3 OOMs with transformers backend rocm;ci-failure ### Test group mi250_1: Multi-Modal Models (Standard) 2: qwen3 + gemma ### Describe the failing test This is not exactly a test failure, but it has bee...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: Gemma3 OOMs with transformers backend rocm;ci-failure ### Test group mi250_1: Multi-Modal Models (Standard) 2: qwen3 + gemma ### Describe the failing test This is not exactly a test failure, but it has bee...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [CI Failure]: Gemma3 OOMs with transformers backend rocm;ci-failure ### Test group mi250_1: Multi-Modal Models (Standard) 2: qwen3 + gemma ### Describe the failing test This is not exactly a test failure, but it has bee...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI Failure]: Gemma3 OOMs with transformers backend rocm;ci-failure ### Test group mi250_1: Multi-Modal Models (Standard) 2: qwen3 + gemma ### Describe the failing test This is not exactly a test failure, but it has b
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [CI Failure]: Gemma3 OOMs with transformers backend rocm;ci-failure ### Test group mi250_1: Multi-Modal Models (Standard) 2: qwen3 + gemma ### Describe the failing test This is not exactly a test failure, but it has bee...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
