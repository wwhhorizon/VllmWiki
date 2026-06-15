# vllm-project/vllm#39358: [vLLM IR] E2E lowering tests

| 字段 | 值 |
| --- | --- |
| Issue | [#39358](https://github.com/vllm-project/vllm/issues/39358) |
| 状态 | open |
| 标签 | vllm-ir |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [vLLM IR] E2E lowering tests

### Issue 正文摘录

Current lowering tests are very one-off: just invoke the `rms_norm` op and manually look at the lowering dictionary in the pass. As more ops are added, we should make sure this testing is robust: per-op, unit tests (with fake ops), and E2E tests on real models. We should add the following tests: - per-op lowering tests, making sure all (supported) op implementations are lowered correctly (part of #38782). These should make sure all implementation and `supports_args` functions are properly executable by Dynamo. We should also check that `supports_args` does not specialize on the batch size by invoking it on an unbacked integer. - lowering unit tests, using fake ops & implementations. Crucially it should stress-test implementation selection by using fake ops with complex `supports_args`. - E2E correctness tests, comparing the lowering pipeline with `ir_enable_torch_wrap=False` where implementations get traced through with Dynamo directly, and comparing with no lowering where IR ops remain in the Inductor-produced artifact. This should compare outputs and confirm the correct number of ops are lowered into chosen implementations.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: cutable by Dynamo. We should also check that `supports_args` does not specialize on the batch size by invoking it on an unbacked integer. - lowering unit tests, using fake ops & implementations. Crucially it should stre...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ness tests, comparing the lowering pipeline with `ir_enable_torch_wrap=False` where implementations get traced through with Dynamo directly, and comparing with no lowering where IR ops remain in the Inductor-produced ar...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ing is robust: per-op, unit tests (with fake ops), and E2E tests on real models. We should add the following tests: - per-op lowering tests, making sure all (supported) op implementations are lowered correctly (part of...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [vLLM IR] E2E lowering tests vllm-ir Current lowering tests are very one-off: just invoke the `rms_norm` op and manually look at the lowering dictionary in the pass. As more ops are added, we should make sure this testi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
