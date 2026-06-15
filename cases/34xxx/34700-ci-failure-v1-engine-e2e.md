# vllm-project/vllm#34700: [CI Failure]: V1 Engine E2E

| 字段 | 值 |
| --- | --- |
| Issue | [#34700](https://github.com/vllm-project/vllm/issues/34700) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: V1 Engine E2E

### Issue 正文摘录

### Name of failing test `v1/e2e/test_spec_decode.py::test_ngram_and_suffix_correctness[speculative_config1] ` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` [2026-02-17T08:12:14Z] FAILED v1/e2e/test_spec_decode.py::test_ngram_and_suffix_correctness[speculative_config1] - assert 53 >= 66 -- [2026-02-17T08:12:14Z] + where 66 = int((0.66 * 100)) [2026-02-17T08:12:14Z] + where 100 = len([RequestOutput(request_id=0, prompt=' system \n\nCutting Knowledge Date: December 2023\nToday Date: 26 Jul 2024\n\n user \n\nplease give a ten-word sentence that\n uses the word hello at least once.\n give no other output than that simple sentence without quotes. assistant \n\n', prompt_token_ids=[128000, 128006, 9125, 128007, 271, 38766, 1303, 33025, 2696, 25, 6790, 220, 2366, 18, 198, 15724, 2696, 25, 220, 1627, 10263, 220, 2366, 19, 271, 128009, 128006, 882, 128007, 271, 31121, 3041, 264, 5899, 38428, 11914, 430, 198, 310, 5829, 279, 3492, 24748, 520, 3325, 3131, 627, 310, 3041, 912, 1023, 2612, 1109, 430, 4382, 11914, 2085, 17637, 13, 128009, 128006, 78191, 128007, 271], encoder_...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: e]: V1 Engine E2E ci-failure ### Name of failing test `v1/e2e/test_spec_decode.py::test_ngram_and_suffix_correctness[speculative_config1] ` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: V1 Engine E2E ci-failure ### Name of failing test `v1/e2e/test_spec_decode.py::test_ngram_and_suffix_correctness[speculative_config1] ` ### Basic information - [ ] Flaky test - [x] Can reproduce locally -
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 1/e2e/test_spec_decode.py::test_ngram_and_suffix_correctness[speculative_config1] ` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ###...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: peculative_config1] ` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` [2026-02-17T08:12:14Z] FAILED...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: outputs=[CompletionOutput(index=0, text='Hello everyone gathered in the room to discuss important topics', token_ids=[9906, 5127, 20802, 304, 279, 3130, 311, 4358, 3062, 13650], routed_experts=None, cumulative_logprob=N...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
