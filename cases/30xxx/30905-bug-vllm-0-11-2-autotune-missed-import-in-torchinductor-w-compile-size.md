# vllm-project/vllm#30905: [Bug]: vLLM 0.11.2 AutoTune Missed Import In TorchInductor w/ Compile Sizes > 1

| 字段 | 值 |
| --- | --- |
| Issue | [#30905](https://github.com/vllm-project/vllm/issues/30905) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM 0.11.2 AutoTune Missed Import In TorchInductor w/ Compile Sizes > 1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When testing Mixtral model in vLLM 0.11.2 version with AutoTune feature enabled and pass compile_sizes>1, inference will fail with below error during TorchInductor on certain Triton kernel generated code, due to missing import error as below: ``` RuntimeError: Failed to run autotuning code block: name 'get_raw_stream' is not defined ``` By looking into torch logs/files, the error seems to be happening in triton_per_fused_2 generated code(or maybe more kernels), where get_raw_stream is invoked before importing ``` with torch.cuda._DeviceGuard(7): stream7 = get_raw_stream(7) from torch._C import _cuda_getCurrentRawStream as get_raw_stream stream7 = get_raw_stream(7) ``` Sample script to reproduce ``` from vllm import LLM, SamplingParams from vllm.config import CompilationConfig prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="mistralai/Mixtral-8x7B-v0.1", compilation_config=CompilationConfig(compile_sizes=[2]),) outputs = llm.generate(prompts, sampling_params) # Print the outpu...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: vLLM 0.11.2 AutoTune Missed Import In TorchInductor w/ Compile Sizes > 1 bug;torch.compile ### Your current environment ### 🐛 Describe the bug When testing Mixtral model in vLLM 0.11.2 version with AutoTune featu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rnels), where get_raw_stream is invoked before importing ``` with torch.cuda._DeviceGuard(7): stream7 = get_raw_stream(7) from torch._C import _cuda_getCurrentRawStream as get_raw_stream stream7 = get_raw_stream(7) ```...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: import error as below: ``` RuntimeError: Failed to run autotuning code block: name 'get_raw_stream' is not defined ``` By looking into torch logs/files, the error seems to be happening in triton_per_fused_2 generated co...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: our current environment ### 🐛 Describe the bug When testing Mixtral model in vLLM 0.11.2 version with AutoTune feature enabled and pass compile_sizes>1, inference will fail with below error during TorchInductor on certa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding cuda;kernel;operator;sampling;triton build_error;crash;import_error;nan_inf env_dependency;memory_layout You...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
