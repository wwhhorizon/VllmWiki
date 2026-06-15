# vllm-project/vllm#1192: run new qwen 7b v1.1 results error?

| 字段 | 值 |
| --- | --- |
| Issue | [#1192](https://github.com/vllm-project/vllm/issues/1192) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> run new qwen 7b v1.1 results error?

### Issue 正文摘录

python -m vllm.entrypoints.api_server --model /***/Qwen-7B-Chat --swap-space 16 --disable-log-requests --host 192.168.19.14 --port 10860 --max-num-seqs 256 --trust-remote-code --tensor-parallel-size 2 --dtype=half It turned out to be full of exclamation marks!!! ![image](https://github.com/vllm-project/vllm/assets/40717349/b3140269-d8e0-4ed2-ac69-8afd9d2292c9)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: run new qwen 7b v1.1 results error? python -m vllm.entrypoints.api_server --model /***/Qwen-7B-Chat --swap-space 16 --disable-log-requests --host 192.168.19.14 --port 10860 --max-num-seqs 256 --trust-remote-code --tenso...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 860 --max-num-seqs 256 --trust-remote-code --tensor-parallel-size 2 --dtype=half It turned out to be full of exclamation marks!!! ![image](https://github.com/vllm-project/vllm/assets/40717349/b3140269-d8e0-4ed2-ac69-8af...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: s.api_server --model /***/Qwen-7B-Chat --swap-space 16 --disable-log-requests --host 192.168.19.14 --port 10860 --max-num-seqs 256 --trust-remote-code --tensor-parallel-size 2 --dtype=half It turned out to be full of ex...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
