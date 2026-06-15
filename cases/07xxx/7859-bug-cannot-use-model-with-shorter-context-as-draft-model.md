# vllm-project/vllm#7859: [Bug]: Cannot use model with shorter context as draft model

| 字段 | 值 |
| --- | --- |
| Issue | [#7859](https://github.com/vllm-project/vllm/issues/7859) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Cannot use model with shorter context as draft model

### Issue 正文摘录

### Your current environment I'm running the latest vllm/vllm-openai docker image on an 8xH100 node ### 🐛 Describe the bug I'm trying to run vllm with mistral large 2 (123B) and mistral 7B 0.3 as the draft model. However, since the 7B model only has a 32k context to the target models 128K context, I often run into raise RuntimeError("Cannot handle cases where distributed draft " "workers generate no tokens") https://github.com/vllm-project/vllm/blob/0b769992ec1d780b3229c46152c6e647da113aa6/vllm/spec_decode/spec_decode_worker.py#L576 Is there a solution to this? How to repro: ``` vllm serve mistralai/Mistral-Large-Instruct-2407 --dtype auto --port 8000 --max-model-len 128000 --served-model-name baseten/8w6xo22w --tensor-parallel-size 8 --speculative-model mistralai/Mistral-7B-Instruct-v0.3 --num-speculative-tokens 10 --num-lookahead-slots 10 --use-v2-block-manager --gpu-memory-utilization 0.95 --uvicorn-log-level warning ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questi...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Cannot use model with shorter context as draft model bug;stale ### Your current environment I'm running the latest vllm/vllm-openai docker image on an 8xH100 node ### 🐛 Describe the bug I'm trying to run vllm wit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nvironment I'm running the latest vllm/vllm-openai docker image on an 8xH100 node ### 🐛 Describe the bug I'm trying to run vllm with mistral large 2 (123B) and mistral 7B 0.3 as the draft model. However, since the 7B mo...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: lai/Mistral-7B-Instruct-v0.3 --num-speculative-tokens 10 --num-lookahead-slots 10 --use-v2-block-manager --gpu-memory-utilization 0.95 --uvicorn-log-level warning ``` ### Before submitting a new issue... - [X] Make sure...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: le ### Your current environment I'm running the latest vllm/vllm-openai docker image on an 8xH100 node ### 🐛 Describe the bug I'm trying to run vllm with mistral large 2 (123B) and mistral 7B 0.3 as the draft model. How...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: s? How to repro: ``` vllm serve mistralai/Mistral-Large-Instruct-2407 --dtype auto --port 8000 --max-model-len 128000 --served-model-name baseten/8w6xo22w --tensor-parallel-size 8 --speculative-model mistralai/Mistral-7...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
