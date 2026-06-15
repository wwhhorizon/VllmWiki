# vllm-project/vllm#18892: [Bug]: some vllm routes can be reached without authorization

| 字段 | 值 |
| --- | --- |
| Issue | [#18892](https://github.com/vllm-project/vllm/issues/18892) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: some vllm routes can be reached without authorization

### Issue 正文摘录

### Your current environment . ### 🐛 Describe the bug I start vllm serve with set `export VLLM_API_KEY=****` in env. ``` vllm serve "$model_name" --host 0.0.0.0 --port 4015 -tp=4 \ --served-model-name="Qwen3" \ --max_num_seqs=64 \ --max_model_len=10240 \ --gpu-memory-utilization=0.85 \ --disable-fastapi-docs \ --disable-log-requests \ --disable-uvicorn-access-log ``` I find the following routes can be reached bypass VLLM_API_KEY without authorization ``` INFO 05-29 16:17:29 [launcher.py:28] Available routes are: INFO 05-29 16:17:29 [launcher.py:36] Route: /health, Methods: GET INFO 05-29 16:17:29 [launcher.py:36] Route: /load, Methods: GET INFO 05-29 16:17:29 [launcher.py:36] Route: /ping, Methods: POST INFO 05-29 16:17:29 [launcher.py:36] Route: /ping, Methods: GET INFO 05-29 16:17:29 [launcher.py:36] Route: /tokenize, Methods: POST INFO 05-29 16:17:29 [launcher.py:36] Route: /detokenize, Methods: POST INFO 05-29 16:17:29 [launcher.py:36] Route: /version, Methods: GET INFO 05-29 16:17:29 [launcher.py:36] Route: /pooling, Methods: POST INFO 05-29 16:17:29 [launcher.py:36] Route: /classify, Methods: POST INFO 05-29 16:17:29 [launcher.py:36] Route: /score, Methods: POST INFO 05-29 1...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: vllm serve with set `export VLLM_API_KEY=****` in env. ``` vllm serve "$model_name" --host 0.0.0.0 --port 4015 -tp=4 \ --served-model-name="Qwen3" \ --max_num_seqs=64 \ --max_model_len=10240 \ --gpu-memory-utilization=0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: some vllm routes can be reached without authorization bug;stale ### Your current environment . ### 🐛 Describe the bug I start vllm serve with set `export VLLM_API_KEY=****` in env. ``` vllm serve "$model_name" --...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: /detokenize, Methods: POST INFO 05-29 16:17:29 [launcher.py:36] Route: /version, Methods: GET INFO 05-29 16:17:29 [launcher.py:36] Route: /pooling, Methods: POST INFO 05-29 16:17:29 [launcher.py:36] Route: /classify, Me...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 08) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
