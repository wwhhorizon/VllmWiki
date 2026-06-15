# vllm-project/vllm#16399: [Usage]: How to use logit-processor in api server？

| 字段 | 值 |
| --- | --- |
| Issue | [#16399](https://github.com/vllm-project/vllm/issues/16399) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to use logit-processor in api server？

### Issue 正文摘录

### Your current environment ```text vllm serve models/Qwen/Qwen2.5-7B-Instruct --served-model-name Qwen2.5-7B-Instruct --port 12345 --dtype auto --trust-remote-code --gpu-memory-utilization 0.6 --logits-processor-pattern "logits_processor.test.process_token" ``` ```python completion = client.completions.create( model=model, prompt=completion, temperature=1.0, extra_body={ "logits_processors": [{ "qualname": "logits_processor.test.process_token", # "kwargs": {"logits": None, "token_ids": None} }] } ``` I'm sorry, but I didn't read exactly how to pass in my process_token function when calling the api, and when I run the code as above, it reminds me that those two parameters are missing: tokens_id and logit ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: it ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: or in api server？ usage ### Your current environment ```text vllm serve models/Qwen/Qwen2.5-7B-Instruct --served-model-name Qwen2.5-7B-Instruct --port 12345 --dtype auto --trust-remote-code --gpu-memory-utilization 0.6...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: truct --served-model-name Qwen2.5-7B-Instruct --port 12345 --dtype auto --trust-remote-code --gpu-memory-utilization 0.6 --logits-processor-pattern "logits_processor.test.process_token" ``` ```python completion = client...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: -memory-utilization 0.6 --logits-processor-pattern "logits_processor.test.process_token" ``` ```python completion = client.completions.create( model=model, prompt=completion, temperature=1.0, extra_body={ "logits_proces...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
