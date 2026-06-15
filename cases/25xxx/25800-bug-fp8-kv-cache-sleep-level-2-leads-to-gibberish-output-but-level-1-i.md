# vllm-project/vllm#25800: [Bug]: FP8 KV cache + sleep(level=2) leads to gibberish output, but level=1 is fine

| 字段 | 值 |
| --- | --- |
| Issue | [#25800](https://github.com/vllm-project/vllm/issues/25800) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FP8 KV cache + sleep(level=2) leads to gibberish output, but level=1 is fine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am on `0.10.2`. When using `llm = LLM(model, enable_sleep_mode=True, kv_cache_dtype="fp8")`, sleep mode with level 2 leads to gibberish output, but level 1 is fine. The following script works (exactly from https://github.com/vllm-project/vllm/blob/b3613e3acece6502c553901fe4433e3f783363b7/tests/basic_correctness/test_cumem.py#L184): ```python import torch from vllm import LLM, SamplingParams def main(): GiB_bytes = 1 << 30 model = "Qwen/Qwen3-0.6B" free, total = torch.cuda.mem_get_info() used_bytes_baseline = total - free # in case other process is running llm = LLM(model, enable_sleep_mode=True) prompt = "How are you?" sampling_params = SamplingParams(temperature=0, max_tokens=10) output = llm.generate(prompt, sampling_params) # Put the engine to deep sleep llm.sleep(level=2) free_gpu_bytes_after_sleep, total = torch.cuda.mem_get_info() used_bytes = total - free_gpu_bytes_after_sleep - used_bytes_baseline assert used_bytes < 3 * GiB_bytes llm.wake_up(tags=["weights"]) llm.collective_rpc("reload_weights") free_gpu_bytes_wake_up_w, total = torch.cuda.mem_get_info() used_bytes = total - free_gpu_bytes_wake_up_w - used_bytes_baseli...

## 现有链接修复摘要

#28783 [Bugfix][sleepmode][fp8 kv cache]: Fix FP8 KV cache + sleep(level=2) gibberish output

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: e4433e3f783363b7/tests/basic_correctness/test_cumem.py#L184): ```python import torch from vllm import LLM, SamplingParams def main(): GiB_bytes = 1 << 30 model = "Qwen/Qwen3-0.6B" free, total = torch.cuda.mem_get_info()...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: FP8 KV cache + sleep(level=2) leads to gibberish output, but level=1 is fine bug ### Your current environment ### 🐛 Describe the bug I am on `0.10.2`. When using `llm = LLM(model, enable_sleep_mode=True, kv_cache...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: B_bytes = 1 << 30 model = "Qwen/Qwen3-0.6B" free, total = torch.cuda.mem_get_info() used_bytes_baseline = total - free # in case other process is running llm = LLM(model, enable_sleep_mode=True) prompt = "How are you?"...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ment ### 🐛 Describe the bug I am on `0.10.2`. When using `llm = LLM(model, enable_sleep_mode=True, kv_cache_dtype="fp8")`, sleep mode with level 2 leads to gibberish output, but level 1 is fine. The following script wor...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: on;sampling_logits;speculative_decoding cache;cuda;fp8;operator;sampling;triton build_error;nan_inf dtype;env_dependency #28783 [Bugfix][sleepmode][fp8 kv cache]: Fix FP8 KV cache + sleep(level=2) gibberish output Your...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#28783](https://github.com/vllm-project/vllm/pull/28783) | closes_keyword | 0.95 | [Bugfix][sleepmode][fp8 kv cache]: Fix FP8 KV cache + sleep(level=2) gibberish output | fixes #25800 where waking from sleep(level=2) with kv_cache_dtype="fp8" results in gibberish output. ### Bug Cause When the engine enters level 2 sleep (llm.sleep(level=2)), all |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
