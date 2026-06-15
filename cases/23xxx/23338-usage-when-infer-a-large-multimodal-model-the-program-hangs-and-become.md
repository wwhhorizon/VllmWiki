# vllm-project/vllm#23338: [Usage]: When infer a large multimodal model, the program hangs and becomes unresponsive.

| 字段 | 值 |
| --- | --- |
| Issue | [#23338](https://github.com/vllm-project/vllm/issues/23338) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: When infer a large multimodal model, the program hangs and becomes unresponsive.

### Issue 正文摘录

### Your current environment vllm 0.10.0 model name：openbmb/MiniCPM-o-2_6-int4 platform: 4090 ### How would you like to use vllm def run_video() -> None: with open('8.mp4', 'rb') as video_file: video_base64 = base64.b64encode(video_file.read()).decode('utf-8') ## Use video url in the payload chat_completion_from_url = client.chat.completions.create( messages=[{ "role": "user", "content": [ { "type": "text", "text": "What's in this video?" }, { "type": "video_url", "video_url": { "url": f"data:video/mp4;base64,{video_base64}", }, }, ], }], model="model", max_completion_tokens=64, ) result = chat_completion_from_url.choices[0].message.content print("Chat completion output from image url:", result) print(run_video()) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: When infer a large multimodal model, the program hangs and becomes unresponsive. usage;stale ### Your current environment vllm 0.10.0 model name：openbmb/MiniCPM-o-2_6-int4 platform: 4090 ### How would you like...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: arge multimodal model, the program hangs and becomes unresponsive. usage;stale ### Your current environment vllm 0.10.0 model name：openbmb/MiniCPM-o-2_6-int4 platform: 4090 ### How would you like to use vllm def run_vid...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: # Your current environment vllm 0.10.0 model name：openbmb/MiniCPM-o-2_6-int4 platform: 4090 ### How would you like to use vllm def run_video() -> None: with open('8.mp4', 'rb') as video_file: video_base64 = base64.b64en...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ()) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
