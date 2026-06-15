# vllm-project/vllm#21512: [CI Failure]: Multi-model Models Test (Extended 2)

| 字段 | 值 |
| --- | --- |
| Issue | [#21512](https://github.com/vllm-project/vllm/issues/21512) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Multi-model Models Test (Extended 2)

### Issue 正文摘录

### Name of failing test tests/models/multimodal/generation/test_common.py test_multi_image_models[qwen2_vl-test_case48] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There is a mismatch in Qwen2-VL output between vLLM and HF. ### 📝 History of failing test Started failing a week ago. Earliest known failure on main is the nightly run of https://github.com/vllm-project/vllm/commit/28a6d5423db63ba9c4df13608f6151a484bdb7c9. I suspect it is caused by #21011 Logs: https://buildkite.com/vllm/ci/builds/24174/steps/canvas?jid=0198168a-f9c4-472a-81b1-fd5163c632e6 ### CC List. cc @Isotr0py @mgoin

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [CI Failure]: Multi-model Models Test (Extended 2) ci-failure ### Name of failing test tests/models/multimodal/generation/test_common.py test_multi_image_models[qwen2_vl-test_case48] ### Basic information - [ ] Flaky te...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: qwen2_vl-test_case48] ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There is a mismatch in Qwen2-VL ou...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: Multi-model Models Test (Extended 2) ci-failure ### Name of failing test tests/models/multimodal/generation/test_common.py test_multi_image_models[qwen2_vl-test_case48] ### Basic information - [ ] Flaky t
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: g. bug in `transformers`) ### 🧪 Describe the failing test There is a mismatch in Qwen2-VL output between vLLM and HF. ### 📝 History of failing test Started failing a week ago. Earliest known failure on main is the night...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: Multi-model Models Test (Extended 2) ci-failure ### Name of failing test tests/models/multimodal/generation/test_common.py test_multi_image_models[qwen2_vl-test_case48] ### Basic information - [ ] Flaky te...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
