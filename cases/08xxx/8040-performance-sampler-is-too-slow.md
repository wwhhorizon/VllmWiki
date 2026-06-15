# vllm-project/vllm#8040: [Performance]: Sampler is too slow?

| 字段 | 值 |
| --- | --- |
| Issue | [#8040](https://github.com/vllm-project/vllm/issues/8040) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Sampler is too slow?

### Issue 正文摘录

### Report of performance regression Background : I am integrating my model to vllm, the model is almost same as llama, but it have a multi-head lm_head, which just something like a for loop in the `sample` function in `LlamaForCausalLM` ```python def sample( self, logits: torch.Tensor, sampling_metadata: SamplingMetadata, ) -> Optional[SamplerOutput]: for i in range(num_head): next_tokens = self.sampler(logits, sampling_metadata) return next_tokens ``` But it seems when num_head goes up from 1 to 8, the latency increased significantly. Can easily repro by below test scrfipt ```python import torch import time from vllm import LLM, SamplingParams torch.random.manual_seed(999) llm = LLM(model='/home/zhn/g/Meta-Llama-3-8B-Instruct', gpu_memory_utilization=0.5) prompts = [ "Hi my name is", ] texts = [] start = time.time() for i in range(10): sampling_params = SamplingParams(temperature=0, top_k=1, max_tokens=200, top_p=1) outputs = llm.generate(prompts, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text texts.append(generated_text) end = time.time() print(f"Time taken: {end - start:.2f}s") ``` num_head=1 [00:02<00:00, 2.48s/it, est....

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: mance]: Sampler is too slow? performance;stale ### Report of performance regression Background : I am integrating my model to vllm, the model is almost same as llama, but it have a multi-head lm_head, which just somethi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ken: 30.51s** **Almost 25% perf regression.** Consider my model is much smaller than llama3 8b, so the perf regression is more obvious. So is this expected? Any idea to mitigate or fix? - [X] Make sure you already searc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e ### Report of performance regression Background : I am integrating my model to vllm, the model is almost same as llama, but it have a multi-head lm_head, which just something like a for loop in the `sample` function i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: creased significantly. Can easily repro by below test scrfipt ```python import torch import time from vllm import LLM, SamplingParams torch.random.manual_seed(999) llm = LLM(model='/home/zhn/g/Meta-Llama-3-8B-Instruct',...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: def sample( self, logits: torch.Tensor, sampling_metadata: SamplingMetadata, ) -> Optional[SamplerOutput]: for i in range(num_head): next_tokens = self.sampler(logits, sampling_metadata) return next_tokens ``` But it se...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
