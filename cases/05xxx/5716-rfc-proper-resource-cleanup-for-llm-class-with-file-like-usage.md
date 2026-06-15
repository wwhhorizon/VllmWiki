# vllm-project/vllm#5716: [RFC]: proper resource cleanup for LLM class with file-like usage

| 字段 | 值 |
| --- | --- |
| Issue | [#5716](https://github.com/vllm-project/vllm/issues/5716) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: proper resource cleanup for LLM class with file-like usage

### Issue 正文摘录

### Motivation. There have been quite a lot requests for releasing the resources taken by the `LLM` class, e.g. in https://github.com/vllm-project/vllm/issues/3874 and https://github.com/vllm-project/vllm/issues/4919#issuecomment-2181018405 . Currently we only have such kind of thing in the CI, introduced in https://github.com/vllm-project/vllm/pull/5357 and https://github.com/vllm-project/vllm/issues/5337 . ### Proposed Change. We can mimic the file API in python, e.g.: ```python with open("a.txt") as f: data = f.read() ``` `LLM` can support the same usage: ```python with LLM("facebook/opt-125m") as llm: output = llm.generate(prompts) ``` When we go out of the context manager, the resource will be released. We can also support the legacy usage with a new `LLM.release` method: ```python llm = LLM("facebook/opt-125m") output = llm.generate(prompts) llm.release() ``` These two usages can be combined into the same implementation: ```python class LLM: ... def __enter__(self): return self def __exit__(self, exc_type, exc_value, traceback): del self.llm_engine self.release() def release(self): # cleanup work here ``` ### Feedback Period. 1 week ### CC List. _No response_ ### Any Other T...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: proper resource cleanup for LLM class with file-like usage RFC;stale ### Motivation. There have been quite a lot requests for releasing the resources taken by the `LLM` class, e.g. in https://github.com/vllm-proj...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: suecomment-2181018405 . Currently we only have such kind of thing in the CI, introduced in https://github.com/vllm-project/vllm/pull/5357 and https://github.com/vllm-project/vllm/issues/5337 . ### Proposed Change. We ca...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
