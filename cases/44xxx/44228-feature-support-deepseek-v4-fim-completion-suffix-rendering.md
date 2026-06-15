# vllm-project/vllm#44228: [Feature]: Support DeepSeek-V4 FIM completion suffix rendering

| 字段 | 值 |
| --- | --- |
| Issue | [#44228](https://github.com/vllm-project/vllm/issues/44228) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support DeepSeek-V4 FIM completion suffix rendering

### Issue 正文摘录

### Motivation DeepSeek's official API documents FIM (Fill In the Middle) completion on the completions endpoint by passing both `prompt` and `suffix` with the beta base URL. This is useful for code completion and editor autocomplete workflows. The current vLLM OpenAI-compatible completions request schema already accepts `suffix`, but the render path rejects any request with `suffix` before tokenization: ```text suffix is not currently supported ``` DeepSeek-V4 checkpoints expose native FIM control tokens in the tokenizer, so vLLM can support this request shape by rendering the completion prompt into the model's FIM prompt format before normal generation. ### Proposed behavior For DeepSeek-V4 completion requests where `suffix` is provided and `prompt` is text, render the engine prompt as: ```text {prompt} {suffix} ``` Then route the request through the existing `/v1/completions` generation path. ### Evidence Using a local `/models/DeepSeek-V4-Flash` checkpoint, the tokenizer contains these FIM tokens: ```text = 128800 = 128801 = 128802 ``` The checkpoint config has: ```text model_type: deepseek_v4 architectures: [DeepseekV4ForCausalLM] ``` An official DeepSeek API probe with `prom...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: n support this request shape by rendering the completion prompt into the model's FIM prompt format before normal generation. ### Proposed behavior For DeepSeek-V4 completion requests where `suffix` is provided and `prom...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: epSeek-V4 FIM completion suffix rendering ### Motivation DeepSeek's official API documents FIM (Fill In the Middle) completion on the completions endpoint by passing both `prompt` and `suffix` with the beta base URL. Th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 128802 ``` The checkpoint config has: ```text model_type: deepseek_v4 architectures: [DeepseekV4ForCausalLM] ``` An official DeepSeek API probe with `prompt="def fib(n):\n if n < 2:\n return n\n return "` and `suffix="\...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: autocomplete workflows. The current vLLM OpenAI-compatible completions request schema already accepts `suffix`, but the render path rejects any request with `suffix` before tokenization: ```text suffix is not currently...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
