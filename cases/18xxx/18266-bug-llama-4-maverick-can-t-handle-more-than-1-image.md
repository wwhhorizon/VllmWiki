# vllm-project/vllm#18266: [Bug]: Llama-4-Maverick can't handle more than 1 image

| 字段 | 值 |
| --- | --- |
| Issue | [#18266](https://github.com/vllm-project/vllm/issues/18266) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Llama-4-Maverick can't handle more than 1 image

### Issue 正文摘录

### Your current environment Is it expected that Maverick can't handle more than 1 image with `vllm serve`? 1. works fine: `vllm serve /hf_home/Llama-4-Maverick-17B-128E-Instruct-for-quant -tp 8 -pp 2 --dtype auto --max-model-len 1000000 --gpu-memory-utilization 0.9 --limit-mm-per-prompt image=1 --enable-chunked-prefill` 2. doesn't work: `vllm serve /hf_home/Llama-4-Maverick-17B-128E-Instruct-for-quant -tp 8 -pp 2 --dtype auto --max-model-len 1000000 --gpu-memory-utilization 0.9 --limit-mm-per-prompt image=5 --enable-chunked-prefill` (diff: image=1 --> image=5) ``` RuntimeError: query, key and positions must have the same number of tokens ``` Full log here: https://pastebin.com/4nYz8f4T vLLM version: 0.8.5.post1 Engine: V0 (V1 engine doesn't work due to issues noted here https://github.com/vllm-project/vllm/issues/18023#issuecomment-2887043290) ### 🐛 Describe the bug . ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Llama-4-Maverick can't handle more than 1 image bug ### Your current environment Is it expected that Maverick can't handle more than 1 image with `vllm serve`? 1. works fine: `vllm serve /hf_home/Llama-4-Maverick...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: works fine: `vllm serve /hf_home/Llama-4-Maverick-17B-128E-Instruct-for-quant -tp 8 -pp 2 --dtype auto --max-model-len 1000000 --gpu-memory-utilization 0.9 --limit-mm-per-prompt image=1 --enable-chunked-prefill` 2. does...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e number of tokens ``` Full log here: https://pastebin.com/4nYz8f4T vLLM version: 0.8.5.post1 Engine: V0 (V1 engine doesn't work due to issues noted here https://github.com/vllm-project/vllm/issues/18023#issuecomment-28...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: . ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: pu-memory-utilization 0.9 --limit-mm-per-prompt image=1 --enable-chunked-prefill` 2. doesn't work: `vllm serve /hf_home/Llama-4-Maverick-17B-128E-Instruct-for-quant -tp 8 -pp 2 --dtype auto --max-model-len 1000000 --gpu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
