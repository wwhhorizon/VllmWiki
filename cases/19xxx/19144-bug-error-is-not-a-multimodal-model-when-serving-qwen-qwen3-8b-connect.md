# vllm-project/vllm#19144: [Bug]: error `is not a multimodal model` when serving `Qwen/Qwen3-8B` connected to `gr.load_chat(...)`

| 字段 | 值 |
| --- | --- |
| Issue | [#19144](https://github.com/vllm-project/vllm/issues/19144) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: error `is not a multimodal model` when serving `Qwen/Qwen3-8B` connected to `gr.load_chat(...)`

### Issue 正文摘录

### Your current environment recent vllm nightly 0.9.0 ### 🐛 Describe the bug In combination with this problem (related to "text_encoded") https://github.com/gradio-app/gradio/issues/11331 I get the error when using `gr.load_chat(...)` to send extremely long prompt and then extremely short prompt into `vllm serve`-d `Qwen/Qwen3-8B` model. Not sure if the problem is in Gradio or in vllm impl of OpenAI server ``` ERROR 06-04 11:39:38 [serving_chat.py:199] Error in preprocessing prompt inputs ERROR 06-04 11:39:38 [serving_chat.py:199] Traceback (most recent call last): ERROR 06-04 11:39:38 [serving_chat.py:199] File "/mnt/fs/venv_cu126_py312/lib/python3.12/site-packages/vllm/entrypoints/openai/serving_chat.py", line 182, in create_chat_completion ERROR 06-04 11:39:38 [serving_chat.py:199] ) = await self._preprocess_chat( ERROR 06-04 11:39:38 [serving_chat.py:199] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 06-04 11:39:38 [serving_chat.py:199] File "/mnt/fs/venv_cu126_py312/lib/python3.12/site-packages/vllm/entrypoints/openai/serving_engine.py", line 679, in _preprocess_chat ERROR 06-04 11:39:38 [serving_chat.py:199] conversation, mm_data_future = parse_chat_messages_futures( ERROR 06-04 11:39...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: error `is not a multimodal model` when serving `Qwen/Qwen3-8B` connected to `gr.load_chat(...)` bug;stale ### Your current environment recent vllm nightly 0.9.0 ### 🐛 Describe the bug In combination with this pro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: model` when serving `Qwen/Qwen3-8B` connected to `gr.load_chat(...)` bug;stale ### Your current environment recent vllm nightly 0.9.0 ### 🐛 Describe the bug In combination with this problem (related to "text_encoded") h...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
