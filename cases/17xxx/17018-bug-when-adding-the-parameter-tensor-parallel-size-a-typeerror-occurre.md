# vllm-project/vllm#17018: [Bug]: When adding the parameter tensor_parallel_size, a TypeError occurred: BackendCompilerFailed.__init__() is missing one required positional argument: 'inner_exception'.

| 字段 | 值 |
| --- | --- |
| Issue | [#17018](https://github.com/vllm-project/vllm/issues/17018) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When adding the parameter tensor_parallel_size, a TypeError occurred: BackendCompilerFailed.__init__() is missing one required positional argument: 'inner_exception'.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams import torch.distributed as dist # Enter a few questions prompts = [ "Hello, who are you?", "Where is the capital of France?", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=100) llm = LLM(model="Qwen2.5-1.5B", trust_remote_code=True, max_model_len=512, gpu_memory_utilization=0.8,tensor_parallel_size=2) outputs = llm.generate(prompts, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}") if dist.is_initialized(): dist.destroy_process_group() ``` ``` INFO 04-23 00:03:59 __init__.py:183] Automatically detected platform cuda. INFO 04-23 00:04:02 config.py:526] This model supports multiple tasks: {'classify', 'score', 'generate', 'embed', 'reward'}. Defaulting to 'generate'. INFO 04-23 00:04:02 config.py:1383] Defaulting to use mp for distributed inference INFO 04-23 00:04:02 llm_engine.py:232] Initializing a V0 LLM engine (v0.7.1) with config: model='Qwen2.5-1.5B', speculative_config=None, tokenizer='Qwen2.5-1.5B', skip_tokenizer_init=False, token...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: __() is missing one required positional argument: 'inner_exception'. bug;stale ### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams import torch.distributed as dist # Enter...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: adding the parameter tensor_parallel_size, a TypeError occurred: BackendCompilerFailed.__init__() is missing one required positional argument: 'inner_exception'. bug;stale ### Your current environment ### 🐛 Describe the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ]: When adding the parameter tensor_parallel_size, a TypeError occurred: BackendCompilerFailed.__init__() is missing one required positional argument: 'inner_exception'. bug;stale ### Your current environment ### 🐛 Desc...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ide_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=512, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=2, pipeline_parallel_size=1, disable_c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ``` INFO 04-23 00:03:59 __init__.py:183] Automatically detected platform cuda. INFO 04-23 00:04:02 config.py:526] This model supports multiple tasks: {'classify', 'score', 'generate', 'embed', 'reward'}. Defaulting to '...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
