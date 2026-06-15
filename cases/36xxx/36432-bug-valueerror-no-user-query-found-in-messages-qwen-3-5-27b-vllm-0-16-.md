# vllm-project/vllm#36432: [Bug]: ValueError: No user query found in messages QWEN 3.5 27B VLLM 0.16.0 NIGHTLY

| 字段 | 值 |
| --- | --- |
| Issue | [#36432](https://github.com/vllm-project/vllm/issues/36432) |
| 状态 | open |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ValueError: No user query found in messages QWEN 3.5 27B VLLM 0.16.0 NIGHTLY

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug (APIServer pid=1) ERROR 03-09 02:34:48 [hf.py:484] An error occurred in `transformers` while applying chat template (APIServer pid=1) ERROR 03-09 02:34:48 [hf.py:484] Traceback (most recent call last): (APIServer pid=1) ERROR 03-09 02:34:48 [hf.py:484] File "/usr/local/lib/python3.12/dist-packages/vllm/renderers/hf.py", line 472, in safe_apply_chat_template (APIServer pid=1) ERROR 03-09 02:34:48 [hf.py:484] return tokenizer.apply_chat_template( (APIServer pid=1) ERROR 03-09 02:34:48 [hf.py:484] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (APIServer pid=1) ERROR 03-09 02:34:48 [hf.py:484] File "/usr/local/lib/python3.12/dist-packages/transformers/tokenization_utils_base.py", line 1667, in apply_chat_template (APIServer pid=1) ERROR 03-09 02:34:48 [hf.py:484] rendered_chat, generation_indices = render_jinja_template( (APIServer pid=1) ERROR 03-09 02:34:48 [hf.py:484] ^^^^^^^^^^^^^^^^^^^^^^ (APIServer pid=1) ERROR 03-09 02:34:48 [hf.py:484] File "/usr/local/lib/python3.12/dist-packages/transformers/utils/chat_template_utils.py", line 539, in render_jinja_template (APIServer pid=1) ERROR 03-09 02:34:48 [hf.py:484] rendered_chat = compiled_templat...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: e (APIServer pid=1) ERROR 03-09 02:34:48 [hf.py:484] rendered_chat = compiled_template.render( (APIServer pid=1) ERROR 03-09 02:34:48 [hf.py:484] ^^^^^^^^^^^^^^^^^^^^^^^^^ (APIServer pid=1) ERROR 03-09 02:34:48 [hf.py:4...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: ValueError: No user query found in messages QWEN 3.5 27B VLLM 0.16.0 NIGHTLY bug ### Your current environment ### 🐛 Describe the bug (APIServer pid=1) ERROR 03-09 02:34:48 [hf.py:484] An error occurred in `transf...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: es. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: entrypoints/openai/chat_completion/serving.py", line 299, in render_chat_request (APIServer pid=1) ERROR 03-09 02:34:48 [serving.py:315] conversation, engine_prompts = await self._preprocess_chat( (APIServer pid=1) ERRO...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
