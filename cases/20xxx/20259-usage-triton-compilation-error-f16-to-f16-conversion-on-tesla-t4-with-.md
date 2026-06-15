# vllm-project/vllm#20259: [Usage]: Triton compilation error (f16 to f16 conversion) on Tesla T4 with Qwen2.5-0.5B-Instruct and LoRA

| 字段 | 值 |
| --- | --- |
| Issue | [#20259](https://github.com/vllm-project/vllm/issues/20259) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;moe;quantization;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Triton compilation error (f16 to f16 conversion) on Tesla T4 with Qwen2.5-0.5B-Instruct and LoRA

### Issue 正文摘录

### Your current environment I am encountering a RuntimeError: Engine process failed to start when trying to serve the Qwen/Qwen2.5-0.5B-Instruct model with a LoRA adapter using vllm serve in a Google Colab environment with a Tesla T4 GPU. The specific error in the output is: ``` Unsupported conversion from f16 to f16 LLVM ERROR: Unsupported rounding mode for conversion. ``` This seems to be a low-level compilation error within the Triton backend. **Expected behaviour:** \ The vLLM server should start successfully, loading the base model and the LoRA adapter. **Actual behaviour:** \ The vLLM engine fails to start with a Triton compilation error related to f16 conversion. --- My code to start the vLLM server: ```python !pip install -q vllm from huggingface_hub import snapshot_download lora_path = snapshot_download(repo_id="my-org/Qwen2.5-0.5B-Instruct-PEFT") print("LoRA path:", lora_path) # output something like "LoRA path: /root/.cache/huggingface/hub/models--my-org--Qwen2.5-0.5B-Instruct-PEFT/snapshots/230786..." !vllm serve Qwen/Qwen2.5-0.5B-Instruct \ --enable-lora \ --lora-modules my-lora={lora_path} ``` --- Just in case, I also attach the way I train my model: --- Note: \ Eve...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Usage]: Triton compilation error (f16 to f16 conversion) on Tesla T4 with Qwen2.5-0.5B-Instruct and LoRA usage ### Your current environment I am encountering a RuntimeError: Engine process failed to start when trying t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: sage]: Triton compilation error (f16 to f16 conversion) on Tesla T4 with Qwen2.5-0.5B-Instruct and LoRA usage ### Your current environment I am encountering a RuntimeError: Engine process failed to start when trying to...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Usage]: Triton compilation error (f16 to f16 conversion) on Tesla T4 with Qwen2.5-0.5B-Instruct and LoRA usage ### Your current environment I am encountering a RuntimeError: Engine process failed to start when trying t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;moe;quantization;scheduler_memory attention;cuda;kernel;operator;quantization;triton build_error;crash dtype;env_dependency;shape Your current environ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: er. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
