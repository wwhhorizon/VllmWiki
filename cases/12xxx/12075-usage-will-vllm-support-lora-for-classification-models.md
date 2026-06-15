# vllm-project/vllm#12075: [Usage]: Will vLLM support LoRA for classification models?

| 字段 | 值 |
| --- | --- |
| Issue | [#12075](https://github.com/vllm-project/vllm/issues/12075) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Will vLLM support LoRA for classification models?

### Issue 正文摘录

### Your current environment I attempted to use LoRA for a classification model with the latest vllm version, but it didn't work. ``` model = LLM( model="./qwen_cls", task="classify", enable_lora = True, max_loras=4 ) (output,) = model.classify("Hello, my name is",lora_request=LoRARequest("cls", 1, './cls_lora') ) probs = output.outputs.probs print(f"Class Probabilities: {probs!r} (size={len(probs)})") ``` ![Image](https://github.com/user-attachments/assets/d7c6948b-cef9-49c5-8426-03f94fb91458) ### How would you like to use vllm _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Will vLLM support LoRA for classification models? usage;stale ### Your current environment I attempted to use LoRA for a classification model with the latest vllm version, but it didn't work. ``` model = LLM( m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Will vLLM support LoRA for classification models? usage;stale ### Your current environment I attempted to use LoRA for a classification model with the latest vllm version, but it didn't work. ``` model = LLM( m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: I attempted to use LoRA for a classification model with the latest vllm version, but it didn't work. ``` model = LLM( model="./qwen_cls", task="classify", enable_lora = True, max_loras=4 ) (output,) = model.classify("He...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: vironment I attempted to use LoRA for a classification model with the latest vllm version, but it didn't work. ``` model = LLM( model="./qwen_cls", task="classify", enable_lora = True, max_loras=4 ) (output,) = model.cl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
