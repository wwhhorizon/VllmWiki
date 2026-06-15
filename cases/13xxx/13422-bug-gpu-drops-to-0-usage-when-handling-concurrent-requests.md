# vllm-project/vllm#13422: [Bug]: GPU drops to 0 usage when handling concurrent requests

| 字段 | 值 |
| --- | --- |
| Issue | [#13422](https://github.com/vllm-project/vllm/issues/13422) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPU drops to 0 usage when handling concurrent requests

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to benchmark an application. This benchmark sends concurrent requests to vLLM. At first, everything works fine. However, after some time, the GPU usage drops to 0 and the output token throughput drops significantly in performance. Requests almost seem to "hang", even though there is still a positive output throughput. Depending on the model, this can happen at the start of the benchmark, or almost at the end, when there are only 5 requests left to process. I am using vllm's docker image : vllm/vllm-openai:latest With the following start command: --host 0.0.0.0 --port 8000 --max-model-len 32000 --tensor-parallel-size 4 --model deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct --max-seq-len-to-capture 32000 --trust-remote-code Initially I did not set --max-seq-len-to-capture and the same thing happened. I have experimented with varying values of max-model-len. ![Image](https://github.com/user-attachments/assets/391bf1fd-90ad-4c88-96ab-3a72242327d1) After some time: ![Image](https://github.com/user-attachments/assets/9a16eda7-1312-4d2f-9428-02f62d1b9b59) ![Image](https://github.com/user-attachments/assets/04399f25-60c9-422f-bd...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: end, when there are only 5 requests left to process. I am using vllm's docker image : vllm/vllm-openai:latest With the following start command: --host 0.0.0.0 --port 8000 --max-model-len 32000 --tensor-parallel-size 4 -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: GPU drops to 0 usage when handling concurrent requests bug;stale ### Your current environment ### 🐛 Describe the bug I am trying to benchmark an application. This benchmark sends concurrent requests to vLLM. At f...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ### Your current environment ### 🐛 Describe the bug I am trying to benchmark an application. This benchmark sends concurrent requests to vLLM. At first, everything works fine. However, after some time, the GPU usage dro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 04) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf;slowdown env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
