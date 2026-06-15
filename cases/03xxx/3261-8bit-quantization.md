# vllm-project/vllm#3261: 8bit quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#3261](https://github.com/vllm-project/vllm/issues/3261) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> 8bit quantization

### Issue 正文摘录

Does vLLM support 8 bit quantization? We need to use vLLM with large context window (>1K tokens). We tried AWQ but the generation quality is not good. Any pointer will be greatly appreciated.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: but the generation quality is not good. Any pointer will be greatly appreciated.
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 8bit quantization stale Does vLLM support 8 bit quantization? We need to use vLLM with large context window (>1K tokens). We tried AWQ but the generation quality is not good. Any pointer will be greatly appreciated.
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 8bit quantization stale Does vLLM support 8 bit quantization? We need to use vLLM with large context window (>1K tokens). We tried AWQ but the generation quality is not good. Any pointer will be greatly appreciated.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
