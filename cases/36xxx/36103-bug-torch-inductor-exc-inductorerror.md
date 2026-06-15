# vllm-project/vllm#36103: [Bug]: torch._inductor.exc.InductorError:

| 字段 | 值 |
| --- | --- |
| Issue | [#36103](https://github.com/vllm-project/vllm/issues/36103) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: torch._inductor.exc.InductorError:

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` (.venv) btcc@spark-4ddc:~/my-project$ python3 -m vllm.entrypoints.openai.api_server --model /home/btcc/huggingface/Qwen/Qwen3-4B-Instruct-2507 --served-model-name Qwen3-4B-Instruct-2507 --gpu-memory-utilization 0.3 --port 8001 /home/btcc/my-project/.venv/lib/python3.12/site-packages/torch/cuda/__init__.py:63: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly, please report this to the maintainers of the package that installed pynvml for you. import pynvml # type: ignore[import] /home/btcc/my-project/.venv/lib/python3.12/site-packages/torch/cuda/__init__.py:283: UserWarning: Found GPU0 NVIDIA GB10 which is of cuda capability 12.1. Minimum and Maximum cuda capability supported by this version of PyTorch is (8.0) - (12.0) warnings.warn( (APIServer pid=1391686) INFO 03-05 14:10:04 [utils.py:287] (APIServer pid=1391686) INFO 03-05 14:10:04 [utils.py:287] █ █ █▄ ▄█ (APIServer pid=1391686) INFO 03-05 14:10:04 [utils.py:287] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.16.0 (APIServer pid=1391686) INFO 03-05 14:10:04 [utils.py:287] █▄█▀ █ █ █ █ model /home/btcc/huggingface/Qwe...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: /__init__.py:63: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly, please report this to the maintainers of the package that installed pynvml f...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ark-4ddc:~/my-project$ python3 -m vllm.entrypoints.openai.api_server --model /home/btcc/huggingface/Qwen/Qwen3-4B-Instruct-2507 --served-model-name Qwen3-4B-Instruct-2507 --gpu-memory-utilization 0.3 --port 8001 /home/b...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=262144, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_siz...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: port 8001 /home/btcc/my-project/.venv/lib/python3.12/site-packages/torch/cuda/__init__.py:63: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly,...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
