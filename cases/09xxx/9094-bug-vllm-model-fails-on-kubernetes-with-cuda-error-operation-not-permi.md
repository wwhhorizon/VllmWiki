# vllm-project/vllm#9094: [Bug]: VLLM Model Fails on Kubernetes with "CUDA error: operation not permitted when stream is capturing"

| 字段 | 值 |
| --- | --- |
| Issue | [#9094](https://github.com/vllm-project/vllm/issues/9094) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM Model Fails on Kubernetes with "CUDA error: operation not permitted when stream is capturing"

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug TLDR; - `enforce_eager=True` - Runs in Docker Compose - Runs in K8S - `enforce_eager=False` - Runs in Docker Compose - *Fails* in K8S --- ### General Info I am encountering a strange issue when deploying a VLLM-based model in Kubernetes, while the same setup works perfectly fine in a Docker Compose environment on an identical hardware setup. I have 2 servers for development: - "Test Server" (uses Docker Compose) - "Stage Server" (uses Kubernetes) Here is the code I'm running on both of them: ```python from langchain_community.llms.vllm import VLLM TEMPERATURE: float = 0.0 TOP_P: float = 0.90 TOP_K: int = 1 PRESENCE_PENALTY: float = 0.4 FREQUENCY_PENALTY: float = 0.4 MODEL_NAME: str = "meta-llama/Llama-3.1-8B-Instruct" NUM_OUTPUT_TOKENS: int = 4096 CONTEXT_SIZE: int = 54_784 llm = VLLM( temperature=TEMPERATURE, top_p=TOP_P, top_k=TOP_K, presence_penalty=PRESENCE_PENALTY, frequency_penalty=FREQUENCY_PENALTY, model=MODEL_NAME, max_new_tokens=NUM_OUTPUT_TOKENS, dtype="float16", tensor_parallel_size=4, trust_remote_code=True, vllm_kwargs={ "gpu_memory_utilization": 0.95, "device": "cuda", "max_model...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: nse_ ### 🐛 Describe the bug TLDR; - `enforce_eager=True` - Runs in Docker Compose - Runs in K8S - `enforce_eager=False` - Runs in Docker Compose - *Fails* in K8S --- ### General Info I am encountering a strange issue wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: : "cuda", "max_model_len": CONTEXT_SIZE, "enable_chunked_prefill": True, "max_num_batched_tokens": 512, "disable_custom_all_reduce": True, "enforce_eager": False, # Causes error when False in k8s }, ) ``` This code **fa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: VLLM Model Fails on Kubernetes with "CUDA error: operation not permitted when stream is capturing" bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug TLDR; - `enforce_eage...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: PENALTY, model=MODEL_NAME, max_new_tokens=NUM_OUTPUT_TOKENS, dtype="float16", tensor_parallel_size=4, trust_remote_code=True, vllm_kwargs={ "gpu_memory_utilization": 0.95, "device": "cuda", "max_model_len": CONTEXT_SIZE...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: VLLM Model Fails on Kubernetes with "CUDA error: operation not permitted when stream is capturing" bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug TLDR; - `enforce_eage...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
