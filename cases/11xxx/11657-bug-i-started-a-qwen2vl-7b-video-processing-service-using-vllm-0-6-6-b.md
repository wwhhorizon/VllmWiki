# vllm-project/vllm#11657: [Bug]: I started a qwen2vl-7b video processing service using vllm (0.6.6), but encountered an error during inference

| 字段 | 值 |
| --- | --- |
| Issue | [#11657](https://github.com/vllm-project/vllm/issues/11657) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: I started a qwen2vl-7b video processing service using vllm (0.6.6), but encountered an error during inference

### Issue 正文摘录

### Your current environment Command： python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8088 --model /app/qwen2vl-7b --tensor-parrallel 1 --gpu-memory-utilization 0.95 --served-model-name qwen2vl-7b --trust-remote-code GPU: A800 80GB Query: query = {"model":"qwen2vl-7b", "messages":[ {"role":"user", "content":[ {"type":"text","text":"A prompt word of about 500 words"}, {"type":"video_url","video_url":{"url":“A downloadable URL, a video of about 5 seconds in mp4 format”} }] }] } Response： {"object":"error","message":"The prompt (total length 43698) is too long to fit into the model (context length 32768). Make sure that `max number of images, and pers than the r mber of text tokens plus multimodal tokens. For image inputs, the number of image tokens depends on the number of images, and possibly their aspect ratios as well.","type":"BadRequestError","param" :nuit, code :400｝ ### Model Input Dumps _No response_ ### 🐛 Describe the bug Command： python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8088 --model /app/qwen2vl-7b --tensor-parrallel 1 --gpu-memory-utilization 0.95 --served-model-name qwen2vl-7b --trust-remote-code GPU: A800 80GB Query: query =...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: I started a qwen2vl-7b video processing service using vllm (0.6.6), but encountered an error during inference bug;stale ### Your current environment Command： python -m vllm.entrypoints.openai.api_server --host 0....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ervice using vllm (0.6.6), but encountered an error during inference bug;stale ### Your current environment Command： python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8088 --model /app/qwen2vl-7b --tens...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 00｝ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
