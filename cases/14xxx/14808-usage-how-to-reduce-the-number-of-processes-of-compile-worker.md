# vllm-project/vllm#14808: [Usage]: how to reduce the number of processes of compile_worker

| 字段 | 值 |
| --- | --- |
| Issue | [#14808](https://github.com/vllm-project/vllm/issues/14808) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to reduce the number of processes of compile_worker

### Issue 正文摘录

### Your current environment vllm： 0.7.3 `vllm serve Qwen/Qwen2.5-7B-Instruct --host 0.0.0.0 --port 6015 --disable-log-requests --max_num_seqs=200 --max_num_batched_tokens=256 -tp=4 --served-model-name Qwen2.5-7B-Instruct --max_model_len=4096 --block-size=16 --gpu-memory-utilization=0.3 --uvicorn-log-level=warning --disable-fastapi-docs` after I start vllm serve, there are 32 subprocesses of compile_worker appeared like this： ![Image](https://github.com/user-attachments/assets/82e6fc55-bf42-4728-9bdc-52bd6b63d4a3) How could I reduce the number of processes. ### How would you like to use vllm ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: mpile_worker usage ### Your current environment vllm： 0.7.3 `vllm serve Qwen/Qwen2.5-7B-Instruct --host 0.0.0.0 --port 6015 --disable-log-requests --max_num_seqs=200 --max_num_batched_tokens=256 -tp=4 --served-model-nam...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Usage]: how to reduce the number of processes of compile_worker usage ### Your current environment vllm： 0.7.3 `vllm serve Qwen/Qwen2.5-7B-Instruct --host 0.0.0.0 --port 6015 --disable-log-requests --max_num_seqs=200 -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: llm ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 256 -tp=4 --served-model-name Qwen2.5-7B-Instruct --max_model_len=4096 --block-size=16 --gpu-memory-utilization=0.3 --uvicorn-log-level=warning --disable-fastapi-docs` after I start vllm serve, there are 32 subprocesses...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: serve Qwen/Qwen2.5-7B-Instruct --host 0.0.0.0 --port 6015 --disable-log-requests --max_num_seqs=200 --max_num_batched_tokens=256 -tp=4 --served-model-name Qwen2.5-7B-Instruct --max_model_len=4096 --block-size=16 --gpu-m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
