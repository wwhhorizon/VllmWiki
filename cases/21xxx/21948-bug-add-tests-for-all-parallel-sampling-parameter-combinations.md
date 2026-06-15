# vllm-project/vllm#21948: [Bug]: Add tests for all parallel sampling parameter combinations

| 字段 | 值 |
| --- | --- |
| Issue | [#21948](https://github.com/vllm-project/vllm/issues/21948) |
| 状态 | open |
| 标签 | bug;good first issue;keep-open;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Add tests for all parallel sampling parameter combinations

### Issue 正文摘录

Verify that we have tests that explicitly exercise parallel sampling (`n>1` request sampling parameter) for all of the following combinations: - Via `AsyncLLM.generate`, via `LLMEngine add_request() / step()` - For `output_kind` equal to each of `CUMULATIVE`, `DELTA`, `FINAL_ONLY` Ideally a test for each of `AsyncLLM` and `LLMEngine` in the appropriate files, with `output_kind` parameterized. Additionally we can still test `LLM.generate()` but this enforces `FINAL_ONLY`. There is already a test for this one [here](https://github.com/vllm-project/vllm/blob/004203e95330ac9a878df8192619570b0770667e/tests/v1/engine/test_llm_engine.py#L120), but I'm not sure about the other cases. @sethkimmel3 has reported that the `LLMEngine` + `CUMULATIVE` combination is not working properly, this should be exposed and fixed if so.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: parallel sampling parameter combinations bug;good first issue;keep-open;stale Verify that we have tests that explicitly exercise parallel sampling (`n>1` request sampling parameter) for all of the following combinations...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: bug;good first issue;keep-open;stale Verify that we have tests that explicitly exercise parallel sampling (`n>1` request sampling parameter) for all of the following combinations: - Via `AsyncLLM.generate`, via `LLMEngi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: Add tests for all parallel sampling parameter combinations bug;good first issue;keep-open;stale Verify that we have tests that explicitly exercise parallel sampling (`n>1` request sampling parameter) for all of t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
