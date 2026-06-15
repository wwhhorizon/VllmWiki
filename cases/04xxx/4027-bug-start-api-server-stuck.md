# vllm-project/vllm#4027: [Bug]: start api server stuck

| 字段 | 值 |
| --- | --- |
| Issue | [#4027](https://github.com/vllm-project/vllm/issues/4027) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: start api server stuck

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` vLLM API server version 0.4.0.post1 ### 🐛 Describe the bug When I started the api service, the startup process got stuck. 2024-04-12 13:45:17,174 INFO worker.py:1752 -- Started a local Ray instance. python -m vllm.entrypoints.openai.api_server \ --model ${MODEL_PATH} \ --tensor-parallel-size ${tensor_parallel_size} \ --port ${port}

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nment ```text The output of `python collect_env.py` ``` vLLM API server version 0.4.0.post1 ### 🐛 Describe the bug When I started the api service, the startup process got stuck. 2024-04-12 13:45:17,174 INFO worker.py:17...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: l Ray instance. python -m vllm.entrypoints.openai.api_server \ --model ${MODEL_PATH} \ --tensor-parallel-size ${tensor_parallel_size} \ --port ${port}

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
