# vllm-project/vllm#20025: [Bug]: Mistrall Small 3.2 doesn't work with images

| 字段 | 值 |
| --- | --- |
| Issue | [#20025](https://github.com/vllm-project/vllm/issues/20025) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 23; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Mistrall Small 3.2 doesn't work with images

### Issue 正文摘录

### Your current environment vLLM 0.9.1 (Docker) `mistralai/Mistral-Small-3.2-24B-Instruct-2506` Using `mistralai/Mistral-Small-3.1-24B-Instruct-2503` with everything else unchanged works. ### 🐛 Describe the bug `ERROR 06-24 14:40:09 [serving_chat.py:200] Error in preprocessing prompt inputs ERROR 06-24 14:40:09 [serving_chat.py:200] Traceback (most recent call last): ERROR 06-24 14:40:09 [serving_chat.py:200] File "/workspace/.venv/lib/python3.12/site-packages/vllm/entrypoints/openai/serving_chat.py", line 183, in create_chat_completion ERROR 06-24 14:40:09 [serving_chat.py:200] ) = await self._preprocess_chat( ERROR 06-24 14:40:09 [serving_chat.py:200] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 06-24 14:40:09 [serving_chat.py:200] File "/workspace/.venv/lib/python3.12/site-packages/vllm/entrypoints/openai/serving_engine.py", line 787, in _preprocess_chat ERROR 06-24 14:40:09 [serving_chat.py:200] conversation, mm_data_future = parse_chat_messages_futures( ERROR 06-24 14:40:09 [serving_chat.py:200] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 06-24 14:40:09 [serving_chat.py:200] File "/workspace/.venv/lib/python3.12/site-packages/vllm/entrypoints/chat_utils.py", line 1196, in parse_chat_messages_f...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: :40:09 [serving_chat.py:200] mm_processor = mm_registry.create_processor(model_config) ERROR 06-24 14:40:09 [serving_chat.py:200] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 06-24 14:40:09 [serving_chat.py:200] Fil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Mistrall Small 3.2 doesn't work with images bug;stale ### Your current environment vLLM 0.9.1 (Docker) `mistralai/Mistral-Small-3.2-24B-Instruct-2506` Using `mistralai/Mistral-Small-3.1-24B-Instruct-2503` with ev...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Mistrall Small 3.2 doesn't work with images bug;stale ### Your current environment vLLM 0.9.1 (Docker) `mistralai/Mistral-Small-3.2-24B-Instruct-2506` Using `mistralai/Mistral-Small-3.1-24B-Instruct-2503` with ev...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: n't work with images bug;stale ### Your current environment vLLM 0.9.1 (Docker) `mistralai/Mistral-Small-3.2-24B-Instruct-2506` Using `mistralai/Mistral-Small-3.1-24B-Instruct-2503` with everything else unchanged works....
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: Using `mistralai/Mistral-Small-3.1-24B-Instruct-2503` with everything else unchanged works. ### 🐛 Describe the bug `ERROR 06-24 14:40:09 [serving_chat.py:200] Error in preprocessing prompt inputs ERROR 06-24 14:40:09 [s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
