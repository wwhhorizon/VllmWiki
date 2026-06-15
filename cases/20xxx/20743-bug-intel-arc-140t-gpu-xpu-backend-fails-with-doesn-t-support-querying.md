# vllm-project/vllm#20743: [Bug]: Intel Arc 140T GPU XPU backend fails with "doesn't support querying the available free memory" error

| 字段 | 值 |
| --- | --- |
| Issue | [#20743](https://github.com/vllm-project/vllm/issues/20743) |
| 状态 | closed |
| 标签 | bug;intel-gpu;unstale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Intel Arc 140T GPU XPU backend fails with "doesn't support querying the available free memory" error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## 🐛 Describe the bug vLLM fails to initialize on Intel Arc GPU (Intel(R) Graphics [0x7d51]) with Intel Core Ultra 9 285H processor. The error occurs during KV cache initialization when vLLM attempts to query available GPU memory using `torch.xpu.mem_get_info()`, which is not supported on Intel Arc GPUs. ### Environment - **GPU**: Intel Arc 140T integrated GPU (Intel(R) Graphics [0x7d51]) - **CPU**: Intel(R) Core(TM) Ultra 9 285H - **OS**: Ubuntu 22.04.5 LTS (Docker container) - **vLLM version**: 0.9.2rc2.dev126+gad6c2e1a0 - **PyTorch**: 2.7.0+xpu - **Intel Extension for PyTorch**: 2.7.10+xpu - **Container**: Based on intel/deep-learning-essentials:2025.0.2-0-devel-ubuntu22.04 - **OneAPI**: 2025.0.2 with Rolling 2448.13 package ### Steps to reproduce 1. Set up Intel Arc GPU with Intel OneAPI 2025.0.2 and Rolling 2448.13 drivers 2. Build vLLM from source with XPU support using the updated Dockerfile (see below) 3. Try to run vLLM server with any model: ```bash docker run -it \ --name vllm-glm4 \ --network=host \ --device /dev/dri \ -v /dev/dri:/dev/dri \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --privileged \ vllm-xpu-en...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: - **CPU**: Intel(R) Core(TM) Ultra 9 285H - **OS**: Ubuntu 22.04.5 LTS (Docker container) - **vLLM version**: 0.9.2rc2.dev126+gad6c2e1a0 - **PyTorch**: 2.7.0+xpu - **Intel Extension for PyTorch**: 2.7.10+xpu - **Contain...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: ng the updated Dockerfile (see below) 3. Try to run vLLM server with any model: ```bash docker run -it \ --name vllm-glm4 \ --network=host \ --device /dev/dri \ -v /dev/dri:/dev/dri \ -v ~/.cache/huggingface:/root/.cach...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: vllm-xpu-env \ --model "THUDM/GLM-4.1V-9B-Thinking" \ --dtype=bfloat16 ``` ### Error message ``` RuntimeError: The device (Intel(R) Graphics [0x7d51]) doesn't support querying the available free memory. You can file an...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Intel Arc 140T GPU XPU backend fails with "doesn't support querying the available free memory" error bug;intel-gpu;unstale ### Your current environment ### 🐛 Describe the bug ## 🐛 Describe the bug vLLM fails to i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: and run on Intel Arc GPUs, either by: 1. Implementing a fallback mechanism when memory querying is not supported 2. Providing better error handling and workaround suggestions ### Possible solutions This appears to be a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
