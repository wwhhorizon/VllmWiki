# vllm-project/vllm#18381: [Bug]: Does not support video input for InternVL series models

| 字段 | 值 |
| --- | --- |
| Issue | [#18381](https://github.com/vllm-project/vllm/issues/18381) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Does not support video input for InternVL series models

### Issue 正文摘录

### Your current environment ``` ValueError: At most 0 video(s) may be provided in one request. You can set `--limit-mm-per-prompt` to increase this limit if the model supports it. /localhome/dlfg/anaconda3/envs/game_vlm/lib/python3.10/site-packages/vllm/entrypoints/openai/serving_chat.py:200: RuntimeWarning: coroutine 'MediaConnector.fetch_video_async' was never awaited return self.create_error_response(f"{e} {e.__cause__}") ``` ### 🐛 Describe the bug Does not support video input for InternVL series models ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Does not support video input for InternVL series models bug ### Your current environment ``` ValueError: At most 0 video(s) may be provided in one request. You can set `--limit-mm-per-prompt` to increase this lim...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: els ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: nvironment ``` ValueError: At most 0 video(s) may be provided in one request. You can set `--limit-mm-per-prompt` to increase this limit if the model supports it. /localhome/dlfg/anaconda3/envs/game_vlm/lib/python3.10/s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
