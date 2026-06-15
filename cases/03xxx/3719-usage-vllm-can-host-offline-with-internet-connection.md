# vllm-project/vllm#3719: [Usage]: vllm can host offline? with internet connection?

| 字段 | 值 |
| --- | --- |
| Issue | [#3719](https://github.com/vllm-project/vllm/issues/3719) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vllm can host offline? with internet connection?

### Issue 正文摘录

### Your current environment python3 python -m vllm.entrypoints.api_server --model TheBloke/CodeLlama-7B-Python-AWQ --quantization awq ### How would you like to use vllm I want to host offline envirment. python3 python -m vllm.entrypoints.api_server --model TheBloke/CodeLlama-7B-Python-AWQ --quantization awq but there is an error

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: our current environment python3 python -m vllm.entrypoints.api_server --model TheBloke/CodeLlama-7B-Python-AWQ --quantization awq ### How would you like to use vllm I want to host offline envirment. python3 python -m vl...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: m vllm.entrypoints.api_server --model TheBloke/CodeLlama-7B-Python-AWQ --quantization awq ### How would you like to use vllm I want to host offline envirment. python3 python -m vllm.entrypoints.api_server --model TheBlo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: vllm can host offline? with internet connection? usage;stale ### Your current environment python3 python -m vllm.entrypoints.api_server --model TheBloke/CodeLlama-7B-Python-AWQ --quantization awq ### How would...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
