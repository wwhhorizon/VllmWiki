# vllm-project/vllm#22249: [Bug]: qwen3 moe fp8 perchannel compressed-tensors model cannot infer

| 字段 | 值 |
| --- | --- |
| Issue | [#22249](https://github.com/vllm-project/vllm/issues/22249) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: qwen3 moe fp8 perchannel compressed-tensors model cannot infer

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I use llm-compressor. I got fp8 perchanel pertoken model of qwen3 moe model. It cannot infer. But when I set enforce_eager=True, it can infer. ``` from transformers import AutoTokenizer from vllm import LLM, SamplingParams model_path = '/mnt/afs_1/yongyang/Qwen3-30B-A3B-fp8-perchannel-vllm' model = LLM(model_path, tensor_parallel_size=8, enforce_eager=False) tokenizer = AutoTokenizer.from_pretrained(model_path) prompts = [ 'Hello, my name is', 'The president of the United States is', 'The capital of France is', 'The future of AI is', ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) outputs = model.generate(prompts, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f'Prompt: {prompt!r}, Generated text: {generated_text!r}') ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: qwen3 moe fp8 perchannel compressed-tensors model cannot infer bug;stale ### Your current environment ### 🐛 Describe the bug I use llm-compressor. I got fp8 perchanel pertoken model of qwen3 moe model. It cannot...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: But when I set enforce_eager=True, it can infer. ``` from transformers import AutoTokenizer from vllm import LLM, SamplingParams model_path = '/mnt/afs_1/yongyang/Qwen3-30B-A3B-fp8-perchannel-vllm' model = LLM(model_pat...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: qwen3 moe fp8 perchannel compressed-tensors model cannot infer bug;stale ### Your current environment ### 🐛 Describe the bug I use llm-compressor. I got fp8 perchanel pertoken model of qwen3 moe model. It cannot...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: l-vllm' model = LLM(model_path, tensor_parallel_size=8, enforce_eager=False) tokenizer = AutoTokenizer.from_pretrained(model_path) prompts = [ 'Hello, my name is', 'The president of the United States is', 'The capital o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
