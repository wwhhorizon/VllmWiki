# vllm-project/vllm#24314: [CI Failure]: v1/e2e/test_spec_decode.py::test_ngram_correctness - AssertionError: assert 68 > 70

| 字段 | 值 |
| --- | --- |
| Issue | [#24314](https://github.com/vllm-project/vllm/issues/24314) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: v1/e2e/test_spec_decode.py::test_ngram_correctness - AssertionError: assert 68 > 70

### Issue 正文摘录

### Name of failing test v1/e2e/test_spec_decode.py::test_ngram_correctness ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` # Heuristic: expect at least 70% of the prompts to match exactly # Upon failure, inspect the outputs to check for inaccuracy. > assert matches > int(0.7 * len(ref_outputs)) E AssertionError: assert 68 > 70 E + where 70 = int((0.7 * 100)) E + where 100 = len([RequestOutput(request_id=0, prompt=None, prompt_token_ids=[128000, 128006, 9125, 128007, 271, 38766, 1303, 33025, 2696, 25, 6790, 220, 2366, 18, 198, 15724, 2696, 25, 220, 1627, 10263, 220, 2366, 19, 271, 128009, 128006, 882, 128007, 271, 31121, 3041, 264, 5899, 38428, 11914, 430, 198, 310, 5829, 279, 3492, 24748, 520, 3325, 3131, 627, 310, 3041, 912, 1023, 2612, 1109, 430, 4382, 11914, 2085, 17637, 13, 128009, 128006, 78191, 128007, 271], encoder_prompt=None, encoder_prompt_token_ids=None, prompt_logprobs=None, outputs=[CompletionOutput(index=0, text='Hello everyone gathered in the room to discuss important topics', token_ids=[9906, 5127, 20802, 304, 279, 3130, 311, 4358, 3062, 13650], c...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: est_ngram_correctness ### Basic information - [x] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` # Heuristic: expect at least 7...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: v1/e2e/test_spec_decode.py::test_ngram_correctness - AssertionError: assert 68 > 70 ci-failure ### Name of failing test v1/e2e/test_spec_decode.py::test_ngram_correctness ### Basic information - [x] Flaky
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [CI Failure]: v1/e2e/test_spec_decode.py::test_ngram_correctness - AssertionError: assert 68 > 70 ci-failure ### Name of failing test v1/e2e/test_spec_decode.py::test_ngram_correctness ### Basic information - [x] Flaky...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: v1/e2e/test_spec_decode.py::test_ngram_correctness - AssertionError: assert 68 > 70 ci-failure ### Name of failing test v1/e2e/test_spec_decode.py::test_ngram_correctness ### Basic information - [x] Flaky...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: outputs=[CompletionOutput(index=0, text='Hello everyone gathered in the room to discuss important topics', token_ids=[9906, 5127, 20802, 304, 279, 3130, 311, 4358, 3062, 13650], cumulative_logprob=None, logprobs=None, f...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
