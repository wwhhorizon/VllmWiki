# vllm-project/vllm#3136: About special tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#3136](https://github.com/vllm-project/vllm/issues/3136) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> About special tokens

### Issue 正文摘录

When I use vllm and fastchat by chatglm3-6b, model always generate "assistant" special tokens, how can i fix it? like: "春风轻拂绿意新，|assistant|助时光荏苒。\n|assistant|勤勉不懈怠，|assistant|智慧照万方。"

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: About special tokens stale When I use vllm and fastchat by chatglm3-6b, model always generate "assistant" special tokens, how can i fix it? like: "春风轻拂绿意新，|assistant|助时光荏苒。\n|assistant|勤勉不懈怠，|assistant|智慧照万方。"
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: About special tokens stale When I use vllm and fastchat by chatglm3-6b, model always generate "assistant" special tokens, how can i fix it? like: "春风轻拂绿意新，|assistant|助时光荏苒。\n|assistant|勤勉不懈怠，|assistant|智慧照万方。"
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: About special tokens stale When I use vllm and fastchat by chatglm3-6b, model always generate "assistant" special tokens, how can i fix it? like: "春风轻拂绿意新，|assistant|助时光荏苒。\n|assistant|勤勉不懈怠，|assistant|智慧照万方。"

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
