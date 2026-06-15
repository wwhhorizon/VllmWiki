# vllm-project/vllm#28683: [CI Failure]: `models/language/pooling_mteb_test/mteb_utils.py:131:  KeyError: 'data'`

| 字段 | 值 |
| --- | --- |
| Issue | [#28683](https://github.com/vllm-project/vllm/issues/28683) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: `models/language/pooling_mteb_test/mteb_utils.py:131:  KeyError: 'data'`

### Issue 正文摘录

### Name of failing test `tests/entrypoints/pooling/correctness$ pytest test_mteb_score.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/ci/builds/38880#019a7ea5-298f-4d57-8eee-8d43a70f490e ```bash [2025-11-13T19:58:41Z] def get_score(self, query, corpus): [2025-11-13T19:58:41Z] response = requests.post( [2025-11-13T19:58:41Z] self.url, [2025-11-13T19:58:41Z] json={ [2025-11-13T19:58:41Z] "model": self.model_name, [2025-11-13T19:58:41Z] "text_1": query, [2025-11-13T19:58:41Z] "text_2": corpus, [2025-11-13T19:58:41Z] "truncate_prompt_tokens": -1, [2025-11-13T19:58:41Z] }, [2025-11-13T19:58:41Z] ).json() [2025-11-13T19:58:41Z] > return response["data"][0]["score"] [2025-11-13T19:58:41Z] E KeyError: 'data' [2025-11-13T19:58:41Z] [2025-11-13T19:58:41Z] models/language/pooling_mteb_test/mteb_utils.py:131: KeyError ``` ### 📝 History of failing test Just now ### CC List. _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: `models/language/pooling_mteb_test/mteb_utils.py:131: KeyError: 'data'` ci-failure ### Name of failing test `tests/entrypoints/pooling/correctness$ pytest test_mteb_score.py` ### Basic information - [ ]
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [CI Failure]: `models/language/pooling_mteb_test/mteb_utils.py:131: KeyError: 'data'` ci-failure ### Name of failing test `tests/entrypoints/pooling/correctness$ pytest test_mteb_score.py` ### Basic information - [ ] Fl...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: t test_mteb_score.py` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test https://buildkite.com/vllm/ci/buil...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: et_score(self, query, corpus): [2025-11-13T19:58:41Z] response = requests.post( [2025-11-13T19:58:41Z] self.url, [2025-11-13T19:58:41Z] json={ [2025-11-13T19:58:41Z] "model": self.model_name, [2025-11-13T19:58:41Z] "tex...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: `models/language/pooling_mteb_test/mteb_utils.py:131: KeyError: 'data'` ci-failure ### Name of failing test `tests/entrypoints/pooling/correctness$ pytest test_mteb_score.py` ### Basic information - [ ] Fl...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
