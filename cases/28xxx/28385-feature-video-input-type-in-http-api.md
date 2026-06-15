# vllm-project/vllm#28385: [Feature]:  video input type in http API

| 字段 | 值 |
| --- | --- |
| Issue | [#28385](https://github.com/vllm-project/vllm/issues/28385) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]:  video input type in http API

### Issue 正文摘录

### 🚀 The feature, motivation and pitch i follows the formats in https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct-FP8 ,but not work. ``` (APIServer pid=1) ERROR 11-09 23:57:25 [serving_chat.py:263] File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/chat_utils.py", line 1318, in _parse_chat_message_content_parts (APIServer pid=1) ERROR 11-09 23:57:25 [serving_chat.py:263] parse_res = _parse_chat_message_content_part( (APIServer pid=1) ERROR 11-09 23:57:25 [serving_chat.py:263] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (APIServer pid=1) ERROR 11-09 23:57:25 [serving_chat.py:263] File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/chat_utils.py", line 1416, in _parse_chat_message_content_part (APIServer pid=1) ERROR 11-09 23:57:25 [serving_chat.py:263] raise NotImplementedError(f"Unknown part type: {part_type}") (APIServer pid=1) ERROR 11-09 23:57:25 [serving_chat.py:263] NotImplementedError: Unknown part type: video ``` ``` video_data_uri = f"data:{mime_type};base64,{video_b64}" messages = [ { "role": "user", "content": [ {"type": "video", "video": video_data_uri}, {"type": "text", "text": "这段视频有多长"} ] } ] ````

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: I feature request ### 🚀 The feature, motivation and pitch i follows the formats in https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct-FP8 ,but not work. ``` (APIServer pid=1) ERROR 11-09 23:57:25 [serving_chat.py:263] Fil...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: follows the formats in https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct-FP8 ,but not work. ``` (APIServer pid=1) ERROR 11-09 23:57:25 [serving_chat.py:263] File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: video input type in http API feature request ### 🚀 The feature, motivation and pitch i follows the formats in https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct-FP8 ,but not work. ``` (APIServer pid=1) ERROR 11...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
