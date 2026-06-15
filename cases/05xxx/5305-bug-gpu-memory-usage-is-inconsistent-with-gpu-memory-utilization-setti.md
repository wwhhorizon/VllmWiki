# vllm-project/vllm#5305: [Bug]: GPU memory usage is inconsistent with gpu_memory_utilization settings

| 字段 | 值 |
| --- | --- |
| Issue | [#5305](https://github.com/vllm-project/vllm/issues/5305) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 |  |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPU memory usage is inconsistent with gpu_memory_utilization settings

### Issue 正文摘录

### Your current environment Deploy using llama factory CUDA_VISIBLE_DEVICES=0 API_PORT=9092 python src/api_demo.py --model_name_or_path /save_model/qwen1_5_7b_pcb_merge --template qwen --infer_backend vllm --max_new_tokens 32768 --vllm_maxlen 32768 --vllm_enforce_eager --vllm_gpu_util 0.95 Inference environment: Python=3.10.14 CUDA=12.2 single A100 80G ### 🐛 Describe the bug There is no other GPU usage during deployment. The expected GPU usage is 76G, but the actual GPU usage is 55G. What is the reason?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: tilization settings bug;stale ### Your current environment Deploy using llama factory CUDA_VISIBLE_DEVICES=0 API_PORT=9092 python src/api_demo.py --model_name_or_path /save_model/qwen1_5_7b_pcb_merge --template qwen --i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tings bug;stale ### Your current environment Deploy using llama factory CUDA_VISIBLE_DEVICES=0 API_PORT=9092 python src/api_demo.py --model_name_or_path /save_model/qwen1_5_7b_pcb_merge --template qwen --infer_backend v...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: el_name_or_path /save_model/qwen1_5_7b_pcb_merge --template qwen --infer_backend vllm --max_new_tokens 32768 --vllm_maxlen 32768 --vllm_enforce_eager --vllm_gpu_util 0.95 Inference environment: Python=3.10.14 CUDA=12.2...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ut the actual GPU usage is 55G. What is the reason? performance cuda env_dependency Your current environment
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: GPU memory usage is inconsistent with gpu_memory_utilization settings bug;stale ### Your current environment Deploy using llama factory CUDA_VISIBLE_DEVICES=0 API_PORT=9092 python src/api_demo.py --model_name_or_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
