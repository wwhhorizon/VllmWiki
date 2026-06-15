# vllm-project/vllm#22284: [Bug] [gpt-oss-20b] [Responses API]: Could not parse header: too many tokens remaining after extracting content-type and recipient

| 字段 | 值 |
| --- | --- |
| Issue | [#22284](https://github.com/vllm-project/vllm/issues/22284) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] [gpt-oss-20b] [Responses API]: Could not parse header: too many tokens remaining after extracting content-type and recipient

### Issue 正文摘录

### Your current environment Install the PR https://github.com/vllm-project/vllm/pull/22259 ``` uv pip install --pre vllm==0.10.1+gptoss \ --extra-index-url https://wheels.vllm.ai/gpt-oss/ \ --extra-index-url https://download.pytorch.org/whl/nightly/cu128 \ --index-strategy unsafe-best-match ``` ``` vllm serve \ openai/gpt-oss-20b \ --tensor_parallel_size \ 2 \ --max-model-len \ 131072 \ --max-num-batched-tokens \ 10240 \ --max-num-seqs \ 128 \ --gpu-memory-utilization \ 0.85 \ --no-enable-prefix-caching \ --async-scheduling ``` ### 🐛 Describe the bug ``` $ python bug-repro.py --failing $ python bug-repro.py --working ``` ``` $ python bug-repro.py --failing Traceback (most recent call last): File "/root/bug-repro/bug-repro.py", line 125, in main() File "/root/bug-repro/bug-repro.py", line 14, in main run_failing_case() File "/root/bug-repro/bug-repro.py", line 72, in run_failing_case resp = send_request({ ^^^^^^^^^^^^^^ File "/root/bug-repro/bug-repro.py", line 121, in send_request raise Exception(f"Failed to get response: {response.status_code} {response.text}") Exception: Failed to get response: 400 {"object":"error","message":"Could not parse header: too many tokens remaining a...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: se header: too many tokens remaining after extracting content-type and recipient bug;stale ### Your current environment Install the PR https://github.com/vllm-project/vllm/pull/22259 ``` uv pip install --pre vllm==0.10....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug] [gpt-oss-20b] [Responses API]: Could not parse header: too many tokens remaining after extracting content-type and recipient bug;stale ### Your current environment Install the PR https://github.com/vllm-project/vl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: oo many tokens remaining after extracting content-type and recipient bug;stale ### Your current environment Install the PR https://github.com/vllm-project/vllm/pull/22259 ``` uv pip install --pre vllm==0.10.1+gptoss \ -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
