# vllm-project/vllm#24383: [Bug]: CUDA Invalid Argument Error During Model Loading with vLLM on NVIDIA RTX PRO 6000 Blackwell (SM120)

| 字段 | 值 |
| --- | --- |
| Issue | [#24383](https://github.com/vllm-project/vllm/issues/24383) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;operator;quantization;sampling |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA Invalid Argument Error During Model Loading with vLLM on NVIDIA RTX PRO 6000 Blackwell (SM120)

### Issue 正文摘录

### Your current environment ### GPU Hardware Information * **Product Name**: NVIDIA RTX PRO 6000 Blackwell Server Edition * **Product Brand**: NVIDIA * **Product Architecture**: Blackwell * **Video Memory**: 96GB GDDR7 **Software Versions:** Driver Version: 580.82.07 CUDA Version: 12.9 vllm version: v0.10.2rc1 Installed via command: `uv pip install vllm --torch-backend=auto --extra-index-url https://wheels.vllm.ai/5438967fbc7a10ae6eee7a98182f4de94101e858` #### Compute Capability (SM version) = SM120 The compute capability was queried using the following code: ```python import torch if torch.cuda.is_available(): capability = torch.cuda.get_device_capability(0) print(f"SM{capability[0]}{capability[1]}") # Returns SM120 ``` ##### Environment Verification - Normal ## Running vllm ```bash vllm serve Qwen/Qwen2.5-VL-32B-Instruct \ --served-model-name qwen-vl-model \ --trust-remote-code \ --tensor-parallel-size 1 \ --host 0.0.0.0 \ --port 8000 ``` **Error occurred during model loading:** ``` DEBUG 09-07 02:31:33 [__init__.py:28] No plugins for group vllm.platform_plugins found. DEBUG 09-07 02:31:33 [__init__.py:34] Checking if TPU platform is available. DEBUG 09-07 02:31:33 [__init__.py...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: t Architecture**: Blackwell * **Video Memory**: 96GB GDDR7 **Software Versions:** Driver Version: 580.82.07 CUDA Version: 12.9 vllm version: v0.10.2rc1 Installed via command: `uv pip install vllm --torch-backend=auto --...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Bug]: CUDA Invalid Argument Error During Model Loading with vLLM on NVIDIA RTX PRO 6000 Blackwell (SM120) bug ### Your current environment ### GPU Hardware Information * **Product Name**: NVIDIA RTX PRO 6000 Blackwell...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: CUDA Invalid Argument Error During Model Loading with vLLM on NVIDIA RTX PRO 6000 Blackwell (SM120) bug ### Your current environment ### GPU Hardware Information * **Product Name**: NVIDIA RTX PRO 6000 Blackwell...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: version: v0.10.2rc1 Installed via command: `uv pip install vllm --torch-backend=auto --extra-index-url https://wheels.vllm.ai/5438967fbc7a10ae6eee7a98182f4de94101e858` #### Compute Capability (SM version) = SM120 The co...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: tecture: Qwen2_5_VLForConditionalGeneration (APIServer pid=44984) `torch_dtype` is deprecated! Use `dtype` instead! (APIServer pid=44984) INFO 09-07 02:31:52 [__init__.py:1773] Using max model len 128000 (APIServer pid=...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
