# vllm-project/vllm#38582: [CI Failure]: tests/models/language/pooling/test_splade_sparse_pooler.py

| 字段 | 值 |
| --- | --- |
| Issue | [#38582](https://github.com/vllm-project/vllm/issues/38582) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: tests/models/language/pooling/test_splade_sparse_pooler.py

### Issue 正文摘录

### Name of failing test tests/models/language/pooling/test_splade_sparse_pooler.py::[1mtest_splade_pooler_matches_reference_formula[2-3-5-7] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Looks like `vllm/model_executor/models/bert.py:641` was changed recently (3/29). Stack trace ``` [2026-03-30T18:22:59Z] ____________ test_splade_pooler_matches_reference_formula[2-3-5-7] _____________ -- [2026-03-30T18:22:59Z] [2026-03-30T18:22:59Z] B = 2, T = 3, H = 5, V = 7 [2026-03-30T18:22:59Z] [2026-03-30T18:22:59Z] @pytest.mark.parametrize("B,T,H,V", [(2, 3, 5, 7)]) [2026-03-30T18:22:59Z] @torch.inference_mode [2026-03-30T18:22:59Z] def test_splade_pooler_matches_reference_formula(B, T, H, V): [2026-03-30T18:22:59Z] """Ensure SPLADESparsePooler forward() matches the mathematical formula: [2026-03-30T18:22:59Z] log1p(relu(logits)) -> max over sequence length (after masking).""" [2026-03-30T18:22:59Z] torch.manual_seed(0) [2026-03-30T18:22:59Z] [2026-03-30T18:22:59Z] # Prepare [B] sequences of shape [T, H] [2026-03-30T18:22:59Z] hs_list = [torch.randn(T, H) for _ in range(B)] [...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [CI Failure]: tests/models/language/pooling/test_splade_sparse_pooler.py ci-failure ### Name of failing test tests/models/language/pooling/test_splade_sparse_pooler.py::[1mtest_splade_pooler_matches_reference_formula[2-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 8:22:59Z] [2026-03-30T18:22:59Z] # MLM head (prefer BertMLMHead, fallback to Linear if unavailable) [2026-03-30T18:22:59Z] try: [2026-03-30T18:22:59Z] mlm_head = BertMLMHead(hidden_size=H, vocab_size=V, layer_norm_eps=1...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ence_formula[2-3-5-7] ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Looks like `vllm/model_executor/mo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI Failure]: tests/models/language/pooling/test_splade_sparse_pooler.py ci-failure ### Name of failing test tests/models/language/pooling/test_splade_sparse_pooler.py::[1mtest_splade_pooler_matches_reference_formula[2-3
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: -03-30T18:22:59Z] prompt_lens_tenser = torch.tensor(prompt_lens, dtype=torch.int32) [2026-03-30T18:22:59Z] token_ids = torch.tensor( [2026-03-30T18:22:59Z] [ [2026-03-30T18:22:59Z] [101, 5, 102], # Batch 0: [CLS], token...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
