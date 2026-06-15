# vllm-project/vllm#31792: [Bug]: VLLM 0.13.0 / Mistral-Small-3.2-24B-Instruct-2506: MistralTokenizer object has no attribute 'convert_tokens_to_ids'

| 字段 | 值 |
| --- | --- |
| Issue | [#31792](https://github.com/vllm-project/vllm/issues/31792) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM 0.13.0 / Mistral-Small-3.2-24B-Instruct-2506: MistralTokenizer object has no attribute 'convert_tokens_to_ids'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When launching VLLM 0.13.0 with `RedHatAI/Mistral-Small-3.2-24B-Instruct-2506-NVFP4`, I get the following error message: ``` (...) (EngineCore_DP0 pid=13140) File "/home/user/vllm-venv/lib/python3.12/site-packages/transformers/models/pixtral/processing_pixtral.py", line 124, in __init__ (EngineCore_DP0 pid=13140) self.image_token_id = tokenizer.convert_tokens_to_ids(self.image_token) (EngineCore_DP0 pid=13140) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (EngineCore_DP0 pid=13140) AttributeError: 'MistralTokenizer' object has no attribute 'convert_tokens_to_ids'. Did you mean: 'convert_tokens_to_string'? ``` I opened this [issue on Transformer side](https://github.com/huggingface/transformers/issues/43110) who redirected me to VLLM. To reproduce: 1. Install: ``` uv pip install setuptools packaging uv pip install https://github.com/vllm-project/vllm/releases/download/v0.13.0/vllm-0.13.0+cu130-cp38-abi3-manylinux_2_35_x86_64.whl --extra-index-url https://download.pytorch.org/whl/cu130 uv pip install datasets psutil pandas torch-c-dlpack-ext ``` 2. Run: ``` VLLM_USE_FLASHINFER_MOE_FP4=1 ENABLE_NVFP4_SM120=1 VLLM_ATTENTION_BACKEND=FLASHINFER vllm...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: launching VLLM 0.13.0 with `RedHatAI/Mistral-Small-3.2-24B-Instruct-2506-NVFP4`, I get the following error message: ``` (...) (EngineCore_DP0 pid=13140) File "/home/user/vllm-venv/lib/python3.12/site-packages/transforme...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: /transformers/issues/43110) who redirected me to VLLM. To reproduce: 1. Install: ``` uv pip install setuptools packaging uv pip install https://github.com/vllm-project/vllm/releases/download/v0.13.0/vllm-0.13.0+cu130-cp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ) File "/home/user/vllm-venv/lib/python3.12/site-packages/transformers/models/pixtral/processing_pixtral.py", line 124, in __init__ (EngineCore_DP0 pid=13140) self.image_token_id = tokenizer.convert_tokens_to_ids(self.i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: stall datasets psutil pandas torch-c-dlpack-ext ``` 2. Run: ``` VLLM_USE_FLASHINFER_MOE_FP4=1 ENABLE_NVFP4_SM120=1 VLLM_ATTENTION_BACKEND=FLASHINFER vllm serve RedHatAI/Mistral-Small-3.2-24B-Instruct-2506-NVFP4 --tensor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: VLLM 0.13.0 / Mistral-Small-3.2-24B-Instruct-2506: MistralTokenizer object has no attribute 'convert_tokens_to_ids' bug ### Your current environment ### 🐛 Describe the bug When launching VLLM 0.13.0 with `RedHatA...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
