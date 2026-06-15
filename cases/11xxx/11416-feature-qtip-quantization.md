# vllm-project/vllm#11416: [Feature]: QTIP Quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#11416](https://github.com/vllm-project/vllm/issues/11416) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: QTIP Quantization

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Over the last year there have been several exciting new low-bit quantization algorithms proposed. These include AQLM (which is now in VLLM) and QuIP (which is in aphrodite engine, a vllm relative). QTIP is a new algorithm which has almost lossless performance even at 2-bits. There is code available implementing the technique here: https://github.com/Cornell-RelaxML/qtip I have run this code and experimented with the 8b lllama 3.1 model quantized down to 2-bits and I have to say I'm very very impressed. I did not notice any performance loss and its certainly way better than other 2-bit quants I have tried (in those cases with exl2 and GGUF the models are noticeably more stupid). Would it be possible to implement this in VLLM? ### Alternatives AQLM and QuIP are alternatives I'm aware of that still retain some performance at 2-bits. GGUF/exl2/etc have extremely degraded performance at 2-bits. According to their paper QTIP retains more performance than AQLM and QuIP. It may also be cheaper to produce quantizations, which to my knowledge for AQLM at least are currently very expensive to make, requiring access to compute clusters. ### Additional c...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Cornell-RelaxML/qtip I have run this code and experimented with the 8b lllama 3.1 model quantized down to 2-bits and I have to say I'm very very impressed. I did not notice any performance loss and its certainly way bet...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: QTIP Quantization feature request;stale ### 🚀 The feature, motivation and pitch Over the last year there have been several exciting new low-bit quantization algorithms proposed. These include AQLM (which is n...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ture, motivation and pitch Over the last year there have been several exciting new low-bit quantization algorithms proposed. These include AQLM (which is now in VLLM) and QuIP (which is in aphrodite engine, a vllm relat...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: QTIP Quantization feature request;stale ### 🚀 The feature, motivation and pitch Over the last year there have been several exciting new low-bit quantization algorithms proposed. These include AQLM (which is n...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 235 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
