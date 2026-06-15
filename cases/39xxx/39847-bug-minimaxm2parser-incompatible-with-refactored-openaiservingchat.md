# vllm-project/vllm#39847: [Bug]: MiniMaxM2Parser incompatible with refactored OpenAIServingChat

| 字段 | 值 |
| --- | --- |
| Issue | [#39847](https://github.com/vllm-project/vllm/issues/39847) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: MiniMaxM2Parser incompatible with refactored OpenAIServingChat

### Issue 正文摘录

### Your current environment build db8a6d66b ### 🐛 Describe the bug ```python (APIServer pid=109941) ERROR 04-14 23:12:44 [serving.py:581] Error in parser creation. (APIServer pid=109941) ERROR 04-14 23:12:44 [serving.py:581] Traceback (most recent call last): (APIServer pid=109941) ERROR 04-14 23:12:44 [serving.py:581] File "/runtime/lib/python3.13/site-packages/vllm/entrypoints/openai/chat_completion/serving.py", line 571, in chat_completion_stream_generator (APIServer pid=109941) ERROR 04-14 23:12:44 [serving.py:581] self.parser_cls( (APIServer pid=109941) ERROR 04-14 23:12:44 [serving.py:581] ~~~~~~~~~~~~~~~^ (APIServer pid=109941) ERROR 04-14 23:12:44 [serving.py:581] tokenizer, (APIServer pid=109941) ERROR 04-14 23:12:44 [serving.py:581] ^^^^^^^^^^ (APIServer pid=109941) ERROR 04-14 23:12:44 [serving.py:581] request.tools, (APIServer pid=109941) ERROR 04-14 23:12:44 [serving.py:581] ^^^^^^^^^^^^^^ (APIServer pid=109941) ERROR 04-14 23:12:44 [serving.py:581] chat_template_kwargs=chat_template_kwargs, (APIServer pid=109941) ERROR 04-14 23:12:44 [serving.py:581] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (APIServer pid=109941) ERROR 04-14 23:12:44 [serving.py:581] ) (APIServer...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ible with refactored OpenAIServingChat bug ### Your current environment build db8a6d66b ### 🐛 Describe the bug ```python (APIServer pid=109941) ERROR 04-14 23:12:44 [serving.py:581] Error in parser creation. (APIServer...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ^^^ (APIServer pid=109941) ERROR 04-14 23:12:44 [serving.py:581] request.tools, (APIServer pid=109941) ERROR 04-14 23:12:44 [serving.py:581] ^^^^^^^^^^^^^^ (APIServer pid=109941) ERROR 04-14 23:12:44 [serving.py:581] ch...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
