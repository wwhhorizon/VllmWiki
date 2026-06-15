# vllm-project/vllm#39408: [Usage]: qwen3-asr-1.7b pre-allocated encoder cache size limit

| 字段 | 值 |
| --- | --- |
| Issue | [#39408](https://github.com/vllm-project/vllm/issues/39408) |
| 状态 | open |
| 标签 | usage |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: qwen3-asr-1.7b pre-allocated encoder cache size limit

### Issue 正文摘录

### Your current environment vllm 0.19.0 ### How would you like to use vllm pip install vllm[audio] exec python3 -m vllm.entrypoints.openai.api_server \ --model /Qwen3-ASR-1.7B \ --host 0.0.0.0 \ --port 30000 \ --served-model-nameqwen3-asr \ --max-model-len "65536" \ --limit-mm-per-prompt '{"audio":{"count":1,"length":32768}}' When i request a longer audio , return {'error': {'message': 'The decoder prompt contains a(n) audio item with length 3476, which exceeds the pre-allocated encoder cache size 2048. Please reduce the input size or increase the encoder cache size by setting --limit-mm-per-prompt at startup.', 'type': 'BadRequestError', 'param': None, 'code': 400}}， how to change limit-mm-per-prompt parameter ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: qwen3-asr-1.7b pre-allocated encoder cache size limit usage ### Your current environment vllm 0.19.0 ### How would you like to use vllm pip install vllm[audio] exec python3 -m vllm.entrypoints.openai.ap
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: --limit-mm-per-prompt '{"audio":{"count":1,"length":32768}}' When i request a longer audio , return {'error': {'message': 'The decoder prompt contains a(n) audio item with length 3476, which exceeds the pre-allocated en...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: urrent environment vllm 0.19.0 ### How would you like to use vllm pip install vllm[audio] exec python3 -m vllm.entrypoints.openai.api_server \ --model /Qwen3-ASR-1.7B \ --host 0.0.0.0 \ --port 30000 \ --served-m
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ter ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
