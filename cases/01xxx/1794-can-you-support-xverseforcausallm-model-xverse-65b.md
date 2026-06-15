# vllm-project/vllm#1794: can you support XverseForCausalLM? model XVERSE-65B

| 字段 | 值 |
| --- | --- |
| Issue | [#1794](https://github.com/vllm-project/vllm/issues/1794) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> can you support XverseForCausalLM? model XVERSE-65B

### Issue 正文摘录

when i try to run python -m vllm.entrypoints.openai.api_server --model XVERSE-65B --port 17861 --trust-remote-code error occurs: Model architectures ['XverseForCausalLM'] are not supported for now vllm version: 0.2.1 it's web site address: https://github.com/xverse-ai/XVERSE-65B

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: odel architectures ['XverseForCausalLM'] are not supported for now vllm version: 0.2.1 it's web site address: https://github.com/xverse-ai/XVERSE-65B
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: --model XVERSE-65B --port 17861 --trust-remote-code error occurs: Model architectures ['XverseForCausalLM'] are not supported for now vllm version: 0.2.1 it's web site address: https://github.com/xverse-ai/XVERSE-65B
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: can you support XverseForCausalLM? model XVERSE-65B when i try to run python -m vllm.entrypoints.openai.api_server --model XVERSE-65B --port 17861 --trust-remote-code error occurs: Model architectures ['XverseForCausalL...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
