# vllm-project/vllm#26653: [Usage]: Qwen3VL image coordinates issue

| 字段 | 值 |
| --- | --- |
| Issue | [#26653](https://github.com/vllm-project/vllm/issues/26653) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Qwen3VL image coordinates issue

### Issue 正文摘录

### Your current environment Hi, i found same image, same prompt, the vLLM serving qwen3vl always have wrong cooridnates back. this is vllm return: Response: "{\"click_type\": \"left_click\", \"coordinate\": [815, 961]}" As you can see, when visualize, the VLLM returned x offset is totally far wrong. Qwen3 official return. Same A3B model. Does the input were cropped or something? My server side just used: ``` vllm serve checkpoints/Qwen3-VL-30B-A3B-Instruct \ --dtype auto --max-model-len 4096 \ --api-key token-abc123 \ --gpu_memory_utilization 0.9 \ --trust-remote-code \ --port 8000 \ --served-model-name 'qwen3-vl' \ --max-model-len 8k \ --limit-mm-per-prompt '{"video": 3}' \ --enable-auto-tool-choice \ --tool-call-parser hermes ``` **note**: when visualize i have already mapping the cordiantes to image space, here just compare raw output, it still biased much on x-axis. ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. dfwr ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentat...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: n visualize, the VLLM returned x offset is totally far wrong. Qwen3 official return. Same A3B model. Does the input were cropped or something? My server side just used: ``` vllm serve checkpoints/Qwen3-VL-30B-A3B-Instru...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Qwen3VL image coordinates issue usage ### Your current environment Hi, i found same image, same prompt, the vLLM serving qwen3vl always have wrong cooridnates back. this is vllm return: Response: "{\"click_type...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ust used: ``` vllm serve checkpoints/Qwen3-VL-30B-A3B-Instruct \ --dtype auto --max-model-len 4096 \ --api-key token-abc123 \ --gpu_memory_utilization 0.9 \ --trust-remote-code \ --port 8000 \ --served-model-name 'qwen3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: fwr ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: --tool-call-parser hermes ``` **note**: when visualize i have already mapping the cordiantes to image space, here just compare raw output, it still biased much on x-axis. ### How would you like to use vllm I want to run...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
