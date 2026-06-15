# vllm-project/vllm#41660: [Bug]: CPUWorker shutdown reports "RuntimeError: Cannot access accelerator device when none is available."

| 字段 | 值 |
| --- | --- |
| Issue | [#41660](https://github.com/vllm-project/vllm/issues/41660) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CPUWorker shutdown reports "RuntimeError: Cannot access accelerator device when none is available."

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug CPU vLLM worker shutdown logs the error `"RuntimeError: Cannot access accelerator device when none is available."` while attempting to access accelerator device, which does not exist. * It seems to be caused by `torch.accelerator.synchronize()` in `gpu_model_runner.py` (`_cleanup_profiling_kv_cache`, line 5915) since the `CPUWorker` class overrides the GPU's `Worker` class implementation without overriding its shutdown function. This repository includes the conda environment, script and steps to reproduce the bug: https://github.com/MichaelLapshin/vllm-shutdown-bug Run the following with a CPU vLLM build to reproduce the error log: ```python from vllm import LLM, SamplingParams def main(): llm = LLM(model="Qwen/Qwen3-0.6B", max_model_len=16) params = SamplingParams(max_tokens=1) outputs = llm.generate(prompts="What is 1+1?", sampling_params=params) # Output assert len(outputs) == 1, "Unexpected (or no) output" assert len(outputs[0].outputs[0].token_ids) == 1, "Too many tokens" print(outputs[0]) if __name__ == "__main__": main() ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: .com/MichaelLapshin/vllm-shutdown-bug Run the following with a CPU vLLM build to reproduce the error log: ```python from vllm import LLM, SamplingParams def main(): llm = LLM(model="Qwen/Qwen3-0.6B", max_model_len=16) p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ild;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding cache;cuda;kernel;operator;quantization;sampling;triton build_error;crash;nan_i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: st. * It seems to be caused by `torch.accelerator.synchronize()` in `gpu_model_runner.py` (`_cleanup_profiling_kv_cache`, line 5915) since the `CPUWorker` class overrides the GPU's `Worker` class implementation without...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: tend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding cache;cuda;kernel;operator;quantization;sampling;triton build_error;crash;nan_inf dtype;env_dependency;memor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
