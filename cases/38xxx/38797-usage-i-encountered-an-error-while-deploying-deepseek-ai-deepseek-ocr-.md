# vllm-project/vllm#38797: [Usage]: I encountered an error while deploying deepseek-ai/DeepSeek-OCR-2using vLLM. The logs show:

| 字段 | 值 |
| --- | --- |
| Issue | [#38797](https://github.com/vllm-project/vllm/issues/38797) |
| 状态 | open |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: I encountered an error while deploying deepseek-ai/DeepSeek-OCR-2using vLLM. The logs show:

### Issue 正文摘录

### Your current environment (APIServer pid=726567) File "/root/ocr_test/lib/python3.11/site-packages/vllm/v1/engine/utils.py", line 1031, in wait_for_engine_startup (APIServer pid=726567) raise RuntimeError( (APIServer pid=726567) RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} /root/.pyenv/versions/3.11.7/lib/python3.11/multiprocessing/resource_tracker.py:254: UserWarning: resource_tracker: There appear to be 1 leaked semaphore objects to clean up at shutdown warnings.warn('resource_tracker: There appear to be %d ' ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ation failed. See root cause above. Failed core proc(s): {} /root/.pyenv/versions/3.11.7/lib/python3.11/multiprocessing/resource_tracker.py:254: UserWarning: resource_tracker: There appear to be 1 leaked semaphore objec...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for re...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: e ### Your current environment (APIServer pid=726567) File "/root/ocr_test/lib/python3.11/site-packages/vllm/v1/engine/utils.py", line 1031, in wait_for_engine_startup (APIServer pid=726567) raise RuntimeError( (APIServ...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
