# vllm-project/vllm#36223: [RFC]: Support quarot for eagle3

| 字段 | 值 |
| --- | --- |
| Issue | [#36223](https://github.com/vllm-project/vllm/issues/36223) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Support quarot for eagle3

### Issue 正文摘录

### Motivation. https://arxiv.org/abs/2404.00456 `quarot` is a nice quant method, it will rotate hidden_states. But for eagle3, we will use hidden_states as inputs. If a model is quantized as `quarot`, then inputs are roatated and eagle3 will crash. ### Proposed Change. Anti-rotate `fc` weights. For some `eagle3` model without `embed_tokens`, we need anti-rotate `embed_tokens`, too. https://github.com/vllm-project/vllm/pull/36225 ### Feedback Period. _No response_ ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: FC ### Motivation. https://arxiv.org/abs/2404.00456 `quarot` is a nice quant method, it will rotate hidden_states. But for eagle3, we will use hidden_states as inputs. If a model is quantized as `quarot`, then inputs ar...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: dden_states. But for eagle3, we will use hidden_states as inputs. If a model is quantized as `quarot`, then inputs are roatated and eagle3 will crash. ### Proposed Change. Anti-rotate `fc` weights. For some `eagle3` mod...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
