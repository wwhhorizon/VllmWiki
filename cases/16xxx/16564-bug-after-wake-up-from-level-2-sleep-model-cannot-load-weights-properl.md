# vllm-project/vllm#16564: [Bug]: After wake up from level 2 sleep, model cannot load weights properly

| 字段 | 值 |
| --- | --- |
| Issue | [#16564](https://github.com/vllm-project/vllm/issues/16564) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: After wake up from level 2 sleep, model cannot load weights properly

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I want to drop all the parameters of the LLM engine and then load it from another state dict. The following code shows that level 1 is OK, while level 2 is problematic (cannot load the weights properly). ![Image](https://github.com/user-attachments/assets/79871b90-a927-402e-bf99-18f1ee4ce48d) ```python import torch import torch.distributed as dist from vllm import SamplingParams, LLM from functools import cached_property class SleepLevelTwoWakeUpIssue: model_path = "Qwen/Qwen2.5-7B-Instruct" def run(self): self.log("\033[91mRaw weights:\033[0m") self.generate_and_print() self.sleep_and_wake_up(1) self.log("\033[91mAfter sleep level 1:\033[0m") self.generate_and_print() self.sleep_and_wake_up(1, load_weights=True) self.log("\033[91mAfter sleep level 1 and load weights:\033[0m") self.generate_and_print() self.sleep_and_wake_up(2) self.log("\033[91mAfter sleep level 2:\033[0m") self.generate_and_print() self.sleep_and_wake_up(2, load_weights=True) self.log("\033[91mAfter sleep level 2 and load weights:\033[0m") self.generate_and_print() def generate_and_print(self): prompts = [ "Hello, how are you?", "France is famous for its", "The...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: user-attachments/assets/79871b90-a927-402e-bf99-18f1ee4ce48d) ```python import torch import torch.distributed as dist from vllm import SamplingParams, LLM from functools import cached_property class SleepLevelTwoWakeUpI...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: seed=0, disable_custom_all_reduce=True, dtype="bfloat16", ) if __name__ == "__main__": dist.init_process_group(backend="nccl") torch.cuda.set_device(dist.get_rank()) SleepLevelTwoWakeUpIssue().run() dist.destroy_process...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: gpu_memory_utilization=0.8, distributed_executor_backend="external_launcher", tensor_parallel_size=4, max_model_len=16384, seed=0, disable_custom_all_reduce=True, dtype="bfloat16", ) if __name__ == "_
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e__ == "__main__": dist.init_process_group(backend="nccl") torch.cuda.set_device(dist.get_rank()) SleepLevelTwoWakeUpIssue().run() dist.destroy_process_group() ``` ### Before submitting a new issue... - [x] Make sure yo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: After wake up from level 2 sleep, model cannot load weights properly bug ### Your current environment ### 🐛 Describe the bug I want to drop all the parameters of the LLM engine and then load it from another state...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
