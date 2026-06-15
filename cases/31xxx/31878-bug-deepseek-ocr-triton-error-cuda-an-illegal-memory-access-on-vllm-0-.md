# vllm-project/vllm#31878: [Bug]: DeepSeek OCR Triton Error [CUDA] an illegal memory access on vLLM 0.11.2 on H100

| 字段 | 值 |
| --- | --- |
| Issue | [#31878](https://github.com/vllm-project/vllm/issues/31878) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;moe;multimodal_vlm |
| 子分类 | cold_start |
| Operator 关键词 | cuda;kernel;moe;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek OCR Triton Error [CUDA] an illegal memory access on vLLM 0.11.2 on H100

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug For certain images only (as far as I observed if mixed with handwritten and digital letters in the same image, but not on all...), I get thrown an error for illegal memory access. Sometimes, for the same image I get thrown RuntimeError: CUDA error: CUBLAS_STATUS_EXECUTION_FAILED when calling cublasGemmEx The server crashes for every request on the same image, but works fine for other images. When I send the same image on a local HF version of the model, the image is processed I am using an OpenAI call to the deployed model on vllm. Dec 09 13:35:40 host deepseek-ocr[206214]: (EngineCore_DP0 pid=86) Process EngineCore_DP0: Dec 09 13:35:40 host deepseek-ocr[206214]: (EngineCore_DP0 pid=86) Traceback (most recent call last): Dec 09 13:35:40 host deepseek-ocr[206214]: (EngineCore_DP0 pid=86) File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap Dec 09 13:35:40 host deepseek-ocr[206214]: (EngineCore_DP0 pid=86) self.run() Dec 09 13:35:40 host deepseek-ocr[206214]: (EngineCore_DP0 pid=86) File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run Dec 09 13:35:40 host deepseek-ocr[206214]: (EngineCor...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: , but works fine for other images. When I send the same image on a local HF version of the model, the image is processed I am using an OpenAI call to the deployed model on vllm. Dec 09 13:35:40 host deepseek-ocr[206214]...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ut works fine for other images. When I send the same image on a local HF version of the model, the image is processed I am using an OpenAI call to the deployed model on vllm. Dec 09 13:35:40 host deepseek-ocr[206214]: (...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: timeError: CUDA error: CUBLAS_STATUS_EXECUTION_FAILED when calling cublasGemmEx The server crashes for every request on the same image, but works fine for other images. When I send the same image on a local HF version o...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: DeepSeek OCR Triton Error [CUDA] an illegal memory access on vLLM 0.11.2 on H100 bug;stale ### Your current environment ### 🐛 Describe the bug For certain images only (as far as I observed if mixed with handwritt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: DeepSeek OCR Triton Error [CUDA] an illegal memory access on vLLM 0.11.2 on H100 bug;stale ### Your current environment ### 🐛 Describe the bug For certain images only (as far as I observed if mixed with handwritt...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
