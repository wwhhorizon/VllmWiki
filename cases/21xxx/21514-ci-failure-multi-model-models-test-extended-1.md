# vllm-project/vllm#21514: [CI Failure]: Multi-model Models Test (Extended 1)

| 字段 | 值 |
| --- | --- |
| Issue | [#21514](https://github.com/vllm-project/vllm/issues/21514) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Multi-model Models Test (Extended 1)

### Issue 正文摘录

### Name of failing test models/multimodal/pooling/test_jinavl_reranker.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The model is being converted using `as_seq_cls_model` even though the original model supports classification already, resulting in an incorrect `score` module which leads to weight mismatch during loading. ### 📝 History of failing test I have fixed the issue in #21470 by refactoring the model conversion logic. ### CC List. cc @noooop

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: Multi-model Models Test (Extended 1) ci-failure ### Name of failing test models/multimodal/pooling/test_jinavl_reranker.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: st_jinavl_reranker.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test The model is being converted using...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Multi-model Models Test (Extended 1) ci-failure ### Name of failing test models/multimodal/pooling/test_jinavl_reranker.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused b
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lready, resulting in an incorrect `score` module which leads to weight mismatch during loading. ### 📝 History of failing test I have fixed the issue in #21470 by refactoring the model conversion logic. ### CC List. cc @...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Multi-model Models Test (Extended 1) ci-failure ### Name of failing test models/multimodal/pooling/test_jinavl_reranker.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
