# vllm-project/vllm#18162: [Bug]: make `test_openai_schema.py` pass, enable it in CI

| 字段 | 值 |
| --- | --- |
| Issue | [#18162](https://github.com/vllm-project/vllm/issues/18162) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: make `test_openai_schema.py` pass, enable it in CI

### Issue 正文摘录

This is a follow up to PR #17664 and issues like #17037 and #17038. As of the time of this writing, the only sub-test in `tests/entrypoints/openai/test_openai_schema.py` that consistently fails is `POST /tokenize` caused by https://github.com/vllm-project/vllm/blob/98ea35601cdb34fdd618f965e7bcc3cb02a677fc/vllm/entrypoints/chat_utils.py#L1083 when `part_type` is `"file"`. The expected response is 200 as documented by the OpenAPI spec. How should we make this test pass? This is a requirement to eventually enabling the test in CI by removing `--ignore=entrypoints/openai/test_openai_schema.py` in `test-pipeline.yaml`. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: make `test_openai_schema.py` pass, enable it in CI bug This is a follow up to PR #17664 and issues like #17037 and #17038. As of the time of this writing, the only sub-test in `tests/entrypoints/openai/test_opena...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: make `test_openai_schema.py` pass, enable it in CI bug This is a follow up to PR #17664 and issues like #17037 and #17038. As of the time of this writing, the only sub-test in `tests/entrypoints/openai/test_opena...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
