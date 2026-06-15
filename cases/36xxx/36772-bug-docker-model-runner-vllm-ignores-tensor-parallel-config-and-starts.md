# vllm-project/vllm#36772: [Bug]: Docker Model Runner vLLM ignores tensor parallel config and starts with world_size=1 on 4x RTX 3060

| 字段 | 值 |
| --- | --- |
| Issue | [#36772](https://github.com/vllm-project/vllm/issues/36772) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Docker Model Runner vLLM ignores tensor parallel config and starts with world_size=1 on 4x RTX 3060

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Environment - Host OS: Ubuntu 22.04 - GPUs: 4x NVIDIA GeForce RTX 3060 12GB - `docker model version`: - Client: `v1.1.8` - Server: `v1.1.11` - `docker model status`: - `llama.cpp Running` - `vllm Running (0.17.0)` ### Model - `huggingface.co/qwen/qwen3.5-9b` - Format shown by `docker model show`: `safetensors` - Size: `19.31GB` ### What I expected Since this is a safetensors model and Docker Model Runner routes safetensors models to vLLM, I expected the model to be served with tensor parallelism across 4 GPUs when configured accordingly. ### What actually happened The model is routed to `vLLM`, but the engine core starts with: - `tensor_parallel_size=1` - `pipeline_parallel_size=1` - `data_parallel_size=1` - `world_size=1` As a result, the model loads only on GPU 0 and fails with CUDA OOM, instead of sharding across 4 GPUs. ### Steps to reproduce 1. Install the runner with vLLM + CUDA: ```bash docker model stop-runner docker model uninstall-runner --images docker model install-runner --backend vllm --gpu cuda docker model status ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: Docker Model Runner vLLM ignores tensor parallel config and starts with world_size=1 on 4x RTX 3060 bug ### Your current environment ### 🐛 Describe the bug ### Environment - Host OS: Ubuntu 22.04 - GPUs: 4x NVIDIA
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Docker Model Runner vLLM ignores tensor parallel config and starts with world_size=1 on 4x RTX 3060 bug ### Your current environment ### 🐛 Describe the bug ### Environment - Host OS: Ubuntu 22.04 - GPUs: 4x NVIDI...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: r vLLM ignores tensor parallel config and starts with world_size=1 on 4x RTX 3060 bug ### Your current environment ### 🐛 Describe the bug ### Environment - Host OS: Ubuntu 22.04 - GPUs: 4x NVIDIA GeForce RTX 3060 12GB -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: docker model uninstall-runner --images docker model install-runner --backend vllm --gpu cuda docker model status ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked t...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: nd fails with CUDA OOM, instead of sharding across 4 GPUs. ### Steps to reproduce 1. Install the runner with vLLM + CUDA: ```bash docker model stop-runner docker model uninstall-runner --images docker model install-runn...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
