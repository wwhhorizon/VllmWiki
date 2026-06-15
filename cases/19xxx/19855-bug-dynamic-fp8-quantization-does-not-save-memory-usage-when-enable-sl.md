# vllm-project/vllm#19855: [Bug]: dynamic fp8 quantization does not save memory usage when enable_sleep_mode=True

| 字段 | 值 |
| --- | --- |
| Issue | [#19855](https://github.com/vllm-project/vllm/issues/19855) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;fp8;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: dynamic fp8 quantization does not save memory usage when enable_sleep_mode=True

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug dynamic fp8 quantization does not save memory used by weights when enable_sleep_mode=True #### test settings vLLM 0.9.1 #### test script ```Python import gc import torch from vllm import LLM from vllm.utils import GiB_bytes def print_current_mem_usage(tag): gc.collect() torch.cuda.empty_cache() free_bytes, total = torch.cuda.mem_get_info() print(f"[mem_usage] {tag} | current used: {(total - free_bytes) / GiB_bytes}") def test_fp8_sleep(): model_path = "Qwen/Qwen2.5-7B-Instruct" model = LLM( model=model_path, dtype="bfloat16", gpu_memory_utilization=0.8, trust_remote_code=True, enable_sleep_mode=True, quantization="fp8", ) print_current_mem_usage("before sleep") model.sleep() print_current_mem_usage("after sleep") model.wake_up(["weights"]) print_current_mem_usage("after wakeup weights") if __name__ == "__main__": test_fp8_sleep() ``` #### test result ||after sleep|after wakeup weights| |-|-|-| |no quantization|2|16| |quantization|2|16| We can see that quantization does not save memory. **By the way, the memory usage before sleep exceeds gpu_memory_utilization * total_memory about 6 GB (not listed here).** #### analysis I think th...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: dynamic fp8 quantization does not save memory usage when enable_sleep_mode=True bug ### Your current environment ### 🐛 Describe the bug dynamic fp8 quantization does not save memory used by weights when enable_sl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: p_mode=True #### test settings vLLM 0.9.1 #### test script ```Python import gc import torch from vllm import LLM from vllm.utils import GiB_bytes def print_current_mem_usage(tag): gc.collect() torch.cuda.empty_cache() f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: GiB_bytes def print_current_mem_usage(tag): gc.collect() torch.cuda.empty_cache() free_bytes, total = torch.cuda.mem_get_info() print(f"[mem_usage] {tag} | current used: {(total - free_bytes) / GiB_bytes}") def test_fp8...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nt used: {(total - free_bytes) / GiB_bytes}") def test_fp8_sleep(): model_path = "Qwen/Qwen2.5-7B-Instruct" model = LLM( model=model_path, dtype="bfloat16", gpu_memory_utilization=0.8, trust_remote_code=True, enable_sle...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ts of frequently asked questions. performance model_support;quantization;scheduler_memory cuda;fp8;quantization dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
