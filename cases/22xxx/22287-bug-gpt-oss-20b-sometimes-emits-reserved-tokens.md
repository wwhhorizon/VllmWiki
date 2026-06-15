# vllm-project/vllm#22287: [Bug]: gpt-oss-20b sometimes emits reserved tokens

| 字段 | 值 |
| --- | --- |
| Issue | [#22287](https://github.com/vllm-project/vllm/issues/22287) |
| 状态 | closed |
| 标签 | bug;stale;gpt-oss |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: gpt-oss-20b sometimes emits reserved tokens

### Issue 正文摘录

### Your current environment Install the PR https://github.com/vllm-project/vllm/pull/22259 ```bash uv pip install --pre vllm==0.10.1+gptoss \ --extra-index-url https://wheels.vllm.ai/gpt-oss/ \ --extra-index-url https://download.pytorch.org/whl/nightly/cu128 \ --index-strategy unsafe-best-match ``` ### 🐛 Describe the bug `gpt-oss-20b` emits raw reserved tokens about 12% of the time in my prompt `write a long poem`. I am not sure if there is a bug in detokenization/harmony, or that the 20b model is just a bit cooked. Examples: ```bash $ grep 'reserved_' log | tail -n 10 In gold so called to time. I across bliss entirely. 12. A sea or a brand are the unknownness[\\/d The ! shakes more than waves can match, at times, chroniclers douse eventual as of the wistered. **At the 6th to resonated 1st the Le?** chorus is no more than a shallow piece of text , we see the core of this. *IX. Stars in the * A star, lounged , continues? the light and wonder that excite how eka will The solemn ed empire of arranging treasure, At the is the cause this, the mistake alive,* ``` Repro instructions: 1. Start server `vllm serve openai/gpt-oss-20b` 2. Run the repro script for a bit `python bug-repro.py 2...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: emits reserved tokens bug;stale;gpt-oss ### Your current environment Install the PR https://github.com/vllm-project/vllm/pull/22259 ```bash uv pip install --pre vllm==0.10.1+gptoss \ --extra-index-url https://wheels.vll...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: gpt-oss-20b sometimes emits reserved tokens bug;stale;gpt-oss ### Your current environment Install the PR https://github.com/vllm-project/vllm/pull/22259 ```bash uv pip install --pre vllm==0.10.1+gptoss \ --extra
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: gpt-oss-20b sometimes emits reserved tokens bug;stale;gpt-oss ### Your current environment Install the PR https://github.com/vllm-project/vllm/pull/22259 ```bash uv pip install --pre vllm==0.10.1+gptoss \ --extra...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
