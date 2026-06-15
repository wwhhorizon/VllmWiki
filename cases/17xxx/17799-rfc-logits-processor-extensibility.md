# vllm-project/vllm#17799: [RFC]: Logits processor extensibility

| 字段 | 值 |
| --- | --- |
| Issue | [#17799](https://github.com/vllm-project/vllm/issues/17799) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Logits processor extensibility

### Issue 正文摘录

### Motivation. Users want logits processor extensibility, i.e. the ability to specify logits processors beyond those such as min-p which are hard-coded into the engine. See for example: * #12678 * https://github.com/NVIDIA/logits-processor-zoo - library of logits processor extensions The purpose of this RFC is to establish the interface for extending the vLLM V1 engine with additional logits processors during engine instantiation. vLLM V0 supports logits processor configuration at request level (`SamplingParams` attribute). For V0 running in server mode, PR #11150 makes it possible for a request to dynamically import one or more logits processor modules, assuming that the necessary modules are available/installed. The `logits_processors` argument (available in the completion, chat completion and transcription API endpoints) allows the custom logits processors’ constructors to be specified as a list of (1) qualified names, or (2) `LogitsProcessorConstructor` data structures (which include the qualified name along with constructor arguments). For security purposes (prevention of arbitrary code execution), `​​--logits-processor-pattern` whitelists specific logits processor libraries...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: tion. Users want logits processor extensibility, i.e. the ability to specify logits processors beyond those such as min-p which are hard-coded into the engine. See for example: * #12678 * https://github.com/NVIDIA/logit...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ocessors during engine instantiation. vLLM V0 supports logits processor configuration at request level (`SamplingParams` attribute). For V0 running in server mode, PR #11150 makes it possible for a request to dynamicall...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ngine instantiation. vLLM V0 supports logits processor configuration at request level (`SamplingParams` attribute). For V0 running in server mode, PR #11150 makes it possible for a request to dynamically import one or m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
