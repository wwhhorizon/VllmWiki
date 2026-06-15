# vllm-project/vllm#32176: [Bug]: deepseekv3.2 core dumped with cpu_offload_gb

| 字段 | 值 |
| --- | --- |
| Issue | [#32176](https://github.com/vllm-project/vllm/issues/32176) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: deepseekv3.2 core dumped with cpu_offload_gb

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug test.py: ```python from vllm import LLM, SamplingParams if __name__ == "__main__": sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM("/storage/DeepSeek-V3.2", enforce_eager=True, cpu_offload_gb=1024, gpu_memory_utilization=0.5) prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] outputs = llm.generate(prompts, sampling_params) ``` ```bash VLLM_USE_DEEP_GEMM=0 VLLM_ENABLE_V1_MULTIPROCESSING=0 CUDA_VISIBLE_DEVICES=2 python test.py ``` The bug only occurs when using cpu_offload_gb ``` /usr/local/lib/python3.12/dist-packages/torch/cuda/__init__.py:63: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly, please report this to the maintainers of the package that installed pynvml for you. import pynvml # type: ignore[import] INFO 01-12 12:28:00 [utils.py:253] non-default args: {'cpu_offload_gb': 1024, 'gpu_memory_utilization': 0.5, 'disable_log_stats': True, 'enforce_eager': True, 'model': '/storage/DeepSeek-V3.2'} WARNING 01-12 12:28:00 [arg_utils.py:1181] The global r...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ent environment ### 🐛 Describe the bug test.py: ```python from vllm import LLM, SamplingParams if __name__ == "__main__": sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM("/storage/DeepSeek-V3.2",...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: odels and can yield errors. INFO 01-12 12:28:00 [config.py:659] Detected quantization_config.scale_fmt=ue8m0; enabling UE8M0 for DeepGEMM. INFO 01-12 12:28:00 [model.py:514] Resolved architecture: DeepseekV32ForCausalLM...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: deepseekv3.2 core dumped with cpu_offload_gb bug;stale ### Your current environment ### 🐛 Describe the bug test.py: ```python from vllm import LLM, SamplingParams if __name__ == "__main__": sampling_params = Samp...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: andom seed is set to 0. Since VLLM_ENABLE_V1_MULTIPROCESSING is set to False, this may affect the random state of the Python process that launched vLLM . You are using a model of type deepseek_v32 to instantiate a model...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: 28:01 [cuda.py:232] Forcing kv cache block size to 64 for FlashMLASparse backend. INFO 01-12 12:28:01 [core.py:93] Initializing a V1 LLM engine (v0.13.0rc2.dev80+g302b2c1eb.d20260108) with config: model='/storage/DeepSe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
