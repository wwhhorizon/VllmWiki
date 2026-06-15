# vllm-project/vllm#10025: [Bug]: Error while trying to run vLLM microsoft/Phi-3-mini-4k-instruct with OpenVINO backend

| 字段 | 值 |
| --- | --- |
| Issue | [#10025](https://github.com/vllm-project/vllm/issues/10025) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;import_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error while trying to run vLLM microsoft/Phi-3-mini-4k-instruct with OpenVINO backend

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm trying to run a vLLM using the OpenVINO backend. For that, I am following [this page](https://docs.vllm.ai/en/stable/getting_started/openvino-installation.html). Using the Dockerfile based installation, I've create the docker image and exec-ed into it, and have modified the script in `examples/offline_inference.py` to change the LLmodel to `microsoft/Phi-3-mini-4k-instruct` When I try running inference using `python3 examples/offline_inference.py` [script](https://github.com/vllm-project/vllm/blob/ad23318928d40ef7ac969451afa0dc198428c04b/examples/offline_inference.py) , I get the following: ``` python3 examples/offline_inference.py WARNING 11-05 06:02:09 _custom_ops.py:19] Failed to import from vllm._C with ModuleNotFoundError("No module named 'vllm._C'") INFO 11-05 06:02:09 importing.py:15] Triton not installed or not compatible; certain GPU-related functions will not be available. INFO 11-05 06:02:13 config.py:323] This model supports multiple tasks: {'generate', 'embedding'}. Defaulting to 'generate'. WARNING 11-05 06:02:13 config.py:460] Async output processing is only supported for CUD...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: wing [this page](https://docs.vllm.ai/en/stable/getting_started/openvino-installation.html). Using the Dockerfile based installation, I've create the docker image and exec-ed into it, and have modified the script in `ex...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disable_...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: one, tokenizer='microsoft/Phi-3-mini-4k-instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, rope_scaling=None, rope_theta=None, tokenizer_revision=None, trust_remote_co...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: while trying to run vLLM microsoft/Phi-3-mini-4k-instruct with OpenVINO backend bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I'm trying to run a vLLM using the OpenVINO bac...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 05 06:02:13 config.py:460] Async output processing is only supported for CUDA, TPU, XPU. Disabling it for other platforms. INFO 11-05 06:02:13 llm_engine.py:247] Initializing an LLM engine (v0.6.3.post2.dev217+gccb5376a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
