# vllm-project/vllm#21858: [Bug]: TORCHINDUCTOR_FORCE_DISABLE_CACHES=1 fails with vLLM-compile in torch <= 2.7.1

| 字段 | 值 |
| --- | --- |
| Issue | [#21858](https://github.com/vllm-project/vllm/issues/21858) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: TORCHINDUCTOR_FORCE_DISABLE_CACHES=1 fails with vLLM-compile in torch <= 2.7.1

### Issue 正文摘录

### Your current environment PyTorch 2.7.1, ### 🐛 Describe the bug `TORCHINDUCTOR_FORCE_DISABLE_CACHES=1 vllm serve` fails with the following. It doesn't matter what model gets used, this fails as long as you're using vLLM-compile. ``` RuntimeError: vLLM failed to compile the model. The most likely reason for this is that a previous compilation failed, leading to a corr upted compilation artifact. We recommend trying to remove ~/.cache/vllm/torch_compile_cache and try again to see the real issue. ``` I believe this problem is fixed in PyTorch 2.8, so we could just wait until then. But I'm not completely sure we can fix this in PyTorch 2.7. If not, the only thing we can do is make the error message better. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: TORCHINDUCTOR_FORCE_DISABLE_CACHES=1 fails with vLLM-compile in torch <= 2.7.1 bug;torch.compile ### Your current environment PyTorch 2.7.1, ### 🐛 Describe the bug `TORCHINDUCTOR_FORCE_DISABLE_CACHES=1 vllm serve...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: er. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: LE_CACHES=1 vllm serve` fails with the following. It doesn't matter what model gets used, this fails as long as you're using vLLM-compile. ``` RuntimeError: vLLM failed to compile the model. The most likely reason for t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
