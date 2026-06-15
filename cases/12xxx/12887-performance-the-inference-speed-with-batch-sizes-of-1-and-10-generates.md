# vllm-project/vllm#12887: [Performance]:    The inference speed with batch sizes of 1 and 10 generates the same number of tokens per request.  (v0.7.2)

| 字段 | 值 |
| --- | --- |
| Issue | [#12887](https://github.com/vllm-project/vllm/issues/12887) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]:    The inference speed with batch sizes of 1 and 10 generates the same number of tokens per request.  (v0.7.2)

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` docker run --runtime nvidia -p 1234:1234 \ --gpus all \ --shm-size=24GB \ vllm/vllm-openai:v0.7.2 \ --gpu-memory-utilization 0.97 \ --served-model-name Mistral-Small-24B-Instruct-2501 \ --model /app/models/Mistral-Small-24B-Instruct-2501 \ --enforce-eager \ --enable-prefix-caching \ --tensor-parallel-size 1 \ --tokenizer_mode mistral \ --config_format mistral \ --load_format mistral \ --tool-call-parser mistral \ --enable-auto-tool-choice ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: current environment ```text The output of `python collect_env.py` ``` docker run --runtime nvidia -p 1234:1234 \ --gpus all \ --shm-size=24GB \ vllm/vllm-openai:v0.7.2 \ --gpu-memory-utilization 0.97 \ --served-model-na...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: lm/vllm-openai:v0.7.2 \ --gpu-memory-utilization 0.97 \ --served-model-name Mistral-Small-24B-Instruct-2501 \ --model /app/models/Mistral-Small-24B-Instruct-2501 \ --enforce-eager \ --enable-prefix-caching \ --tensor-pa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .2 \ --gpu-memory-utilization 0.97 \ --served-model-name Mistral-Small-24B-Instruct-2501 \ --model /app/models/Mistral-Small-24B-Instruct-2501 \ --enforce-eager \ --enable-prefix-caching \ --tensor-parallel-size 1 \ --t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: eed with batch sizes of 1 and 10 generates the same number of tokens per request. (v0.7.2) usage ### Your current environment ```text The output of `python collect_env.py` ``` docker run --runtime nvidia -p 1234:1234 \...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
