# vllm-project/vllm#5780: [Usage]: 使用vllm最新版0.5.0.post1启动模型

| 字段 | 值 |
| --- | --- |
| Issue | [#5780](https://github.com/vllm-project/vllm/issues/5780) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: 使用vllm最新版0.5.0.post1启动模型

### Issue 正文摘录

### Your current environment python -m vllm.entrypoints.api_server --host 0.0.0.0 --port 8005 --max-model-len 20480 \ --model /workspace/Chat-v1.1 --enforce-eager \ --tensor-parallel-size 1 为什么启动后没有/v1/chat/completions 这个方法，需要怎么配置吗 ![image](https://github.com/vllm-project/vllm/assets/50564015/d8a79417-891b-4af1-9bba-386b699a4b75) ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: 5) ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: python -m vllm.entrypoints.api_server --host 0.0.0.0 --port 8005 --max-model-len 20480 \ --model /workspace/Chat-v1.1 --enforce-eager \ --tensor-parallel-size 1 为什么启动后没有/v1/chat/completions 这个方法，需要怎么配置吗 ![image](https:/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
