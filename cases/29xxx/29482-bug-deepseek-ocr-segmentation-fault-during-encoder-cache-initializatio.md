# vllm-project/vllm#29482: [Bug]: DeepSeek-OCR - segmentation fault during encoder cache initialization on WSL2

| 字段 | 值 |
| --- | --- |
| Issue | [#29482](https://github.com/vllm-project/vllm/issues/29482) |
| 状态 | closed |
| 标签 | bug;torch.compile;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek-OCR - segmentation fault during encoder cache initialization on WSL2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM 0.11.2 consistently crashes with a segmentation fault when initializing the encoder cache for the `deepseek-ai/DeepSeek-OCR` model on WSL2 (Windows Subsystem for Linux). The crash occurs during the torch.compile/torch.dynamo bytecode transformation phase, specifically when processing the multimodal encoder. **Environment:** WSL2 (Ubuntu 22.04.3 LTS) with RTX 4090 **Crash Location:** During encoder cache initialization, immediately after the log message: ``` INFO Encoder cache will be initialized with a budget of 8192 tokens INFO Using cache directory: /home/user/.cache/vllm/torch_compile_cache/.../backbone for vLLM's torch.compile INFO Dynamo bytecode transform time: X.XX s !!!!!!! Segfault encountered !!!!!!! ``` ### Reproduction Steps **Minimal Reproducible Code:** ```python import os os.environ['VLLM_USE_V1'] = '0' # V1 engine is used regardless from vllm import LLM, SamplingParams from PIL import Image if __name__ == "__main__": llm = LLM( model="deepseek-ai/DeepSeek-OCR", trust_remote_code=True, dtype="bfloat16", gpu_memory_utilization=0.9, max_model_len=4096, enforce_eager=False, enable_prefix_caching=False, ) image =...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: segmentation fault during encoder cache initialization on WSL2 bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug vLLM 0.11.2 consistently crashes with a segmentation fault when initializing the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: t when initializing the encoder cache for the `deepseek-ai/DeepSeek-OCR` model on WSL2 (Windows Subsystem for Linux). The crash occurs during the torch.compile/torch.dynamo bytecode transformation phase, specifically wh...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: the multimodal encoder. **Environment:** WSL2 (Ubuntu 22.04.3 LTS) with RTX 4090 **Crash Location:** During encoder cache initialization, immediately after the log message: ``` INFO Encoder cache will be initialized wit...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: force_eager=False` - ✗ `enable_prefix_caching=False` - ✗ `VLLM_ATTENTION_BACKEND=XFORMERS` - ✗ `TORCH_COMPILE_DISABLE=1` - ✗ `VLLM_USE_V1=0` (V1 engine is still used) - ✗ `VLLM_TORCH_COMPILE_LEVEL=0` **Version attempts:...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: odel="deepseek-ai/DeepSeek-OCR", trust_remote_code=True, dtype="bfloat16", gpu_memory_utilization=0.9, max_model_len=4096, enforce_eager=False, enable_prefix_caching=False, ) image = Image.open("test.png").convert("RGB"...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
