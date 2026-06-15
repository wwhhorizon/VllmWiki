# vllm-project/vllm#2189: The inference results of vllm and HF are inconsistent

| 字段 | 值 |
| --- | --- |
| Issue | [#2189](https://github.com/vllm-project/vllm/issues/2189) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | frontend_api;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;sampling |
| 症状 | mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> The inference results of vllm and HF are inconsistent

### Issue 正文摘录

# vllm和HF推理结果不一致 ## Config Info - vllm 0.2.5 - transformers 4.36.0 - LLM chatglm3-6b-32k - Python 3.10.12 - OS ubuntu - GPU NVIDIA A100 80G - CUDA 12.1 - NVIDIA Driver 525.125.06 ## Test ### vLLM ``` python from vllm import LLM, SamplingParams llm = LLM(model="/mnt/data/NewLLM/THUDM/chatglm3-6b-32k", trust_remote_code=True) sampling_params = SamplingParams( top_p=0.9, top_k=3, best_of=6, repetition_penalty=1.2, temperature=0.7, max_tokens=500 ) prompts = [ "你好", ] outputs = llm.generate(prompts, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") # Output Prompt: '你好', Generated text: '！请问有什么问题我可以帮您解答吗？' prompts = [ "晚上睡不着应该怎么办", ] outputs = llm.generate(prompts, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") # Output Prompt: '晚上睡不着应该怎么办', Generated text: '？\n 根据问题，我们需要解决的是晚上睡不着的问题。首先，我们可以尝试改变自己的睡眠环境，比如保持床铺整洁、安静、温暖等，这些都有助于提高入睡质量。其次，我们也可以通过一些放松的方式来缓解压力和焦虑，例如冥想、深呼吸、瑜伽等等。此外，避免在睡前过度使用电子设备也是非常重要的，因为蓝光会抑制褪黑素的分泌，影响我们的睡眠质量。最后，如果以上方法都无法解决问题，建议咨询医生或专业机构寻求帮助。...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 10.12 - OS ubuntu - GPU NVIDIA A100 80G - CUDA 12.1 - NVIDIA Driver 525.125.06 ## Test ### vLLM ``` python from vllm import LLM, SamplingParams llm = LLM(model="/mnt/data/NewLLM/THUDM/chatglm3-6b-32k", trust_remote_code...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: The inference results of vllm and HF are inconsistent # vllm和HF推理结果不一致 ## Config Info - vllm 0.2.5 - transformers 4.36.0 - LLM chatglm3-6b-32k - Python 3.10.12 - OS
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: - NVIDIA Driver 525.125.06 ## Test ### vLLM ``` python from vllm import LLM, SamplingParams llm = LLM(model="/mnt/data/NewLLM/THUDM/chatglm3-6b-32k", trust_remote_code=True) sampling_params = SamplingParams( top_p=0.9,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: 00 80G - CUDA 12.1 - NVIDIA Driver 525.125.06 ## Test ### vLLM ``` python from vllm import LLM, SamplingParams llm = LLM(model="/mnt/data/NewLLM/THUDM/chatglm3-6b-32k", trust_remote_code=True) sampling_params = Sampling...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: HF correctness frontend_api;model_support;sampling_logits cuda;sampling mismatch env_dependency vllm和HF推理结果不一致

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
