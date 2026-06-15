# vllm-project/vllm#11284: [Bug]: Issues with vLLM tool call functionality leading to abnormal requests

| 字段 | 值 |
| --- | --- |
| Issue | [#11284](https://github.com/vllm-project/vllm/issues/11284) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Issues with vLLM tool call functionality leading to abnormal requests

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am encountering issues while using the tool call capability of vLLM. Some requests are behaving abnormally, and the log indicates the following error: ![20241218-135723](https://github.com/user-attachments/assets/e9d4e618-74d2-43f7-94ea-37089a2543d0) Additionally, my startup script is as follows: -d vllm/vllm-openai:v0.6.3.post1 \ --host 0.0.0.0 --port 30000 \ --model /llm/models/Qwen2.5-32B-Instruct \ --served-model-name qwen2.5-32b-instruct \ --dtype auto \ --tensor-parallel-size 2 \ --gpu-memory-utilization 0.90 \ --enable-prefix-caching \ --enable-auto-tool-choice \ --tool-call-parser hermes Currently, I am using vLLM version:vllm/vllm-openai:v0.6.3.post1 Could you please provide guidance on how to resolve this issue? Any help would be greatly appreciated. Thank you! ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: l-choice \ --tool-call-parser hermes Currently, I am using vLLM version:vllm/vllm-openai:v0.6.3.post1 Could you please provide guidance on how to resolve this issue? Any help would be greatly appreciated. Thank you! ###...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: # 🐛 Describe the bug I am encountering issues while using the tool call capability of vLLM. Some requests are behaving abnormally, and the log indicates the following error: ![20241218-135723](https://github.com/user-at...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ding to abnormal requests bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am encountering issues while using the tool call capability of vLLM. Some requests are behavi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Issues with vLLM tool call functionality leading to abnormal requests bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am encountering issues while using the too...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: -Instruct \ --served-model-name qwen2.5-32b-instruct \ --dtype auto \ --tensor-parallel-size 2 \ --gpu-memory-utilization 0.90 \ --enable-prefix-caching \ --enable-auto-tool-choice \ --tool-call-parser hermes Currently,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
