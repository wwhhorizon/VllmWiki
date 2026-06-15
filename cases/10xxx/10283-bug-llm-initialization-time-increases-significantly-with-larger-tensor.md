# vllm-project/vllm#10283: [Bug]: LLM initialization time increases significantly with larger tensor parallel size and Ray

| 字段 | 值 |
| --- | --- |
| Issue | [#10283](https://github.com/vllm-project/vllm/issues/10283) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: LLM initialization time increases significantly with larger tensor parallel size and Ray

### Issue 正文摘录

### Your current environment vllm 0.5.2 ### Model Input Dumps just test the vllm init time ### 🐛 Describe the bug ### Issue Description We observed significant and unexpected increases in VLLM initialization time when scaling tensor parallelism (TP), especially with Ray enabled. ### Observed Behavior - TP=1: ~7 seconds initialization time - TP=4: ~14 seconds initialization time - TP=4 with Ray: ~24 seconds initialization time ### Expected Behavior Initialization time should remain relatively constant or have minimal increase when scaling tensor parallelism and use ray. ### Environment - VLLM version: 0.5.2 - Model: Qwen2-7B - GPU: NVIDIA L20Z - Number of GPUs: 8 ### Additional Context The initialization time increase appears disproportionate to the tensor parallel size, suggesting a potential bottleneck in the initialization process, particularly when Ray is involved. ### Reproducible Steps 1. Run VLLM with TP=1 2. Run VLLM with TP=4 3. Run VLLM with TP=4 and Ray enabled 4. Compare initialization times ### vllm start time ```python def run_vllm( requests: List[Tuple[str, int, int]], model: str, tokenizer: str, quantization: Optional[str], tensor_parallel_size: int, seed: int, n: i...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: es in VLLM initialization time when scaling tensor parallelism (TP), especially with Ray enabled. ### Observed Behavior - TP=1: ~7 seconds initialization time - TP=4: ~14 seconds initialization time - TP=4 with Ray: ~24...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ected increases in VLLM initialization time when scaling tensor parallelism (TP), especially with Ray enabled. ### Observed Behavior - TP=1: ~7 seconds initialization time - TP=4: ~14 seconds initialization time - TP=4...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: llel size and Ray bug;ray ### Your current environment vllm 0.5.2 ### Model Input Dumps just test the vllm init time ### 🐛 Describe the bug ### Issue Description We observed significant and unexpected increases in VLLM...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: e initialization times ### vllm start time ```python def run_vllm( requests: List[Tuple[str, int, int]], model: str, tokenizer: str, quantization: Optional[str], tensor_parallel_size: int, seed: int, n: int, use_beam_se...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: prefill: bool, max_num_batched_tokens: int, distributed_executor_backend: Optional[str], gpu_memory_utilization: float = 0.9, num_scheduler_steps: int = 1, use_v2_block_manager: bool = False, download_dir: Optional[str]...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
