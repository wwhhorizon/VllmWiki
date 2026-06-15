# vllm-project/vllm#16337: [Bug]: FP8 Quantization with enforce_eager=False Causes Gibberish Output on Llama-4-Scout Model (VLLM_USE_V1=1)

| 字段 | 值 |
| --- | --- |
| Issue | [#16337](https://github.com/vllm-project/vllm/issues/16337) |
| 状态 | closed |
| 标签 | bug;torch.compile;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: FP8 Quantization with enforce_eager=False Causes Gibberish Output on Llama-4-Scout Model (VLLM_USE_V1=1)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running Llama-4-Scout-17B-16E-Instruct with the following combination of vars/args: - VLLM_USE_V1=1 - quantization="fp8" - enforce_eager=False The model produces gibberish. To reproduce the issue, run the following script: ```bash VLLM_WORKER_MULTIPROC_METHOD=spawn SAFETENSORS_FAST_GPU=1 VLLM_USE_V1=1 python example.py ``` ```python #example.py from vllm import LLM, SamplingParams def test(): prompts = [ "The color of the sky is blue but sometimes it can also be", "The capital of France is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=256) llm = LLM( model="/app/model/Llama-4-Scout-17B-16E-Instruct/", tensor_parallel_size=4, quantization="fp8", max_model_len=8192, enforce_eager=False, ) outputs = llm.generate(prompts, sampling_params) # Print the outputs. for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") if __name__ == "__main__": test() ``` This issue occurs only when `enforce_eager=False`. Setting `enforce_eager` to true will generate reasonable output. Furthermore, removing cuda graph padding...

## 现有链接修复摘要

#42779 Zero padded model inputs before execution

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Causes Gibberish Output on Llama-4-Scout Model (VLLM_USE_V1=1) bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug When running Llama-4-Scout-17B-16E-Instruct with the following combination of va...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: FP8 Quantization with enforce_eager=False Causes Gibberish Output on Llama-4-Scout Model (VLLM_USE_V1=1) bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug When running Llama-4-Scout-17B-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: g]: FP8 Quantization with enforce_eager=False Causes Gibberish Output on Llama-4-Scout Model (VLLM_USE_V1=1) bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug When running Llama-4-Scout-17B-16E...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ce_eager` to true will generate reasonable output. Furthermore, removing cuda graph padding from `num_input_tokens` in `vllm/v1/worker/gpu_model_runner.py` seems to resolve this issue: ```python # Remove cuda padding #...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: FP8 Quantization with enforce_eager=False Causes Gibberish Output on Llama-4-Scout Model (VLLM_USE_V1=1) bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug When running Llama-4-Scout-17B-...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42779](https://github.com/vllm-project/vllm/pull/42779) | closes_keyword | 0.95 | Zero padded model inputs before execution | fixed stale CUDA graph padding `positions` in `_preprocess`. - #16337 discussed CUDA graph padding executing models with padded inputs beyond `total_num_scheduled_tokens`, but wa |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
