# vllm-project/vllm#18599: [Bug]: v0 + flashinfer0.2.5 might generate response filled with exclamation mark

| 字段 | 值 |
| --- | --- |
| Issue | [#18599](https://github.com/vllm-project/vllm/issues/18599) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: v0 + flashinfer0.2.5 might generate response filled with exclamation mark

### Issue 正文摘录

### Your current environment ```shell root=path/2/test_fi_025 cd $root export TORCH_CUDA_ARCH_LIST="7.5 8.0 8.6 8.7 9.0+PTX" export VLLM_ATTENTION_BACKEND=FLASHINFER python test_fi_025.py 2>&1 | tee $root/test_fi_025.log ``` test_fi_025.py: ```python from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="./Qwen3-30B-A3B") outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") ``` ### 🐛 Describe the bug ![Image](https://github.com/user-attachments/assets/cb79eba8-0be0-4517-9dfb-f71fa1f1c256) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: v0 + flashinfer0.2.5 might generate response filled with exclamation mark bug;stale ### Your current environment ```shell root=path/2/test_fi_025 cd $root export TORCH_CUDA_ARCH_LIST="7.5 8.0 8.6 8.7 9.0+PTX" exp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nt environment ```shell root=path/2/test_fi_025 cd $root export TORCH_CUDA_ARCH_LIST="7.5 8.0 8.6 8.7 9.0+PTX" export VLLM_ATTENTION_BACKEND=FLASHINFER python test_fi_025.py 2>&1 | tee $root/test_fi_025.log ``` test_fi_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="./Qwen3-30B-A3B") outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt genera...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: &1 | tee $root/test_fi_025.log ``` test_fi_025.py: ```python from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: flashinfer0.2.5 might generate response filled with exclamation mark bug;stale ### Your current environment ```shell root=path/2/test_fi_025 cd $root export TORCH_CUDA_ARCH_LIST="7.5 8.0 8.6 8.7 9.0+PTX" export VLLM_ATT...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
