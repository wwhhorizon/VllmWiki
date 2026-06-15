# vllm-project/vllm#2391: getting error RuntimeError: unable to mmap 18329065000 bytes from file </home/.cache/huggingface/hub/models--TheBloke--CodeLlama-34B-Instruct-GPTQ/snapshots/0a2785d47fb7330388e0487e0526bbc53d87c156/model.safetensors>: Cannot allocate memory (12) 

| 字段 | 值 |
| --- | --- |
| Issue | [#2391](https://github.com/vllm-project/vllm/issues/2391) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> getting error RuntimeError: unable to mmap 18329065000 bytes from file </home/.cache/huggingface/hub/models--TheBloke--CodeLlama-34B-Instruct-GPTQ/snapshots/0a2785d47fb7330388e0487e0526bbc53d87c156/model.safetensors>: Cannot allocate memory (12) 

### Issue 正文摘录

i am getting error RuntimeError: unable to mmap 18329065000 bytes from file : Cannot allocate memory (12) When ran python3 -m vllm.entrypoints.openai.api_server --model TheBloke/CodeLlama-34B-Instruct-GPTQ --quantization gptq --gpu-memory-utilization 1 --enforce-eager Can anyone please help?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: r RuntimeError: unable to mmap 18329065000 bytes from file </home/.cache/huggingface/hub/models--TheBloke--CodeLlama-34B-Instruct-GPTQ/snapshots/0a2785d47fb7330388e0487e0526bbc53d87c156/model.safetensors>: Cannot alloca...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ypoints.openai.api_server --model TheBloke/CodeLlama-34B-Instruct-GPTQ --quantization gptq --gpu-memory-utilization 1 --enforce-eager Can anyone please help?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
