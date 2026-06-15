# vllm-project/vllm#3348: inference with AWQ quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#3348](https://github.com/vllm-project/vllm/issues/3348) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> inference with AWQ quantization

### Issue 正文摘录

Hi, i got an anomaly while inference mistral with AWQ, below is the GPU usage on 3090 consume 20GB GPU. even if we inference the base model only consume 19GB GPU here is the command: python -m vllm.entrypoints.openai.api_server --model ../Mistral-AWQ --disable-log-requests --port 9000 --host 127.0.0.1 --max-num-seqs 500 --max-model-len 27000 --quantization awq can anyone help?, thank you.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: inference with AWQ quantization stale Hi, i got an anomaly while inference mistral with AWQ, below is the GPU usage on 3090 consume 20GB GPU. even if we inference the base model only consume 19GB GPU here is the command...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: inference with AWQ quantization stale Hi, i got an anomaly while inference mistral with AWQ, below is the GPU usage on 3090 consume 20GB GPU. even if we inference the base model only consume 19GB GPU here is the command...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: is the GPU usage on 3090 consume 20GB GPU. even if we inference the base model only consume 19GB GPU here is the command: python -m vllm.entrypoints.openai.api_server --model ../Mistral-AWQ --disable-log-requests --port...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
