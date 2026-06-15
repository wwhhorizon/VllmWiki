# vllm-project/vllm#3965: [Bug]: NVIDIA A100 actually supports fp8_e5m2 quantization.

| 字段 | 值 |
| --- | --- |
| Issue | [#3965](https://github.com/vllm-project/vllm/issues/3965) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: NVIDIA A100 actually supports fp8_e5m2 quantization.

### Issue 正文摘录

### Your current environment NVIDIA-SMI 530.30.02 Driver Version: 530.30.02 CUDA Version: 12.1 NVIDIA A100-SXM4-80GB ### 🐛 Describe the bug I successfully ran the following code, but it should not be because the GPU is A100 and it does not support fp8. Why? `from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="facebook/opt-125m", kv_cache_dtype="fp8_e5m2") outputs = llm.generate(prompts, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")`

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: NVIDIA A100 actually supports fp8_e5m2 quantization. bug ### Your current environment NVIDIA-SMI 530.30.02 Driver Version: 530.30.02 CUDA Version: 12.1 NVIDIA A100-SXM4-80GB ### 🐛 Describe the bug I successfully...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: NVIDIA A100 actually supports fp8_e5m2 quantization. bug ### Your current environment NVIDIA-SMI 530.30.02 Driver Version: 530.30.02 CUDA Version: 12.1 NVIDIA A100-SXM4-80GB ### 🐛 Describe the bug I successf
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: g ### Your current environment NVIDIA-SMI 530.30.02 Driver Version: 530.30.02 CUDA Version: 12.1 NVIDIA A100-SXM4-80GB ### 🐛 Describe the bug I successfully ran the following code, but it should not be because the GPU i...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="facebook/opt-125m", kv_cache_dtype="fp8_e5m2") outputs = llm.generate(prompts, sampling_params) for output in outputs: prompt = output.promp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
