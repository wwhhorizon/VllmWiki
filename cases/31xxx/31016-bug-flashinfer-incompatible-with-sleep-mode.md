# vllm-project/vllm#31016: [Bug]: FlashInfer Incompatible with Sleep Mode

| 字段 | 值 |
| --- | --- |
| Issue | [#31016](https://github.com/vllm-project/vllm/issues/31016) |
| 状态 | open |
| 标签 | bug;help wanted |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: FlashInfer Incompatible with Sleep Mode

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Here is a script to reproduce the bug: I use vllm=v0.10.1 and flashinfer-python=v0.5.3. ``` from vllm import LLM, SamplingParams if __name__ == "__main__": model_pth = "xxx/Qwen3-1.7B" tp_size = 1 llm = LLM( model=model_pth, enable_sleep_mode=True, tensor_parallel_size=tp_size, gpu_memory_utilization=0.7, ) llm.sleep(level=1) llm.wake_up() prompts = [ "What is AI?", "Where is the Machu Picchu located?", "What is the capital of France?", "Who painted the Mona Lisa?", ] sampling_params = SamplingParams( temperature=0.7, top_p=0.9, max_tokens=64, ) outputs = llm.generate(prompts, sampling_params) for i, out in enumerate(outputs): prompt = prompts[i] generated = out.outputs[0].text print(f"Prompt {i}: {prompt!r}") print(f"Generation: {generated}\n") ``` ### Root Cause The bug occurs because the FlashInfer backend’s `attn_metadata` is stateful. It holds a `block_table_arange` tensor that is initialized once and then reused across subsequent calls to `build`: ```python self.block_table_arange = torch.arange( max_num_pages_per_req, dtype=torch.int32, device=self.device, ) ``` This `block_table_arange` tensor is allocated in the mempool...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: the bug: I use vllm=v0.10.1 and flashinfer-python=v0.5.3. ``` from vllm import LLM, SamplingParams if __name__ == "__main__": model_pth = "xxx/Qwen3-1.7B" tp_size = 1 llm = LLM( model=model_pth, enable_sleep_mode=True,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: FlashInfer Incompatible with Sleep Mode bug;help wanted ### Your current environment ### 🐛 Describe the bug Here is a script to reproduce the bug: I use vllm=v0.10.1 and flashinfer-python=v0.5.3. ``` from vllm im...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: `` ### Root Cause The bug occurs because the FlashInfer backend’s `attn_metadata` is stateful. It holds a `block_table_arange` tensor that is initialized once and then reused across subsequent calls to `build`: ```pytho...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ``` from vllm import LLM, SamplingParams if __name__ == "__main__": model_pth = "xxx/Qwen3-1.7B" tp_size = 1 llm = LLM( model=model_pth, enable_sleep_mode=True, tensor_parallel_size=tp_size, gpu_memory_utilization=0.7,...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: Your current environment ### 🐛 Describe the bug Here is a script to reproduce the bug: I use vllm=v0.10.1 and flashinfer-python=v0.5.3. ``` from vllm import LLM, SamplingParams if __name__ == "__main__": model_pth = "xx...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
