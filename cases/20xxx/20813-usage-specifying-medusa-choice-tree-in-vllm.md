# vllm-project/vllm#20813: [Usage]: Specifying Medusa Choice Tree in vllm"

| 字段 | 值 |
| --- | --- |
| Issue | [#20813](https://github.com/vllm-project/vllm/issues/20813) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Specifying Medusa Choice Tree in vllm"

### Issue 正文摘录

### How would you like to use vllm **Description** I'm using `vllm` to load a model with a Medusa heads. My current implementation uses the following setup: ```python from vllm import SamplingParams from vllm import EngineArgs, LLMEngine MODEL_NAME = "JackFram/llama-68m" SPEC_MODEL = "abhigoyal/vllm-medusa-llama-68m-random" llm = LLM( model=MODEL_NAME, max_model_len=1024, speculative_config={ "method" : "medusa", "model": SPEC_MODEL, "num_speculative_tokens": 3, }, tensor_parallel_size=1, seed=0, ) outputs = llm.generate(prompts=["Hi! How are you doing?", "Hi! How are you doing?"], use_tqdm=True) ``` Question I want to know how to specify the Medusa choice tree for the model. Could you provide guidance or examples on how to do this? Environment - Python version: 3.11 - vllm version: 0.9.2 - OS: linux ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Usage]: Specifying Medusa Choice Tree in vllm" usage;stale ### How would you like to use vllm **Description** I'm using `vllm` to load a model with a Medusa heads. My current implementation uses the following setup: ``...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: w would you like to use vllm **Description** I'm using `vllm` to load a model with a Medusa heads. My current implementation uses the following setup: ```python from vllm import SamplingParams from vllm import EngineArg...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Specifying Medusa Choice Tree in vllm" usage;stale ### How would you like to use vllm **Description** I'm using `vllm` to load a model with a Medusa heads. My current implementation uses the following setup: ``...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nux ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
