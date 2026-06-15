# vllm-project/vllm#31044: [CI Failure]: Blackwell Fusion Tests

| 字段 | 值 |
| --- | --- |
| Issue | [#31044](https://github.com/vllm-project/vllm/issues/31044) |
| 状态 | closed |
| 标签 | help wanted;torch.compile;ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;quantization |
| 子分类 |  |
| Operator 关键词 | fp8 |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: Blackwell Fusion Tests

### Issue 正文摘录

### Name of failing test FAILED tests/compile/test_fusion_attn.py::test_attention_quant_pattern[AttentionBackendEnum.TRITON_ATTN-nvidia/Llama-4-Scout-17B-16E-Instruct-FP8-TestAttentionFp8StaticQuantPatternModel--quant_fp8-dtype1-533-128-40-8] - AssertionError: Tensor-likes are not close! ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test On B200: FAILED tests/compile/test_fusion_attn.py::test_attention_quant_pattern[AttentionBackendEnum.TRITON_ATTN-nvidia/Llama-4-Scout-17B-16E-Instruct-FP8-TestAttentionFp8StaticQuantPatternModel--quant_fp8-dtype1-533-128-40-8] - AssertionError: Tensor-likes are not close! ```bash pytest -v -x tests/compile/test_fusion_attn.py::test_attention_quant_pattern ``` ### 📝 History of failing test x ### CC List. x

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [CI Failure]: Blackwell Fusion Tests help wanted;torch.compile;ci-failure ### Name of failing test FAILED tests/compile/test_fusion_attn.py::test_attention_quant_pattern[AttentionBackendEnum.TRITON_ATTN-nvidia/Llama-4-Sc
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: f failing test FAILED tests/compile/test_fusion_attn.py::test_attention_quant_pattern[AttentionBackendEnum.TRITON_ATTN-nvidia/Llama-4-Scout-17B-16E-Instruct-FP8-TestAttentionFp8StaticQuantPatternModel--quant_fp8-dtype1-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: py::test_attention_quant_pattern[AttentionBackendEnum.TRITON_ATTN-nvidia/Llama-4-Scout-17B-16E-Instruct-FP8-TestAttentionFp8StaticQuantPatternModel--quant_fp8-dtype1-533-128-40-8] - AssertionError: Tensor-likes are not...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: tests/compile/test_fusion_attn.py::test_attention_quant_pattern[AttentionBackendEnum.TRITON_ATTN-nvidia/Llama-4-Scout-17B-16E-Instruct-FP8-TestAttentionFp8StaticQuantPatternModel--quant_fp8-dtype1-533-128-40-8] - Assert...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [CI Failure]: Blackwell Fusion Tests help wanted;torch.compile;ci-failure ### Name of failing test FAILED tests/compile/test_fusion_attn.py::test_attention_quant_pattern[AttentionBackendEnum.TRITON_ATTN-nvidia/Llama-4-S...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
