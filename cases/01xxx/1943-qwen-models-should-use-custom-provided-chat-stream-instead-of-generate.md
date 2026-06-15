# vllm-project/vllm#1943: Qwen models should use custom provided chat_stream instead of generate

| 字段 | 值 |
| --- | --- |
| Issue | [#1943](https://github.com/vllm-project/vllm/issues/1943) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Qwen models should use custom provided chat_stream instead of generate

### Issue 正文摘录

Hi, I found there are plenty of issues on the generation parameters related to vllm support for Qwen, I've practiced integrating Qwen into ooba's textgen-webui, and I found the only proper way out is to use Qwen's chat interface instead of calling geneate directly, see here https://github.com/yhyu13/text-generation-webui/commit/26a3091147e31f1d0d39dae5f2fef98e9f755c9d It's chat_stream bascially handle everthing a streaming generation needs I will try create a pr for this if I have time

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Qwen models should use custom provided chat_stream instead of generate Hi, I found there are plenty of issues on the generation parameters related to vllm support for Qwen, I've practiced integrating Qwen into ooba's
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: bui/commit/26a3091147e31f1d0d39dae5f2fef98e9f755c9d It's chat_stream bascially handle everthing a streaming generation needs I will try create a pr for this if I have time

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
