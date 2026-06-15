# vllm-project/vllm#16050: [Performance]: LLM Offline Inference Slowing Down Over Time

| 字段 | 值 |
| --- | --- |
| Issue | [#16050](https://github.com/vllm-project/vllm/issues/16050) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: LLM Offline Inference Slowing Down Over Time

### Issue 正文摘录

### Proposal to improve performance I have encountered an issue with using vllm for offline LLM inference. Initially, the inference runs smoothly with a decent speed, but over time, the output speed gradually decreases to extremely low values. Below are the details of my experience: • Initial performance: • The system starts off with a processing speed around 190 tokens per second, which is expected. • For example: Processed prompts: 34%|███▍ | 174/512 [00:00<00:01, 190.18it/s, est. speed input: 465756.51 toks/s, output: 380.36 toks/s] • Later performance degradation: • As the process continues, the output speed progressively decreases and eventually reaches very low values like 1 token per second. Processed prompts: 44%|████▍ | 226/512 [00:32<01:46, 2.68it/s, est. speed input: 16807.13 toks/s, output: 14.06 toks/s] Observed issue: • The performance starts off well but gradually degrades over time, with the output tokens per second reducing significantly. • This issue impacts the overall efficiency and processing time for large datasets, leading to slower inference and potentially longer completion times. My configuration: GPU: H20 # Initializing LLM self.llm = LLM( model='Qwen/Qw...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: leading to slower inference and potentially longer completion times. My configuration: GPU: H20 # Initializing LLM self.llm = LLM( model='Qwen/Qwen2.5-VL-32B-Instruct', tensor_parallel_size=2, trust_remote_code=True, dt...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: B-Instruct', tensor_parallel_size=2, trust_remote_code=True, dtype="bfloat16", gpu_memory_utilization=0.8, limit_mm_per_prompt={"image": 5, "video": 0} if is_multimodal else None, enable_prefix_caching=True, ) I would a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: with using vllm for offline LLM inference. Initially, the inference runs smoothly with a decent speed, but over time, the output speed gradually decreases to extremely low values. Below are the details of my experience:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: r time or if this is a known issue with vllm. ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: but gradually degrades over time, with the output tokens per second reducing significantly. • This issue impacts the overall efficiency and processing time for large datasets, leading to slower inference and potentially...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
