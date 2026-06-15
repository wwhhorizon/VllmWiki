# vllm-project/vllm#28035: [Usage]: deepseek-ocr The output token count is too low and unstable.

| 字段 | 值 |
| --- | --- |
| Issue | [#28035](https://github.com/vllm-project/vllm/issues/28035) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: deepseek-ocr The output token count is too low and unstable.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm python3 -m vllm.entrypoints.openai.api_server --served-model-name deepseek-ocr --model deepseekocr --tensor-parallel-size 1 --gpu-memory-utilization 0.95 --disable-log-requests --logits_processors vllm.model_executor.models.deepseek_ocr:NGramPerReqLogitsProcessor { "model": "DeepSeek-OCR", "messages": [{ "role": "user", "content": [ { "type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{self.image_to_base64(image_path)}"} }, {"type": "text", "text": ” \nFree OCR.“} ] }], "vllm_xargs": { "ngram_size": 30, "window_size": 100, "whitelist_token_ids": "[128821, 128822]" }, "temperature": 0.0, "max_tokens": 4096 } "finish_reason":"stop" but "completion_tokens":200+ ，cannot output the complete image content. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: age]: deepseek-ocr The output token count is too low and unstable. usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm python3 -m vllm.entrypoint...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nt. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: like to use vllm python3 -m vllm.entrypoints.openai.api_server --served-model-name deepseek-ocr --model deepseekocr --tensor-parallel-size 1 --gpu-memory-utilization 0.95 --disable-log-requests --logits_processors vllm....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
