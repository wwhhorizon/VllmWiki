# vllm-project/vllm#8264: [Bug]: how to set gpu id in code？

| 字段 | 值 |
| --- | --- |
| Issue | [#8264](https://github.com/vllm-project/vllm/issues/8264) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: how to set gpu id in code？

### Issue 正文摘录

### Your current environment as official code is: from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="facebook/opt-125m") outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") then i want to set GPU ID as i want,such as specific ID,one GPU or seral GPU.default set is device="auto", but how to set device="1,2,3"? ### 🐛 Describe the bug as official code is: from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="facebook/opt-125m") outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ow to set gpu id in code？ bug;stale ### Your current environment as official code is: from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: is device="auto", but how to set device="1,2,3"? when set os.environ['CUDA_VISIBLE_DEVICES'] = "0,1,2" it is invalid,is there any other ways? ### Before submitting a new issue... - [X] Make sure you already searched for...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="facebook/opt-125m") outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt gene...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: how to set gpu id in code？ bug;stale ### Your current environment as official code is: from vllm import LLM, SamplingParams prompts = [ "Hello, my name is", "The president of the United States is", "The capital o...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
