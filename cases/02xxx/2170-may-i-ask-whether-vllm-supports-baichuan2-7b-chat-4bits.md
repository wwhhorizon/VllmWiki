# vllm-project/vllm#2170: May I ask whether vllm supports Baichuan2-7B-Chat-4bits

| 字段 | 值 |
| --- | --- |
| Issue | [#2170](https://github.com/vllm-project/vllm/issues/2170) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> May I ask whether vllm supports Baichuan2-7B-Chat-4bits

### Issue 正文摘录

When I execute this line of instruction： VLLM_USE_MODELSCOPE=True python -m vllm.entrypoints.openai.api_server --model="baichuan-inc/Baichuan2-13B-Chat" --download-dir="/root/autodl-tmp/model/" --revision='v1.0.3' --trust-remote-code When I execute this line of instruction ValueError: Unknown quantization method: gptq. Must be one of ['awq', 'squeezellm'].

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: remote-code When I execute this line of instruction ValueError: Unknown quantization method: gptq. Must be one of ['awq', 'squeezellm'].
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: aichuan2-7B-Chat-4bits When I execute this line of instruction： VLLM_USE_MODELSCOPE=True python -m vllm.entrypoints.openai.api_server --model="baichuan-inc/Baichuan2-13B-Chat" --download-dir="/root/autodl-tmp/model/" --...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
