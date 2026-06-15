# vllm-project/vllm#3781: Best server cmd for mistralai/Mistral-7B-v0.1

| 字段 | 值 |
| --- | --- |
| Issue | [#3781](https://github.com/vllm-project/vllm/issues/3781) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Best server cmd for mistralai/Mistral-7B-v0.1

### Issue 正文摘录

``` export MODEL=mistralai/Mistral-7B-v0.1 python3 -m vllm.entrypoints.openai.api_server --model $MODEL \ --tensor-parallel-size=1 \ --enable-prefix-caching --max-model-len=4096 --trust-remote-code | tee server_mistral.log & ``` raises `NotImplementedError: Sliding window is not allowed with prefix caching enabled!` Is there a way to turn off sliding window and keep prefix caching? (More generally is there a list of commands to serve common models efficiently?)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: (More generally is there a list of commands to serve common models efficiently?)
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Best server cmd for mistralai/Mistral-7B-v0.1 usage;stale ``` export MODEL=mistralai/Mistral-7B-v0.1 python3 -m vllm.entrypoints.openai.api_server --model $MODEL \ --tensor-parallel-size=1 \ --enable-prefix-caching --ma...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Best server cmd for mistralai/Mistral-7B-v0.1 usage;stale ``` export MODEL=mistralai/Mistral-7B-v0.1 python3 -m vllm.entrypoints.openai.api_server --model $MODEL \ --tensor-parallel-size=1 \ --enable-prefix-caching --ma...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
