# vllm-project/vllm#34162: [CI Failure]:  mi325_1: ROCm GPT-OSS Eval

| 字段 | 值 |
| --- | --- |
| Issue | [#34162](https://github.com/vllm-project/vllm/issues/34162) |
| 状态 | closed |
| 标签 | rocm;ci-failure |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]:  mi325_1: ROCm GPT-OSS Eval

### Issue 正文摘录

### Name of failing test `VLLM_ROCM_USE_AITER_MHA=0 VLLM_ROCM_USE_AITER=1 VLLM_USE_AITER_UNIFIED_ATTENTION=1 pytest -s -v tests/evals/gpt_oss/test_gpqa_correctness.py --model openai/gpt-oss-20b --metric 0.58` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There was a recent regression in this test group, due to a torch API version update that breaks GPT-OSS on ROCm. This regression is expected to be fixed by: https://github.com/vllm-project/vllm/pull/34153 ### 📝 History of failing test https://buildkite.com/vllm/amd-ci/builds/4400/steps/canvas?sid=019c4133-8c53-4904-9a39-dc136650163d&tab=output

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: mi325_1: ROCm GPT-OSS Eval rocm;ci-failure ### Name of failing test `VLLM_ROCM_USE_AITER_MHA=0 VLLM_ROCM_USE_AITER=1 VLLM_USE_AITER_UNIFIED_ATTENTION=1 pytest -s -v tests/evals/gpt_oss/test_gpqa_correctnes
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: mi325_1: ROCm GPT-OSS Eval rocm;ci-failure ### Name of failing test `VLLM_ROCM_USE_AITER_MHA=0 VLLM_ROCM_USE_AITER=1 VLLM_USE_AITER_UNIFIED_ATTENTION=1 pytest -s -v tests/evals/gpt_oss/test_gpqa_correctnes...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [CI Failure]: mi325_1: ROCm GPT-OSS Eval rocm;ci-failure ### Name of failing test `VLLM_ROCM_USE_AITER_MHA=0 VLLM_ROCM_USE_AITER=1 VLLM_USE_AITER_UNIFIED_ATTENTION=1 pytest -s -v tests/evals/gpt_oss/test_gpqa_correctnes...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: Cm GPT-OSS Eval rocm;ci-failure ### Name of failing test `VLLM_ROCM_USE_AITER_MHA=0 VLLM_ROCM_USE_AITER=1 VLLM_USE_AITER_UNIFIED_ATTENTION=1 pytest -s -v tests/evals/gpt_oss/test_gpqa_correctness.py --model openai/gpt-o...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ss-20b --metric 0.58` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test There was a recent regression in t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
