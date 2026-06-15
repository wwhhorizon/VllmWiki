# vllm-project/vllm#2871: HQQ quantization support

| 字段 | 值 |
| --- | --- |
| Issue | [#2871](https://github.com/vllm-project/vllm/issues/2871) |
| 状态 | closed |
| 标签 | unstale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> HQQ quantization support

### Issue 正文摘录

As we have a few models with Half-Quadratic Quantization (HQQ) out there, VLLM should also support them: ```sh api_server.py: error: argument --quantization/-q: invalid choice: 'hqq' (choose from 'awq', 'gptq', 'squeezellm', None) ``` E.g. * https://huggingface.co/mobiuslabsgmbh/Mixtral-8x7B-Instruct-v0.1-hf-attn-4bit-moe-2bit-HQQ

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: HQQ quantization support unstale As we have a few models with Half-Quadratic Quantization (HQQ) out there, VLLM should also support them: ```sh api_server.py: error: argument --quantization/-q: invalid choice: 'hqq' (ch...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: HQQ quantization support unstale As we have a few models with Half-Quadratic Quantization (HQQ) out there, VLLM should also support them: ```sh api_server.py: error: argument --quantization/-q: invalid choice: 'hqq' (ch...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ://huggingface.co/mobiuslabsgmbh/Mixtral-8x7B-Instruct-v0.1-hf-attn-4bit-moe-2bit-HQQ
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: HQQ quantization support unstale As we have a few models with Half-Quadratic Quantization (HQQ) out there, VLLM should also support them: ```sh api_server.py: error: argument --quantization/-q: invalid choice: 'hqq' (ch...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
