# vllm-project/vllm#21616: [Bug]: Very Low Prompt Evaluation Speed

| 字段 | 值 |
| --- | --- |
| Issue | [#21616](https://github.com/vllm-project/vllm/issues/21616) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Very Low Prompt Evaluation Speed

### Issue 正文摘录

### 🐛 Describe the bug I am using the following code snippet to benchmark latency: Prompt Speed: 3.5 tok/s Text Generation Speed: 45 tok/s ``` from vllm import LLM, SamplingParams conversation = [ { "role": "user", "content": "hi" }, ] def run(): sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=128) llm = LLM(model="aravind/Qwen3-1.7B-W4A16-G128", max_num_seqs=1, gpu_memory_utilization=0.5, max_num_batched_tokens=512*2, max_model_len=512*2) for i in range(10): outputs = llm.chat(conversation, sampling_params) for output in outputs: print(len(output.prompt_token_ids)) prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") if __name__=="__main__": run() ``` 2 observations: - The max tokens in sampling params is affecting the prompt evaluation speed which should never be. - If the prompt length is less than the max_num_batched_tokens/max_model_len, the prompt evaluation speed is low. Note that my usecase requires one single request to be passed at a single time. # How to tackle these scenarios? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues,...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: Very Low Prompt Evaluation Speed bug;stale ### 🐛 Describe the bug I am using the following code snippet to benchmark latency: Prompt Speed: 3.5 tok/s Text Generation Speed: 45 tok/s ``` from vllm import LLM, Samp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: SamplingParams(temperature=0.8, top_p=0.95, max_tokens=128) llm = LLM(model="aravind/Qwen3-1.7B-W4A16-G128", max_num_seqs=1, gpu_memory_utilization=0.5, max_num_batched_tokens=512*2, max_model_len=512*2) for i in range(...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Very Low Prompt Evaluation Speed bug;stale ### 🐛 Describe the bug I am using the following code snippet to benchmark latency: Prompt Speed: 3.5 tok/s Text Generation Speed: 45 tok/s ``` from vllm import LLM, Samp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Prompt Speed: 3.5 tok/s Text Generation Speed: 45 tok/s ``` from vllm import LLM, SamplingParams conversation = [ { "role": "user", "content": "hi" }, ] def run(): sampling_params = SamplingParams(temperature=0.8, top_p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: os? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
