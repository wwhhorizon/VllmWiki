# vllm-project/vllm#14300: [Usage]: Logprobs Scaling with O(n) Complexity – Unexpected Performance Degradation

| 字段 | 值 |
| --- | --- |
| Issue | [#14300](https://github.com/vllm-project/vllm/issues/14300) |
| 状态 | open |
| 标签 | usage;unstale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;sampling |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Logprobs Scaling with O(n) Complexity – Unexpected Performance Degradation

### Issue 正文摘录

**Title:** Logprobs Scaling with O(n) Complexity – Unexpected Performance Degradation **Description:** When increasing the `logprobs` parameter, I expected only a minor increase in runtime due to slicing the top-k values from the full vocabulary logits. However, my experiments show an almost O(n) increase in runtime, which suggests that retrieving logprobs is more computationally expensive than anticipated. ### **Reproduction Code** ```python import time from vllm import LLM from vllm.sampling_params import SamplingParams def test_generation_time(llm, logprobs_value, batch_size=32): sampling_params = SamplingParams(logprobs=logprobs_value, max_tokens=1) # Timed run start_time = time.time() output = llm.generate(["Tell me something about LLMs."] * batch_size, sampling_params=sampling_params, use_tqdm=False) end_time = time.time() return end_time - start_time def main(): print("Initializing model...") llm = LLM(model="Qwen/Qwen2.5-7B-Instruct", max_logprobs=152_064) # vocab size batch_size = 32 logprobs_values = [10, 100, 1000, 10000, 100000, 152064] results = [] print("\nStarting tests...") for logprobs in logprobs_values: time_taken = test_generation_time(llm, logprobs, batch_size...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: gprobs` parameter, I expected only a minor increase in runtime due to slicing the top-k values from the full vocabulary logits. However, my experiments show an almost O(n) increase in runtime, which suggests that retrie...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 0.7.4.dev142+g9804145c.d20250228 - Model: `Qwen/Qwen2.5-7B-Instruct` - CUDA Version: CUDA Version: 12.5 Looking forward to insights on whether this is expected behavior or a possible optimization opportunity! Thanks! ##...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: return end_time - start_time def main(): print("Initializing model...") llm = LLM(model="Qwen/Qwen2.5-7B-Instruct", max_logprobs=152_064) # vocab size batch_size = 32 logprobs_values = [10, 100, 1000, 10000, 100000, 152...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: caling with O(n) Complexity – Unexpected Performance Degradation usage;unstale **Title:** Logprobs Scaling with O(n) Complexity – Unexpected Performance Degradation **Description:** When increasing the `logprobs` parame...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: mputed logits. ### **Questions:** 1. **Why does increasing `logprobs` scale in an O(n) fashion?** - Is the model recomputing or performing expensive operations instead of just slicing logits? 2. **Is there a way to retr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
