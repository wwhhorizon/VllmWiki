# vllm-project/vllm#1647: Triton Server Example does not work

| 字段 | 值 |
| --- | --- |
| Issue | [#1647](https://github.com/vllm-project/vllm/issues/1647) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Triton Server Example does not work

### Issue 正文摘录

Hi, I run into this issue when following the triton inference tutorial with vllm here: https://github.com/triton-inference-server/tutorials/tree/main/Quick_Deploy/vLLM I'm running on a AWS Ubuntu machine with this default [image](https://aws.amazon.com/releasenotes/aws-deep-learning-ami-gpu-pytorch-2-0-amazon-linux-2/) on an A10 GPU. `UNAVAILABLE: Internal: AssertionError: vLLM Triton backend must be configured to use decoupled model transaction policy` Thank you

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: Triton Server Example does not work Hi, I run into this issue when following the triton inference tutorial with vllm here: https://github.com/triton-inference-server/tutorials/tree/main/Quick_Deploy/vLLM I'm running on
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: U. `UNAVAILABLE: Internal: AssertionError: vLLM Triton backend must be configured to use decoupled model transaction policy` Thank you

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
