# vllm-project/vllm#24133: [Bug]: vLLM stuck when serving GLM-4.5 model

| 字段 | 值 |
| --- | --- |
| Issue | [#24133](https://github.com/vllm-project/vllm/issues/24133) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM stuck when serving GLM-4.5 model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Tried serving [GLM-4.5](https://huggingface.co/zai-org/GLM-4.5) model on 8xH100 setup: ``` VLLM_LOGGING_LEVEL=DEBUG VLLM_TRACE_FUNCTION=1 vllm serve zai-org/GLM-4.5 --max-model-len 32768 --enforce-eager -tp 8 ``` After model loading, vLLM seems to be hung waiting for a local process to start here: https://github.com/vllm-project/vllm/blob/862f2ef893d9751db0a92bd2d4ae0e3d9677872f/vllm/v1/engine/utils.py#L776-L779 ``` (APIServer pid=300606) DEBUG 09-02 17:29:06 [utils.py:777] Waiting for 1 local, 0 remote core engine proc(s) to start. (APIServer pid=300606) DEBUG 09-02 17:29:16 [utils.py:777] Waiting for 1 local, 0 remote core engine proc(s) to start. ``` Tried another MoE model dots1 (`rednote-hilab/dots.vlm1.inst`) but this works. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: vLLM stuck when serving GLM-4.5 model bug;stale ### Your current environment ### 🐛 Describe the bug Tried serving [GLM-4.5](https://huggingface.co/zai-org/GLM-4.5) model on 8xH100 setup: ``` VLLM_LOGGING_LEVEL=DE...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ied serving [GLM-4.5](https://huggingface.co/zai-org/GLM-4.5) model on 8xH100 setup: ``` VLLM_LOGGING_LEVEL=DEBUG VLLM_TRACE_FUNCTION=1 vllm serve zai-org/GLM-4.5 --max-model-len 32768 --enforce-eager -tp 8 ``` After mo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vLLM stuck when serving GLM-4.5 model bug;stale ### Your current environment ### 🐛 Describe the bug Tried serving [GLM-4.5](https://huggingface.co/zai-org/GLM-4.5) model on 8xH100 setup: ``` VLLM_LOGGING_LEVEL=DE...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: g for 1 local, 0 remote core engine proc(s) to start. ``` Tried another MoE model dots1 (`rednote-hilab/dots.vlm1.inst`) but this works. ### Before submitting a new issue... - [x] Make sure you already searched for rele...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
