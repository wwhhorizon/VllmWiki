# vllm-project/vllm#9050: [Bug]: TypeError: inputs must be a string, TextPrompt, or TokensPrompt

| 字段 | 值 |
| --- | --- |
| Issue | [#9050](https://github.com/vllm-project/vllm/issues/9050) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: TypeError: inputs must be a string, TextPrompt, or TokensPrompt

### Issue 正文摘录

### Your current environment I am using `torchserve` to spin up the vLLM instance (https://github.com/pytorch/serve?tab=readme-ov-file#-quick-start-llm-deployment-with-docker). ### Model Input Dumps _No response_ ### 🐛 Describe the bug Here's the stacktrace I see: ``` 2024-10-03T17:37:44,150 [INFO ] W-9000-model_1.0-stdout MODEL_LOG - result = task.result() 2024-10-03T17:37:44,150 [INFO ] W-9000-model_1.0-stdout MODEL_LOG - File "/home/venv/lib/python3.9/site-packages/vllm/engine/async_llm_engine.py", line 661, in engine_step 2024-10-03T17:37:44,150 [INFO ] W-9000-model_1.0-stdout MODEL_LOG - await self.engine.add_request_async(**new_request) 2024-10-03T17:37:44,150 [INFO ] W-9000-model_1.0-stdout MODEL_LOG - File "/home/venv/lib/python3.9/site-packages/vllm/engine/async_llm_engine.py", line 419, in add_request_async 2024-10-03T17:37:44,150 [INFO ] W-9000-model_1.0-stdout MODEL_LOG - preprocessed_inputs = await self.input_preprocessor.preprocess_async( 2024-10-03T17:37:44,150 [INFO ] W-9000-model_1.0-stdout MODEL_LOG - File "/home/venv/lib/python3.9/site-packages/vllm/inputs/preprocess.py", line 528, in preprocess_async 2024-10-03T17:37:44,150 [INFO ] W-9000-model_1.0-stdout MODEL...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ub.com/pytorch/serve?tab=readme-ov-file#-quick-start-llm-deployment-with-docker). ### Model Input Dumps _No response_ ### 🐛 Describe the bug Here's the stacktrace I see: ``` 2024-10-03T17:37:44,150 [INFO ] W-9000-model_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ug]: TypeError: inputs must be a string, TextPrompt, or TokensPrompt bug;stale ### Your current environment I am using `torchserve` to spin up the vLLM instance (https://github.com/pytorch/serve?tab=readme-ov-file#-quic...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: /serve?tab=readme-ov-file#-quick-start-llm-deployment-with-docker). ### Model Input Dumps _No response_ ### 🐛 Describe the bug Here's the stacktrace I see: ``` 2024-10-03T17:37:44,150 [INFO ] W-9000-model_1.0-stdout MOD...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
