# vllm-project/vllm#41415: [bug] `spawn_new_process_for_each_test` decorator broken

| 字段 | 值 |
| --- | --- |
| Issue | [#41415](https://github.com/vllm-project/vllm/issues/41415) |
| 状态 | closed |
| 标签 | bug;help wanted;ci/build |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [bug] `spawn_new_process_for_each_test` decorator broken

### Issue 正文摘录

The spawn decorator for tests is broken, it always passes no matter what the decorated function does. This is critical, because it means the tests using the decorator are not actually getting run, so we might have a bunch of silent failures. Pointed out by Claude in [this PR comment](https://github.com/vllm-project/vllm/pull/36823#discussion_r3169534100). Repro: ``` @create_new_process_for_each_test("spawn") def test_failing(): raise ValueError ``` Output: ``` -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html ============================================================================================ 1 passed, 17 warnings in 11.40s ============================================================================================ sys:1: DeprecationWarning: builtin type swigvarlink has no __module__ attribute ``` cc @vllmellm @tjtanaa

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [bug] `spawn_new_process_for_each_test` decorator broken bug;help wanted;ci/build The spawn decorator for tests is broken, it always passes no matter what the decorated function does. This is critical, because it means...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [bug] `spawn_new_process_for_each_test` decorator broken bug;help wanted;ci/build The spawn decorator for tests is broken, it always passes no matter what the decorated function does. This is critical, because it means...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
