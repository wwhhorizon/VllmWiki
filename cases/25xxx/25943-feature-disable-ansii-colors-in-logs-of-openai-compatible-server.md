# vllm-project/vllm#25943: [Feature]: Disable ANSII colors in logs of OpenAI compatible server

| 字段 | 值 |
| --- | --- |
| Issue | [#25943](https://github.com/vllm-project/vllm/issues/25943) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Disable ANSII colors in logs of OpenAI compatible server

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently it seems there isn't any way to disable the ANSII escape sequences in the logs of the OpenAI compatible server. For some deployment env (such as runpod) it means the log is polluted with the following output: ``` [1;36m(APIServer pid=20)[0;0m INFO 09-30 02:56:46 [launcher.py:44] Route: /v1/audio/transcriptions, Methods: POST [1;36m(APIServer pid=20)[0;0m INFO 09-30 02:56:46 [launcher.py:44] Route: /v1/audio/translations, Methods: POST [1;36m(APIServer pid=20)[0;0m INFO 09-30 02:56:46 [launcher.py:44] Route: /rerank, Methods: POST [1;36m(APIServer pid=20)[0;0m INFO 09-30 02:56:46 [launcher.py:44] Route: /v1/rerank, Methods: POST [1;36m(APIServer pid=20)[0;0m INFO 09-30 02:56:46 [launcher.py:44] Route: /v2/rerank, Methods: POST [1;36m(APIServer pid=20)[0;0m INFO 09-30 02:56:46 [launcher.py:44] Route: /scale_elastic_ep, Methods: POST [1;36m(APIServer pid=20)[0;0m INFO 09-30 02:56:46 [launcher.py:44] Route: /is_scaling_elastic_ep, Methods: POST [1;36m(APIServer pid=20)[0;0m INFO 09-30 02:56:46 [launcher.py:44] Route: /invocations, Methods: POST [1;36m(APIServer pid=20)[0;0m INFO 09-30 02:56:46 [launcher.py:44] Route:...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ature]: Disable ANSII colors in logs of OpenAI compatible server feature request;stale ### 🚀 The feature, motivation and pitch Currently it seems there isn't any way to disable the ANSII escape sequences in the logs of...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 36m(APIServer pid=20)[0;0m INFO 09-30 02:56:46 [launcher.py:44] Route: /scale_elastic_ep, Methods: POST [1;36m(APIServer pid=20)[0;0m INFO 09-30 02:56:46 [launcher.py:44] Route: /is_scaling_elastic_ep, Methods: POST...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
