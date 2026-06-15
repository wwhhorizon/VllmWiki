# vllm-project/vllm#10207: [Usage]: The issue of memory usage with quantized models.

| 字段 | 值 |
| --- | --- |
| Issue | [#10207](https://github.com/vllm-project/vllm/issues/10207) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: The issue of memory usage with quantized models.

### Issue 正文摘录

### Your current environment ```text My environment: vllm: 0.6.2 transformers: 4.45.2 auto_gptq: 0.7.1 ``` ### How would you like to use vllm Hello, I have a question. I am deploying the Qwen2.5-7B-Instruct and Qwen2.5-7B-Instruct-GPTQ-Int4 models using vllm, and I notice that the GPTQ-Int4 model consumes a lot of video memory. I expected it to consume only a quarter of the video memory compared to the non-quantized model. Is there any issue or parameter that I should pay attention to? ![image](https://github.com/user-attachments/assets/97e0e8a9-ed2b-4d1c-81b1-c308a965a02d) Here is my deployment command: ``` # Qwen2.5-7B-Instruct CUDA_VISIBLE_DEVICES=0 python -m vllm.entrypoints.openai.api_server --port=8000 --model=/models/qwen2.5/models--Qwen--Qwen2.5-7B-Instruct/snapshots/acbd96531cda22292a3ceaa67e984955d3965282 # Qwen2.5-7B-Instruct-GPTQ-Int4 CUDA_VISIBLE_DEVICES=1 python -m vllm.entrypoints.openai.api_server --port=8001 --model=/models/qwen2.5/models--Qwen--Qwen2.5-7B-Instruct-GPTQ-Int4/snapshots/e9c932ac1893a49ae0fc497ad6e1e86e2e39af20 ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Usage]: The issue of memory usage with quantized models. usage;stale ### Your current environment ```text My environment: vllm: 0.6.2 transformers: 4.45.2 auto_gptq: 0.7.1 ``` ### How would you like to use vllm Hello,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: -c308a965a02d) Here is my deployment command: ``` # Qwen2.5-7B-Instruct CUDA_VISIBLE_DEVICES=0 python -m vllm.entrypoints.openai.api_server --port=8000 --model=/models/qwen2.5/models--Qwen--Qwen2.5-7B-Instruct/snapshots...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: The issue of memory usage with quantized models. usage;stale ### Your current environment ```text My environment: vllm: 0.6.2 transformers: 4.45.2 auto_gptq: 0.7.1 ``` ### How would you like to use vllm Hello,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: The issue of memory usage with quantized models. usage;stale ### Your current environment ```text My environment: vllm: 0.6.2 transformers: 4.45.2 auto_gptq: 0.7.1 ``` ### How would you like to use vllm Hello,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
