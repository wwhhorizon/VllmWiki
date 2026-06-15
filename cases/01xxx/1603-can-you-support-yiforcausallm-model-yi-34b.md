# vllm-project/vllm#1603: can you support YiForCausalLM? model Yi-34B

| 字段 | 值 |
| --- | --- |
| Issue | [#1603](https://github.com/vllm-project/vllm/issues/1603) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> can you support YiForCausalLM? model Yi-34B

### Issue 正文摘录

when i try to run python -m vllm.entrypoints.openai.api_server --model Yi-34B-200K --port 18081 --trust-remote-code error occurs: Model architectures ['YiForCausalLM'] are not supported for now it's web site address: https://github.com/01-ai/Yi

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: --model Yi-34B-200K --port 18081 --trust-remote-code error occurs: Model architectures ['YiForCausalLM'] are not supported for now it's web site address: https://github.com/01-ai/Yi
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: can you support YiForCausalLM? model Yi-34B when i try to run python -m vllm.entrypoints.openai.api_server --model Yi-34B-200K --port 18081 --trust-remote-code error occurs: Model architectures ['YiForCausalLM'] are not...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
