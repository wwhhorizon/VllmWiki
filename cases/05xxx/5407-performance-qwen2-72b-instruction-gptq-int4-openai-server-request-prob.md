# vllm-project/vllm#5407: [Performance]: Qwen2-72B-Instruction-GPTQ-Int4 Openai Server Request Problem

| 字段 | 值 |
| --- | --- |
| Issue | [#5407](https://github.com/vllm-project/vllm/issues/5407) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Qwen2-72B-Instruction-GPTQ-Int4 Openai Server Request Problem

### Issue 正文摘录

Hello, I wish you good work. When I use the Qwen2-72B-Instruction-GPTQ-Int4 model, when the model works on Vllm, it collects all the requests at first and then responds when receiving multiple requests. But when I use your Qwen2-7B-Instruction model, it receives them in a scattered manner. While I do not have such a problem with other models, I see a problem with Qwen2-72B-Instruction and other quantization models receiving the requests completely and then responding. I would be glad if you help. CUDA_VISIBLE_DEVICES=0 python -m vllm.entrypoints.openai.api_server --model /opt/GPT/MODEL/Qwen2-72B-Instruct-GPTQ-Int4 --host 10.12.112.160 --port 9001 --max-model-len 8192 --tensor-parallel-size 1

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Performance]: Qwen2-72B-Instruction-GPTQ-Int4 Openai Server Request Problem performance;stale Hello, I wish you good work. When I use the Qwen2-72B-Instruction-GPTQ-Int4 model, when the model works on Vllm, it collects...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Performance]: Qwen2-72B-Instruction-GPTQ-Int4 Openai Server Request Problem performance;stale Hello, I wish you good work. When I use the Qwen2-72B-Instruction-GPTQ-Int4 model, when the model works on Vllm, it collects...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: Qwen2-72B-Instruction-GPTQ-Int4 Openai Server Request Problem performance;stale Hello, I wish you good work. When I use the Qwen2-72B-Instruction-GPTQ-Int4 model, when the model works on Vllm, it collects...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e requests completely and then responding. I would be glad if you help. CUDA_VISIBLE_DEVICES=0 python -m vllm.entrypoints.openai.api_server --model /opt/GPT/MODEL/Qwen2-72B-Instruct-GPTQ-Int4 --host 10.12.112.160 --port...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
