# vllm-project/vllm#39179: [Bug]: GLM5 on B300 generates garbage output

| 字段 | 值 |
| --- | --- |
| Issue | [#39179](https://github.com/vllm-project/vllm/issues/39179) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GLM5 on B300 generates garbage output

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## reproduce code ```python from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] # Create a sampling params object. sampling_params = SamplingParams(temperature=1.0, top_p=0.95) def main(): # Create an LLM. llm = LLM( model="zai-org/GLM-5-FP8", tensor_parallel_size=8, trust_remote_code=True, load_format="fastsafetensors", ) # Generate texts from the prompts. # The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) # Print the outputs. print("\nGenerated Outputs:\n" + "-" * 60) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}") print(f"Output: {generated_text!r}") print("-" * 60) if __name__ == "__main__": main() ``` ## output ```bash Generated Outputs: ------------------------------------------------------------ Prompt: 'Hello, my name is' Output: '1111111111111111' ------------------------------------------------------------ Prompt: 'T...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ment ### 🐛 Describe the bug ## reproduce code ```python from vllm import LLM, SamplingParams # Sample prompts. prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The f...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: main(): # Create an LLM. llm = LLM( model="zai-org/GLM-5-FP8", tensor_parallel_size=8, trust_remote_code=True, load_format="fastsafetensors", ) # Generate texts from the prompts. # The output is a list of RequestOutput...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: .0, top_p=0.95) def main(): # Create an LLM. llm = LLM( model="zai-org/GLM-5-FP8", tensor_parallel_size=8, trust_remote_code=True, load_format="fastsafetensors", ) # Generate texts from the prompts. # The output is a li...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ) # Generate texts from the prompts. # The output is a list of RequestOutput objects # that contain the prompt, generated text, and other information. outputs = llm.generate(prompts, sampling_params) # Print the outputs...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
